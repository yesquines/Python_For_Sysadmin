#!/usr/bin/python3
import requests

#GET - Crumb
grumb = requests.get('http://172.10.10.10:8080/crumbIssuer/api/json', auth=('admin','4linux')).json()
headers = {grumb['crumbRequestField'] : grumb["crumb"]}

#Post - Build
build = requests.post('http://172.10.10.10:8080/job/App/build', auth=('admin','4linux'), headers=headers)
