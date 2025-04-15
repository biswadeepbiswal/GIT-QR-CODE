import qrcode
import qrcode.image.pil
import qrcode.constants
from PIL import Image  

qr = qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_H,
                   box_size=10, border=4)
qr.add_data("https://github.com/biswadeepbiswal")
qr.make(fit=True)
img = qr.make_image(fill_color="blue", back_color="black")
img.save("git_qrcode.png")
