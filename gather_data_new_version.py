import os
from netmiko import ConnectHandler

'''
Function to connect to devices
'''
def myfunc(args,**kwargs):
    print args
    print kwargs
    print kwargs.get('ip')

    try:
        net_connect = ConnectHandler(**kwargs)
        working=kwargs.get('ip')+",Working\n"
        ffile = open("devices_working.csv","a")
        ffile.write(working)
        ffile.close()
    except Exception as err:
        exception_type = type(err).__name__
        print(exception_type)
        not_working=kwargs.get('ip')+","+exception_type+"\n"
        print(not_working)
        ffile = open("devices_working.csv","a")
        ffile.write(not_working)
        ffile.close()
        return
    '''
    Get show commands from the device and redir de output to a file
    in a directory named after the command.
    '''
    for show in args:
        output = net_connect.send_command(show)
        '''Create the directory name after the command '''
        directory=show.replace(" ", "_") + ".dir"

        '''Create the directory'''
        if not os.path.exists(directory):
            os.makedirs(directory)

        '''Create a file in the directory and write with output'''
        ffile = open(directory +"/"+ host, 'w')
        print (output)
        ffile.write(output)
        ffile.close()




''' Gather the list of hosts'''
with open('./list.txt') as f:
    hosts=f.readlines()
    print hosts
hosts = [x.strip() for x in hosts]

'''Gather the list of show commands'''
with open('./show.txt') as f:
    shows = f.readlines()
    print shows
shows = [x.strip() for x in shows]

''' Dictionary for connecthandler'''
device = {
    'device_type':'cisco_nxos',
    #'ip':host,
    'username':'xxx',
    'password':'xxx',
}


''' Iterate through hosts sending show commands'''
for host in hosts:
    device['ip']=host
    print "\n\n>>>>>>>>> Device {0} <<<<<<<<<".format(host)
    myfunc(shows,**nexus)
