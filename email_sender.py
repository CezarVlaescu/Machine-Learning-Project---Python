import smtplib

def send_email(product, ans, recipient_email):
    s = smtplib.SMTP('smtp.mail.yahoo.com', 587)
    s.starttls()

    # Message

    email_subject = f"{product} Product Availability"
    email_body = f"The product {product} is available. Status : {ans}"

    headers = "\r\n".join([
        "from: your_email@yahoo.com",
        f"subject: {email_subject}",
        f"to: {recipient_email}",
        "mime-version: 1.0",
        "content-type: text/html"
    ])

    content = headers + "\r\n\r\n" + email_body
    s.sendmail("your_email@yahoo.com", recipient_email, content)
    s.quit()