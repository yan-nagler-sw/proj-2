print(__file__)
print("===")
print()


import requests
from selenium import webdriver
import time

import db_connector as db

print("__name__:", __name__)
print()


def print_usrs (usrs):
    print("---")
    for usr in usrs:
        print(usr)

def print_cfgs (cfgs):
    print("---")
    for cfg in cfgs:
        print(cfg)


rc, conn = db.open_conn()
if (rc != db.rc_ok):
    print("Error: Failed to execute function - db.open_conn")


# Init table: users

rc = db.del_usrs(conn)
if (rc != db.rc_ok):
    print("Error: Failed to execute function - db.del_usrs")

print()


rc, usrs = db.get_usrs(conn)
if (rc != db.rc_ok):
    print("Error: Failed to execute function - db.get_usrs")

print_usrs(usrs)
print()


# Init table: config

rc = db.del_cfgs(conn)
if (rc != db.rc_ok):
    print("Error: Failed to execute function - db.del_cfgs")

print()


url_cfg = "http://127.0.0.1:30001/users/get_user_data/1"
cfg = {db.cfg_url: url_cfg, db.cfg_bws: "chrome", db.cfg_usr_name: "name-a"}

rc = db.add_cfg(conn, cfg)
if (rc != db.rc_ok):
    print("Error: Failed to execute function - db.add_cfg")

print()


rc, cfgs = db.get_cfgs(conn)
if (rc != db.rc_ok):
    print("Error: Failed to execute function - db.get_cfgs")

print_cfgs(cfgs)
print()


# Obtain config data

rc, cfgs = db.get_cfg(conn, url_cfg)
if (rc != db.rc_ok):
    print("Error: Failed to execute function - db.get_cfg")

print_cfgs(cfgs)
print()

bws_cfg = cfgs[0][db.cfg_bws_idx]
usr_name_cfg = cfgs[0][db.cfg_usr_name_idx]


# Handle REST

rest_url_base = "http://127.0.0.1:30000"
rest_url_stop = "{url}/stop_server".format(url = rest_url_base)
rest_url_usrs = "{url}/{tbl}".format(url = rest_url_base, tbl = db.tbl_users)


# Add user - REST

url = "{url}/{id}".format(url = rest_url_usrs, id = 1)
print(url)

usr_json = {db.usr_name: usr_name_cfg}
print(usr_json)

resp = requests.post(url, json = usr_json)
print(resp)
if (not resp.ok):
    print("Failed to execute request - POST")

print(resp.json())
print()


# Get user - REST

resp = requests.get(url)
print(resp)
if (not resp.ok):
    print("Failed to execute request - GET")

print(resp.json())
print()

usr_name_rest = resp.json()["Result"][0][db.usr_name_idx]


# Get user - DB

rc, usrs = db.get_usr(conn, 1)
if (rc != db.rc_ok):
    print("Error: Failed to execute function - db.get_usr")

print_usrs(usrs)
print()

usr_name_db = usrs[0][db.usr_name_idx]


# Compare: REST - DB

print("User name - REST: " + usr_name_rest)
print("User name - DB: " + usr_name_db)

if (usr_name_rest == usr_name_db):
    print("Equal")
else:
    print("Not equal")

print()


rc = db.close_conn(conn)
if (rc != db.rc_ok):
    print("Error: Failed to execute function - db.close_conn")


# Handle Web

web_url_base = "http://127.0.0.1:30001"
web_url_stop = "{url}/stop_server".format(url = web_url_base)


# Handle Browser - Chrome

bws_support_chrome = "chrome"

print("Browser - DB: " + bws_cfg)
print("Browser - Supported: " + bws_support_chrome)

if (bws_cfg != bws_support_chrome):
    raise Exception("The browser is not supported")

exe_drv_chrome = "./chromedriver"

print()


time_impl_wait_sec = 10
time_sleep_sec = 0 #600

elm_id_usr = "user"


drv = webdriver.Chrome(executable_path = exe_drv_chrome)
drv.implicitly_wait(time_impl_wait_sec)
drv.get(url_cfg)

elm = drv.find_element_by_id(elm_id_usr)
usr_name_fe = elm.text

time.sleep(time_sleep_sec)

drv.close()
drv.quit()


# Compare: DB - Web

print("User name - DB: " + usr_name_db)
print("User name - FE: " + usr_name_fe)

if (usr_name_db == usr_name_fe):
    print("Equal")
else:
    print("Not equal")

"""
print()


# Stop servers: REST, Web

url = rest_url_stop
print(url)

resp = requests.get(url)
print(resp)
if (not resp.ok):
    print("Failed to execute request - GET")

print()


url = web_url_stop
print(url)

resp = requests.get(url)
print(resp)
if (not resp.ok):
    print("Failed to execute request - GET")
"""

print()
print()
