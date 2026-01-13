"""
Main Entry Point
Run this file to start the chatbot
"""

import os
from dotenv import load_dotenv
from agents.product_agent import ProductAgent

def main():
    # Load environment variables
    load_dotenv()
    
    # Get API key
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        print("❌ Error: GROQ_API_KEY not found in .env file")
        return
    
    # Initialize agent
    agent = ProductAgent(api_key)
    
    # Welcome message
    print("=" * 70)
    print("🏥 Pharmaceutical Product Assistant")
    print("=" * 70)
    print()
    
    # First message from agent
    print("Agent: Assalam o Alaikum! Main Umer hoon customer support team se.")
    print("       Aap ko kaise help kar sakta hoon aaj?\n")
    
    # Chat loop
    while True:
        user_input = input("You: ").strip()
        
        if user_input.lower() in ['quit', 'exit', 'bye', 'khatam']:
            print("\nAgent: Shukriya! Allah Hafiz, khayal rakhna! 👋\n")
            break
        
        if not user_input:
            continue
        
        # Get response
        response = agent.chat(user_input)
        print(f"\nAgent: {response}\n")

if __name__ == "__main__":
    main()