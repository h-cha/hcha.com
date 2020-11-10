from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


#def index(request):
 #   return render(request, 'hello/index.html')

def test(request):
    params = {
        'goto' : 'work1',
    }
    return render(request, 'hello/test.html',params)

def index(request):
    params = {
        'title' : 'hcha',
        'goto_work1' : 'work1',
        'goto_work2' : 'work2',
        'goto_work3' : 'work3',
        'goto_work4' : 'work4',
    }
    return render(request, 'hello/index.html', params)


def work1(request):
    params = {
        'goto' : 'index',
        'work_name' : 'リアルタイムオンラインチャット',
        'text' : 'ユーザー認証付きのチャットアプリ<br>django_channelsというライブラリを使ってWebSocket通信を行いました。<br>もともとはワードウルフゲームをする予定でしたが、難しくて断念',
        'skill' : '#Django #SQLite #html #css #javascript',
    }

    return render(request, 'hello/works.html',params)

def work2(request):
    params = {
        'goto' : 'index',
        'work_name' : '中学生の数学のWEB教科書',
        'text' : '動画解説を見た後問題演習を行うアプリ<br>中学校に行き、中学生の数学の学習補助を行いました。<br>そこで中学生がつまづいていた課題をサポートするWEBアプリを２人で作成しました。<br>動画解説はWEBの教科書にしかできない利点として評価されました。',
        'skill' : '#Django #SQLite #html #css',
    }
    return render(request, 'hello/works.html', params)

def work3(request):
    params = {
        'goto' : 'index',
        'work_name' : '地域の高齢化がわかるアプリ',
        'text' : '郵便番号を入力するとその地域の世代別人口の割合が円グラフで表示されるアプリを作りました。',
        'skill' : '#java #postgreSQL #html #css #javascript',
    }
    return render(request, 'hello/works.html',params)

def work4(request):
    params = {
        'goto' : 'index',
        'work_name' : '食材残さないよ太郎',
        'text' : '現在作成中です',
        'skill' : '#django #SQLite #html #css',
    }
    return render(request, 'hello/works.html', params)