print(__file__)
print("===")
print()


from selenium import webdriver
import time

import db_connector as db

print("__name__:", __name__)
print()


def print_cfgs (cfgs):
    print("---")
    for cfg in cfgs:
        print(cfg)


rc, conn = db.open_conn()
if (rc != db.rc_ok):
    print("Error: Failed to execute function - db.open_conn")


rc = db.del_cfgs(conn)
if (rc != db.rc_ok):
    print("Error: Failed to execute function - db.del_cfgs")

print()


rc, cfgs = db.get_cfgs(conn)
if (rc != db.rc_ok):
    print("Error: Failed to execute function - db.get_cfgs")

print_cfgs(cfgs)
print()


url = "http://127.0.0.1:30001/users/get_user_data/1"

cfg = {db.cfg_url: url, db.cfg_bws: "chrome", db.cfg_usr_name: "name-a"}

rc = db.add_cfg(conn, cfg)
if (rc != db.rc_ok):
    print("Error: Failed to execute function - db.add_cfg")

print()


rc, cfgs = db.get_cfg(conn, url)
if (rc != db.rc_ok):
    print("Error: Failed to execute function - db.get_cfg")

print_cfgs(cfgs)
print()

bws_db = cfgs[0][db.cfg_bws_idx]
usr_name_db = cfgs[0][db.cfg_usr_name_idx]

rc = db.close_conn(conn)
if (rc != db.rc_ok):
    print("Error: Failed to execute function - db.close_conn")


bws_support_chrome = "chrome"

print("Browser - DB: " + bws_db)
print("Browser - Supported: " + bws_support_chrome)

if (bws_db != bws_support_chrome):
    raise Exception("The browser is not supported")

exe_drv_chrome = "./chromedriver"

print()


time_impl_wait_sec = 10
time_sleep_sec = 0 #600

elm_id_usr = "user"


drv = webdriver.Chrome(executable_path = exe_drv_chrome)
drv.implicitly_wait(time_impl_wait_sec)
drv.get(url)

elm = drv.find_element_by_id(elm_id_usr)
usr_name_fe = elm.text

time.sleep(time_sleep_sec)

drv.close()
drv.quit()


print("User name - DB: " + usr_name_db)
print("User name - FE: " + usr_name_fe)

if (usr_name_db == usr_name_fe):
    print("Equal")
else:
    print("Not equal")

print()
print()
