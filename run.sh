#!/bin/bash

#set -x
set -e


usr = 'yannagler'
crs_dir = "/Users/$usr/Desktop/dev-ops-course"
py_dir = "$crs_dir/py"

py = "python3.9"
pkgs_dir="$py_dir/venv/lib/$py/site-packages"


export PYTHONPATH="$pkgs_dir:$PYTHONPATH"
echo $PYTHONPATH
echo


python3.9 backend_testing_db.py

nohup $py rest_app.py &
nohup $py web_app.py &
sleep 1
$py backend_testing.py
$py frontend_testing.py
$py combined_testing.py
$py clean_environment.py

echo "Done"


exit 0
