#coding:utf-8
from django.shortcuts import render,HttpResponse,redirect
from django.template import Template, Context
from exec_mysql import ExecMysql
from form import IpList
import uuid
from cmdb import models
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
    if request.method == 'POST':
        form = IpList(data=request.POST)
        if form.is_valid():
            m_id = '"'+ str(uuid.uuid4()) + '"'
            m_ip = '"'+ form.cleaned_data['ip']+ '"'
            m_hostname ='"'+ form.cleaned_data['hostname'] + '"'
            m_group = '"'+form.cleaned_data['group']+ '"'
            m_system = '"'+ form.cleaned_data['system']+'"'
            m_product = '"'+form.cleaned_data['product']+'"'
            add_sql = 'insert into iplist (uuid,ip,hostname,groupname,system,product) value (%s,%s,%s,%s,%s,%s);'%(m_id,m_ip,m_hostname,m_group,m_system,m_product)
            print add_sql
            db = ExecMysql(dbconfig)
            add_result_all = db.dml(add_sql)
            print add_result_all
            query_sql = 'select * from iplist;'
            query_result_all = db.query(query_sql)
            print query_result_all
            db.close()
            q_data = models.ip_list.objects.all().all()
            return render(request,'cmdb/add_host.html',{"form": form,"q_data": q_data})
    else:

        q_data = models.ip_list.objects.all().all()

        print q_data
        return render(request, 'cmdb/add_host.html', {"form": form, "q_data": q_data})

def add_config(request):
    pass


def query_ip(request):
    pass

def query_resource(request):
    print models.ip_list.objects.all().values('ip')
    for ip in models.ip_list.objects.all().values('ip'):
        print ip
    return render(request,'cmdb/index.html')
    # for ip in models.ip_list.ip:
    #     print ip