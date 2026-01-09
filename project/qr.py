import qrcode

# Data to encode
data = "https://www.google.com"

# Create a QR Code instance
qr = qrcode.QRCode(
    version=1,  # size of the QR code (1 to 40), 1 is the smallest
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # error correction level
    box_size=10,  # size of each box in pixels
    border=4,  # thickness of the border (default is 4)
)

# Add data to the instance
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR Code instance
img = qr.make_image(fill_color="black", back_color="white")

# Save the image
img.save("qrcode.png")

print("QR Code generated and saved as qrcode.png")
