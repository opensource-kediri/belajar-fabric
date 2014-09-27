from fabric.api import run, sudo

def hostname():
    hostname = run('hostname')
    print '-------------------------------'
    print 'hostname : %s' %hostname
    print '-------------------------------'

def ping_google():
    run('ping -c 4 google.com')

def upgrade_os():
   sudo('apt-get update')
   sudo('apt-get upgrade')
