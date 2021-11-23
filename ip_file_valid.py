import os.path
import sys

#checking IP address file and content validity
def ip_file_valid():
    
    #prompting user for input
    ip_file = input("\n[+] Enter IP file path and name (e.g. D:\MyApps\myfile.txt): ")
    
    #changin exception message
    if os.path.isfile(ip_file) == True:
        print("\n[+] IP file is valid :)\n")
        
    else:
        print(f"\n[+] File {ip_file} does not exist :( Please check and try again.\n")
        sys.exit()
        
    #open user selected file for reading (IP addresses file)
    selected_ip_file = open(ip_file, 'r')
    
    #Starting from the beginning of the file
    selected_ip_file.seek(0)
    
    #reading from the beginning of the file
    ip_list = selected_ip_file.readlines()
    
    #closing the file
    selected_ip_file.close()
    
    return ip_list

#ip_file_valid()