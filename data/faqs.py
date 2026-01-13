"""
FAQ Data Module
Common questions and answers
"""

FAQS = [
    {
        "question": "What payment methods do you accept?",
        "answer": "We accept cash, credit/debit cards, and bank transfers for bulk orders.",
        "category": "payment"
    },
    {
        "question": "Do you offer home delivery?",
        "answer": "Yes, we offer home delivery for orders above ₹500. Delivery charges may apply for orders below this amount.",
        "category": "delivery"
    },
    {
        "question": "What is your return policy?",
        "answer": "We accept returns within 7 days of purchase for unopened products with original packaging and receipt.",
        "category": "returns"
    },
    {
        "question": "Do you have a minimum order quantity?",
        "answer": "For wholesale orders, minimum order quantity varies by product. Please contact our sales team for details.",
        "category": "orders"
    },
    {
        "question": "Are your products genuine?",
        "answer": "Yes, all our products are 100% genuine and sourced directly from authorized manufacturers.",
        "category": "product"
    },
    {
        "question": "Do you provide bulk discounts?",
        "answer": "Yes, we offer special discounts for bulk orders. Please contact our sales team for a customized quote.",
        "category": "pricing"
    },
    {
        "question": "What are your business hours?",
        "answer": "We are open Monday to Saturday, 9:00 AM to 7:00 PM. Closed on Sundays and public holidays.",
        "category": "general"
    },
    {
        "question": "How can I track my order?",
        "answer": "You will receive a tracking number via SMS/email once your order is dispatched. You can use this to track your order.",
        "category": "delivery"
    }
]

def get_all_faqs():
    """Return all FAQs"""
    return FAQS

def search_faq(query):
    """Search FAQ by question or answer"""
    query = query.lower()
    results = []
    for faq in FAQS:
        if query in faq['question'].lower() or query in faq['answer'].lower():
            results.append(faq)
    return results

def get_faqs_by_category(category):
    """Get FAQs by category"""
    return [faq for faq in FAQS if faq['category'].lower() == category.lower()]