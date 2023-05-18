import configparser

config = configparser.RawConfigParser()
config.read('./res/config/config.properties')

def discord_token() -> str:
    return config.get('DiscordCredentials', 'discord.token')