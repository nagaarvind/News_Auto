# # import smtplib
# # import getpass
# import win32com.client

# #outlook mail
# def auto_mate(msg):
#     ol = win32com.client.Dispatch('Outlook.Application')

#     olmailitem_dimension = 0x0
#     newmail = ol.createItem(olmailitem_dimension)

#     newmail.subject = 'News Auto Testing mail'

#     newmail.To = "nagaarvind.n@ingrammicro.com"
#     newmail.CC = "narayankumar.m@ingrammicro.com"

#     newmail.Body = "Hello, this is testing email in outlook"
#     newmail.Display()

#     newmail.send()
#     newmail.quit()

# print("mail sent")




# # def auto_mate(msg):
# #     userMail = "officialteche@gmail.com"
# #     password = "yqgd crfb qqdi brto"
# #     print("password entered:", '*****')
# #     # senderMail = input('sender_mail:')
# # #    senderMail = "narenmicom@gmail.com"
# #     senderMail =['nagaarvind.n@ingrammicro.com','narayankumar.m@ingrammicro.com',msg]
# #     server = smtplib.SMTP('smtp-mail.outlook.com',587)
# #     #to start a safe tls., connecting server to send mail to the client
# #     server.starttls()
# #     server.login(userMail,password)
# #     server.sendmail(userMail,senderMail)
# #     server.sendmail

# #     print('mail sent')
# #     server.quit()
