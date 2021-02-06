#!/bin/bash

#set -x
set -e


ws_dir="/Users/yannagler/Desktop/dev-ops-course/py"
pkgs_dir="$ws_dir/venv/lib/python3.9/site-packages/"
proj_dir="$ws_dir/proj-1"

PYTHONPATH=""
export PYTHONPATH="$pkgs_dir:$PYTHONPATH"
echo $PYTHONPATH
echo


cd $proj_dir

python3.9 backend_testing_db.py

nohup python3.9 rest_app.py &
nohup python3.9 web_app.py &
sleep 1
python3.9 backend_testing.py
python3.9 frontend_testing.py
python3.9 combined_testing.py
python3.9 clean_environment.py

echo "Done"


exit 0
