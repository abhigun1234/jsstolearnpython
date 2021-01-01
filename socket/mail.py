
try:
    # name=userData['name']
    # print(name)
    # phone_no=userData['phone_no']
    # city=userData['city']
    # country=userData['country']
    # email=userData['email']
    # birth_date=userData['birth_date']
    # # Python code to illustratdde Sending mail from
    # # your Gmail account
    # print(request.json)
    import smtplib

    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.ehlo()
    # start TLS for security
    s.starttls()
    s.ehlo()
    # Authentication
    s.login("justolearnpune@gmail.com", "justo.007")

    # message to be sent
    message = "new enquiry genrated by user "

    # sending the mail
    s.sendmail("justolearnpune@gmail.com", "justolearnpune@gmail.com", message)

    # terminating the session
    s.quit()
    # user=User(name=name,phone_no=phone_no,city=city,email=email,birth_date=birth_date)
    # user.save()
    response = 'registerd'

except:
    response = 'error'

