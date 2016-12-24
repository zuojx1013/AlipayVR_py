#支付宝VR红包图片生成 成功率60%左右

from PIL import Image, ImageFilter

im = Image.open("IMG_2704.PNG")

box = im.copy()
box = (200, 630, 550, 980) #适配iPhone6屏幕.其他手机屏幕修改参数
region = im.crop(box)


boder = 6  #修改位移数值
box1 = im.copy()
box1= (200, 630+boder, 550, 980+boder)
region1 = im.crop(box1)

res = Image.blend(region,region1,0.5)


# 高斯模糊
class MyGaussianBlur(ImageFilter.Filter):
    name = "GaussianBlur"

    def __init__(self, radius=2, bounds=None):
        self.radius = radius
        self.bounds = bounds

    def filter(self, image):
        if self.bounds:
            clips = image.crop(self.bounds).gaussian_blur(self.radius)
            image.paste(clips, self.bounds)
            return image
        else:
            return image.gaussian_blur(self.radius)

bounds = (0, 0, 340, 340)
image = res
image = image.filter(MyGaussianBlur(radius=2.5, bounds=bounds))  #radius=模糊系数
image.show()
