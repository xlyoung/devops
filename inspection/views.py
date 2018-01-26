# coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt


def inspection(request):
    ip_list = "{01:{id:01,text:'10.249.242.26'},02:{id:02,text:'10.249.242.27'}}"
    return render(request, 'inspection/inspection.html', {'IpList': json.dumps(ip_list)})


@csrf_exempt
def index(request):
    if request.method == 'POST':
        # print request.POST.get('ipList')
        print type(request.POST.get('ipList'))
        ip_list = str(request.POST.get('ipList'))
        print ip_list
        ip_dict = eval(ip_list)
        print ip_dict[0]["text"]

        return HttpResponse("htllo,this is a test")
    else:
        print 2222
        return HttpResponse("hahahahah")