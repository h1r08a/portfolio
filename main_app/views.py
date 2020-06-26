from django.shortcuts import render
from django.views.generic import TemplateView, FormView, ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Diary
from .forms import InquiryForm, DiaryCreateForm
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

class DiaryListView(ListView, LoginRequiredMixin):  #ログイン状態でないとアクセスできなくする
    template_name = "diary_list.html"
    model = Diary
    paginate_by = 3

    def get_queryset(self):
        tmp = Diary.objects.filter(user=self.request.user)
        diaries = tmp.order_by('-created_at')
        return diaries
    # ログインユーザーの投稿を持ってくる
    # filter 検索条件を指定
    # 作成順に並べ替え

class DiaryDetailView(DetailView, LoginRequiredMixin):
    template_name = "diary_detail.html"
    model = Diary

class DiaryCreateView(CreateView, LoginRequiredMixin):
    template_name = "diary_create.html"
    model = Diary
    form_class = DiaryCreateForm
    # 自作のFormを(読み込み)オーバーライド
    success_url = reverse_lazy('main_app:diary_list')
    # 処理が完了した際の遷移先を指定

    # formのバリデーションに問題がないとき実行される
    def form_valid(self, form):
        diary = form.save(commit=False)
        # DBにフォーム内容を保存する前にモデルオブジェクト(Diary)を取得して、値を代入する
        diary.user = self.request.user
        # ログインuserを自動で取得する
        diary.save()
        # 最後にDBへ保存
        messages.success(self.request, "日記を作成しました")
        return super().form_valid(form)

    # バリデーション失敗時に実行される
    def form_invalid(self, form):
        messages.error(self.request, "日記の作成に失敗しました")
        return super().form_invalid(form)