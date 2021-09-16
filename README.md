# Oracle bot

The magic ball of predictions is a very simple and positive way to find out the answer to your question. The magic ball can give both a specific answer to the question yes or no, and surprise you a little with the answer.

  
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
/help | Show Help Message.


## License
[MIT](https://choosealicense.com/licenses/mit/)