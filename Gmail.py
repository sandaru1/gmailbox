#!/usr/bin/env python
#-*- coding:utf-8 -*-

import urllib
import feedparser
import Config

class GmailFeed(urllib.FancyURLopener):

	def __init__(self,username,passwd):
		urllib.FancyURLopener.__init__(self)
		self.username = username
		self.passwd = passwd
		self.tried = False
		self.invalid = False
		
	def http_error_401(self, url, fp, errcode, errmsg, headers, data=None):
		if self.tried :
			self.invalid = True
			return
		self.tried = True
		return urllib.FancyURLopener.http_error_401(self, url, fp, errcode, errmsg, headers, data);
	
	def prompt_user_passwd(self, host, realm):
		"""Don't prompt for credentials"""
		return self.username,self.passwd

class Gmail:

	def __init__(self,email,passwd):
		self.email = email
		self.passwd = passwd
		username , domain = self.email.split('@')
		if domain != "gmail.com" : 
			domain = "a/" + domain
		else : 
			domain = "gmail"
		self.feedUrl = Config.FEED % domain
		self.feed = GmailFeed(self.email,self.passwd)

 	def inbox(self):
 		self.feed.tried = False
		f = self.feed.open(self.feedUrl)
		if self.feed.invalid :
			print "Invalid Username/Password"
			return []
		else :
			atom = feedparser.parse(f.read())
			mails = []
			for mail in atom.entries:
				mails.append([mail.author,mail.title,mail.link])
			return mails

