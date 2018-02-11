

"""
装饰器
"""

Django为视图提供了数个装饰器，用以支持相关的HTTP服务。


<b>限制视图只能服务规定的http方法。</b>
用法：
from django.views.decorators.http import require_http_methods

@require_http_methods(["GET", "POST"])
def my_view(request):
    # I can assume now that only GET or POST requests make it this far
    # ...
    pass
  
注意，HTTP请求的方法名必须大写。

require_GET()
只允许视图接受GET方法的装饰器。

require_POST()
只允许视图接受POST方法的装饰器。

require_safe()
只允许视图接受 GET 和 HEAD 方法的装饰器。 这些方法通常被认为是安全的，因为方法不该有请求资源以外的目的。

备注：
Django 会自动清除对HEAD 请求的响应中的内容而只保留头部，所以在你的视图中你处理HEAD 请求的方式可以完全与GET 请求一致。因为某些软件，例如链接检查器，依赖于HEAD 请求，所以你可能应该使用require_safe 而不是require_GET。

<b>可控制的视图处理<b/>


django.views.decorators.http 中的以下装饰器可以用来控制特定视图的缓存行为。

condition(etag_func=None, last_modified_func=None)[source]¶
etag(etag_func)[source]¶
last_modified(last_modified_func)[source]¶
这些装饰器可以用于生成ETag 和Last-Modified 头部；参考 conditional view processing.

GZip 压缩¶
django.views.decorators.gzip 里的装饰器基于每个视图控制其内容压缩。

gzip_page()¶
如果浏览器允许gzip 压缩，这个装饰器将对内容进行压缩。它设置相应的Vary头部，以使得缓存根据Accept-Encoding头来存储信息。

Vary 头部¶
django.views.decorators.vary 可以用来基于特定的请求头部来控制缓存。

vary_on_cookie(func)[source]¶
vary_on_headers(*headers)[source]¶
到当构建缓存的键时，Vary 头部定义一个缓存机制应该考虑的请求头。
