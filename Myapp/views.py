from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.
import json
from Myapp.models import *
# Create your views here.
import time

def get_tools(request):
    keys = request.GET.get('keys',None)
    if keys:
        tools = DB_tool.objects.filter(name__contains=keys)
    else:
        tools = DB_tool.objects.all()
    res = {}
    res['tools'] = list(tools.values())
    return HttpResponse(json.dumps(res),content_type='application/json')

def del_tool(request):
    tool_id = request.GET['tool_id']
    DB_tool.objects.filter(id=tool_id).delete()
    return get_tools(request)


def add_order(name,body,uid_from):
    DB_order.objects.create(name=name,body=body,uid_from=uid_from,ctime=str(time.ctime()),state=False)

def get_orders(request):
    orders = DB_order.objects.all()
    res = {}
    res['orders'] = list(orders.values())
    return HttpResponse(json.dumps(res), content_type='application/json')

def add_tool(request):
    for i in request.POST.lists():
        datas = json.loads(i[0])
    name = '新增工具申请'
    body = '工具名称：%s 。工具描述：%s'%(datas['name'],datas['des'])
    #uid_from = request.user.id
    uid_from = '普通用户'
    add_order(name,body,uid_from)
    return HttpResponse('')

def save_tool(request):
    form_data = json.loads(request.body.decode('utf-8'))
    DB_tool.objects.filter(id=form_data['id']).update(**form_data)
    return get_tools(request)