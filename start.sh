#!/bin/sh

USR="arthur"
DIR="samples"
cat /etc/passwd | grep "$USR" > /dev/null
if [[ $? -ne 0 ]]
then
  adduser $USR
fi
if [ -d "$DIR" ]
then
  python3 run.py
  rm -r __pycache__
  chown -R $USR:$USR $DIR
else
  echo "Dir $DIR not found!"
  exit 1
fi
exit 0
