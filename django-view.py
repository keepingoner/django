"""
View
"""
<h3>一个视图函数，简称视图，是一个简单的Python 函数，它接受Web请求并且返回Web响应。

响应可以是一张网页的HTML内容，一个重定向，一个404错误，一个XML文档，或者一张图片

无论视图本身包含什么逻辑，都要返回响应。代码写在哪里也无所谓，只要它在你的Python目录下面。


为了将代码放在某处，约定是将视图放置在项目或应用程序目录中的名为views.py的文件中。

</h3>

<p>
自定义错误视图
Django中默认的错误视图对于大多数web应用已经足够了

但是如果你需要任何自定义行为，重写它很容易。只要在你的URLconf中指定下面的处理器（在其他任何地方设置它们不会有效）。


handler404 = 'mysite.views.my_custom_page_not_found_view'
handler500覆盖了server_error()视图：

handler500 = 'mysite.views.my_custom_error_view'
handler403覆盖了permission_denied()视图：

handler403 = 'mysite.views.my_custom_permission_denied_view'
handler400覆盖了bad_request()视图：

handler400 = 'mysite.views.my_custom_bad_request_view'
</p>
