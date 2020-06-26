from django.contrib import admin
from .models import Diary

# adminページ上にモデルを登録
admin.site.register(Diary)