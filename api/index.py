from http.server import BaseHTTPRequestHandler
import os
import requests
import json
from urllib.parse import urlparse, parse_qs

class handler(BaseHTTPRequestHandler):
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
    
    def do_GET(self):
        self.handle_request()
    
    def do_POST(self):
        self.handle_request()
    
    def handle_request(self):
        """Vercel serverless function that sends text to AI and checks if response contains a specific word."""
        try:
            # Parse query parameters
            parsed_path = urlparse(self.path)
            query_params = parse_qs(parsed_path.query)
            
            # Get request body for POST
            content_length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(content_length) if content_length > 0 else b''
            
            # Parse JSON body if present
            data = {}
            if body:
                try:
                    data = json.loads(body.decode('utf-8'))
                except:
                    pass
            
            # Get parameters from body or query
            text_to_ai = data.get('text_to_ai', '') or (query_params.get('text_to_ai', [''])[0] if query_params.get('text_to_ai') else '')
            word_to_check = data.get('word_to_check', '') or (query_params.get('word_to_check', [''])[0] if query_params.get('word_to_check') else '')
            
            # Validate parameters
            if not text_to_ai:
                self.send_response(400)
                self.send_header('Access-Control-Allow-Origin', '*')
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'error': 'Missing required parameter: text_to_ai'}).encode())
                return
            
            if not word_to_check:
                self.send_response(400)
                self.send_header('Access-Control-Allow-Origin', '*')
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'error': 'Missing required parameter: word_to_check'}).encode())
                return
            
            # Call AI service
            ai_response = call_ai_service(text_to_ai)
            
            # Check if word is in response
            word_found = word_to_check.lower() in ai_response.lower()
            
            # Return response
            result = {
                'text_to_ai': text_to_ai,
                'word_to_check': word_to_check,
                'ai_response': ai_response,
                'word_found': word_found,
                'message': f"Word '{word_to_check}' {'found' if word_found else 'not found'} in AI response"
            }
            
            self.send_response(200)
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(result).encode())
            
        except Exception as e:
            self.send_response(500)
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({
                'error': str(e),
                'message': 'An error occurred while processing the request'
            }).encode())


def call_ai_service(text):
    """Calls the AI service with the provided text."""
    ai_api_key = os.environ.get('AI_API_KEY', '')
    ai_api_url = os.environ.get('AI_API_URL', 'https://api.openai.com/v1/chat/completions')
    ai_model = os.environ.get('AI_MODEL', 'gpt-3.5-turbo')
    
    if not ai_api_key:
        # Fallback: Return a mock response if no API key is configured
        return f"This is a mock AI response to: {text}. The response includes various words."
    
    try:
        # OpenAI API format
        headers = {
            'Authorization': f'Bearer {ai_api_key}',
            'Content-Type': 'application/json'
        }
        
        payload = {
            'model': ai_model,
            'messages': [
                {'role': 'user', 'content': text}
            ],
            'max_tokens': 500,
            'temperature': 0.7
        }
        
        response = requests.post(ai_api_url, headers=headers, json=payload, timeout=30)
        response.raise_for_status()
        
        data = response.json()
        
        # Extract text from OpenAI response
        if 'choices' in data and len(data['choices']) > 0:
            return data['choices'][0]['message']['content'].strip()
        else:
            raise ValueError("Unexpected response format from AI service")
            
    except requests.exceptions.RequestException as e:
        raise Exception(f"Error calling AI service: {str(e)}")
    except KeyError as e:
        raise Exception(f"Error parsing AI response: {str(e)}")
