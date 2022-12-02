import qrcode
from PIL import Image

def createqr(text):
    logo = Image.open("img/tic_logo.jpg")

    # taking base width
    basewidth = 100

    # adjust image size
    wpercent = (basewidth/float(logo.size[0]))
    hsize = int((float(logo.size[1])*float(wpercent)))
    logo = logo.resize((basewidth, hsize), Image.Resampling.LANCZOS)
    QRcode = qrcode.QRCode(
        error_correction=qrcode.constants.ERROR_CORRECT_H
    )

    # adding URL or text to QRcode
    QRcode.add_data(text)

    # generating QR code
    QRcode.make(fit=True)

    # taking color name from user
    QRcolor = 'black'

    # adding color to QR code
    QRimg = QRcode.make_image(
        fill_color=QRcolor, back_color="white").convert('RGB')

    # set size of QR code
    pos = ((QRimg.size[0] - logo.size[0]) // 2,
        (QRimg.size[1] - logo.size[1]) // 2)
    QRimg.paste(logo, pos)

    QRimg.save('img/ticit_QR.png')
        
    respond = 'QR code generated!'
    print(respond)

