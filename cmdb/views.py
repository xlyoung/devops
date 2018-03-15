#coding:utf-8
from django.shortcuts import render,HttpResponse,redirect
from exec_mysql import ExecMysql
from form import IpList
from django.contrib.auth.decorators import login_required
# Create your views here.

dbconfig = {'host': '127.0.0.1',
            'port': 3306,
            'user': 'root',
            'passwd': '123456',
            'db': 'devops',
            'charset': 'utf8'}




# @login_required
def index(request):
    return render(request, 'cmdb/index.html')


def select(request):
    pass

def config_update(request):
    return render(request,'cmdb/config_update.html')


def add_host(request):
    form = IpList()
    # print form
    return  render(request,'cmdb/add_host.html',{"form":form})


def add_config(request):
    if request.method == 'POST':
        form = IpList(request.POST)
        print form
        if form.is_valid():
            print form.cleaned_data
        # return redirect('cmdb/index.html')
        else:
            print "失败"



# db = ExecMysql(dbconfig)
# sql_select = "SELECT * FROM iplist"
# result_all = db.query(sql_select)
# print result_all
# db.close()
