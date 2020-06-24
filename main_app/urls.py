from django.urls import path
from . import views

app_name = 'main_app'
# ルーティング自体に名前をつける　逆引きの際に使用

urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    # viewsのIndexViewに処理を渡す 逆引きの際にnameを利用する as_viewsとすることでクラスベースのビューを関数化する

    path('inquiry/', views.InquiryView.as_view(), name="inquiry"),
]