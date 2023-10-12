from discord_webhook import DiscordWebhook

print ("--- webhook url ---")
urlwebhook = input()
print ("--- enter the message to send ---")
message = input()

webhook = DiscordWebhook(url=urlwebhook, content=message)
response = webhook.execute()