# Make some local operations

# First let's import the necessary lib
from fabric.api import *

# Setup environments
# Example: fab staging deploy
# First call for setting environment then call for deploying


def production():
    env.hosts = ['root@162.13.90.185:22']
    env.code_dir = '/var/www/demo.cmsbase.cotidia.com/cmsbasedemo'
    env.collectstatic = "source ../bin/activate && python manage.py collectstatic --settings=cmsbasedemo.settings.production"


def _commit():
    # This command will prompt the user with VI to enter a commit message
    local('git add -A && git commit && git push')

def _update():

    with settings(warn_only=True):
        if run("test -d %s" % env.code_dir).failed:
            run("git clone https://github.com/guillaumepiot/cmsbasedemo.git %s" % env.code_dir)

    with cd(env.code_dir):
        run("git pull")
        run("cd ../ && chown -R cmsdemo:cotidia cmsbasedemo")
        run(env.collectstatic)

    # Restart wsgi server
    with settings(warn_only=True):
        if run("service cmsbasedemo restart").failed:
            run("service cmsbasedemo start")


def deploy(commit=True, update=True):
    # Add, commit and push
    if commit==True:
        _commit()
    # Now update files on the server from the repo
    if update==True:
        _update()