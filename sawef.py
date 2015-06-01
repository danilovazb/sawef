#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Danilo Vaz aka UNK"
__credits__ = ["Danilo Vaz"]
__license__ = "GPL"
__version__ = "0.1"
__maintainer__ = "Danilo Vaz aka UNK"
__email__ = "danilovazb@gmail.com"

"""
Gr33tz: @geolado, @slayer_owner, @Rogy153, SlackDummies,@GoogleInurl, Gr0upWhatsApp [DEV]l33t0s

Thank my brother Geolado the basis of this script, 
it is based on https://github.com/geolado/P0st3r/blob/master/p0st3r.py

"""

import threading
import time
import argparse
import requests
import json
 
# Função para cada thread
def send_cmd(qtd,url,data,user_agent):
	response = requests.post(url, data=data, headers=user_agent)
	status = response.status_code
	print "[%s] STATUS CODE = %s" % (qtd,status)

if __name__ == "__main__":
	
	parser = argparse.ArgumentParser(prog='tool',formatter_class=lambda prog: argparse.HelpFormatter(prog,max_help_position=50))
	parser.add_argument("--url", help = "URL to request" , metavar= "http://url.com/" ,  required=True)
	parser.add_argument("--user_agent",type=json.loads, \
		help = "For a longer list, visit: http://www.useragentstring.com/pages/useragentstring.php" , metavar= "\'{\"User-agent\": \"Mozilla/5.0 (Windows; U; Windows NT 5.1; hu-HU; rv:1.7.8) Gecko/20050511 Firefox/1.0.4\"}\"" ,  default='{"User-agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; hu-HU; rv:1.7.8) Gecko/20050511 Firefox/1.0.4"}')
	parser.add_argument("--threads", help = "Threads" , metavar= "10" , default=1)
	parser.add_argument("--data", type=json.loads, help = "Data to be transmitted by post" , metavar= "\'{\"data\":\"value\",\"data1\":\"value\"}\'" ,  required=True)
	parser.add_argument("--qtd", help = "Quantity requests" , metavar= "5" ,  default=1)
	parser.add_argument("--referer", help = "Referer" , metavar= "http://url.com/")
	parser.add_argument("--cookies", type=json.loads,help = "Cookies from site" , metavar= "\'{\"__utmz\":\"176859643.1432554849.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)\"}\'")
	args = parser.parse_args()
	
	url = args.url
	user_agent = args.user_agent
	threads = args.threads
	data = args.data
	qtd = args.qtd
	cookie = args.cookies
	referer = args.referer

	MAX_CONEXOES = threads
	# Thread principal
	lista_threads = []
	for i in range(int(qtd)):
		while threading.active_count() > MAX_CONEXOES:
			print("Esperando 1s...")
			time.sleep(1)
		thread = threading.Thread(target=send_cmd, args=(qtd,url,data,user_agent))
		lista_threads.append(thread)
		thread.start()
	 
	# Esperando pelas threads abertas terminarem
	print("Esperando threads abertas terminarem...")
	for thread in lista_threads:
		thread.join()
