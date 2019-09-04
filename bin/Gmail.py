import smtplib
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

PASSWORD = 'XXXXXXXXX'
MY_ADDRESS = 'XXXXXX@gmail.com'

def send_gmail(user,pwd,recipient,subject,body):
    FROM = user
    TO = recipient if isinstance(recipient, list) else [recipient]
    SUBJECT = subject
    TEXT = body

    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        # make sure you allow less secure app to avoid failure
        # https://www.google.com/settings/security/lesssecureapps
        server.login(user, pwd)
        server.sendmail(FROM, TO, message)
        server.quit()
        print('successfully sent the mail')

    except:
        print("failed to send mail")


if __name__ == "__main__":
    send_gmail(MY_ADDRESS,PASSWORD,"delin.bio@gmail.com","Test from Python", "This is a test")






