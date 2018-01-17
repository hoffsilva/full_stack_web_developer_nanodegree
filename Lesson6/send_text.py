from twilio.rest import Client

# Your Account SID from twilio.com/console

# Your Auth Token from twilio.com/console


client = Client(account_sid, auth_token)

client.api.account.messages.create(
    to="+5561991212700",
    from_="+14079069848",
    body="Hello there!")

