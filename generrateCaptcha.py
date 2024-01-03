from captcha.image import ImageCaptcha
import random

image = ImageCaptcha(width=180, height=90) # 이미지 사이즈

def captchaGenerator():                                 #이미지 생성 함수
    captchaKey = str(random.randint(100000,1000000))    #이미지에 들어갈 숫자 범위 지정과 램덤으로 수 생성

    image.generate(captchaKey)

    captchaKeyName = captchaKey + '.png'

    img_path = 'captchaExamples' + '/' + captchaKeyName

    image.write(captchaKey,img_path)
    
the_amount  = int(input('Please enter the amount you want to : '))
    
for i in range(the_amount):
    captchaGenerator()
    
print("captchaGenerator generated",the_amount,"images successfully")