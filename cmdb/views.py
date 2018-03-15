#coding:utf-8
from django.shortcuts import render,HttpResponse,redirect
from exec_mysql import ExecMysql
from form import IpList
import uuid
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
        form = IpList(data=request.POST)

        # print form
        # print form.cleaned_data['hostname']
        if form.is_valid():
            print form.cleaned_data
            print form.cleaned_data['ip']
            m_id = '"'+ str(uuid.uuid4()) + '"'
            m_ip = '"'+ form.cleaned_data['ip']+ '"'
            m_hostname ='"'+ form.cleaned_data['hostname'] + '"'
            m_group = '"'+form.cleaned_data['group']+ '"'
            m_system = form.cleaned_data['system']
            m_product = form.cleaned_data['product']
            print m_id,m_ip,m_hostname,m_group,m_system,m_product
            add_sql = 'insert into iplist (id,ip,hostname,groupname,system,product) value (%s,%s,%s,%s,%s,%s);'%(m_id,m_ip,m_hostname,m_group,m_system,m_product)
            print add_sql
            db = ExecMysql(dbconfig)
            add_result_all = db.dml(add_sql)
            print add_result_all
            query_sql = 'select * from iplist;'
            query_result_all = db.query(query_sql)
            print query_result_all
            db.close()
            return render(request,'cmdb/add_host.html',{"queryip":query_result_all})



def query_ip(request):
    pass


