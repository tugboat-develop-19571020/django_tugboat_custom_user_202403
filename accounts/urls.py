from django.urls import path
from accounts import views

# アプリケーション URL にProfileViewを指定 => 逆引き名はprofile
urlpatterns = [
    path('profile/', views.ProfileView.as_view(), name='profile')
]
