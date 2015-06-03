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

Th4nk my br0th3r g30l4d0 th3 b4$1$ 0f th1$ $cr1pt, 
1t 1$ b4$3d 0n https://github.com/geolado/P0st3r/blob/master/p0st3r.py

██╗     ██████╗ ██████╗ ████████╗ ██████╗ ███████╗    ██╗  ██╗██╗  ██╗██╗  ██╗ ██████╗ ██████╗ ███████╗
██║     ╚════██╗╚════██╗╚══██╔══╝██╔═████╗██╔════╝    ██║  ██║██║  ██║╚██╗██╔╝██╔═████╗██╔══██╗██╔════╝
██║      █████╔╝ █████╔╝   ██║   ██║██╔██║███████╗    ███████║███████║ ╚███╔╝ ██║██╔██║██████╔╝███████╗
██║      ╚═══██╗ ╚═══██╗   ██║   ████╔╝██║╚════██║    ██╔══██║╚════██║ ██╔██╗ ████╔╝██║██╔══██╗╚════██║
███████╗██████╔╝██████╔╝   ██║   ╚██████╔╝███████║    ██║  ██║     ██║██╔╝ ██╗╚██████╔╝██║  ██║███████║
╚══════╝╚═════╝ ╚═════╝    ╚═╝    ╚═════╝ ╚══════╝    ╚═╝  ╚═╝     ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝
                                                                                                       
0x01 - 4g0r4 3h 0 hu3hu3hu3br qu3 m4nd4, g00gl31nurlbr j4h 3$tá n4 c3n4, 4v4nt3 40 hu3hu31nth3w0rld
0x02 - $1t3: http://unk-br.blogspot.com.br
0x03 - $1t3: http://moshcode.com.br
0x04 - $1t3: http://blog.inurl.com.br
0x05 - $1t3: http://slayerowner.blogspot.com.br
0x06 - $1t3: http://koubacktr.wordpress.com/
0x07 - $1t3: http://b00t4nd0.com/
0x08 - $1t3: http://blog.inurl.com.br                                                                                                       

"""
 
import threading
import time
import argparse
import requests
import json
 
def retorno_status(retorno,response):
	if 'status_code' in retorno:
		status = response.status_code
		print "\n[+] STATUS CODE = %s" % (status)
	elif 'headers' in retorno:
		status = response.headers
		print "\n[+] HEADERS = %s" % (status)
	elif 'encoding' in retorno:
		status = response.encoding
		print "\n[+] ENCODING = %s" % (status)
	elif 'html' in retorno:
		status = response.text
		print "\n[+] HTML = %s" % (status)
	elif 'json' in retorno:
		status = response.json()
		print "\n[+] JSON = %s" % (status)
	elif 'all' in retorno:
		status = response.status_code
		print "\n[+] STATUS CODE = %s" % (status)
		status1 = response.headers
		print "\n[+] HEADERS = %s" % (status1)
		status2 = response.encoding
		print "\n[+] ENCODING = %s" % (status2)
		status2 = response.text
		print "\n[+] HTML = %s" % (status2)
		status3 = response.json()
		print "\n[+] JSON = %s" % (status3)

def request_url(qtd,url,data,user_agent,retorno,cookie,referer):
	if referer != None:
		user_agent.update(referer)
	if cookie is None:
		response = requests.post(url, data=data, headers=user_agent)
	elif cookie != None:
		response = requests.post(url, data=data, headers=user_agent, cookies=cookie)

	return response

# Função para cada thread
def send_cmd(qtd,url,data,user_agent,retorno,cookie,referer):
	response = request_url(qtd,url,data,user_agent,retorno,cookie,referer)
	retorno = retorno_status(retorno,response)
	

if __name__ == "__main__":
	
	parser = argparse.ArgumentParser(prog='tool',formatter_class=lambda prog: argparse.HelpFormatter(prog,max_help_position=20))
	parser.add_argument("--url", help = "URL to request" , metavar= "http://url.com/" ,  required=True)
	parser.add_argument("--user_agent",type=json.loads, \
		help = "For a longer list, visit: http://www.useragentstring.com/pages/useragentstring.php" , metavar= "\'{\"User-agent\": \"Mozilla/5.0 (Windows; U; Windows NT 5.1; hu-HU; rv:1.7.8) Gecko/20050511 Firefox/1.0.4\"}\"" ,  default='{"User-agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; hu-HU; rv:1.7.8) Gecko/20050511 Firefox/1.0.4"}')
	parser.add_argument("--threads", help = "Threads" , metavar= "10" , default=1)
	parser.add_argument("--data", type=json.loads, help = "Data to be transmitted by post" , metavar= "\'{\"data\":\"value\",\"data1\":\"value\"}\'" ,  required=False)
	parser.add_argument("--qtd", help = "Quantity requests" , metavar= "5" ,  default=1)
	parser.add_argument("--referer", type=json.loads,help = "Referer" , metavar= "\'{\"referer\": \"http://url.com\"}\'")
	parser.add_argument("--response", help = "Status return" , metavar= "status_code|headers|encoding|html|json", default="status_code")
	parser.add_argument("--cookies", type=json.loads,help = "Cookies from site" , metavar= "\'{\"__utmz\":\"176859643.1432554849.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)\"}\'")
	args = parser.parse_args()
	
	url = args.url
	user_agent = args.user_agent
	threads = args.threads
	data = args.data
	qtd = args.qtd
	cookie = args.cookies
	referer = args.referer
	retorno = args.response

	MAX_CONEXOES = threads
	# Thread principal
	lista_threads = []
	for i in range(int(qtd)):
		while threading.active_count() > MAX_CONEXOES:
			print("Esperando 1s...")
			time.sleep(1)
		thread = threading.Thread(target=send_cmd, args=(qtd,url,data,user_agent,retorno,cookie,referer))
		lista_threads.append(thread)
		thread.start()
	 
	# Esperando pelas threads abertas terminarem
	#print("Esperando threads abertas terminarem...")
	for thread in lista_threads:
		thread.join()
