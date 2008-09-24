#!/usr/bin/env python
#-*- coding:utf-8 -*-

class MailView:
	def __init__(self,tray):
		self.tray = tray
		self.mails = {}
		self.tray.connect('tooltip',self.tooltip);
		
	def tooltip(self,tray,show) :
		pass

	def update(self,mails):
		if len(mails) == 0 :
			self.tray.change(False)
		else : 
			self.tray.change(True)
		current_mails = {}
		for mail in mails :
			current_mails[mail[2]] = mail
			if not self.mails.has_key(mail[2]) :
				text = "<b>From</b> : " + mail[0] + "\n" + "<b>Subject</b> : " + mail[1];
				self.tray.popup("New Mail",text)
		self.mails = current_mails

