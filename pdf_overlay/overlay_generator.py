import io
from reportlab.pdfgen import canvas
from PyPDF2 import PdfReader, PdfWriter

BASE_PDF = "pdf_templates/affidavit_background1.pdf"
FONT = "Times-Bold"
FONT_SIZE = 11

SHOW_GRID = False   # ← SET True ONLY FOR DEBUG


def draw_grid(can, width, height, step=50):
    can.setFont("Times-Bold", 6)
    for x in range(0, int(width), step):
        can.drawString(x + 2, height - 10, str(x))
        can.line(x, 0, x, height)
    for y in range(0, int(height), step):
        can.drawString(2, y + 2, str(y))
        can.line(0, y, width, y)


def place(can, w, h, x_pct, y_pct, text):
    """
    x_pct, y_pct are percentages (0–100)
    """
    x = w * (x_pct / 100)
    y = h * (y_pct / 100)
    can.drawString(x, y, text)


def generate_filled_affidavit(data, output_path):
    base_reader = PdfReader(BASE_PDF)
    base_page = base_reader.pages[0]

    width = float(base_page.mediabox.width)
    height = float(base_page.mediabox.height)

    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=(width, height))
    can.setFont(FONT, FONT_SIZE)

    # 🔍 OPTIONAL GRID FOR CALIBRATION
    if SHOW_GRID:
        draw_grid(can, width, height)

    # ✅ FINAL RELATIVE POSITIONS (STABLE)
    place(can, width, height, 26, 77, data["name"])
    place(can, width, height, 20, 74.5, data["father_name"])
    place(can, width, height, 52, 74.5, data["address"])
    place(can, width, height, 26, 69.5, data["dob"])

    place(can, width, height, 31, 61.5, data["father_name"])
    place(can, width, height, 33, 59, data["mother_name"])
    place(can, width, height, 36, 56.5, data["spouse_name"])

    place(can, width, height, 67, 54, data["residence_from"])

    place(can, width, height, 18, 16.5, data["place"])
    place(can, width, height, 18, 14, data["date"])

    can.save()
    packet.seek(0)

    overlay_pdf = PdfReader(packet)
    overlay_page = overlay_pdf.pages[0]

    writer = PdfWriter()
    base_page.merge_page(overlay_page)
    writer.add_page(base_page)

    with open(output_path, "wb") as f:
        writer.write(f)
