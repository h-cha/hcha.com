from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


#def index(request):
 #   return render(request, 'hello/index.html')

def test(request):
    return render(request, 'hello/test.html')

#def index(request):
 #   params = {
  #      'goto_work1' : 'work1',
   #     'goto_work2' : 'work2',
    #    'goto_work3' : 'work3',
     #   'goto_work4' : 'work4',
    #}
    #return render(request, 'hello/index.html',params)


#def work1(request):

 #   return render(request, 'hello/works.html')

#def work2(request):
    
 #   return render(request, 'hello/works.html')

#def work3(request):
    
 #   return render(request, 'hello/works.html')

#def work4(request):
    
 #   return render(request, 'hello/works.html')