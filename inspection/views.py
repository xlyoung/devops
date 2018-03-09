# coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
import json
#csrf 防止500
from django.views.decorators.csrf import csrf_exempt
from inspection.exec_ssh import  SSHConnection
import re


def inspection(request):
    ip_list = {01:{"id":01,"text":'39.108.182.47'},02:{"id":02,"text":'10.249.242.27'}}
    return render(request, 'inspection/inspection.html', {'IpList': json.dumps(ip_list)})


@csrf_exempt
def get_ip(request):
    if request.method == 'POST':
        # print request.POST.get('ipList')
        print type(request.POST.get('ipList'))
        ip_list = str(request.POST.get('ipList'))
        print ip_list
        ip_dict = eval(ip_list)
        try:
            print ip_dict[0]["text"]
        except IndexError,e:
            print e.message
        cmd1 = "ps -ef |grep java "
        t = SSHConnection(cmd1=cmd1)
        t.run()
        # tomcatPath = re.findall(r"file\=(\/\S*)conf", str(t.run()))
        # print tomcatPath
        # return HttpResponse(json.dumps(t.run()))
        # context = {'tomcat_paths': [{'tomcat_path': 1}, {'tomcat_path': 2}, {'tomcat_path': 3}]}
        return render(request, 'inspection/inspection.html')
    else:
        print 2222
        return HttpResponse("hahahahah")