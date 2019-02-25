import os
import sys
import time
import configparser

config = configparser.ConfigParser()
config.read('nagios_node_config.conf')
hostList = config['new_nodes']['new_ip_list']

if hostList == "":
    print ("\nNo new Redfish enabled node available for Nagios configuration.\n")
    #print (config['config_nodes']['config_ip_list'])
    sys.exit(0)
else:
    print ("\nThe following Redfish-enabled nodes are found for Nagios configuration:\n")
    print (hostList)
    print("\n")
    file = open(r"/usr/local/nagios/etc/objects/hosts.cfg","w")
    hosts = hostList.split(',')
    
    for host in hosts:
        name, ip = host.split(':')
        #HOST Informaton
        print ("\n\nConfiguring Redfish node: ["+name+"] for Nagios monitoring\n\n")
        file.write("\ndefine host{") 
        file.write("\n\tuse\tlinux-server")
        file.write("\n\thost_name\t"+name) 
        file.write("\n\talias\tlocalhost")
        file.write("\n\taddress\t"+ip) 
        file.write("\n\t}") 

        #Services/Hardware components information

        # BMC Check 
        file.write("\ndefine service{") 
        file.write("\n\tuse\tlocal-service")
        file.write("\n\thost_name\t"+name)
        file.write("\nservice_description\tcheck bmc health")
        file.write("\ncheck_command\tcheck-bmc")
        file.write("\n\t}")

        # CPU Check
        file.write("\ndefine service{") 
        file.write("\n\tuse\tlocal-service")
        file.write("\n\thost_name\t"+name)
        file.write("\nservice_description\tcheck cpu health")
        file.write("\ncheck_command\tcheck-cpu")
        file.write("\n\t}")

        # Memory Check
        file.write("\ndefine service{") 
        file.write("\n\tuse\tlocal-service")
        file.write("\n\thost_name\t"+name)
        file.write("\nservice_description\tcheck memory health")
        file.write("\ncheck_command\tcheck-memory")
        file.write("\n\t}")

        # Fan Check
        file.write("\ndefine service{") 
        file.write("\n\tuse\tlocal-service")
        file.write("\n\thost_name\t"+name)
        file.write("\nservice_description\tcheck fans health")
        file.write("\ncheck_command\tcheck-fans")
	file.write("\n\t}")
	
	# Temperature Check
	file.write("\ndefine service{")
	file.write("\n\tuse\tlocal-service")
	file.write("\n\thost_name\t"+name)
	file.write("\nservice_description\tcheck temperature")
	file.write("\ncheck_command\tcheck-temperature")
        file.write("\n\t}")
	
        time.sleep(1)

    file.close() 

    # If this is first time that Redfish node(s) are being configured for Nagios  
    if  config['config_nodes']['config_ip_list'] == "":
        config['config_nodes']['config_ip_list'] = hostList
    else:
        config['config_nodes']['config_ip_list']=config['config_nodes']['config_ip_list']+','+new_ip_list

    # Set new_ip_list empty
    config['new_nodes']['new_ip_list']=''

    with open('nagios_node_config.conf', 'w') as configfile:
        config.write(configfile)

    # stop Apache and Nagios services
    os.system("sudo service httpd stop")
    os.system("sudo service nagios stop")

    # Start Apache and Nagios Services with new configuration
    os.system("sudo service httpd start")
    os.system("sudo service nagios start")



        
	
        
        
