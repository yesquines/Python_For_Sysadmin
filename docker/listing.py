#!/usr/bin/python3
import docker

DOCKER_URL='tcp://127.0.0.1:2376'

#unix://var/run/docker.sock
client = docker.DockerClient(base_url=DOCKER_URL, version='auto')

containers = client.containers.list(all=True)
print('{0:<25}{1:<20}{2:<10}'.format('NOME','IMAGE','STATUS'))
for c in containers:
    print('{0:.<25}{1:.<20}{2:.>10}'.format(c.name, c.image.tags[0], c.status))
