#importing libraries

import paramiko
import os.path
import time
import sys
import re

#asking user input file path and name.  
user_file = input("\n[+] Enter user file path and name (e.g. D:\MyApps\myfile.txt): ")


#creating loop that checking file path and name are True if so then will print out file is valid,
#if not then warning for the user that put right information
if os.path.isfile(user_file) == True:
    print("\n[+]Username/password file is valid :)\n")
    
else:
    print("\n[+] File {} does not exist :( Please check and try again. \n".format(user_file))
    sys.exit()

#creating var that asking user input file path and name.
cmd_file = input("\n[+] Enter commands file path and name (e.g. D:\MyApps\myfile.txt): ")

#creating for loop that checks commands valid or not. 
if os.path.isfile(cmd_file) == True:
    print("\n [+] Command file is valid :)\n")
    
else:
    print("\n[-] File {} does not exist :( Please check and try again.\n".format(cmd_file))
    sys.exit()
    
#Creating 
def ssh_connection(ip):
    
    global user_file
    global cmd_file
    
    try:
        selected_user_file = open(user_file, 'r')
        selected_user_file.seek(0)
        username = selected_user_file.readlines()[0].split(',')[0].rstrip("\n")
        selected_user_file.seek(0)
        password = selected_user_file.readlines()[0].split(',')[1].rstrip("\n")
        session = paramiko.SSHClient()
        session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
        session.connect(ip.rstrip("\n"), username = username, password = password)
        connection = session.invoke_shell()
        
        connection.send("enable\n")
        connection.send("terminal length 0\n")
        time.sleep(1)
        
        connection.send("\n")
        connection.send("configure terminal\n")
        time.sleep(1)
        
        selected_cmd_file = open(cmd_file, 'r')
        
        selected_cmd_file.seek(0)
        
        for each_line in selected_cmd_file.readlines():
            connection.send(each_line + '\n')
            time.sleep(2)
            
            selected_user_file.close()
            
            selected_cmd_file.close()
            
            router_output = connection.rev(65535)
            
            if re.search(b"% Invalid input", router_output):
                print("* There was at least one IOS syntax error on device {} :(".format(ip))
                
            else:
                print("\n DONE for device {} :)\n".format(ip))
                
            print(str(router_output) + "\n")
            
            session.close()
            
    except paramiko.AuthenticationException:
        print("* Invalid username or password :( \n* Please check the username/password file or the device configuration. ")
        print("* Closing prongram... Bye! ")
    
