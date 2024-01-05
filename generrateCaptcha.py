from captcha.image import ImageCaptcha
import random

image = ImageCaptcha(width=180, height=90) # 이미지 사이즈

    
the_amount  = int(input('Please enter the amount you want to : '))


captchaKey = random.sample(range(100000,1000000),the_amount)

for unchangedStringCaptchaKey in captchaKey:
    
    changedStringCaptchaKey = str(unchangedStringCaptchaKey)
    
    image.generate(changedStringCaptchaKey)

    captchaKeyName = changedStringCaptchaKey + '.png'

    img_path = 'captchaExamples' + '/' + captchaKeyName

    image.write(changedStringCaptchaKey,img_path)

print("captchaGenerator generated",the_amount,"images successfully")