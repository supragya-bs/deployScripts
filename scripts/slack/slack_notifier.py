import requests

def get_context_message(name, reason):
    string = "*" + name + "*"
    string = string + " notifies the group of upcoming deploy machine config usage for"
    string = string + " *" + reason + "*."
    string = string + " Ping the user in case you are currently using this config."
    string = string + " Do not use the following deploy config till presented with release noitification on this channel."
    return string

def get_section_message():
    string = "*Blocking: * `deploy` folder, `deploy2` folder, `winDB1` database, `macDB2` database"
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
                        "text": get_context_message("Supragya Raj", "Opera 67")
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