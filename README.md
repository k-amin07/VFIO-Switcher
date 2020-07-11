# VFIO-Switcher
A simple python script to automatically enable or disable GPU passthrough with VFIO.
This is a helper script to enable or disable VFIO if needed. It can be modified for hardware specific needs.

Refer to my [GUIDE](https://gist.github.com/k-amin07/47cb06e4598e0c81f2b42904c6909329) for complete setup. After initial setup, this script can be used to automate GPU isolation, blacklisting and running mkinitcpio, for both enabling and disabling GPU passthrough.

If you are using AMD GPU, with an Intel CPU, this script should work for you out of the box, just replace the BusID with your own. If your hardware is different, this script can still be used as a reference to write your own.

Script must be run with sudo.

Disclaimer: Use the script at your own risk.
