import os
import json
import requests

def handler(request):
    """
    Vercel serverless function that sends text to AI and checks if response contains a specific word.
    """
    # Handle CORS
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Content-Type': 'application/json'
    }
    
    # Handle preflight
    if hasattr(request, 'method') and request.method == 'OPTIONS':
        return {
            'statusCode': 200,
            'headers': headers,
            'body': ''
        }
    
    try:
        # Get request body
        body = getattr(request, 'body', '')
        if isinstance(body, bytes):
            body = body.decode('utf-8')
        
        data = {}
        if body:
            try:
                data = json.loads(body)
            except:
                pass
        
        # Get query parameters
        query = getattr(request, 'query', {}) or getattr(request, 'args', {}) or {}
        
        # Get parameters from body or query
        text_to_ai = data.get('text_to_ai', '') or query.get('text_to_ai', '')
        word_to_check = data.get('word_to_check', '') or query.get('word_to_check', '')
        
        # Validate parameters
        if not text_to_ai:
            return {
                'statusCode': 400,
                'headers': headers,
                'body': json.dumps({'error': 'Missing required parameter: text_to_ai'})
            }
        
        if not word_to_check:
            return {
                'statusCode': 400,
                'headers': headers,
                'body': json.dumps({'error': 'Missing required parameter: word_to_check'})
            }
        
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
        
        return {
            'statusCode': 200,
            'headers': headers,
            'body': json.dumps(result)
        }
        
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': headers,
            'body': json.dumps({
                'error': str(e),
                'message': 'An error occurred while processing the request'
            })
        }


def call_ai_service(text):
    """Calls the AI service with the provided text."""
    ai_api_key = os.environ.get('AI_API_KEY', '')
    ai_api_url = os.environ.get('AI_API_URL', 'https://api.openai.com/v1/chat/completions')
    ai_model = os.environ.get('AI_MODEL', 'gpt-3.5-turbo')
    
    if not ai_api_key:
        # Fallback: Return a mock response if no API key is configured
        return f"This is a mock AI response to: {text}. The response includes various words."
    
    try:
        headers = {
            'Authorization': f'Bearer {ai_api_key}',
            'Content-Type': 'application/json'
        }
        
        payload = {
            'model': ai_model,
            'messages': [{'role': 'user', 'content': text}],
            'max_tokens': 500,
            'temperature': 0.7
        }
        
        response = requests.post(ai_api_url, headers=headers, json=payload, timeout=30)
        response.raise_for_status()
        
        data = response.json()
        
        if 'choices' in data and len(data['choices']) > 0:
            return data['choices'][0]['message']['content'].strip()
        else:
            raise ValueError("Unexpected response format from AI service")
            
    except requests.exceptions.RequestException as e:
        raise Exception(f"Error calling AI service: {str(e)}")
    except KeyError as e:
        raise Exception(f"Error parsing AI response: {str(e)}")
