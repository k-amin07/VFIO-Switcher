import os
print('Please read the guide first, before using this script.\n\
The script assumes that you have followed the guide. \n\
The purpose of this script is only to enable or disable GPU\n\
This script must be run with sudo\n')
print('Link to guide: https://gist.github.com/k-amin07/47cb06e4598e0c81f2b42904c6909329\n')
select = 0
while(not select in ['1','2']):
    select = input('Enter 1 to enable, 2 to disable: ')
out = []
with open('/etc/modprobe.d/vfio.conf','r') as vfio:
    lines = vfio.readlines()
    for line in lines:
        if (select == '1'): 
            try:
                out.append(line.split('#')[1])
            except IndexError:
                pass
        if (select == '2' and line.split('#')[0]): 
            out.append('#' + line)
if(not out): 
    print('Nothing to write. The file is empty or is already %s' % ('enabled!' if select == '1' else 'disabled!'))
    exit()
with open('/etc/modprobe.d/vfio.conf','w') as vfio:
    for line in out:
        vfio.write(line)
if(select == '1'):
    with open('/etc/X11/xorg.conf.d/10-intel.conf', 'w') as intel:
        intel.write('Section "Device"\n\
        Identifier "Intel GPU"\n\
        Driver "modesetting"\n\
        BusID  "PCI:0:2:0"\nEndSection')
if(select == '2'):
    os.system('rm -f /etc/X11/xorg.conf.d/10-intel.conf')
os.system('sudo mkinitcpio -g /boot/linux-custom.img')
print('Everything appears to be okay, please reboot.')