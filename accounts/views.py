from django.views import View
from django.shortcuts import render, redirect

# 自由度の高い get 関数を使用して作成します。
# profile.html をレンダリングするのみとしておきます。
class ProfileView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'accounts/profile.html')
