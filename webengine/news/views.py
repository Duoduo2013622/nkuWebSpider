#coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

#视图接收http请求
def index(request):

    #return HttpResponse('hello world')

    
    return render(request,'news/index.html')

def search(request):
    res = None
    if 'q' in request.GET and request.GET['q']:
        res = request.GET['q']
        db = NewsInfo.news.all()
        po_list = []
        for i in db :
            if res in i.title:
                x = i.title+ '  ' + i.url + '  ' + i.pub_date
                po_list.append(x)



    return render(request, 'news/result.html', {"resp":po_list})
