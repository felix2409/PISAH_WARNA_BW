import fitz
from pypdf import PdfReader, PdfWriter

def is_color_page(page):
    pix = page.get_pixmap()
    img_data = pix.samples
    step = pix.n

    total_pixel = len(img_data) // step
    warna = 0
    grayscale = 0

    for i in range(0, len(img_data), step * 10):
        r = img_data[i]
        g = img_data[i + 1]
        b = img_data[i + 2]
        if r == g == b:
            grayscale += 1
        else:
            warna += 1

    return warna > (grayscale + warna) * 0.01

def split_pdf_by_color(input_pdf, output_color='warna.pdf', output_bw='hitamputih.pdf'):
    doc = fitz.open(input_pdf)
    reader = PdfReader(input_pdf)
    writer_color = PdfWriter()
    writer_bw = PdfWriter()

    for i, page in enumerate(doc):
        pdf_page = reader.pages[i]
        if is_color_page(page):
            writer_color.add_page(pdf_page)
        else:
            writer_bw.add_page(pdf_page)

    with open(output_color, "wb") as f:
        writer_color.write(f)
    with open(output_bw, "wb") as f:
        writer_bw.write(f)
