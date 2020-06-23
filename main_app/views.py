from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import InquiryForm
import logging

logger = logging.getLogger(__name__)

class IndexView(TemplateView):
    template_name = "index.html"

class InquiryView(FormView):
    template_name = "inquiry.html"
    form_class = InquiryForm
    success_url = reverse_lazy('main_app:inquiry')

    def form_valid(self, form):
        form.send_email()
        messages.success(self.request, 'メッセージを送信しました。')
        logger.info('Inquiry sent by {}'.format(form.cleaned_data['name']))
        return super().form_valid(form)