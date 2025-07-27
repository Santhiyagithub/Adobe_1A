import os
import json
from utils.pdf_parser import extract_pdf_elements
from utils.heading_detector import detect_hierarchy

INPUT_DIR = "/app/input"
OUTPUT_DIR = "/app/output"

def process_pdf_files():
    for filename in os.listdir(INPUT_DIR):
        if filename.endswith(".pdf"):
            filepath = os.path.join(INPUT_DIR, filename)
            elements = extract_pdf_elements(filepath)
            title, outline = detect_hierarchy(elements)

            output_data = {
                "title": title,
                "outline": outline
            }

            output_filename = os.path.splitext(filename)[0] + ".json"
            output_path = os.path.join(OUTPUT_DIR, output_filename)

            with open(output_path, "w") as f:
                json.dump(output_data, f, indent=2)

if __name__ == "__main__":
    process_pdf_files()
