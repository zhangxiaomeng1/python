
from .models import *
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

# 自定义编辑器
def htmlEditor(request):
    return render(request, 'htmlEditor.html')

def htmlEditorHandle(request):

    html = request.POST['hcontent']
    # test1=Test1.objects.get(pk=1)
    # test1.content=html
    # test1.save()
    test1 = Test1()
    test1.content = html
    test1.save()
    context = {'content': html}
    return render(request, 'htmlShow.html', context)


def index(request):
    # temp=loader.get_template('booktest/index.html')
    # return HttpResponse(temp.render())
    bookList = Student.objects.all()
    context = {'list': bookList}
    return render(request, 'index.html', context)