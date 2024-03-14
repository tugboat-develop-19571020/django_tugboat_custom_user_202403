from django.urls import path
from app import views

#アプリケーションURLにビューを指定 => IndexView => 逆引き名はindex
urlpatterns = [
    path('', views.IndexView.as_view(), name='index')
]
