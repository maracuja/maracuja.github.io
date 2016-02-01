from fabric.api import *

def live():
    """ Set the target to production. """
    env.hosts = ['kurosaki@ichigo']
    env.remote_app_dir = '/home/kurosaki/htdocs/setr.co.uk/'
    env.build_dir = '_site/'

def push():
    """
        Pushes the code to nominated server.
        restart included.
        doesn't touch the db
    """
    require('hosts', provided_by=[live, ])
    put('%s*' % (env.build_dir,), env.remote_app_dir)


def start():
    local('jekyll serve')

