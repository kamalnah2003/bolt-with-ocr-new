from twilio.rest import Client

account_sid = "AC382d7aafc03868eb670d620aa46eca71"
auth_token = "3f4a661b4cb13b6ad708c67b527f77dd"
client = Client(account_sid, auth_token)

call = client.calls.create(
  to="+918072250051",
  from_="+918072250051",
  url="http://demo.twilio.com/docs/voice.xml"
)

print(call.sid)