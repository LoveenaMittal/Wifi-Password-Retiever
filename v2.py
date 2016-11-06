# -*- coding: utf-8 -*-
"""
Script for retrieving wifi passwords saved on the system.The script displays
the wifi profiles along with their passwords.
**Kindly note, you need to run cmd in admin privileges**

Created on Sun Nov 06 11:24:10 2016

@author: Loveena
"""

import subprocess

SHOW_PROFILES = "netsh wlan show profiles"
SHOW_PASSWORDS="netsh wlan show profile name={} key=clear"


# change this this should not be in caps as only batch commands variable 
# are in caps

profiles = subprocess.check_output(SHOW_PROFILES).split("\n")
# collecting all the wifi profiles
# this also should not be in caps same reason as above
wifi_list =[]

# use a slice objects
#slice object for profile name
profile_name_index = 9
#got this profile_name index using enumerate and finding line number as
"""
for i,line in enumerate(profiles):
    print(i,line)
"""
for wifi_entries in profiles[profile_name_index:]:
    if wifi_entries and ':' in wifi_entries:
        wifi_list.append(wifi_entries.split(":")[1].strip())
#        print(WIFI_LIST)
        

# this should not be in caps reason as above
passwords=[]

# follw the pep8 standard as any line should not cross the 80 charater mark

#slice object for security key
security_key_index = 29
#got this security key index using enumerate on a test output for 
# as below:
"""
test = subprocess.check_output(SHOW_PASSWORDS.format(name)). \
                     split("\n")
for i,line in test:
    print(i,line)
"""
# collecting passwords
for name in wifi_list:  # this should be `for profile in WIFI_LIST`
    passwords.append(subprocess.check_output(SHOW_PASSWORDS.format(name)). \
                     split("\n")[security_key_index].split(":")[1].strip())
#    print(PASSWORDS)
    
# displaying wifi passwords
# use proper names
print("WIFI NAME : PASSWORD")
file_variable = open("wifi_password.txt","w")
for index in range(len(wifi_list)):
    file_variable.write(wifi_list[index]+" : "+passwords[index])
	
file_variable.close()


