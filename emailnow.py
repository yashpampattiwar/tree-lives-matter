import smtplib
server = smtplib.SMTP('smtp.gmail.com',465)
server.starttls()
server.login("raspi.iot33","raspberryPi33")
msg = 'test msg'
server.sendmail("raspi.iot33","aaditya.newaskar@gmail.com",msg)
server.quit()