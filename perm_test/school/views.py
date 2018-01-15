from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
# Create your views here.
from .models import *

def index(request):
    # temp=loader.get_template('booktest/index.html')
    # return HttpResponse(temp.render())
    bookList = Student.objects.all()
    context = {'list': bookList}
    return render(request, 'index.html', context)

def htmlEditorHandle(request):


    # print('33333333333')
    #
    # html = request.POST['hcontent']
    # # test1=Test1.objects.get(pk=1)
    # # test1.content=html
    # # test1.save()
    # test1 = Test1()
    # test1.content = html
    # test1.save()
    # context = {'content': '2'}
    return HttpResponse('ok')






