from PIL import Image, ImageFilter, ImageEnhance
import pytesseract

# fp = open('file.jpg','rb')
img1 = Image.open('0633.JPG')  # 以后的操作都 是基于这个对象
print('format:%s\tsize:%s\tmode:%s' % (img1.format, img1.size, img1.mode))  # format:JPEG	size:(3024, 4032)	mode:RGB
# img1.show() #显示图像

copy_img = img1.rotate(-90, expand=1).resize((1920, 1080))  # 加上expand不然会有黑边,resize要的是一个tuple对象
copy_img.save('copy_temp.jpg')
box = (50, 600, 1800, 800)  # 一个区域
region = copy_img.crop(box)  # 复制这个区域图像到一个临时image对象中, img1对象 还在，可以操作的
# img1.show()
region.show()
region = region.convert('L')#.transpose(Image.ROTATE_90) # 镜像
region.save("temp_region.jpg")
content = pytesseract.image_to_string(region)
print('content:' ,content)

# r, g, b = region.split()  # r g b 三通道
# r.save('r.jpg')
# g.save('g.jpg')
# b.save('b.jpg')

# out = img1.filter(ImageFilter.BLUR)  # 图片加强滤镜
# out.save('filter.jpg')

# b = b.point(lambda i: i*0.5 if i< 100 else i * 1.5)  # 操作每个像素点
# b.save('b2.jpg')

# ehb = ImageEnhance.Contrast(b)
# ehb.enhance(1.5)
# ehb.save('ehb.jpg')

# Image.new(Image.ImageMode.getmode(Image.BICUBIC))

