from captcha.image import ImageCaptcha
import random

image = ImageCaptcha(width=180, height=90)

def captchaGenerator():
    captchaKey = str(random.randint(100000,1000000))

    image.generate(captchaKey)

    captchaKeyName = captchaKey + '.png'

    img_path = 'captchaExamples' + '/' + captchaKeyName

    image.write(captchaKey,img_path)
    
the_amount  = int(input('Please enter the amount you want to : '))
    
for i in range(the_amount):
    captchaGenerator()
    
print("captchaGenerator generated",the_amount,"images successfully")