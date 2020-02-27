import requests

def get_context_message(name):
    string = "*" + name + "*"
    string = string + " is releasing deploy machine config that was being used."
    return string

def get_section_message(lst):
    string = "*Releasing: * 
    for l in lst:
        if l[1] == 'f':
            if l[0] == 1:
                string = string + "`deploy` folder "
            elif l[0] > 1 and l[0] <= 6:
                string = string + "`deploy" + l[0] + "` folder "
            else
                print "Wrong args!"
                exit(1)
        elif l[1] == 'd':
            if l[0] >= 1 and l[0] <= 3:
            string = string + "`deploy" + l[0] + "` database "
    return string

if __name__ == "__main__":
    alert_json = {
        "alert_type": "DEPLOY_MACHINE_ALERT",
        'message_blocks' : [
            {
                "type": "context",
                "elements": [
                    {
                        "type": "mrkdwn",
                        "text": get_context_message("Supragya Raj")
                    }
                ]
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": get_section_message()
                }
            }
        ],
        'auth_key': 'start'
    }
    response = requests.post('http://forwardslack.bsstag.com/send_text_message_to_slack', json=alert_json)
    print "NOTIFIED!!"