from django.urls import path
from . import views



#http://127.0.0.1:8000/        --> index
#http://127.0.0.1:8000/index   --> index
#http://127.0.0.1:8000/blogs   --> blogs
#http://127.0.0.1:8000/blogs/3   --> blogs



urlpatterns = [
    path('',views.index),
    path('index',views.index),
    path('blogs',views.blogs),
    path('blog/<int:id>',views.blogs_details),

]