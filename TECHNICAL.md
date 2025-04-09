# 📄 TECHNICAL.md — Technical Documentation

## 📘 Project: PDF Comparison Tool  
A web-based app to compare two PDF documents and highlight textual changes using a user-friendly interface.

---

## 1. 🧠 Approach

The tool follows a simple but effective pipeline:

1. **File Upload via Streamlit UI**  
   - Users upload two PDF documents (original and modified).

2. **Text Extraction**  
   - `pdfplumber` is used to extract readable text from each PDF page.
   - For scanned (image-based) PDFs, optional OCR support via `pytesseract` and `pdf2image` is suggested.

3. **Text Comparison**  
   - Python's `difflib.Differ` compares the extracted texts line by line.
   - Results are classified as:
     - Additions (`+`): New content in the modified PDF
     - Deletions (`-`): Removed content
     - Modifications (`?`): Line-level edits

4. **Visualization**  
   - Using Streamlit's markdown + HTML rendering, changes are color-coded:
     - 🟩 Green for additions
     - 🟥 Red for deletions
     - 🟨 Yellow for modified lines

5. **Summary Generation**  
   - The app counts and reports the number of changes by category (added/removed/modified).

---

## 2. 🧰 Libraries Used & Rationale

| Library        | Purpose                                            | Reason |
|----------------|----------------------------------------------------|--------|
| `streamlit`    | UI/Frontend                                         | Easy to build and share interactive apps |
| `pdfplumber`   | Text extraction from PDF                            | Accurate for extracting structured text from native PDFs |
| `difflib`      | Text comparison                                     | Native, efficient, and readable diffs |
| `pytesseract`  | OCR (optional)                                      | To handle image-based PDFs |
| `pdf2image`    | Convert scanned PDF pages to images for OCR        | Enables Tesseract to work on scanned pages |
| `Pillow`       | Image preprocessing for OCR                         | Compatible with pdf2image |

---

## 3. 💡 Challenges & How They Were Handled

| Challenge                               | Solution |
|----------------------------------------|----------|
| Some PDFs had missing or unreadable text | Added fallback OCR logic (planned for future extension) |
| Differ output was too verbose           | Parsed and filtered only meaningful changes |
| HTML rendering in Streamlit             | Used `unsafe_allow_html=True` carefully to display styled diffs |
| Matching modified lines                 | `difflib` `?` lines are used to detect line-level modifications |

---

## 4. 🚀 Potential Improvements

1. **OCR Integration**  
   Add built-in OCR pipeline to support scanned/image-only PDFs.

2. **Side-by-Side Comparison**  
   Display both versions next to each other for a more traditional diff view.

3. **Exportable Diff Report**  
   Generate and download a report as a new highlighted PDF or HTML file.

4. **Word-Level Diff**  
   Enhance accuracy by using word-level or token-based diffing instead of line-level.

5. **Performance Optimization**  
   Parallelize extraction/comparison for larger PDFs.

---

## 5. 🔧 Setup Notes

- Python 3.8+
- Make sure `poppler` is installed for `pdf2image` (needed for OCR):
  ```bash
  sudo apt-get install poppler-utils
