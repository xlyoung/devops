# -*- coding:utf-8 -*-
import paramiko
import re

class SSHConnection(object):

    def __init__(self, host='39.108.182.47', port=22, username='root', pwd='Lwxtest123', cmd1 ="ps -ef|grep java" ):
        self.host = host
        self.port = port
        self.username = username
        self.pwd = pwd
        self.__k = None
        self.cmd1 = cmd1

    def run(self):
        self.connect()  # 连接远程服务器
        # self.upload('db.py', '/tmp/1.py')  # 将本地的db.py文件上传到远端服务器的/tmp/目录下并改名为1.py
        # 执行df 命令
        self.cmd(self.cmd1)
        self.close()  # 关闭连接

    def connect(self):
        transport = paramiko.Transport((self.host, self.port))
        transport.connect(username=self.username, password=self.pwd)
        self.__transport = transport

    def close(self):
        self.__transport.close()

    def upload(self, local_path, target_path):
        sftp = paramiko.SFTPClient.from_transport(self.__transport)
        sftp.put(local_path, target_path)

    def cmd(self, command):
        ssh = paramiko.SSHClient()
        ssh._transport = self.__transport
        # 执行命令
        stdin, stdout, stderr = ssh.exec_command(command)
        # 获取命令结果
        result = stdout.readlines()
        tomcatPath = re.findall(r"file\=(\/\S*)conf", str(result))
        dic = {}
        # dic = {i: i ,for i in range(len(result))}

        return tomcatPath
