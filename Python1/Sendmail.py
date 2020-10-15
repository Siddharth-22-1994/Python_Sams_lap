# 1st step:
# Go to this page --> Less secure app access - https://myaccount.google.com/lesssecureapps?pli=1

# --------------------------------------------------------
# Normail GMail----> No attachment

# import smtplib
# emailuser = 'siddharthece1994@gmail.com'
# emailsent = 'sagarmarri21@gmail.com'
# server = smtplib.SMTP('smtp.gmail.com', 587)
# server.starttls()

# server.login(emailuser, 'siddhu1994')
# message = 'Hey iam sending this through python, You have got selected in cruew training'
# server.sendmail(emailuser, emailsent, message)
# server.quit()

# ------------------------------------------------------------------
# Gmail ----> With attachment

# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# from email.mime.base import MIMEBase
# from email import encoders

# email_user = 'siddharthece1994@gmail.com'
# email_password = 'siddhu1994'
# # email_send = 'siva9014475682@gmail.com'
# email_send = 'sagarmarri21@gmail.com'

# subject = 'This is mail from Python with Attachment'

# msg = MIMEMultipart()
# msg['From'] = email_user
# msg['To'] = email_send
# msg['Subject'] = subject

# body = 'Hi there, sending this email from Python!'
# msg.attach(MIMEText(body, 'plain'))

# filename = 'Sendmail.py'
# attachment = open(filename, 'rb')

# part = MIMEBase('application', 'octet-stream')
# part.set_payload((attachment).read())
# encoders.encode_base64(part)
# part.add_header('Content-Disposition', "attachment; filename= "+filename)

# msg.attach(part)
# text = msg.as_string()
# server = smtplib.SMTP('smtp.gmail.com', 587)
# server.starttls()
# server.login(email_user, email_password)


# server.sendmail(email_user, email_send, text)
# server.quit()


# https://www.youtube.com/watch?v=bXRYJEKjqIM - src lnk
