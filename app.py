from PIL import Image
from io import BytesIO

def convert_jpeg_to_pdf(jpeg_data):
    # Open the JPEG image using Pillow
    image = Image.open(BytesIO(jpeg_data))
    # Create a new PDF image with the same size as the JPEG
    pdf_image = Image.new('RGB', image.size, (255, 255, 255))
    # Paste the JPEG image into the PDF image
    pdf_image.paste(image, mask=image.split()[3])
    # Save the PDF image to a BytesIO buffer
    pdf_buffer = BytesIO()
    pdf_image.save(pdf_buffer, format='PDF')
    # Return the PDF data
    return pdf_buffer.getvalue()
