import os
import json
import requests
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/', methods=['GET', 'POST', 'OPTIONS'])
def handler():
    """
    Railway Flask app that sends text to AI and checks if response contains a specific word.
    """
    # Handle preflight
    if request.method == 'OPTIONS':
        return '', 200
    
    try:
        # Get parameters from body or query
        if request.is_json:
            data = request.get_json() or {}
        else:
            data = {}
        
        query = request.args.to_dict()
        
        text_to_ai = data.get('text_to_ai', '') or query.get('text_to_ai', '')
        word_to_check = data.get('word_to_check', '') or query.get('word_to_check', '')
        
        # Validate parameters
        if not text_to_ai:
            return jsonify({'error': 'Missing required parameter: text_to_ai'}), 400
        
        if not word_to_check:
            return jsonify({'error': 'Missing required parameter: word_to_check'}), 400
        
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
        
        return jsonify(result), 200
        
    except Exception as e:
        return jsonify({
            'error': str(e),
            'message': 'An error occurred while processing the request'
        }), 500


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


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)

