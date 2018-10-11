import serial_shell
import rest

print('# Testing NameServers')

# Open a serial connection to the unit under test
con = serial_shell.Shell('COM7')

# Get the list of nameservers (ignore the prompt status)
_status,output = con.execute('cat /etc/resolv.conf | grep nameserver')
# Parse the output from the shell
ns = output[0][11:].strip().split(' ')

# Open a connection to the Redfish server
red = rest.Rest('https://10.207.15.119','admin','admin')

# Get the list of nameservers
json = red.get('/redfish/v1/Managers/1/EthernetInterfaces/enp2s0')
ns_red = json['NameServers']

# Compare the actual list with what Redfish says
if ns!=ns_red:
    raise Exception('Redfish does not match the system:'+str(ns_red)+':'+str(ns)+':')
print('OK Redfish list of servers matches the system config file.')

# Change the list of nameservers
print('Changing the list of NameServers to [1.2.3.4]')
red.patch('/redfish/v1/Managers/1/EthernetInterfaces/enp2s0',
    {
        'NameServers' : ['1.2.3.4']
    }
)

# Reboot the box
con.execute('reboot')

# Wait for the unit to come back up
con.wait_for_prompt()

# Get the nameservers again
json = red.get('/redfish/v1/Managers/1/EthernetInterfaces/enp2s0')
ns_red = json['NameServers']

if ns_red!=['1.2.3.4']:
    raise Exception('Nameservers do not match')

print('OK NameServers changed to [1.2.3.4]')