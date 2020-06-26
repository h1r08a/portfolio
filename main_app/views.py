from django.shortcuts import render
from django.views.generic import TemplateView, FormView, ListView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Diary
from .forms import InquiryForm
# カレントディレクトリのforms.からimport

import logging

logger = logging.getLogger(__name__)
# ロガーを取得

class IndexView(TemplateView):
    template_name = "index.html"
    # 指定したテンプレートファイルをtemplatesディレクトリから探す

class InquiryView(FormView):
    template_name = "inquiry.html"
    form_class = InquiryForm
    # クラス関数：form_classをオーバーライド　formsで作成したInquiryFormを呼び出し
    success_url = reverse_lazy('main_app:inquiry')
    # 処理が問題ない時にリダイレクト　urlへ逆引き

    # フォームバリデーションに問題がなかったら（POSTされたら）実行される
    def form_valid(self, form):
        form.send_email()
        # メール送信メソッド実行
        messages.success(self.request, 'メッセージを送信しました。')
        # messagesメソッド　送信完了したことを通知
        return super().form_valid(form)
        # オーバーライドしたform_validを実行？　親クラスを実行する

class PostListView(ListView, LoginRequiredMixin):  #ログイン状態でないとアクセスできなくする
    template_name = "post_list.html"
    model = Diary
    # データを持ってくるDBを記述
    context_object_name = 'diaries'

    def get_queryset(self):
        tmp = Diary.objects.filter(user=self.request.user)
        diaries = tmp.order_by('-created_at')
        return diaries
    # ログインユーザーの投稿を持ってくる
    # filter 検索条件を指定
    # 作成順に並べ替え

class Post(TemplateView):
    template_name = "post.html"