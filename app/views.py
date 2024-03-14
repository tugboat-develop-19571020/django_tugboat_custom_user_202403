# from django.shortcuts import render
from django.views.generic import TemplateView

# TemplateViewを使用して、固定ページにします => テンプレート名は、app/index.htmlです。
class IndexView(TemplateView):
  template_name = "app/index.html"





