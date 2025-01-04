import argparse as ap


def create(description: str, app_name="passmate") -> ap.ArgumentParser:
    return ap.ArgumentParser(prog=app_name, description=description)


def get_args(parser: ap.ArgumentParser) -> ap.Namespace:
    parser.add_argument("-v", "--version", action="version", version="%(prog)s 1.0-BETA")
    command = parser.add_subparsers(
        dest="command",
        help="Comandos Disponiveis",
    )
    _command_module_generate_passw(command)
    _command_module_manager_passw(command)
    return parser.parse_args()


def _command_module_generate_passw(command) -> None:
    generate_cmd = command.add_parser(
        "gen",
        help="Comando Responsável por Gerar as Senhas",
    )
    generate_cmd.add_argument(
        "-l",
        "--quantity-letters",
        type=int,
        default=4,
        help="informa a quantidade de letras tem que devem conter na senha",
    )
    generate_cmd.add_argument(
        "-d",
        "--quantity-digits",
        type=int,
        default=4,
        help="informa a quantidade de digitos tem que devem conter na senha",
    )
    generate_cmd.add_argument(
        "-s",
        "--quantity-special-chars",
        type=int,
        default=4,
        help="informa a quantidade de caracteres especiais tem que devem conter na senha",
    )

    generate_cmd.add_argument(
        "-a",
        "--save-password",
        action="store_true",
        help="Salva a Senha Gerada",
    )


def _command_module_manager_passw(command) -> None:
    manager_cmd = command.add_parser(
        "manage",
        help="Comando Responsável por Armazenar e Listar As Senhas Salvas",
    )
    manager_cmd.add_argument(
        "-v",
        "--view-list",
        action="store_true",
        help="Lista as Senhas Salvas",
    )
    manager_cmd.add_argument(
        "-A",
        "--add-password",
        action="store_true",
        help="Adiciona a Senha a Lista De Senhas Salvas",
    )
