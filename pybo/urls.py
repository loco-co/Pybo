from django.urls import path

from . import views

app_name = 'pybo'  # 충돌방지용 네임스페이스

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),  # url하드코딩을 피하기 위한 네이밍
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
    path('question/create/', views.question_create, name='question_create'),
    path('question/modify/<int:question_id>/', views.question_modify,
         name='question_modify'),  # no reverse match 오류유발
]
