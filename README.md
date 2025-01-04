# PASSWORD MANAGER

Esse projeto é um gerenciador de senhas e logins feito em python permitindo
gerar senhas fortes e armazena-las fazendo o gerenciamento de senha ser centralizado em um ponto só.

## INSTALANDO O COMANDO

Clone o repositorio:
```bash
    git clone https://github.com/j0n4t45d3v/password-manager.git
```
Move o repositorio para o `~/.local/share/`
```bash
    mv /path/to/password-manager/ ~/.local/share/
```

Após mover crie um link symbolico em `~/.local/bin/` usando esse comando:
```bash
    ln -s /path/to/password-manager/passmate ~/.local/bin/passmate
```

Depois disso execute um `passmate -v` para ver se está funcionando deve retornar dessa forma:
```bash
    passmate <versao>
```
