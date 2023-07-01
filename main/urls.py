from django.urls import path
from main.views import *

urlpatterns = [
    path('accounts/profile/',index,name="index"),path('',index,name="index"),
    path('specific',specific,name="specific"),
    path('getResponce',getResponce,name="getResponce"),
    # path('article/<int:article_id>',views.article,name="article")
]