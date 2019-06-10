import qrcode
from PIL import Image, ImageDraw, ImageFilter
import os

TARGET_DIR = "QRs"
if not os.path.isdir(TARGET_DIR):
    os.makedirs(TARGET_DIR)


def crop_center(pil_img, crop_width, crop_height):
    img_width, img_height = pil_img.size
    return pil_img.crop(((img_width - crop_width) // 2,
                         (img_height - crop_height) // 2,
                         (img_width + crop_width) // 2,
                         (img_height + crop_height) // 2))


def crop_max_square(pil_img):
    return crop_center(pil_img, min(pil_img.size), min(pil_img.size))


def mask_circle_solid(pil_img, background_color, blur_radius, offset=0):
    background = Image.new(pil_img.mode, pil_img.size, background_color)

    offset = blur_radius * 2 + offset
    mask = Image.new("L", pil_img.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((offset, offset, pil_img.size[0] - offset, pil_img.size[1] - offset), fill=255)
    mask = mask.filter(ImageFilter.GaussianBlur(blur_radius))

    return Image.composite(pil_img, background, mask)


text = input("text: ")
color = input("color: ")
back_color = input("back_color: ")
fname = input("filename: ")

qr = qrcode.QRCode(
    error_correction=qrcode.constants.ERROR_CORRECT_L,
)

qr.add_data(text)
qr.make()
img = qr.make_image()
img.save('QRs\\qrcode.png')

qr = qrcode.QRCode(
    error_correction=qrcode.constants.ERROR_CORRECT_Q,
)

qr.add_data(text)
qr.make()
color_img = qr.make_image(fill_color=color, back_color=back_color).convert('RGB')

color_img.save('QRs\\colored_qr.png')

qr = qrcode.QRCode(
    version=8,
    error_correction=qrcode.constants.ERROR_CORRECT_Q,
    box_size=3,
    border=6
)

img_qr = qr.make_image(fill_color=color, back_color=back_color).convert('RGB')

if fname != "":
    logo = Image.open(fname)
    logo = crop_max_square(logo).resize((40, 40), Image.LANCZOS)
    pos = ((img_qr.size[0] - logo.size[0]) // 2, (img_qr.size[1] - logo.size[1]) // 2)
    img_qr.paste(logo, pos)
    img_qr.save('QRs\\decorated_qr.png')
