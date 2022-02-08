#!/usr/bin/python2.7
# made with python 2.7
import subprocess
import optparse
import re


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify an interface, use --help for more information.")
    elif not options.new_mac:
        parser.error("[-] Please specify a new mac, use --help for more information.")
    return options


def change_mac(interface, new_mac):
    print("changing mac address for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
  
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)

    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("[-]couldn't read mac address.")



options = get_arguments()
current_mac = get_current_mac(options.interface)
print("current MAC = " + str(current_mac))
change_mac(options.interface, options.new_mac) 

current_mac = get_current_mac(options.interface)
if current_mac == options.new_mac:
    print("[+]Mac address was successfuly changed to ", current_mac)
else:
    print("[-]Unable to change Mac address.")








