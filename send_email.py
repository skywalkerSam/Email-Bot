"""
Developer: @skywalkerSam
Purpose: Automating Regular Emails
Date: 12022.10.01.21:16:00

"""
import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

print("""
 _____           ___  ___      _ _   ______       _   
|  ___|          |  \/  |     (_) |  | ___ \     | |  
| |__    ______  | .  . | __ _ _| |  | |_/ / ___ | |_ 
|  __|  |______| | |\/| |/ _` | | |  | ___ \/ _ \| __|
| |___           | |  | | (_| | | |  | |_/ / (_) | |_ 
\____/           \_|  |_/\__,_|_|_|  \____/ \___/ \__|

""")
email = EmailMessage()
email['from'] = "AUTHOR'S NAME"             # Sam Skywalker
email['to'] = "CLIENT'S E-MAIL ADDRESS"     # asaiinc.org@gmail.com
email['subject'] = "EMAIL'S SUBJECT"        # Greetings from me...

# Content Specfic parameters (DEMO)
email_content = Template(Path("./templates/cortana41.html").read_text())
email.set_content(email_content.substitute(name='Master Chief', ai_system='Cortana'), 'html')


def send_email():
    print("Please wait, It might take a while :)\n")
    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login("AUTHOR'S E-MAIL", "AUTHOR'S EMAIL PASSKEY")     # contact.samskywalker@gmail.com, abcdefghijklmnopq
        smtp.send_message(email)


if __name__ == '__main__':
    try:
        print("Sending E-Mail...\n")
        send_email()
        print('\n\t Email Sent :) \n')
    
    except KeyboardInterrupt:
        print('\n\t Operation Cancelled By User :( \n')
    
    except Exception as e:
        print(f'\n\t Something went wrong :( \n\n\t {e} \n')
        