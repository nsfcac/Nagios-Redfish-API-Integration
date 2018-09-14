#!/bin/bash

manager_uri=$(curl -k https://$1/redfish/v1/Managers/ -u root:redfish | jq '.Members|.[0]|."@odata.id"' | sed 's/"//g')

health=$(curl -k https://$1$manager_uri -u root:redfish | jq '.Status|.Health' | sed 's/"//g')

if [ "$health" == "OK" ]; then
                echo "OK - BMC working correctly!"
                exit 0
elif [ "$health" == "Warning" ]; then
                echo "WARNING - BMC working, but needs attention!"
                exit 1

elif [ "$health" == "Critical" ]; then
                echo "CRITICAL - BMC not working correctly and requires immediate attention!"
                exit 2
else
                echo "UNKNOWN - Plugin was unable to determine the status for the BMC!"
                exit 3
fi
