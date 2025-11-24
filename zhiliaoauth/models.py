from django.db import models

# Create your models here.
class CaptchaModel(models.Model):
    email = models.EmailField(unique=True, verbose_name='邮箱')
    captcha = models.CharField(max_length=4,verbose_name='验证码')
    created_time = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')