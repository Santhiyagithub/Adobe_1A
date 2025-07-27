import fitz  # PyMuPDF

def extract_pdf_elements(path):
    doc = fitz.open(path)
    elements = []
    for i, page in enumerate(doc):
        blocks = page.get_text("dict")["blocks"]
        for b in blocks:
            for l in b.get("lines", []):
                for s in l.get("spans", []):
                    if s["text"].strip():
                        elements.append({
                            "text": s["text"].strip(),
                            "font_size": s["size"],
                            "font": s["font"],
                            "page": i + 1
                        })
    return elements
