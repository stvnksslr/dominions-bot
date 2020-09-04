# Dominions 5 Slack Bot

Quick and dirty bot for checking dominions turns for use in slack.

## Requirements

- Python 3.7+
- Poetry

### Setup

- `poetry install`
- `poetry shell`
- `cd src`
- `slack-machine`

### Caveats

- Currently only supports games on snek.earth
- Code for grabbing game data from a binary stream fetch is hacky and terrible and i need to clean it up, it also changes sometimes

### Current Commands

- !check `port number`
