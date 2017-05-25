import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from sense_hat import SenseHat

def Alert(sensor):
    fromaddr = "chabe@mtemtf.com"
    toaddr = "salcaraz@mtemtf.com"
    cc = ['salcaraz@mtemtf.com','satfer@gmail.com']
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    toaddrs = [toaddr] + cc
    msg['Subject'] = "ALERTE CLIM"
    temperature = str(sensor)

    body = "CLIM A VERIFIER TEMPERATURE : "+temperature+" degres"
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('ssl0.ovh.net', 587)
    server.starttls()
    server.login(fromaddr, "che47u")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddrs, text)
    server.quit()

def TestTemperature():
    sense = SenseHat()
    temp = sense.temp
    temperature = int(temp)
    temp = int(temp)
    temp = str(temp)
    sense.show_message(temp, text_colour=(255, 255, 0), back_colour=(0, 0, 255))
    sense.clear()
    if temperature > 30:
        Alert(temp)

TestTemperature()

