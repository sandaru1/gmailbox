#!/usr/bin/env python
#-*- coding:utf-8 -*-

import xml.dom.minidom
from xml.dom.minidom import Node
import os

CONFIG_FILE = os.path.expanduser('~')+"/.gmailbox/mailboxes.xml"
MAIL_ICON = "data/mail.png"
NOMAIL_ICON = "data/nomail.png"
FEED = "https://mail.google.com/%s/feed/atom"

class Config:

	def __init__(self):
		self.mailboxes = []

		doc = xml.dom.minidom.parse(CONFIG_FILE)
 
		for node in doc.getElementsByTagName("mailbox"):
			email = node.getAttribute("email")
			passwd = node.getAttribute("password")
			self.mailboxes.append([email,passwd])

	def getMailboxes(self):
		return self.mailboxes
