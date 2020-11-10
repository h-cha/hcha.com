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
        'text1' : 'ユーザー認証付きのチャットアプリ',
        'text2' : 'django_channelsというライブラリを使ってWebSocket通信を行いました。',
        'text3' : 'もともとはワードウルフゲームをする予定でしたが、難しくて断念',
        'text4' : '',
        'image1' : 'hello/images/room.PNG',
        'image2' : 'hello/images/login.PNG',
        'image3' : 'hello/images/signup.PNG',
        'image4' : 'hello/images/home.PNG',
        'skill' : '#Django #SQLite #html #css #javascript',
        'github' : 'https://github.com/h-cha/django_online_chat',
    }

    return render(request, 'hello/works.html',params)

def work2(request):
    params = {
        'goto' : 'index',
        'work_name' : '中学生の数学のWEB教科書',
        'text1' : '動画解説を見た後問題演習を行うアプリ',
        'text2' : '中学校に行き、中学生の数学の学習補助を行いました。',
        'text3' : 'そこで中学生がつまづいていた課題をサポートするWEBアプリを２人で作成しました。',
        'text4' : '動画解説はWEBの教科書にしかできない利点として評価されました。',
        'image1' : 'hello/images/no_image.png',
        'image2' : 'hello/images/no_image.png',
        'image3' : 'hello/images/no_image.png',
        'image4' : 'hello/images/no_image.png',
        'skill' : '#Django #SQLite #html #css',
        'github' : 'https://github.com/h-cha/Django_terakoya',
    }
    return render(request, 'hello/works.html', params)

def work3(request):
    params = {
        'goto' : 'index',
        'work_name' : '地域の高齢化がわかるアプリ',
        'text1' : '郵便番号を入力するとその地域の世代別人口の割合が',
        'text2' : '円グラフで表示されるアプリを作りました。',
        'text3' : '入力した数字が郵便番号ではない場合エラー表示を出しました。',
        'text4' : '',
        'image1' : 'hello/images/room.PNG',
        'skill' : '#java #postgreSQL #html #css #javascript',
        'github' : '',
    }
    return render(request, 'hello/work3.html',params)

def work4(request):
    params = {
        'goto' : 'index',
        'work_name' : '食材残さないよ太郎',
        'text1' : '現在作成中です',
        'text2' : '',
        'text3' : '',
        'text4' : '',
        'image1' : 'hello/images/top.PNG',
        'image2' : 'hello/images/register.PNG',
        'image3' : 'hello/images/search.PNG',
        'image4' : 'hello/images/no_image.png',
        'skill' : '#django #SQLite #html #css',
        'github' : '',
    }
    return render(request, 'hello/works.html', params)