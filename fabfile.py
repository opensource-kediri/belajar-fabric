from fabric.api import run

def hostname():
    hostname = run('hostname')
    print '-------------------------------'
    print 'hostname : %s' %hostname
    print '-------------------------------'


def ping_google():
    run('ping -c 4 google.com')

