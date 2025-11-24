import string
import random
from django.shortcuts import render,redirect,reverse
from django.http import JsonResponse
from django.core.mail import send_mail
from .models import CaptchaModel
from django.views.decorators.http import require_http_methods
from .forms import RegisterForm,LoginForm
from django.contrib.auth import get_user_model,login,logout
User = get_user_model()
# Create your views here.

@require_http_methods(['GET','POST'])
def zllogin(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            remember = form.cleaned_data.get('remember')
            user = User.objects.filter(email=email).first()
            if user and user.check_password(password):
                # 登录
                login(request,user)
                # user.is_authenticated
                #判断是否记住登录
                if not remember:
                    # 如果没有记住登录，就设置session的过期时间为0
                    request.session.set_expiry(0)
                # 如果点击了记住登录，就设置session的过期时间为2周
                return redirect('/')
            else:
                print('邮箱或密码错误')
                # form.add_error('email','邮箱或密码错误')
                # return render(request,'login.html',{'form':form})
                return redirect(reverse('zhiliaoauth:login'))

def zllogout(request):
    logout(request)
    return redirect('/')
@require_http_methods(['GET', 'POST'])
def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        form = RegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            User.objects.create_user(email=email,username=username,password=password)
            return redirect(reverse('zhiliaoauth:login'))
        else:
            print(form.errors)
            # 重新跳转到注册页面
            return redirect(reverse('zhiliaoauth:register'))
            # return render(request, 'register.html', {'form': form})

def send_email_captcha(request):
    email = request.GET.get('email')
    if not email:
        return JsonResponse({'code': 400, 'msg': '请输入邮箱'})
    # 生成验证码
    captcha = ''.join(random.sample(string.digits,k=4))
    # 存到数据库
    CaptchaModel.objects.update_or_create(email=email,defaults={'captcha':captcha} )
    send_mail('测试验证码',message=f'您的验证码是{captcha}',from_email=None, recipient_list=[email])


    return JsonResponse({'code': 200, 'msg': '验证码发送成功'})