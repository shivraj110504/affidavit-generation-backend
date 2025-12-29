from PIL import Image

img = Image.open("pdf_templates/affidavit_bg1.jpg")
img.save(
    "pdf_templates/affidavit_background.pdf",
    "PDF",
    resolution=300
)

print("Background PDF created successfully")
