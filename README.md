# Discord Dictionary Bot
Text bot that will give definition(s) to a requested word

---

## Usage:
There must be a text channel called `definitions`. When the bot sees any message that has a single word, it will return with
the definition of the word.

### Example:
```
User: engineer
```

```
Bot: 
engineer:
1. Noun: a person who uses scientific knowledge to solve practical problems
2. Noun: the operator of a railway locomotive
3. Verb: design as an engineer
4. Verb: plan and direct (a complex undertaking
```

---

## Features:

- Dictionary lookup using `PyDictionary`
- Autocorrect using `autocorrect`

---

## Setting up

- Create a bot by going to https://discord.com/developers/applications and give it the proper reading/writing permissions
- Create a token for the bot (Keep this code secure and saved somewhere safe. You will only be able to view it once when it is generated)
- Create a URL to invite the bot by going to OAuth2 -> URL Generator. Again, give it the proper reading/writing permissions
- Invite the bot to your server using the newly generated URL
- Go to `/res/config/config.properties` and replace the `discord.token` parameter with the newly created token
- Create a `definitions` text channel
- You're all set!