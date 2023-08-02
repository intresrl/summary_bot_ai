# Summary Bot AI
This Telegram bot is built through the https://github.com/eternnoir/pyTelegramBotAPI library.

When a voice message is forwarded to the bot, it returns a summary of the message along with a possible response.

## Telegram Token
First of all, you need to set up a new bot, and to do that you need to talk to BotFather, the head of all Telegram bots.
To do this, simply send to the BotFather the `/newbot` message and follow the wizard.

When setting up a new bot, the BotFather provides an HTTP API token.
To use your Telegram Token in this bot, you need to add to an `.env` file the following environment variable:

```TELEGRAM_TOKEN=YOUR_API_KEY```

Alternatively, you can define this environment variable in your run configuration.

## OpenAI API Key
An API key is required to use OpenAI services. To create one, you must have an OpenAI account.
To create a new API key, after logging into the OpenAI site you need to go to your personal area and then navigate to the API keys section.

To use your OpenAI API Key in this bot, you need to add to an `.env` file the following environment variable:

```OPENAI_API_KEY=YOUR_API_KEY```

Alternatively, you can define this environment variable in your run configuration.

## Dependency installation
The list of bot dependencies is contained in the `requirements.txt` file. To install them you can run the following command from the root:

```bash
pip install -r requirements.txt
```

## Run the summary bot
The execution of the bot starts from the main.py file, so to run it you can use the following command from the root:

```bash
python main.py
```