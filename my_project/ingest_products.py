from endee import Endee
from sentence_transformers import SentenceTransformer
import uuid

# 1. Initialize Client
client = Endee("127.0.0.1:8080")
model = SentenceTransformer('all-MiniLM-L6-v2')

# 2. Get the Index Object (This is where the 'upsert' method lives!)
print("Connecting to index...")
try:
    # Try to get the index if it exists
    store_index = client.get_index("store_items")
except Exception:
    # Create it if it doesn't
    client.create_index("store_items", dimension=384, space_type="cosine")
    store_index = client.get_index("store_items")

# 3. Product Catalog
products = [
    {"name": "Ultra-Warm Parka", "desc": "Heavy winter jacket for sub-zero temperatures.", "price": "$120"},
    {"name": "Breathable Running Shoes", "desc": "Lightweight footwear for marathons and jogging.", "price": "$85"},
    {"name": "Waterproof Umbrella", "desc": "Compact wind-resistant umbrella for rainy weather.", "price": "$25"},
    {"name": "Sun-Protection Hat", "desc": "Wide-brimmed hat perfect for beach days and summer heat.", "price": "$15"},
    {"name": "Noise-Canceling Headphones", "desc": "Over-ear headphones for deep focus and travel.", "price": "$200"}
]

# 4. Use the index object to upsert
print("Adding products to Endee...")
for p in products:
    vector = model.encode(p['desc']).tolist()
    # Notice we are calling store_index.upsert, NOT client.upsert
    store_index.upsert({
        "id": str(uuid.uuid4()),
        "vector": vector,
        "metadata": p
    })

print("✅ Store is stocked!")