# [@oracleot_bot](https://t.me/oracleot_bot) main repository

[![Maintainability](https://api.codeclimate.com/v1/badges/dae0b3f62973419eb49b/maintainability)](https://codeclimate.com/github/znhv/oracle/maintainability) [![Test Coverage](https://api.codeclimate.com/v1/badges/dae0b3f62973419eb49b/test_coverage)](https://codeclimate.com/github/znhv/oracle/test_coverage)

The bot can give both a specific yes or no answer to your question and surprise you a bit with the answer.

## Installation

Clone the repo and install packages
```shell
$ git clone https://github.com/znhv/oracle.git && cd oracle && pip3 install -r requirements.txt
```

Copy and edit `.env` with your own values.
```shell
oracle$ cd bot && cp sample.env .env
```

#### Environment variables
`BOT_TOKEN` — Telegram bot token


## Usage


Once you've setup your database and your configuration (see below) is complete, simply run:
```shell
$ python3 -m bot
```

## Commands
Command | Description
:--- | :---
/start | Start bot.
/fortune | Random Response.
/help | Show Help.


## License
[MIT](https://choosealicense.com/licenses/mit/)