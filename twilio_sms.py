from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'AC588a8c58c227cd2389261d3a6d0d9bb5'
auth_token = 'bc3157a1a8e01542c81798642cd4ff0b'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                    body="You got a twilio message.",
                    from_='+14193301848',
                    to='+919764834026'
                )

print(message.sid)
