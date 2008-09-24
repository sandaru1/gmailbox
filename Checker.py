#!/usr/bin/env python
#-*- coding:utf-8 -*-

import time,gobject
from threading import Thread
import Gmail,Config

class Checker(Thread) :

	def __init__(self,view) :
		Thread.__init__(self)
		self.view = view
		c = Config.Config()
		self.mailboxes = []
		self.stop = False
		self.checking = True
		for box in c.getMailboxes():
			g = Gmail.Gmail(box[0],box[1])
			self.mailboxes.append(g)

	def check(self) :
		print "checking"
		mails = []
		for box in self.mailboxes :
			mails += box.inbox()
		self.view.update(mails)
		self.checking = False

	def run(self) :
		self.check()
		while not self.stop :
			if not self.checking :
				self.checking = True
				gobject.timeout_add(60000,self.check)
			time.sleep(1)
