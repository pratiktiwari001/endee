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
# -------------------------------------------------------
import streamlit as st
from endee import Endee
from sentence_transformers import SentenceTransformer

# 1. Page Configuration & Custom CSS
st.set_page_config(page_title="Endee Luxe Search", layout="wide", page_icon="🛍️")

st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #ff4b4b; color: white; }
    .product-card { 
        padding: 20px; 
        border-radius: 10px; 
        background-color: #1e2130; 
        border: 1px solid #3e4150;
        margin-bottom: 10px;
        height: 350px;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Resources
@st.cache_resource
def load_assets():
    model = SentenceTransformer('all-MiniLM-L6-v2')
    client = Endee("127.0.0.1:8080")
    index = client.get_index("store_items")
    return model, index

model, store_index = load_assets()

# 3. Sidebar for "Best Functioning"
with st.sidebar:
    st.title("⚙️ Search Settings")
    num_results = st.slider("Results to show", 3, 12, 6)
    st.info("This engine uses Vector Embeddings to understand your intent, not just keywords.")

# 4. Hero Section
st.title("🛍️ Endee Luxe Discovery")
query = st.text_input("Describe what you need...", placeholder="e.g. 'I need something for a professional meeting in a rainy city'")

if query:
    query_vec = model.encode(query).tolist()
    results = store_index.query(query_vec, top_k=num_results)

    if results:
        # Create a grid: 3 columns wide
        rows = [results[i:i + 3] for i in range(0, len(results), 3)]
        
        for row in rows:
            cols = st.columns(3)
            for i, res in enumerate(row):
                doc = res.get('meta', {})
                score = res.get('similarity', 0.0)
                
                with cols[i]:
                    with st.container():
                        st.markdown(f"### {doc.get('name', 'Product')}")
                        st.caption(f"Confidence: {score:.2f}")
                        st.write(doc.get('desc', '...'))
                        st.subheader(doc.get('price', 'Contact for Price'))
                        st.button("Add to Cart", key=f"btn_{doc.get('name')}_{i}")
                        st.markdown("---")
    else:
        st.error("No matches found in our luxury catalog.")