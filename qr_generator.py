import qrcode

# Replace with your data URL
data_url = "data:text/html;base64,DATAURL_OBTAINED"

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(data_url)
qr.make(fit=True)


img = qr.make_image(fill_color="black", back_color="white")
img.save("qr.png")
