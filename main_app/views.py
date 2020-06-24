from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from django.urls import reverse_lazy
from django.contrib import messages
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
        # messagesメソッド　success
        return super().form_valid(form)
        # オーバーライドしたform_validを実行？　親クラスを実行する