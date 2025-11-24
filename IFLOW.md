# Django博客项目

## 项目概述

这是一个基于Django框架开发的博客系统，使用Python语言编写。项目包含用户认证、博客文章管理、评论功能等核心功能。

### 主要技术栈
- **后端框架**: Django 5.1.3
- **数据库**:  MySQL (生产环境)
- **前端**: HTML5, CSS3, JavaScript, Bootstrap 5
- **编辑器**: WangEditor (富文本编辑器)
- **邮件服务**: 163邮箱SMTP服务

### 项目结构
```
django_blog/
├── blog/                    # 博客应用
│   ├── models.py           # 博客文章模型
│   ├── views.py            # 视图逻辑
│   ├── urls.py             # URL路由
│   ├── forms.py            # 表单定义
│   └── admin.py            # 管理后台配置
├── zhiliaoauth/            # 用户认证应用
│   ├── models.py           # 用户模型
│   ├── views.py            # 认证视图
│   ├── urls.py             # 认证路由
│   └── forms.py            # 认证表单
├── django_blog/            # 项目配置
│   ├── settings.py         # 项目设置
│   ├── urls.py             # 主URL配置
│   └── wsgi.py             # WSGI配置
├── templates/              # HTML模板
│   ├── base.html           # 基础模板
│   ├── index.html          # 首页
│   ├── blog_detail.html    # 博客详情页
│   ├── login.html          # 登录页
│   ├── register.html       # 注册页
│   └── pub_blog.html       # 发布博客页
├── static/                 # 静态文件
│   ├── bootstrap5/         # Bootstrap框架
│   ├── css/                # 自定义CSS
│   ├── js/                 # JavaScript文件
│   ├── images/             # 图片资源
│   └── wangeditor/         # 富文本编辑器
├── db.sqlite3              # SQLite数据库文件
├── manage.py               # Django管理脚本
└── my.cnf                  # MySQL配置文件
```

## 构建和运行

### 环境准备
1. 确保已安装Python 3.8+
2. 安装Django依赖:
   ```bash
   pip install django
   pip install mysqlclient
   ```

### 数据库配置
项目支持SQLite和MySQL两种数据库:
- **开发环境**: 使用SQLite (db.sqlite3)
- **生产环境**: 使用MySQL (配置在my.cnf中)

### 常用命令

#### 数据库迁移
```bash
# 创建迁移文件
python manage.py makemigrations

# 应用迁移
python manage.py migrate
```

#### 运行开发服务器
```bash
python manage.py runserver
```

#### 创建超级用户
```bash
python manage.py createsuperuser
```

#### 收集静态文件
```bash
python manage.py collectstatic
```

## 开发规范

### 应用结构
- 每个Django应用包含models.py, views.py, urls.py, forms.py, admin.py
- 模型定义在models.py中，遵循Django ORM规范
- 视图逻辑在views.py中，使用类视图和函数视图
- URL配置在urls.py中，保持路由清晰

### 模板规范
- 使用Bootstrap 5框架进行响应式设计
- 基础模板为base.html，其他模板继承此模板
- 使用Django模板语言进行动态内容渲染

### 静态文件管理
- CSS文件存放在static/css/目录
- JavaScript文件存放在static/js/目录
- 图片资源存放在static/images/目录
- 第三方库(Bootstrap, jQuery等)存放在对应目录

### 数据库设计
- 使用Django ORM定义数据模型
- 模型字段命名使用下划线命名法
- 外键关系明确定义on_delete行为

### 安全考虑
- 使用Django内置的CSRF保护
- 用户密码使用Django的密码哈希机制
- 敏感配置信息(如邮箱密码)应使用环境变量

## 邮件配置

项目配置了163邮箱服务用于发送验证码:
- SMTP服务器: smtp.163.com
- 端口: 465 (SSL加密)
- 发件人: m15373522716@163.com

## 部署注意事项

1. 生产环境需要设置DEBUG=False
2. 配置ALLOWED_HOSTS为实际域名
3. 使用环境变量管理敏感信息
4. 配置生产级数据库(MySQL)
5. 设置静态文件服务
6. 配置HTTPS证书

## 扩展功能

项目预留了以下扩展接口:
- 博客评论系统
- 文章分类和标签
- 用户权限管理
- 文件上传功能
- 搜索功能