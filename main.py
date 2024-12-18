import os
import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Function to fetch a motivational quote
def get_motivational_quote():
    response = requests.get("https://api.quotable.io/random")
    if response.status_code == 200:
        quote_data = response.json()
        return f'"{quote_data["content"]}" - {quote_data["author"]}'
    else:
        return "Could not retrieve a quote."

# Function to send an email
def send_email(quote, sender_email, sender_password, recipient_email):
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = "Daily Motivational Quote"

    body = quote
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        text = msg.as_string()
        server.sendmail(sender_email, recipient_email, text)
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Main function
def main():
    sender_email = os.getenv('SENDER_EMAIL')
    sender_password = os.getenv('SENDER_PASSWORD')
    recipient_email = os.getenv('RECIPIENT_EMAIL')

    quote = get_motivational_quote()
    send_email(quote, sender_email, sender_password, recipient_email)

if __name__ == "__main__":
    main()
