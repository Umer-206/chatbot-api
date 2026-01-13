"""
Flask API Backend for Chatbot
Save this as: app.py
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from dotenv import load_dotenv
from agents.product_agent import ProductAgent

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Store conversation sessions
sessions = {}

def get_agent(session_id):
    """Get or create agent for session"""
    if session_id not in sessions:
        api_key = os.getenv("GROQ_API_KEY")
        sessions[session_id] = ProductAgent(api_key)
    return sessions[session_id]

@app.route('/api/chat', methods=['POST'])
def chat():
    """Chat endpoint"""
    try:
        data = request.json
        message = data.get('message', '')
        session_id = data.get('session_id', 'default')
        
        if not message:
            return jsonify({'error': 'Message is required'}), 400
        
        # Get agent and process message
        agent = get_agent(session_id)
        response = agent.chat(message)
        
        return jsonify({
            'response': response,
            'session_id': session_id
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/reset', methods=['POST'])
def reset():
    """Reset conversation"""
    try:
        data = request.json
        session_id = data.get('session_id', 'default')
        
        if session_id in sessions:
            sessions[session_id].reset_conversation()
        
        return jsonify({'message': 'Conversation reset successfully'})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({'status': 'ok', 'message': 'Chatbot API is running'})

# Vercel ke liye
if __name__ != '__main__':
    # Production (Vercel)
    application = app
else:
    # Local development
    app.run(debug=True, host='0.0.0.0', port=5000)