print(__file__)
print("===")
print()


import os
import signal
from flask import Flask, request

import db_connector as db

print("__name__:", __name__)
print()


app = Flask(__name__)

rc_ok = 200
rc_err = 500


@app.route('/test', methods = ['GET'])
def test ():
    print("test()")

    ret_json = {"Status": "Ok"}
    print(ret_json)

    return ret_json, rc_ok


@app.route('/stop_server', methods = ['GET'])
def stop_server ():
    print("stop_server()")

    os.kill(os.getpid(), signal.SIGKILL)

    ret_json = {"Status": "Ok"}
    print(ret_json)

    return ret_json, rc_ok


@app.route('/users/get_user_data/<id>', methods = ['GET'])
def get_usr (id):
    print("get_usr()")

    try:
        rc, usr = db.get_usr(conn, id)
        if (rc != db.rc_ok):
            print("Error: Failed to execute - db.get_usr")
            exit(1)

        if (len(usr) == 0):
            return "<H1 id='error'>" + "Error: Invalid ID - " + id + "</H1>"

    except Exception as ex:
        print("Error - get_usr: {0}".format(ex))
        exit(1)

    return "<H1 id='user'>" + usr[0][db.usr_name_idx] + "</H1>"


rc, conn = db.open_conn()
if (rc != db.rc_ok):
    print("Error: Failed to execute - db.open_conn")
    exit(1)

app.run(host = '127.0.0.1', debug = True, port = 30001)

print()
print()
