import streamlit as st
from endee import Endee
from sentence_transformers import SentenceTransformer

# 1. UI Setup
st.set_page_config(page_title="Endee Shopper", layout="wide")
st.title("🛍️ Smart Recommendation Engine")
st.markdown("Powered by **Endee Vector Database**")

# 2. Initialize Models & Connection
# Using st.cache_resource so it doesn't reload every time you click a button
@st.cache_resource
def load_resources():
    model = SentenceTransformer('all-MiniLM-L6-v2')
    client = Endee("127.0.0.1:8080")
    index = client.get_index("store_items")
    return model, index

model, store_index = load_resources()

# 3. User Input
query = st.text_input("What are you looking for?", placeholder="e.g., 'something for a rainy day'")

if query:
    with st.spinner("Searching for the best matches..."):
        # Convert text to vector
        query_vec = model.encode(query).tolist()
        
        # Search using the index object (not the client)
        try:
            # Try the most common name first
            results = store_index.query(query_vec, top_k=3)
        except AttributeError:
            try:
                # Try the alternative if 'query' doesn't exist
                results = store_index.search(vector=query_vec, top_k=3)
            except AttributeError:
                # The fallback for some 0.1.x versions
                results = store_index.search_index(query_vec, top_k=3)
        
        if results:
            st.subheader("Recommended for you:")
            cols = st.columns(3)
            
            for i, res in enumerate(results):
                # 1. Determine where the product data is
                if isinstance(res, dict):
                    doc = res.get('document', res.get('data', res.get('metadata', res)))
                    score = res.get('score', 0.0)
                else:
                    # If it's an object with attributes
                    doc = getattr(res, 'document', getattr(res, 'metadata', res))
                    score = getattr(res, 'score', 0.0)
    
                # 2. Display the card
                with cols[i]:
                    st.success(f"**{doc.get('name', 'Product')}**")
                    st.write(doc.get('desc', 'No description available.'))
                    st.button(f"Buy for {doc.get('price', 'N/A')}", key=f"btn_{i}")
                    st.caption(f"Match Confidence: {score:.2f}")
        else:
            st.warning("No matches found. Try describing your needs differently!")