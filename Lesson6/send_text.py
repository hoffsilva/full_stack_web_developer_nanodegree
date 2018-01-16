from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACe520bfd9bd56b41a2a6fa870e1417a5b"
# Your Auth Token from twilio.com/console
auth_token  = "e2c5a3b9c8814604801b6823847a550d"

client = Client(account_sid, auth_token)

client.api.account.messages.create(
    to="+5561991212700",
    from_="+14079069848",
    body="Hello there!")

