from fabric.api import run, sudo

# chapter-01

def hostname(): # nama fungsi
    hostname = run('hostname')
    print '-------------------------------'
    print 'hostname : %s' %hostname
    print '-------------------------------'

def ping_google(): # nama fungsi
    run('ping -c 4 google.com')

# chapter-02

def upgrade_os(): # nama fungsi
    run('apt-get update')
    run('apt-get upgrade')