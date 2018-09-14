#!/bin/bash

chassis_uri=$(curl -k https://$1/redfish/v1/Chassis/ -u root:redfish | jq '.Members|.[0]|."@odata.id"' | sed 's/"//g')

health=$(curl -k https://$1$chassis_uri/Thermal/ -u root:redfish | jq '.Fans[]|(.FanName,.Reading, .ReadingUnits,(.Stat\
us|.Health))' | sed 's/"//g')

ok='OK'
warning='Warning'
critical='Critical'

if [[ $health == *"Critical"* ]] ; then
  severity='Critical'
elif [[ $health == *"Warning"* ]]; then
  severity='Warning'
elif [[ $health == *"OK"* ]]; then
    severity='OK'
fi                       

if [ "$severity" == "OK" ]; then
                echo $health
		exit 0
elif [ "$severity" == "Warning" ]; then
                echo $health
                exit 1

elif [ "$severity" == "Critical" ]; then
                echo $health
                exit 2
else
                echo "UNKNOWN - Plugin was unable to determine the status for the host fans!\
"
                exit 3
fi
