import sys
# import requests

def get_context_message(name, reason):
    string = "*" + name + "*"
    string = string + " is blocking deploy machine config usage for"
    string = string + " *" + reason + "*."
    string = string + " Ping the user in case you are currently using this config."
    string = string + " Do not use the following deploy config till presented with release noitification on this channel."
    return string

def get_section_message(lst):
    string = "*Releasing: * "
    for l in lst:
        print "l is " + l
        if l[1] == 'f':
            if int(l[0]) == 1:
                string = string + "`deploy` folder "
            elif int(l[0]) > 1 and int(l[0]) <= 6:
                string = string + "`deploy" + l[0] + "` folder "
            else:
                print "Wrong args!"
                exit(1)
        elif l[1] == 'd':
            if len(l) != 5:
                print "Wrong args!"
                exit(1)
            if int(l[0]) >= 1 and int(l[0]) <= 3:
                string = string + "`deploy" + l[0] + "` database for " + l[2:]
            else:
                print "Wrong args!"
                exit(1)
    return string

if __name__ == "__main__":
    print len(sys.argv)
    print "Arguments: " + str(sys.argv)

    alert_json = {
        "alert_type": "DEPLOY_MACHINE_ALERT",
        'message_blocks' : [
            {
                "type": "context",
                "elements": [
                    {
                        "type": "mrkdwn",
                        "text": get_context_message(sys.argv[1], sys.argv[2])
                    }
                ]
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": get_section_message(sys.argv[3:])
                }
            }
        ],
        'auth_key': 'start'
    }
    print alert_json
    # response = requests.post('http://forwardslack.bsstag.com/send_text_message_to_slack', json=alert_json)
    print "NOTIFIED!!"