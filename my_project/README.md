# 🛍️ Endee Luxe Discovery Engine  

**Built with grit and vectors by Pratik Prakash Tiwari**

---

## 👋 The "Why" Behind This Project  

Traditional search systems can be frustrating—if the exact keyword isn’t used, they often return *“No results found.”*  

This project aims to solve that problem by building an intelligent storefront that understands **user intent**, not just keywords.  

Whether a user searches:  
- *“I'm going to a cold place”*  
- *“I'm a coder who needs to stay awake”*  

The system interprets the meaning behind the query and suggests relevant products accordingly.

---

## 🧠 How the Magic Happens (System Design)  

This project is built using a **Dense Retrieval pipeline**, focusing on semantic similarity instead of keyword matching.

### 🔹 The Translator  
- Uses the **all-MiniLM-L6-v2 model**  
- Converts product descriptions into **384-dimensional vectors**  
- Captures semantic meaning instead of raw text  

### 🔹 The Memory  
- Powered by **Endee (Vector Database)**  
- Stores vector embeddings efficiently  
- Uses **Cosine Similarity** to find the closest matching products in real-time  

### 🔹 The Storefront  
- Built with **Streamlit**  
- Clean, dark-themed UI  
- Fast, interactive, and user-friendly  

---

## 🛠️ Behind the Scenes (Challenges & Learnings)  

Real-world engineering comes with challenges—and that’s where the learning happens.

### ⚡ The Hidden Schema  
- Faced undocumented quirks in Endee v0.1.17  
- Discovered metadata needed to be stored under a specific `meta` key  
- Used Python logging to debug and understand internal structure  

### ⚡ The Parameter Pivot  
- Bridged traditional DB limits with ML search needs  
- Implemented **top_k retrieval logic** for better results  

### ⚡ UI Resilience  
- Built a **flexible-key system** in frontend  
- Ensures stability even if API response structure changes  

---

## 🚀 Get the Store Running  

### 1️⃣ Prerequisites  
- Python **3.10+**  
- Docker installed and running  

---

### 2️⃣ Start the Vector Database  

```bash
docker pull endee/endee:latest
docker run -p 8080:8080 endee/endee:latest
```

---

### 3️⃣ Install Dependencies  
```bash
pip install -r requirements.txt  
```

---

### 4️⃣ Load Product Data  

```bash
python ingest_products.py
```

---

### 5️⃣ Run the Application
```bash
streamlit run app.py
```
---

## 📸 Example Use Case  

Even with a complex query like:  

> “I'm going to a cold place”  

The system intelligently prioritizes relevant items like:  

- THermal Wool Socks  
- Acoustic Guitar

### 🖼️ Demo Preview  
![Smart Shopper Demo](my_project\screenshots\Screenshot 2026-03-18 000955.png)

---

---

## 📬 Let's Connect!  

I’m **Pratik Prakash Tiwari**, passionate about building intelligent systems that make technology feel more human and intuitive. 🚀  

- 🔗 LinkedIn: https://www.linkedin.com/in/tiwaripratik222  
- 📧 Email: tiwaripratik222@gmail.com  

---

⭐ If you found this project interesting, consider giving it a star and connecting with me!
