import smtplib
import ssl
# Set up the SMTP server
smtp_server = 'smtp.qq.com'
smtp_port = 465
smtp_username = '1879599141@qq.com'
smtp_password = 'a1879599141'

# Create a secure SSL context
context = ssl.create_default_context()

# Connect to the SMTP server
with smtplib.SMTP_SSL(smtp_server, smtp_port, context=context) as server:
    server.login(smtp_username, smtp_password)
    # Send email here