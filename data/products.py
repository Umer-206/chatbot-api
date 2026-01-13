"""
Product Data Module
Contains all product information
"""

PRODUCTS = [
    {
        "id": 1,
        "code": "02020009",
        "name": "Uritrac Sachet",
        "pack": "10s",
        "mrp": 300.00,
        "gst": 18,
        "category": "Sachet"
    },
    {
        "id": 2,
        "code": "02030001",
        "name": "Vaneka Cream",
        "pack": "15ml",
        "mrp": 560.00,
        "gst": 25,
        "category": "Cream"
    },
    {
        "id": 3,
        "code": "02030011",
        "name": "Vaneka Cream",
        "pack": "50ml",
        "mrp": 1200.00,
        "gst": 25,
        "category": "Cream"
    },
    {
        "id": 4,
        "code": "02030031",
        "name": "Vita Age Cracked Hand, Footcare Cream",
        "pack": "30ml",
        "mrp": 499.00,
        "gst": 25,
        "category": "Cream"
    },
    {
        "id": 5,
        "code": "02030033",
        "name": "Vita Age Glow And Anti Aging Cream",
        "pack": "30ml",
        "mrp": 960.00,
        "gst": 25,
        "category": "Cream"
    },
    {
        "id": 6,
        "code": "02030002",
        "name": "Vita Age Mamma Cream",
        "pack": "100ml",
        "mrp": 1320.00,
        "gst": 25,
        "category": "Cream"
    },
    {
        "id": 7,
        "code": "02030022",
        "name": "Vita Age Mamma Cream",
        "pack": "50ml",
        "mrp": 640.00,
        "gst": 25,
        "category": "Cream"
    },
    {
        "id": 8,
        "code": "02020010",
        "name": "Vitkal Plus Tablet",
        "pack": "10s",
        "mrp": 180.00,
        "gst": 18,
        "category": "Tablet"
    },
    {
        "id": 9,
        "code": "02020011",
        "name": "Vitkal Plus Tablet",
        "pack": "30s",
        "mrp": 850.00,
        "gst": 18,
        "category": "Tablet"
    },
    {
        "id": 10,
        "code": "02020012",
        "name": "Vitkalplus Sachet",
        "pack": "10s",
        "mrp": 254.20,
        "gst": 18,
        "category": "Sachet"
    },
    {
        "id": 11,
        "code": "02020013",
        "name": "Anselax",
        "pack": "10s",
        "mrp": 1200.00,
        "gst": 18,
        "category": "Tablet"
    },
    {
        "id": 12,
        "code": "02020014",
        "name": "B ARGIE",
        "pack": "10s",
        "mrp": 255.00,
        "gst": 18,
        "category": "Tablet"
    },
    {
        "id": 13,
        "code": "02020015",
        "name": "BRISCAL SACHET",
        "pack": "10s",
        "mrp": 85.00,
        "gst": 18,
        "category": "Sachet"
    },
    {
        "id": 14,
        "code": "02020016",
        "name": "MayCal",
        "pack": "10s",
        "mrp": 110.00,
        "gst": 18,
        "category": "Tablet"
    },
    {
        "id": 15,
        "code": "02020017",
        "name": "Azonam Injection 1G",
        "pack": "1s",
        "mrp": 1200.00,
        "gst": 1,
        "category": "Injection"
    },
    {
        "id": 16,
        "code": "02020018",
        "name": "DIPROFOL 10MG/ML",
        "pack": "5s",
        "mrp": 3060.00,
        "gst": 1,
        "category": "Injection"
    },
    {
        "id": 17,
        "code": "02010048",
        "name": "Limet Infusion",
        "pack": "1s",
        "mrp": 784.00,
        "gst": 0,
        "category": "Infusion"
    },
    {
        "id": 18,
        "code": "02010046",
        "name": "Limet Tablet",
        "pack": "12s",
        "mrp": 1650.00,
        "gst": 1,
        "category": "Tablet"
    },
    {
        "id": 19,
        "code": "02020021",
        "name": "Vasparin 25000IU/5ml Heparin Sodium",
        "pack": "1s",
        "mrp": 1344.00,
        "gst": 1,
        "category": "Injection"
    },
    {
        "id": 20,
        "code": "02020022",
        "name": "Isphagol 25gm Pack",
        "pack": "1s",
        "mrp": 180.00,
        "gst": 18,
        "category": "Powder"
    },
    {
        "id": 21,
        "code": "02020023",
        "name": "Isphagol 4gm Sachet",
        "pack": "24s Hanger",
        "mrp": 720.00,
        "gst": 18,
        "category": "Sachet"
    },
    {
        "id": 22,
        "code": "02020024",
        "name": "Isphagol 50gm Pack",
        "pack": "1s",
        "mrp": 325.00,
        "gst": 18,
        "category": "Powder"
    },
    {
        "id": 23,
        "code": "02020025",
        "name": "Isphagol 95gm Pack",
        "pack": "1s",
        "mrp": 675.00,
        "gst": 18,
        "category": "Powder"
    }
]

def get_all_products():
    """Return all products"""
    return PRODUCTS

def search_product(query):
    """Search product by name"""
    query = query.lower()
    return [p for p in PRODUCTS if query in p['name'].lower()]

def get_product_by_id(product_id):
    """Get product by ID"""
    for p in PRODUCTS:
        if p['id'] == product_id:
            return p
    return None

def get_products_by_category(category):
    """Get products by category"""
    return [p for p in PRODUCTS if p['category'].lower() == category.lower()]