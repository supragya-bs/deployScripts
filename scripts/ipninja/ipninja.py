import re

linesout = "test.host.com (10.200.100.10)"
pat = re.compile("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")
test = pat.findall(linesout)
if test:
        print "Acceptable ip address"
        print test
else:
        print "Unacceptable ip address"

filename = "bestand.py"

# Open the file as f.
# The function readlines() reads the file.
with open(filename) as f:
    content = f.readlines()

# Show the file contents line by line.
# We added the comma to print single newlines and not double newlines.
# This is because the lines contain the newline character '\n'.
for line in content:
    print(line),


https://forwardslack.bsstag.com/send_text_message_to_slack

alert_json = {
    "alert_type": "DEPLOY_MACHINE_ALERT",
    'message_blocks' : [
        {
            'type': 'section',
            'text': {
                'type': 'mrkdwn',
                'text': "*" + "This is test message" + "*"
            }
        }
    ],
    'auth_key': 'start'
}