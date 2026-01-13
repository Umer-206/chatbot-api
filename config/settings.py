"""
Configuration Settings
"""

# Company Information
COMPANY_NAME = "Your Pharma Company"
SUPPORT_EMAIL = "support@yourcompany.com"
SUPPORT_PHONE = "+92-300-1234567"

# Groq Settings
GROQ_MODEL = "llama-3.3-70b-versatile"
GROQ_TEMPERATURE = 0.7
GROQ_MAX_TOKENS = 512

# Order Settings
MIN_ORDER_AMOUNT = 500  # Minimum order for free delivery
DELIVERY_CHARGE = 50    # Delivery charge below minimum

# Business Hours
BUSINESS_HOURS = {
    "monday": "9:00 AM - 7:00 PM",
    "tuesday": "9:00 AM - 7:00 PM",
    "wednesday": "9:00 AM - 7:00 PM",
    "thursday": "9:00 AM - 7:00 PM",
    "friday": "9:00 AM - 7:00 PM",
    "saturday": "9:00 AM - 7:00 PM",
    "sunday": "Closed"
}