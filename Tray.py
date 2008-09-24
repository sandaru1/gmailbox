#!/usr/bin/env python
#-*- coding:utf-8 -*-

import gtk
import Config
import pynotify
import egg.trayicon
import gobject

class Tray(gobject.GObject):
	__gsignals__ = {
		'tooltip' : (gobject.SIGNAL_RUN_LAST, gobject.TYPE_NONE,(gobject.TYPE_BOOLEAN,))
	}
	
	def on_quit(self, menu) :
		self.quit_function()
        
	def __init__(self,quit):
		gobject.GObject.__init__(self)
		pynotify.init("gmailbox")
		
		self.quit_function = quit
		self.nomail_icon = gtk.gdk.pixbuf_new_from_file(Config.NOMAIL_ICON)
		self.mail_icon = gtk.gdk.pixbuf_new_from_file(Config.MAIL_ICON)

		self.buildMenu()
		self.buildIcon()

	def buildIcon(self):
		self.tray = egg.trayicon.TrayIcon('gmailbox')
		
		self.image = gtk.Image()
		self.image.set_from_pixbuf(self.nomail_icon)

		self.eventBox = gtk.EventBox()

		self.eventBox.set_events(gtk.gdk.BUTTON_PRESS_MASK)
		self.eventBox.connect_object('button_press_event', self.on_click, self.eventBox)

		self.eventBox.add(self.image)
		
		self.tray.add(self.eventBox)

		self.eventBox.show_all()
		self.tray.show_all()

	def on_click(self, widget, event):
		if event.type == gtk.gdk.BUTTON_PRESS:
			if event.button == 1: # Left Click
				pass
			elif event.button == 3: # Right Click
				self.menu.popup(None, None, None, event.button, event.time)

	def buildMenu(self):
		self.menu = gtk.Menu()

		menuItem = gtk.ImageMenuItem( gtk.STOCK_QUIT )
		menuItem.connect('activate', self.on_quit)

		self.menu.append(menuItem)
		self.menu.show_all()

	def popup(self,subject,text):
		notification = pynotify.Notification(subject, text, attach=self.tray)
		notification.set_timeout(5000)
		notification.show()
		
	def change(self,mail=False) :
		if mail : 
			self.image.set_from_pixbuf(self.mail_icon);
		else:
			self.image.set_from_pixbuf(self.nomail_icon);
