from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import sys

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agents.product_agent import ProductAgent
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

sessions = {}

def get_agent(session_id):
    if session_id not in sessions:
        api_key = os.getenv("GROQ_API_KEY")
        sessions[session_id] = ProductAgent(api_key)
    return sessions[session_id]

@app.route('/api/chat', methods=['POST', 'OPTIONS'])
def chat():
    if request.method == 'OPTIONS':
        return '', 200
    
    try:
        data = request.json
        message = data.get('message', '')
        session_id = data.get('session_id', 'default')
        
        if not message:
            return jsonify({'error': 'Message is required'}), 400
        
        agent = get_agent(session_id)
        response = agent.chat(message)
        
        return jsonify({
            'response': response,
            'session_id': session_id
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({
        'status': 'ok',
        'message': 'Chatbot API is running on Vercel'
    })