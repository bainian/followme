import pytesseract
from PIL import Image

img = Image.open('../sfz1.jpg')
img = img.rotate(90)
gray = img.convert('L')
gray.save('captcha_gray.jpg')
# print('width %s height %s ' % (gray.width, gray.height))
# box = (280, 600, 1400, 900)
# gray = gray.crop(box)
bw = gray.point(lambda z: 0 if z < 125 else 255, '1')
bw.save('captcha_thresholded.jpg')

string = pytesseract.image_to_string(bw)
r = ''.join(c for c in string if c in ' 1234567890')
print(r.strip())
