from django.urls import path
from . import views

app_name = 'main_app'
# ルーティング自体に名前をつける　逆引きの際に使用

urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    # viewsのIndexViewに処理を渡す 逆引きの際にnameを利用する as_viewsとすることでクラスベースのビューを関数化する

    path('inquiry/', views.InquiryView.as_view(), name="inquiry"),
    path('diary_list/', views.DiaryListView.as_view(), name="diary_list"),
    path('diary_detail/<int:pk>/', views.DiaryDetailView.as_view(), name="diary_detail"),
    path('diary_create/', views.DiaryCreateView.as_view(), name="diary_create"),
    path('diary_update/<int:pk>/', views.DiaryUpdateView.as_view(), name="diary_update"),
    path('diary_delete/<int:pk>/', views.DiaryDeleteView.as_view(), name="diary_delete"),
]