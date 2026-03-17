"""
Extract images from the reference PDF and save to assets folder.
"""
import os

try:
    import fitz  # PyMuPDF
    pdf_path = r"c:\Users\HAMID KAMAL\Downloads\bcom final year research project\project reference.pdf"
    assets_dir = r"c:\Users\HAMID KAMAL\Downloads\bcom final year research project\assets"
    os.makedirs(assets_dir, exist_ok=True)

    doc = fitz.open(pdf_path)
    img_count = 0
    for page_num, page in enumerate(doc):
        images = page.get_images(full=True)
        for img_index, img in enumerate(images):
            xref = img[0]
            base_image = doc.extract_image(xref)
            img_bytes = base_image["image"]
            ext = base_image["ext"]
            out_path = os.path.join(assets_dir, f"ref_img_{page_num}_{img_index}.{ext}")
            with open(out_path, "wb") as f:
                f.write(img_bytes)
            print(f"Saved: {out_path} ({len(img_bytes)} bytes)")
            img_count += 1
    print(f"\nTotal images extracted: {img_count}")
except ImportError:
    print("PyMuPDF not found. Installing...")
    os.system("pip install pymupdf")
    print("Please run this script again after installation.")
