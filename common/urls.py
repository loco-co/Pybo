from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


app_name = 'common'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='common/login.html'),
         name='login'),  # 공통 디렉토리의 템플릿을 이용하기 위해
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
]
