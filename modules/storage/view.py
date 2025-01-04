import json
import modules.storage.config as c


def list_logins():
    with open(c.LOGINS_FILE, "r") as login_file:
        datas = json.load(login_file)
    return datas
