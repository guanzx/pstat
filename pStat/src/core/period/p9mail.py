#!/usr/bin/python
# -*- coding:utf-8 -*-

import smtplib, sys
from sys import argv

file_dir = argv[1]
fromaddr = "microlens_admin@funshion.com"
toaddrs = ["guanzx@funshion.com"]
subject = " p9_series data "
username = "microlens_admin@funshion.com"
password = "321,qwer!"

# Add the From: and To: headers at the start!
msg = ("From: %s\r\nTo: %s\r\nSubject: %s\r\n\r\n"
       % (fromaddr, ", ".join(toaddrs), subject))

msg += open(file_dir).read()                                                              
    
server = smtplib.SMTP('mail.funshion.com', 25, 'muse0')
server.login(username, password)
server.sendmail(fromaddr,toaddrs,msg)
server.quit()            