"""
django问题描述：static文件夹配置
"""
网站通常需要其它文件，例如：图片、JavaScript 或者CSS。在Django 中，我们将这类文件统称为“静态文件”

Django 提供django.contrib.staticfiles 来帮助管理它们。

配置静态文件

在你的INSTALLED_APPS 中添加

django.contrib.staticfiles 

在你的settings 文件中定义STATIC_URL，例如：

STATIC_URL = '/static/'
"""
我个人理解的URL 相当于一个根目录，不管你的静态文件放置在哪里，你寻找的时候，都要从根出发
例如 
<a href="/static/index.html"></a>
<img class="fl" src="{% static 'images/logo.jpg' %}"/>

如果你的STATIC_URL = '/static_new/'  更改为这样，相应的，你的查询根也要改变  

<a href="/static_new/index.html"></a>
"""

在模板中，你可以硬编码
/static/my_app/myexample.jpg 这样的URL，

或者使用static 模板标签以及配置的STATICFILES_STORAGE为给出的相对路径创建URL（这使得换成CDN 来保存静态文件更加容易）。
#记得 load千万不要忘记
{% load staticfiles %}
<img src="{% static "my_app/myexample.jpg" %}" alt="My image"/>
在你的应用中，将静态文件存储在名为static 目录下。例如：my_app/static/my_app/myimage.jpg。

启用静态文件服务

除了这些配置步骤之外，实际中你还需要启用静态文件服务。

在开发过程中，如果你使用django.contrib.staticfiles，当DEBUG 设置成True 时，runserver 会自动启用静态文件服务


这个方法非常低效而且可能不安全，所以它不适合线上环境。


你的项目可能还有一些静态文件不属于任何一个特定的应用。除了在应用中使用static/ 目录，你还可以在settings 文件中定义一个目录列表（STATICFILES_DIRS），Django 会在其中查找静态文件。例如：
# 这个 STATICFILES_DIRS 就是你的静态文件存放的地址，你放到哪里，就从哪里找，是不是很简单
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
    '/var/www/static/',
)

静态文件的命名空间

现在，我们虽然能够将静态文件直接放在my_app/static/之下（而不用创建另外一个my_app 子目录），但是这是一个坏主意。
Django 将使用它找到的名称匹配第一个静态文件， 如果你在另外一个不同 的应用中有相同名称的静态文件，Django 将无法区分它们。
我们需要让Django 能够找到正确的静态文件，最简单的方法是给它们加上命名空间。方法是将这些静态文件放在与应用同名的另外一个目录中。


如上所述，如果你启用django.contrib.staticfiles，当DEBUG 设置为True 时，runserver 将自动启用静态文件服务。
如果django.contrib.staticfiles 不在INSTALLED_APPS 中，你仍然可以使用django.contrib.staticfiles.views.serve() 
视图手工启用静态文件服务。

这不适合在线上环境中使用！。

例如，如果STATIC_URL 定义为/static/，你可以通过在urls.py 中加入以下代码片段启用：

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # ... the rest of your URLconf goes here ...
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
注

这个辅助函数只在debug 模式下工作，而且给定的前缀必须是本地的（例如，/static/）而不能是一个URL（例如，http://static.example.com/）。

另外这个辅助函数只查找STATIC_ROOT 目录下的文件；它不会像django.contrib.staticfiles 那样查找静态文件。


