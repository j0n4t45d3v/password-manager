import os
import json

_BASE_USER_PATH = os.path.expanduser("~")
LOGINS_FILE = os.path.join(_BASE_USER_PATH, ".logins.json")


def init_config_if_not_configured() -> None:
    if not os.path.exists(LOGINS_FILE):
        with open(LOGINS_FILE, "w") as storage_file:
            json.dump({}, storage_file, indent=4)
