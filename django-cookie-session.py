"""
django cookie session
"""
cookie 和 session 应用

浏览器请求服务器是无状态的。
无状态指一次用户请求时，浏览器、服务器无法知道之前这个用户做过什么，每次请求都是一次新的请求。
无状态的应用层面的原因是：浏览器和服务器之间的通信都遵守HTTP协议。
根本原因是：浏览器与服务器是使用Socket套接字进行通信的，服务器将请求结果返回给浏览器之后，
会关闭当前的Socket连接，而且服务器也会在处理页面完毕之后销毁页面对象。

有时需要保持下来用户浏览的状态，比如用户是否登录过，浏览过哪些商品等。 实现状态保持主要有两种方式：
在客户端存储信息使用Cookie。
在服务器端存储信息使用Session。


启用和禁用Session
Django项目默认启用Session。
禁用Session：
将Session中间件删除。

    'django.contrib.sessions.middleware.SessionMiddleware',
 
存储方式
打开项目的settings.py文件，设置SESSION_ENGINE项指定Session数据存储的方式，可以存储在数据库、缓存、Redis等。

1.存储在数据库中，如下设置可以写，也可以不写，这是默认存储方式。注意使用数据库存储，需要在项目INSTALLED_APPS中安装Session应用。然后执行迁移，才会在数据库中生成session表
SESSION_ENGINE=’django.contrib.sessions.backends.db’

2.存储在缓存中：存储在本机内存中，如果丢失则不能找回，比数据库的方式读写更快。
SESSION_ENGINE=’django.contrib.sessions.backends.cache’

3.混合存储：优先从本机内存中存取，如果没有则从数据库中存取。
SESSION_ENGINE=’django.contrib.sessions.backends.cached_db’

依赖于Cookie
所有请求者的Session都会存储在服务器中，服务器如何区分请求者和Session数据的对应关系呢？ 
答：在使用Session后，会在Cookie中存储一个sessionid的数据，每次请求时浏览器都会将这个数据发给服务器，服务器在接收到sessionid后，会根据这个值找出这个请求者的Session。

结果：如果想使用Session，浏览器必须支持Cookie，否则就无法使用Session了。

存储Session时，键与Cookie中的sessionid相同，值是开发人员设置的键值对信息，进行了base64编码，过期时间由开发人员设置。

session对象及方法操作
通过HttpRequest对象的Session属性进行会话的读写操作。

1 以键值对的格式写会话。
request.session[‘键’]=值

2.根据键读取值。
request.session.get(‘键’,默认值)

3.清除所有会话，在存储中删除值部分，保留键。
request.session.clear()

4.清除会话数据，在存储中删除会话的整条数据。
request.session.flush()

5.删除会话中的指定键及值，在存储中只删除某个键及对应的值。
del request.session[‘键’]

设置会话的超时时间，如果没有指定过期时间则两个星期后过期。
如果value是一个整数，会话将在value秒没有活动后过期。
如果value为0，那么用户会话的Cookie将在用户的浏览器关闭时过期。
如果value为None，那么会话永不过期。 
request.session.set_expiry(value)
使用Redis存储Session
会话还支持文件、纯cookie、Memcached、Redis等方式存储，下面演示使用redis存储。



1,安装包。
pip install django-redis-sessions

2,修改项目settings文件，增加如下项：
#配置将session信息保存在redis数据库中
SESSION_ENGINE = 'redis_sessions.session' #讲session信息保存在redis数据库中
SESSION_REDIS_HOST = 'localhost' #redis数据库所在主机
SESSION_REDIS_PORT = 6379 #redis数据库的端口号
SESSION_REDIS_DB = 1 #使用哪个数据库
SESSION_REDIS_PASSWORD = '' #密码
SESSION_REDIS_PREFIX = 'session'

3,打开应用app下views.py文件，修改session_test视图如下：
def session_test(request):
    request.session['name']='xiaoke'
    # name=request.session.get('name')
    # del request.session['name']
    # request.session.flush()
    return HttpResponse('成功')

4.管理redis的命令，需要保证redis服务被开启。
查看：ps ajx|grep redis
启动：sudo service redis start
停止：sudo service redis stop
使用客户端连接服务器：redis-cli
切换数据库：select 1
查看所有的键：keys *
获取指定键的值：get 键名
