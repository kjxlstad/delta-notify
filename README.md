<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9f/Greek_lc_delta.svg/1200px-Greek_lc_delta.svg.png" alt="drawing" width="200"/>

# Delta Notify

[Link to hosted bot](https://discord.com/api/oauth2/authorize?client_id=940913828873502760&permissions=2048&scope=bot)

Quick and dirty discord bot that notifies users when specified content on websites changes. Users can message the bot with a URL and a CSS selector, the bot will then check the document at that location for changes every 30 minutes and message you back if the content is changed.

## Requirements
```sh
pip install -r requirements.txt
```
or manually install
- bs4
- requests
- dotenv
- discord.py

## Setup
Set the TOKEN environment variable to your discord bot token inside a `.env` file Start the server by running main.py.

## Usage
```
$help
```
to see some simple usage information or 
```
$notify [url] [css selector]
```
to start tracking changes to a website.
