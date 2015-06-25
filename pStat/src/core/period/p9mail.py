#!/usr/bin/python
# -*- coding:utf-8 -*-

import smtplib, sys
from sys import argv

file_dir = argv[1]
fromaddr = "**************"
toaddrs = ["**************"]
subject = " p9_series data "
username = "*****************"
password = "********"

# Add the From: and To: headers at the start!
msg = ("From: %s\r\nTo: %s\r\nSubject: %s\r\n\r\n"
       % (fromaddr, ", ".join(toaddrs), subject))

msg += open(file_dir).read()                                                              
    
server = smtplib.SMTP('*******', 25, '****')
server.login(username, password)
server.sendmail(fromaddr,toaddrs,msg)
server.quit()            
