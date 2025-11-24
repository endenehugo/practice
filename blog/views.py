from django.shortcuts import render,reverse,redirect
# 判断用户是否登录
from django.contrib.auth.decorators import login_required
# 加载完整个项目之后再判断
from django.urls.base import reverse_lazy
from django.views.decorators.http import require_http_methods,require_POST,require_GET
from django.http import JsonResponse
from .models import Blog, BlogCategory, BlogComment
from .forms import PubBlogForm
from django.db.models import Q

# Create your views here.
def index(request):
    blogs = Blog.objects.all()
    return render(request, 'index.html', {'blogs':blogs})


def blog_detail(request, blog_id):
    try:
        blog = Blog.objects.get(pk=blog_id)
    except Exception as e:
        blog = None
    return render(request, 'blog_detail.html', context={'blog':blog})


@require_http_methods(['GET','POST'])
@login_required(login_url=reverse_lazy('zhiliaoauth:login'))
# @login_required(login_url='/auth/login') #更简单
# @login_required() 再在settings中设置LOGIN_URL,可以直接使用
# @login_required()
def pub_blog(request):
    # get渲染页面
    if request.method == 'GET':
        categories = BlogCategory.objects.all()
        return render(request,'pub_blog.html', context={"categories":categories})
    # post 进行表单验证渲染页面
    else:
        form = PubBlogForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            content = form.cleaned_data.get('content')
            category_id = form.cleaned_data.get('category')
            # 保存到数据库
            blog = Blog.objects.create(title=title,content=content,category_id=category_id, author=request.user)
            return JsonResponse({"code": 200, "message": "博客发布成功", "data": {"blog_id":blog.id}})
        else:
            print(form.errors)
            return JsonResponse({"code": 400, "message": "参数错误"})


@require_POST
@login_required(login_url=reverse_lazy('zhiliaoauth:login'))
def pub_comment(request):
    blog_id = request.POST.get('blog_id')
    content = request.POST.get('content')
    BlogComment.objects.create(content=content,blog_id=blog_id,author=request.user)
    return redirect(reverse('blog:blog_detail',kwargs={'blog_id':blog_id}))


@require_GET
def search(request):
    # /search?q=xxx
    q = request.GET.get('q')
    # 从博客的标题和内容中搜索
    blogs = Blog.objects.filter(Q(title__icontains=q) | Q(content__icontains=q)).all()
    return render(request,'index.html', context={"blogs":blogs})