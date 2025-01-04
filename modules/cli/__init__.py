import argparse as ap


def create(description: str, app_name="passmate") -> ap.ArgumentParser:
    return ap.ArgumentParser(prog=app_name, description=description)


