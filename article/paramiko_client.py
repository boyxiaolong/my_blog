import paramiko
import ConfigParser
import time
from models import SSHInfo

class ParamikoClient:
    def __init__(self):
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.sftp_client = None
        self.client_state = 0

    def connect(self, sshinfo):
        try:
            self.client.connect(hostname=sshinfo.host
                                , port=sshinfo.port
                                , username=sshinfo.usr
                                , password=sshinfo.pwd
                                , timeout=1.0)
            self.client_state = 1
            return True
        except Exception,e:
            print e
            try:
                self.client.close()
                return False
            except:
                pass

    def run_cmd(self, cmd_str):
        stdin, stdout, stderr = self.client.exec_command(cmd_str)
        return stdout.read()


    def get_sftp_client(self):
        if self.client_state == 0:
            self.connect()
        if not self.sftp_client:
            self.sftp_client = paramiko.SFTPClient.from_transport(self.client.get_transport())
        return self.sftp_client

    def multi_run_command(self, cmd_list):
        if not self.shell:
            self.shell = self.client.invoke_shell()

        for cmd in cmd_list:
            print 'do cmd :', cmd
            self.shell.send(cmd+'\n')
            time.sleep(0.5)
            receive_buf = self.shell.recv(1024)
            print 'get cmd return: ', receive_buf


