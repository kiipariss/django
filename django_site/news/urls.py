from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.news_home, name='news_home'),
    path('create_news', views.create_news, name='create_news'),
    path('<int:pk>', views.newsDetailViev.as_view(), name='news-detail'),
    path('<int:pk>/update', views.newsUpDate.as_view(), name='news-update'),
    path('<int:pk>/del', views.newsDel.as_view(), name='news-del'),
]
