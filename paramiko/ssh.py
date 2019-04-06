#!/usr/bin/python3
import paramiko
import scp

client = paramiko.client.SSHClient()
client.load_system_host_keys()
#ssh -o strichostkeycheking=no
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

client.connect('52.90.63.246', username='ec2-user', key_filename='Python.pem')

stdin, out, err = client.exec_command('sudo zypper install -y nginx ; sudo rm /srv/www/htdocs/50x.html')
print(out.read().decode('utf-8'))


with scp.SCPClient(client.get_transport()) as scp:
    scp.put('index.html','/tmp/index.html')

stdin, out, err = client.exec_command('sudo mv /tmp/index.html /srv/www/htdocs/')
