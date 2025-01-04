import json
import modules.storage.config as c
import modules.storage.view as v


def save_passwd(login: dict) -> None:
    data_exist: dict = v.list_logins()
    group: str | None = login.get("group")
    login.pop("group")
    group_in_data: list | None = data_exist.get(group)
    if group_in_data is not None:
        group_in_data.append(login)
    else:
        login = {login.get("group"): [login]}
        data_exist.update(login)
    with open(c.LOGINS_FILE, "w") as login_file:
        json.dump(data_exist, login_file, indent=4)
