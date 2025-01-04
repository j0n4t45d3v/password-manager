from argparse import ArgumentParser, Namespace

import modules.generate.passw as passw
from modules.storage import save, view
from modules.storage.config import init_config_if_not_configured


def resolve(parser: ArgumentParser, args: Namespace) -> None:
    commands: dict = {
        "gen": generate_password,
        "manage": manage_password,
    }

    command = commands.get(args.command)
    if command is None:
        parser.print_help()
        exit(1)

    command(args)


def generate_password(args: Namespace):
    qtd_letters: int = args.quantity_letters
    qtd_digits: int = args.quantity_digits
    qtd_special_chars: int = args.quantity_special_chars
    password_generated: str = passw.generate_password(
        qtd_letters,
        qtd_digits,
        qtd_special_chars,
    )

    print(f"Senha Gerada: {password_generated}")
    if args.save_password:
        save_login(password_generated)


def manage_password(args: Namespace):
    init_config_if_not_configured()
    if args.add_password:
        save_login()
    elif args.view_list:
        format_login_list(view.list_logins())


def save_login(password: str | None = None) -> None:
    group: str = input("Digite o Grupo Da Senha a Qual Vai Ser Vinculado: ")
    app: str = input("Digite o Site/App Da Senha a Qual a Senha Pertence: ")
    if password is None:
        password = input("Digite a Senha Que Você Quer Salvar: ")
    login: str = input("Digite o Usuario/Email Que Usa Para Se Logar: ")
    struct_to_save: dict = {
        "group": group,
        "site/app": app,
        "pass": password,
        "user": login,
    }
    save.save_passwd(struct_to_save)
    print("Login salvo com sucesso!")
    print(
        "Caso Queira Ver Sua Senha Use o Comando Manage -v Para a Sua Lista De Logins Salvos"
    )


def format_login_list(logins: dict):
    exit_list_logins: bool = False
    while not exit_list_logins:
        clean_console()
        categories = list(logins.keys())
        for index, key in enumerate(categories, start=1):
            print(f"{index} - {key.capitalize()}")

        option: int = int(
            input("Escolha uma categoria para listar (ou '0 - sair' para encerrar):  ")
        )

        if option == 0:
            break

        clean_console()
        category: str = categories[option - 1]
        content_category: list[dict] = logins[category]
        print(category.capitalize())
        for index, content in enumerate(content_category, start=1):
            print(f"{index}.")
            print(f"  Site or Application: {content["site/app"]}")
            print(f"  Username or Email: {content["user"]}")
            print(f"  Senha: {content["pass"]}")

        print()
        exit_option = input("Precione 'Enter' para voltar ao menu - Sair: '0' ou 'q'  ")

        if exit_option == "q" or exit_option == "0":
            exit_list_logins = True


def clean_console():
    print("\033[2J\033[H", end="")
    print()
