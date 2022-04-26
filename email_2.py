import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

me = "essgroup7@gmail.com"
my_password = r"group7@ess"
you = "saurabhpowar1823@gmail.com"
msg = MIMEMultipart('alternative')
msg['Subject'] = "Fire Detected Alert!!!"
msg['From'] = me
msg['To'] = you

html = "<html><body><h1>Fire!</h1><h3>This email is to inform you that a Fire is detected in this area.</h3></body></html>"
part2 = MIMEText(html, 'html')

msg.attach(part2)

# Send the message via gmail's regular server, over SSL - passwords are being sent, afterall
s = smtplib.SMTP_SSL('smtp.gmail.com')
# uncomment if interested in the actual smtp conversation

s.login(me, my_password)

s.sendmail(me, you, msg.as_string())
s.quit()