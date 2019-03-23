#!/bin/sh

USR="arthur"
DIR="samples"
adduser $USR
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
