# ---------------------------------------------------------
# Project: Endee Luxe Discovery Engine
# Author:  Pratik Prakash Tiwari
# Stack:   Python, Streamlit, Sentence-Transformers, Endee DB
# Date:    March 2026
#
# Technical Identity Note: 
# This implementation was developed to bridge the gap between 
# raw vector storage and high-utility consumer search, 
# resolving specific v0.1.17 SDK mapping challenges.
# ---------------------------------------------------------
from endee import Endee
from sentence_transformers import SentenceTransformer
import uuid

client = Endee("127.0.0.1:8080")
model = SentenceTransformer('all-MiniLM-L6-v2')

# Expanded Inventory
products = [
    # Winter/Cold
    {"name": "Arctic Expedition Parka", "desc": "Sub-zero protection with down filling and fur hood.", "price": "$450"},
    {"name": "Thermal Wool Socks", "desc": "Keep your feet warm in the harshest winter blizzards.", "price": "$25"},
    {"name": "Alpine Ski Goggles", "desc": "Anti-fog lenses for high-altitude mountain visibility.", "price": "$120"},
    # Professional/Tech
    {"name": "Executive Leather Briefcase", "desc": "Sleek Italian leather for the modern professional.", "price": "$299"},
    {"name": "Ergonomic Mechanical Keyboard", "desc": "Type all day with tactile switches and wrist support.", "price": "$150"},
    {"name": "4K Ultra-Wide Monitor", "desc": "Massive screen real estate for designers and coders.", "price": "$600"},
    # Fitness/Summer
    {"name": "Quick-Dry Gym Shirt", "desc": "Moisture-wicking fabric for intense cardio sessions.", "price": "$40"},
    {"name": "Smart Fitness Tracker", "desc": "Monitor your heart rate, steps, and sleep patterns.", "price": "$130"},
    {"name": "Polarized Aviator Shades", "desc": "Classic style with UV protection for sunny beach days.", "price": "$80"},
    # Home/Lifestyle
    {"name": "Espresso Machine Pro", "desc": "Barista-quality coffee at the touch of a button.", "price": "$850"},
    {"name": "Silk Weighted Blanket", "desc": "Deep pressure therapy for a better night's sleep.", "price": "$180"},
    {"name": "Acoustic Guitar", "desc": "Rich, warm tones for campfire songs and studio recording.", "price": "$550"}
]

print("Wiping old data for a fresh start...")
try: client.delete_index("store_items")
except: pass

client.create_index("store_items", dimension=384, space_type="cosine")
store_index = client.get_index("store_items")

print(f"Ingesting {len(products)} luxury items...")
for p in products:
    vector = model.encode(p['desc']).tolist()
    store_index.upsert([{
        "id": str(uuid.uuid4()),
        "vector": vector,
        "meta": p
    }])

print("✅ Catalog fully loaded. The store is open!")