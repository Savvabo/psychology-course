# def send_email(body, email):
#     email_from = 'savvabogun@gmail.com'
#     import smtplib
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.starttls()
#     server.login(email_from, 'k.,k.Rbh.ie')
#     message = """From: %s\nTo: %s\n\n%s
#     """ % (email_from, email, body)
#     server.sendmail(email_from, email, message)
#     server.close()
#
#
# if __name__ == '__main__':
#         send_email('khuyi', 'martindevil666666@gmail.com')


def format_message(person_data):
    template = "    1. {person_phone}     \n " \
               "    2. {person_name}     \n " \
               "    3. {person_messenger} "
    message = template.format(person_phone=person_data['Phone'],
                              person_name=person_data['Name'],
                              person_messenger=person_data['Выберите мессенжер для связи'],
                              )
    return message
