import smtplib

my_email = ""
password = ""

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    address = ""

    for i in range(1, 101):
        connection.sendmail(from_addr=my_email, to_addrs=address, msg="Subject: IMPORTANTE!\n\n" +
        ("Tigrinho ta pagando, " * 100))

# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# print(year)
#
# date_of_birth = dt.datetime(year= 1895, month=12, day=11)
# print(date_of_birth)
