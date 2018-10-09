from django.shortcuts import render,redirect,HttpResponse
from app01 import models
import json

def students(request):
    cls_list = models.Classes.objects.all()
    stu_list = models.Student.objects.all()
    return render(request,'students.html',{'stu_list':stu_list,'cls_list':cls_list})

def add_students(request):
    response = {'status':True,'msg':None,'data':None}
    try:
        n = request.POST.get('name')
        a = request.POST.get('age')
        g = request.POST.get('gender')
        c = request.POST.get('cls_id')
        obj = models.Student.objects.create(
            name=n,
            age=a,
            gender=g,
            cs_id=c,
        )
        response['data'] = obj.id
    except Exception as e:
        response['status'] = False
        response['msg'] = '用户输入错误'
    result = json.dumps(response)
    return HttpResponse(result)

def del_students(request):
    ret = {'status' : True}
    try:
        nid = request.GET.get('nid')
        models.Student.objects.filter(id=nid).delete()
    except Exception:
        ret['status'] = False
    return HttpResponse(json.dumps(ret))

def del_stu(request):
    sid = request.GET.get('sid')
    models.Student.objects.filter(id=sid).delete()
    return redirect('/students')