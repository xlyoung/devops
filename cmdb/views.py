from django.shortcuts import render
from exec_mysql import ExecMysql
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





db = ExecMysql(dbconfig)
sql_select = "SELECT * FROM iplist"
result_all = db.query(sql_select)
print result_all
db.close()
