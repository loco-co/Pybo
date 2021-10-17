from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from common.forms import UserForm


def signup(request):
    """
    계정생성
    """
    if request.method == "POST":  # signup이 POST방식의 호출일 경우
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')  # 개별 데이터 얻기
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)  # 자동 로그인
            return redirect('index')
    else:  # signup이 GET방식의 호출일 경우
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})
