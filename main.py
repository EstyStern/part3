import functions_framework
import os
import requests
import json
from flask import jsonify

AI_API_KEY = os.environ.get('AI_API_KEY', '')
AI_API_URL = os.environ.get('AI_API_URL', 'https://api.openai.com/v1/chat/completions')
AI_MODEL = os.environ.get('AI_MODEL', 'gpt-3.5-turbo')

@functions_framework.http
def check_ai_response(request):
    """
    Cloud Function that sends text to AI and checks if response contains a specific word.
    
    Parameters (via JSON body or query params):
    - text_to_ai: The text to send to the AI
    - word_to_check: The word to check in the AI response
    
    Returns:
    - AI response with check result
    """
    # Handle CORS for public access
    if request.method == 'OPTIONS':
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Max-Age': '3600'
        }
        return ('', 204, headers)
    
    # Set CORS headers
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Content-Type': 'application/json'
    }
    
    try:
        # Get parameters from request
        if request.is_json:
            data = request.get_json()
            text_to_ai = data.get('text_to_ai', '')
            word_to_check = data.get('word_to_check', '')
        else:
            text_to_ai = request.args.get('text_to_ai', '')
            word_to_check = request.args.get('word_to_check', '')
        
        # Validate parameters
        if not text_to_ai:
            return jsonify({
                'error': 'Missing required parameter: text_to_ai'
            }), 400, headers
        
        if not word_to_check:
            return jsonify({
                'error': 'Missing required parameter: word_to_check'
            }), 400, headers
        
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
        
        return jsonify(result), 200, headers
        
    except Exception as e:
        return jsonify({
            'error': str(e),
            'message': 'An error occurred while processing the request'
        }), 500, headers


def call_ai_service(text):
    """
    Calls the AI service with the provided text.
    Supports OpenAI API by default, but can be configured for other services.
    """
    if not AI_API_KEY:
        # Fallback: Return a mock response if no API key is configured
        # This allows testing without API key setup
        return f"This is a mock AI response to: {text}. The response includes various words."
    
    try:
        # OpenAI API format
        headers = {
            'Authorization': f'Bearer {AI_API_KEY}',
            'Content-Type': 'application/json'
        }
        
        payload = {
            'model': AI_MODEL,
            'messages': [
                {'role': 'user', 'content': text}
            ],
            'max_tokens': 500,
            'temperature': 0.7
        }
        
        response = requests.post(AI_API_URL, headers=headers, json=payload, timeout=30)
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

