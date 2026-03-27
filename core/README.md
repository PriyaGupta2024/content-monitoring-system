# 🛡️ Content Monitoring System (Django + DRF)

## 📌 Overview

This project is a **Content Monitoring System** that scans content based on predefined keywords and flags relevant content automatically.

It simulates how platforms detect and monitor content using keyword matching.

---

## 🚀 Features

* ✅ Add Keywords
* ✅ Scan Content (Mock Data)
* ✅ Calculate Relevance Score
* ✅ Auto Flag Creation
* ✅ View All Flags
* ✅ Update Flag Status (Pending / Relevant / Irrelevant)

---

## 🛠️ Tech Stack

* Backend: **Django**
* API: **Django REST Framework**
* Database: **SQLite**
* Testing Tool: **Postman**

---

## 📂 Project Structure

```
core/
│── models.py        # Database models
│── views.py         # API logic
│── serializers.py   # Data serialization
│── utils.py         # Helper functions (score calculation)
```

---

## 🧠 How It Works

1. User adds keywords (e.g., "django")
2. System scans content (mock data)
3. Keyword matching is performed
4. Score is calculated based on keyword frequency
5. Flags are created if content is relevant
6. User can update flag status

---

## 📌 API Endpoints

### 🔹 1. Add Keyword

**POST** `/keywords/`

```json
{
    "name": "django"
}
```

---

### 🔹 2. Scan Content

**POST** `/scan/`

➡️ Automatically processes content and creates flags

---

### 🔹 3. Get All Flags

**GET** `/flags/`

---

### 🔹 4. Update Flag Status

**PATCH** `/flags/{id}/`

```json
{
    "status": "relevant"
}
```

---

## 📊 Sample Workflow

1. Add keyword → `django`
2. Run scan API
3. System creates flags
4. Fetch flags using GET
5. Update status using PATCH

---

## 🧮 Scoring Logic

```python
def calculate_score(keyword, content):
    text = content.title + " " + content.body
    return text.lower().count(keyword.lower())
```

---

## 📸 Postman Testing

👉 Add your Postman screenshots here:

### 🔹 Keyword Creation

![Keyword API](result_imges\API_keywords.png)

### 🔹 Scan API

![Scan API](result_imges\API_scaning.png)

### 🔹 Get Flags

![Flags API](result_imges\API_flags.png)

### 🔹 Update Status

![Update API](result_imges\API_update.png)

---

## ⚠️ Important Notes

* Mock data is used for scanning
* Duplicate content may be created (can be optimized)
* Basic keyword matching is implemented

---

## 🚀 Future Improvements

* 🔥 AI/NLP-based content scoring
* 🔥 Duplicate flag prevention
* 🔥 Real-time content ingestion
* 🔥 React Dashboard
* 🔥 Authentication system

---

## 👩‍💻 Author

Priya Gupta

---

## ⭐ Conclusion

This project demonstrates:

* Backend API development
* Database design
* Content filtering logic
* Real-world problem solving

---
