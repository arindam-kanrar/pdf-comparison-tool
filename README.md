# 📄 PDF Comparison Tool

A Streamlit web app to compare two PDF files and highlight the textual differences using color-coded changes. Ideal for engineers, editors, or researchers reviewing document revisions.

---

## ✨ Features

- ✅ Upload two PDF files for comparison
- 🟩 Highlights **additions** in green
- 🟥 Highlights **deletions** in red
- 🟨 Highlights **modifications** in yellow
- 📊 Summary report showing count of changes

---

## 📦 Tech Stack

- [Streamlit](https://streamlit.io/) – for frontend UI
- [pdfplumber](https://github.com/jsvine/pdfplumber) – for text extraction
- Python’s built-in `difflib` – for text comparison

---

## 🚀 Getting Started

### 1. Clone the repo



```bash
git clone https://github.com/arindam-kanrar/pdf-comparison-tool.git
cd pdf-comparison-tool

```

To RUN :
1. pip install -r requirements.txt
2. streamlit run app.py
