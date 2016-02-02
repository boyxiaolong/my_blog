#coding:utf-8
from django.shortcuts import render
from django.shortcuts import render_to_response
# Create your views here.
from django.http import HttpResponse
from models import SSHInfo

# Create your views here.
import ConfigParser
import paramiko_client

def home(request):
    for key in request.FILES:
        file = request.FILES[key]
        config = ConfigParser.ConfigParser()
        config.readfp(file)
        for section in config.sections():
            print section
            host_name = config.get(section, 'host_name')
            host = config.get(section, 'host')
            port = config.get(section, 'port')
            usr = config.get(section, 'username')
            pwd = config.get(section, 'password')
            new_post,create = SSHInfo.objects.update_or_create(host_name=host_name
                                                               , host = host
                                                               , port = port
                                                               , usr = usr
                                                               , pwd = pwd)
            new_post.save()

        sshs = SSHInfo.objects.all()
        print len(sshs)
        return render_to_response("sshlist.html", {'sshs':sshs})
    return render_to_response("django_view.html")

def install_django_project(requset):
    print 'install_django_project'
    sshs = SSHInfo.objects.all()
    cmd_res = {}
    for ssh in sshs:
        print ssh
        client = paramiko_client.ParamikoClient()
        client.connect(ssh)
        res = client.run_cmd('date')
        print res
        cmd_res[ssh.host_name] = res
    return render_to_response("cmd_res.html", {'cmd_res':cmd_res})
