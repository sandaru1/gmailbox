#!/usr/bin/env python
#-*- coding:utf-8 -*-

import gobject,gtk,signal,os
import Tray, Checker, MailView

def quit():
	c.stop = True
	#gtk.main_quit()
	os._exit(0)

def signal_handler (*args):
	quit()

if __name__ == "__main__":
	signal.signal (signal.SIGINT, signal_handler)
	signal.signal (signal.SIGSEGV, signal_handler)

	tray = Tray.Tray(quit)
	view = MailView.MailView(tray)
	c = Checker.Checker(view)
	c.start()
	gobject.threads_init()
	gtk.main()
