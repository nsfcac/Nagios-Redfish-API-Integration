#!/bin/bash

system_uri=$(curl -k https://$1/redfish/v1/Systems/ -u root:redfish | jq '.Members|.[0]|."@odata.id"' | sed 's/"//g')

health=$(curl -k https://$1$system_uri -u root:redfish | jq '.Status|.HealthRollup' | sed 's/"//g')

if [ "$health" == "OK" ]; then
                echo "OK - Host working correctly!"
                exit 0
elif [ "$health" == "Warning" ]; then
                echo "WARNING - Host working, but needs attention!"
                exit 1

elif [ "$health" == "Critical" ]; then
                echo "CRITICAL - Host not working correctly and requires immediate attention!"
                exit 2
else
                echo "UNKNOWN - Plugin was unable to determine the status for the host!"
                exit 3
fi
