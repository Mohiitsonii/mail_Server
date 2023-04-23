import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
   
fromaddr = "Mohitsoni004488@gmail.com"
toaddr = "Mohitsonims04@gmail.com"
   

msg = MIMEMultipart()
msg['From'] = fromaddr 
msg['To'] = toaddr
  
# storing the subject 
msg['Subject'] = "Prabhu Kripa"
  
# string to store the body of the mail
body = "Prabhu Kripa"
  
# attach the body with the msg instance
msg.attach(MIMEText(body, 'plain'))
  
# open the file to be sent 
filename = "Mohit_soni_resume.pdf"
attachment = open("mail_server/mohit_soni_resume.pdf", "rb")
  
# instance of MIMEBase and named as p
p = MIMEBase('application', 'octet-stream')
  
# To change the payload into encoded form
p.set_payload((attachment).read())
  

encoders.encode_base64(p)
   
p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
  
msg.attach(p)
  

s = smtplib.SMTP('smtp.gmail.com', 587)
  

s.starttls()
  
s.login(fromaddr, "yppfczkynkkmqghv")
  
text = msg.as_string()
  
s.sendmail(fromaddr, toaddr, text)

s.quit()