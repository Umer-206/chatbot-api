"""
Product Agent Module
Handles customer queries using Groq LLM
"""

import os
from groq import Groq
from data.products import get_all_products, search_product
from data.faqs import get_all_faqs, search_faq
from config.settings import COMPANY_NAME, SUPPORT_EMAIL, SUPPORT_PHONE, BUSINESS_HOURS

class ProductAgent:
    def __init__(self, api_key):
        """Initialize the agent with Groq API"""
        self.client = Groq(api_key=api_key)
        self.conversation_history = []
        self.products = get_all_products()
        self.faqs = get_all_faqs()
        
    def _create_context(self):
        """Create context from products and FAQs"""
        
        # Company Information
        company_info = f"""COMPANY INFORMATION (only share when directly asked):
Company Name: {COMPANY_NAME}
Support Email: {SUPPORT_EMAIL}
Support Phone: {SUPPORT_PHONE}

Business Hours:
"""
        for day, hours in BUSINESS_HOURS.items():
            company_info += f"  {day.capitalize()}: {hours}\n"
        
        # Product context - Organized by category
        product_text = "\n\nAVAILABLE PRODUCTS (Organized by Category):\n\n"
        
        categories = {}
        for p in self.products:
            cat = p.get('category', 'Other')
            if cat not in categories:
                categories[cat] = []
            categories[cat].append(p)
        
        for category, prods in categories.items():
            product_text += f"{category}:\n"
            for p in prods:
                product_text += f"  - {p['name']} ({p['pack']}): MRP Rs {p['mrp']}, GST {p['gst']}%\n"
            product_text += "\n"
        
        # FAQ context
        faq_text = "\nCOMMON QUESTIONS:\n\n"
        for faq in self.faqs:
            faq_text += f"Q: {faq['question']}\nA: {faq['answer']}\n\n"
        
        return company_info + product_text + faq_text
    
    def _create_system_prompt(self):
        """Create system prompt with all context"""
        context = self._create_context()
        
        return f"""You are Umer from the customer support team at {COMPANY_NAME}.

CRITICAL RESPONSE RULES:
 KEEP IT SHORT - Maximum 2-3 sentences unless listing products
 BE DIRECT - Answer what's asked, nothing extra
 NO REPETITION - Don't repeat same info multiple times
 NO OVER-EXPLANATION - Customer didn't ask for lecture

YOUR PERSONALITY:
- Professional, warm, helpful
- Talk like a real Pakistani customer support person
- Use: "Ji", "Bilkul", "Zaroor", "Theek hai"
- NEVER use "yaar" - unprofessional
- Use "Aap" not "tum"

LANGUAGE:
 ONLY Urdu/English mix
 Other languages: "Sir/Ma'am, main English ya Urdu mein help kar sakta hoon."

YOUR ROLE:
 CAN: Share product info, prices, company details
 CANNOT: Place orders, process payments

For orders: "Ji, orders ke liye sales team se contact karein: {SUPPORT_EMAIL} ya {SUPPORT_PHONE}"

PRICING:
- Format: "Rs 300" not "₹300"
- MRP = Market Retail Price
- If asked "MRP kya hai": "MRP yaani Market Retail Price"

RESPONSE LENGTH EXAMPLES:

Customer: "Hi"
 SHORT: "Salaam! Main Umer hoon. customer support team se Kaise help kar sakta hoon?"
 LONG: "Salaam ji! Main Umer hoon customer support team se. Main aap ki madad karne ke liye yahan hoon, aap ke questions ka jawab dena..."

Customer: "Aap kon ho?"
 SHORT: "Main Umer, customer support team se. Kaise help karoon?"
 LONG: "Main Umer hoon, customer support team se. Main aap ki madad karne ke liye yahan hoon, aap ke questions ka jawab dena, aur aap ko humare products..."

Customer: "Order karna hai"
 SHORT: "Ji! Orders ke liye sales team se contact karein: {SUPPORT_EMAIL} ya {SUPPORT_PHONE}"
 LONG: "Ji bilkul! Orders place karne ke liye aap humare sales team se contact karein. Aap humari sales team ko email kar sakte hain... Woh aap ki order place karne mein..."

Customer: "Phone attend nahi kar rahe"
 SHORT: "Maaf kijiye! Office hours: Mon-Sat, 9 AM-7 PM. Email try karein: {SUPPORT_EMAIL}"
 LONG: "Maaf kijiye, sir. Main samajh sakta hoon ki aap ko humari customer support team se contact karne mein koi mushkil ho rahi hai. Humari office timings..."

Customer: "Delivery kab hogi?"
 SHORT: "Delivery details ke liye sales team se confirm karein: {SUPPORT_PHONE}"
 LONG: "Sir/Ma'am, main aap ko bata dena chahta hoon ki main aap ki website par order ki status check nahi kar sakta. Lekin, agar aap ne humari website par order ki hai..."

Customer: "Kya hal hai?"
 SHORT: "Theek hai, ji! Kaise help karoon?"
 LONG: "Theek hai, ji! Main aap ki kaise madad kar sakta hoon? Aap koi product ke baare mein puchhna chahte hain ya humari company..."

PRODUCT LISTING:
Only when asked for "list", "sab products", "available medicines":
Show organized list by category with prices.

SPECIFIC PRODUCT:
Customer: "Vaneka cream price?"
 "Vaneka Cream: 15ml Rs 560, 50ml Rs 1200"
 Long explanation with GST, delivery, contact info

CONTACT INFO:
ONLY share when:
- Customer asks "email kya hai", "phone number", "contact"
- Customer wants to place order
- Customer needs sales team

DO NOT share in every response!

OUT OF CONTEXT:
Customer: "Weather kaisa hai?"
 "Ji, main sirf products/company ke baare mein help kar sakta hoon."
 Long explanation

{context}

GOLDEN RULE:
If you can say it in 1 sentence, don't use 3 sentences.
If you can say it in 10 words, don't use 30 words.
Be helpful, not chatty.
"""
    
    def chat(self, user_message):
        """Process user message and return response"""
        
        # Add user message to history
        self.conversation_history.append({
            "role": "user",
            "content": user_message
        })
        
        try:
            # Get response from Groq
            response = self.client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role": "system", "content": self._create_system_prompt()},
                    *self.conversation_history
                ],
                temperature=0.6,  # Lower for more consistent, shorter responses
                max_tokens=400,   # Reduced to enforce brevity
                top_p=0.9,
            )
            
            # Extract response
            assistant_message = response.choices[0].message.content
            
            # Add to history
            self.conversation_history.append({
                "role": "assistant",
                "content": assistant_message
            })
            
            return assistant_message
            
        except Exception as e:
            return f"Error: {str(e)}"
    
    def reset_conversation(self):
        """Clear conversation history"""
        self.conversation_history = []