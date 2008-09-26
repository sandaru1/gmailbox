#!/usr/bin/env python
#-*- coding:utf-8 -*-

import gtk

class MailView:
	def __init__(self,tray):
		self.tray = tray
		self.mails = {}
		self.mailLabels = {}
		self.tray.connect('tooltip',self.tooltip)
		self.createWindow()
		
	def tooltip(self,tray,show) :
		self.VBox.resize_children()
		self.window.resize_children()
		if show :
			self.window.show_all()
		else:
			self.window.hide()

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
				self.mailLabels[mail[2]] = gtk.Label()
				self.mailLabels[mail[2]].set_markup(text)
				self.mailLabels[mail[2]].set_alignment(0,0)
				self.VBox.pack_start(self.mailLabels[mail[2]],True,True,10)
		for mail in self.mails:
			if not current_mails.has_key(mail):
				self.VBox.remove(self.mailLabels[mail])
		self.mails = current_mails

	def createWindow(self):
		self.window = gtk.Window(gtk.WINDOW_POPUP)
		self.window.set_resize_mode(gtk.RESIZE_IMMEDIATE)
		self.window.modify_bg(gtk.STATE_NORMAL,gtk.gdk.Color(65535,65535,65535))
		self.VBox = gtk.VBox()
		self.VBox.set_resize_mode(gtk.RESIZE_IMMEDIATE)
		hbox = gtk.HBox()
		hbox.pack_start(self.VBox,True,True,10)
		self.window.add(hbox)

