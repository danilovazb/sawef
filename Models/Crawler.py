import threading
import time
import argparse
import requests
import json
import re,sys
from bs4 import BeautifulSoup


class crawler(object):

	def request_page(self,url):
		regex = re.compile('((https?|ftp)://|www\.)[^\s/$.?#].[^\s]*')
		t_or_f = regex.match(url) is None
		if t_or_f is True:
			pass
		else:
			try:
				user_agent = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; hu-HU; rv:1.7.8) Gecko/20050511 Firefox/1.0.4'}
				response = requests.get(url,headers=user_agent,timeout=10.000)
				html = response.text
				return html
			except:
				pass

	def parser_email(self,html):
		regex = re.compile(("([a-z0-9!#$%&'*+\/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+\/=?^_`{|}~-]+)*(@|\sat\s)(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?(\.|\sdot\s))+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?)"))
		try:
			emails = re.findall(regex, html)
			for count_email in xrange(len(emails)):
				if emails[count_email][0] in self.list_email:
					pass
				else:
					self.list_email.append(emails[count_email][0])
		except:
			pass

	def filtro_http(self,url,link):
		if url in link or 'http://' in link or 'https://' in link:
			return link
		else:
			url = "%s%s" % (url, link)

	def consulta_link(self,html,url):
		soup = BeautifulSoup(html)
		for link in soup.find_all('a', href=True):
			if link['href'] in self.lista_links or '#' == link['href'] or '/' == link['href']:
				pass
			else:
				try:
					link_completo = self.filtro_http(url,link['href'])
					html = self.request_page(link_completo)
					self.parser_email(html)
					self.lista_links.append(link_completo)
				except:
					pass

	def __init__(self,url):
		self.url = url
		self.list_email = []
		self.lista_links = []

	def crawl(self):
		#try:
			url = self.url
			ultimo_char = url[len(url)-1]
			if '/' == ultimo_char:
				pass
			else:
				url = "%s/" % url
			html = self.request_page(url)
			self.parser_email(html)
			self.consulta_link(html,url)
			############
			## Habilite para um FULLSCAN - AVISO - DEMORA PRA CARALHO
			############
			# for i in xrange(len(self.lista_links)):
			# 	#print lista_links[i]
			# 	html = self.request_page(self.lista_links[i])
			# 	if "www.facebook.com" in self.lista_links[i]:
			# 		pass
			# 	else:
			# 		self.consulta_link(html,self.lista_links[i])
			print "Emails: \n"
			for email in xrange(len(self.list_email)):
				print "[+] %s" % self.list_email[email]
			print "\nTwitter:"
			for twitter in xrange(len(self.lista_links)):
				r_twitter = re.compile('(https?):\/\/(www\.|)twitter\.com\/(#!\/)?[a-zA-Z0-9_]+')
				t_or_f = r_twitter.match(self.lista_links[twitter]) is None
				if t_or_f is True:
					pass
				else:
					print "[+] %s" % self.lista_links[twitter]
			print "\nLinkedin:"
			for linkedin in xrange(len(self.lista_links)):
				r_linkedin = re.compile('(https?):\/\/br\.linkedin\.com\/(in\/)?[a-zA-Z0-9_]+')
				t_or_f = r_linkedin.match(self.lista_links[linkedin]) is None
				if t_or_f is True:
					pass
				else:
					print "[+] %s" % self.lista_links[linkedin]
			print "\nGoogle Plus:"
			for plus in xrange(len(self.lista_links)):
				r_plus = re.compile('(https?):\/\/plus\.google\.com\/[+a-zA-Z0-9_]+')
				t_or_f = r_plus.match(self.lista_links[plus]) is None
				if t_or_f is True:
					pass
				else:
					print "[+] %s" % self.lista_links[plus]
			print "\nFacebook:"
			for facebook in xrange(len(self.lista_links)):
				r_facebook = re.compile('(https?):\/\/(www\.|)facebook\.com\/(pages\/|)[-/+a-zA-Z0-9_]+')
				t_or_f = r_facebook.match(self.lista_links[facebook]) is None
				if t_or_f is True:
					pass
				else:
					print "[+] %s" % self.lista_links[facebook]
			print "\nYoutube:"
			for youtube in xrange(len(self.lista_links)):
				r_youtube = re.compile('(https?):\/\/(www\.|)youtube\.com\/(user\/)?[a-zA-Z0-9_]+')
				t_or_f = r_youtube.match(self.lista_links[youtube]) is None
				if t_or_f is True:
					pass
				else:
					print "[+] %s" % self.lista_links[youtube]
		# except:
		# 	pass			