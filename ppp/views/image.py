import qrcode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data('Some data')
qr.make(fit=True)
x=47
img = qr.make_image(fill_color="black", back_color="white")
src = "../static/images/"+str(x)+".png"
img.save(src)


