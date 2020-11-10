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
    }

    return render(request, 'hello/works.html',params)

def work2(request):
    params = {
        'goto' : 'index',
    }
    return render(request, 'hello/works.html', params)

def work3(request):
    params = {
        'goto' : 'index',
    }
    return render(request, 'hello/works.html',params)

def work4(request):
    params = {
        'goto' : 'index',
    }
    return render(request, 'hello/works.html', params)