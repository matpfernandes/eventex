# Eventex

Sistema de eventos encomendado pela Morena.
https://eventex-matheusfernandes.herokuapp.com/

[![Build Status](https://travis-ci.org/matpfernandes/eventex.svg?branch=master)](https://travis-ci.org/matpfernandes/eventex)
[![Maintainability](https://api.codeclimate.com/v1/badges/fdf9a0e6d8e23bd7844b/maintainability)](https://codeclimate.com/github/matpfernandes/eventex/maintainability)

## Como desenvolver?

1. Clone o repositório
2. Crie um virtualenv com Python 3.5
3. Ative o virtualenv.
4. Instale as dependências.
5. Configure a instância com o .env
6. Execute os testes

```console
git clone git@github.com:matpfernandes/eventex.git wttd
cd wttd
python -m venv .wttd
source .wttd/bin/activate
pip install -r requirements-dev.txt
cp contrib/env-sample .env
python manage.py test

```
## Como fazer o deploy?

1. Crie uma instância no heroku
2. Envie as configurações para o heroku
3. Defina uma SECRET_KEY segura para a instância
4. Defina DEBUG=False
5. Configure o serviço de email
6. Envie o código para o heroku

```console
heroku create minhainstancia
heroku config:push
heroku config:set SECRET_KEY='python contrib/secret_gen.py'
heroku config:set DEBUG=False
# Configurar o email
git push heroku master --force
```
