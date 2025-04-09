import streamlit as st
import pdfplumber
import difflib
from io import BytesIO
from collections import Counter

# Set page config
st.set_page_config(page_title="PDF Comparison Tool", layout="wide")

st.title("📄 PDF Comparison Tool")
st.markdown("Upload two PDF documents to compare their text content and highlight the differences.")

# --- Helper Functions ---
def extract_text_from_pdf(uploaded_file):
    with pdfplumber.open(uploaded_file) as pdf:
        text = "\n".join(page.extract_text() or "" for page in pdf.pages)
    return text

def generate_diff(old_text, new_text):
    old_lines = old_text.splitlines()
    new_lines = new_text.splitlines()
    d = difflib.Differ()
    diff = list(d.compare(old_lines, new_lines))
    return diff

def highlight_diff(diff):
    result_html = ""
    counts = Counter({"added": 0, "removed": 0, "modified": 0})
    for line in diff:
        tag = line[:2]
        content = line[2:].strip()
        if tag == "+ ":
            result_html += f'<div style="background-color:#d4f8d4;">+ {content}</div>'
            counts["added"] += 1
        elif tag == "- ":
            result_html += f'<div style="background-color:#ffd6d6;">- {content}</div>'
            counts["removed"] += 1
        elif tag == "? ":
            result_html += f'<div style="background-color:#fffac8;">? {content}</div>'
            counts["modified"] += 1
        else:
            result_html += f'<div>{line}</div>'
    return result_html, counts

# --- File Upload ---
col1, col2 = st.columns(2)

with col1:
    pdf1 = st.file_uploader("Upload Original PDF", type=["pdf"], key="pdf1")

with col2:
    pdf2 = st.file_uploader("Upload Modified PDF", type=["pdf"], key="pdf2")

# --- Compare PDFs ---
if pdf1 and pdf2:
    with st.spinner("Extracting text..."):
        text1 = extract_text_from_pdf(BytesIO(pdf1.read()))
        text2 = extract_text_from_pdf(BytesIO(pdf2.read()))

    st.subheader("🔍 Comparison Results")
    diff = generate_diff(text1, text2)
    diff_html, summary_counts = highlight_diff(diff)

    st.markdown("### 📝 Changes Summary")
    st.write(f"- 🟩 Additions: **{summary_counts['added']}**")
    st.write(f"- 🟥 Deletions: **{summary_counts['removed']}**")
    st.write(f"- 🟨 Modifications: **{summary_counts['modified']}**")

    st.markdown("### 📑 Differences Highlighted")
    st.markdown(diff_html, unsafe_allow_html=True)

else:
    st.info("Please upload both PDFs to begin comparison.")
