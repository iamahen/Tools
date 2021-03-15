#!/bin/bash

#### Preprocessing on Beijin's recorded data ####
echo "Welcome to SensorChecker!"

echo "---------- Start Checking  ----------"
record_arr=()
for i in $(ls -1 -d record*/* | sort -V)
  do
    sudo python3 GnssImuChecker.py ${i}
done

exec bash