#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Danilo Vaz aka UNK"
__credits__ = ["Danilo Vaz"]
__license__ = "GPL"
__version__ = "0.1"
__maintainer__ = "Danilo Vaz aka UNK"
__email__ = "danilovazb@gmail.com"

"""
My blog: http://unk-br.blogspot.com.br
GitHub: http://github.com/danilovazb
Twitter: http://twitter.com/unknownantisec

Gr33tz: @geolado, @slayer_owner, @Rogy153, SlackDummies,@GoogleInurl, Gr0upWhatsApp [DEV]l33t0s

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
import re
from bs4 import BeautifulSoup


def retorno_form(response):
    html = response.text
    html_proc = BeautifulSoup(response.text)
    qntd_form = len(html_proc.find_all("form"))
    for i in range(int(qntd_form)):
            if html_proc.find_all("form")[i].has_attr('name'):
                    nome_form = html_proc.find_all("form")[i]['name']
            else:
                    nome_form = "None"
            if html_proc.find_all("form")[i].has_attr('action'):
                    url_action = html_proc.find_all("form")[i]['action']
            else:
                        url_action = "None"
            if html_proc.find_all("form")[i].has_attr('method'):
                    method = html_proc.find_all("form")[i]['method']
            else:
                    method = "None"
            print "\n--------------------------------"
            print "\nNOME_FORM[%s]\nURL[%s]\nMETHOD[%s]\n" % (nome_form, url_action, method)
            qntd_input = len(html_proc.find_all("form")[i].find_all("input"))
            for a in range(int(qntd_input)):
                    if html_proc.find_all("form")[i].find_all("input")[a].has_attr('name'):
                        nome_input = html_proc.find_all("form")[i].find_all("input")[a]['name']
                        if "" == nome_input:
                            nome_input = "<NONE>"
                    else:
                        nome_input = "<NONE>"
                    if html_proc.find_all("form")[i].find_all("input")[a].has_attr('value'):
                        valor_input = html_proc.find_all("form")[i].find_all("input")[a]['value']
                        if "" == valor_input:
                            valor_input = "<NONE>"
                    else:
                        valor_input = "<NONE>"
                    if html_proc.find_all("form")[i].find_all("input")[a].has_attr('type'):
                        tipo_input = html_proc.find_all("form")[i].find_all("input")[a]['type']
                        if "" == tipo_input:
                            tipo_input = "<NONE>"
                    else:
                        tipo_input = "<NONE>"
                    print "%s:%s        (%s)" % (nome_input, valor_input, tipo_input)
    
     
def retorno_status(retorno, response):
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
    elif 'links' in retorno:
        status = response.text
        soup = BeautifulSoup(status)
        found_link = 0
        new_list_links = []
        for link in soup.find_all('a', href=True):
            if link['href'] in new_list_links:
                pass
            else:
                if url in link['href'] or 'http://' in link['href']:
                    print "[+] LINK = %s" % (link['href'])
                    new_list_links.append(link['href'])
                else:
                    url_completa = "%s%s" % (url,link['href'])
                    print "[+] LINK = %s" % (url_completa)
                    new_list_links.append(url_completa)
                    
        print "[+] FOUND = %s" % (str(len(new_list_links)))
    elif 'emails' in retorno:
        status = response.text
        regex = re.compile(("([a-z0-9!#$%&'*+\/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+\/=?^_`{|}~-]+)*(@|\sat\s)(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?(\.|\sdot\s))+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?)"))
        emails = re.findall(regex, status)
        count = 0
        new_list_email = []
        for count_email in range(len(emails)):
            if emails[count_email][0] in new_list_email:
                pass
            else:
                new_list_email.append(emails[count_email][0])
                print "[+] EMAIL = %s" % (emails[count_email][0])
        print "FOUND = %s" % (str(len(new_list_email)))
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
    elif 'form' in retorno:
        form = retorno_form(response)

def request_url(qtd, url, data, user_agent, retorno, cookie, referer, method):
    if referer != None:
        user_agent.update(referer)
    if cookie is None:
        if 'post' == method: # is 'post':
            response = requests.post(url, data=data, headers=user_agent)
        else:
            response = requests.get(url, data=data, headers=user_agent)
    elif cookie != None:
        if 'post' == method: #is 'post':
            response = requests.post(url, data=data, headers=user_agent, cookies=cookie)
        else:
            response = requests.post(url, data=data, headers=user_agent, cookies=cookie)

    return response

# Função para cada thread
def send_cmd(qtd, url, data, user_agent, retorno, cookie, referer, method):
    response = request_url(qtd, url, data, user_agent, retorno, cookie, referer, method)
    retorno = retorno_status(retorno, response)
    

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(prog='tool', formatter_class=lambda prog: argparse.HelpFormatter(prog, max_help_position=20))
    parser.add_argument("--url", help = "URL to request", metavar= "http://url.com/",  required=True)
    parser.add_argument("--user_agent", type=json.loads, \
        help = "For a longer list, visit: http://www.useragentstring.com/pages/useragentstring.php", metavar= "\'{\"User-agent\": \"Mozilla/5.0 (Windows; U; Windows NT 5.1; hu-HU; rv:1.7.8) Gecko/20050511 Firefox/1.0.4\"}\"",  default='{"User-agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; hu-HU; rv:1.7.8) Gecko/20050511 Firefox/1.0.4"}')
    parser.add_argument("--threads", help = "Threads", metavar= "10", default=1)
    parser.add_argument("--data", type=json.loads, help = "Data to be transmitted by post", metavar= "\'{\"data\":\"value\", \"data1\":\"value\"}\'",  required=False)
    parser.add_argument("--qtd", help = "Quantity requests", metavar= "5",  default=1)
    parser.add_argument("--method", help = "Method sends requests", metavar= "post|get",  default='get')
    parser.add_argument("--referer", type=json.loads, help = "Referer", metavar= "\'{\"referer\": \"http://url.com\"}\'")
    parser.add_argument("--response", help = "Status return", metavar= "status_code|headers|encoding|html|form|links|emails", default="status_code")
    parser.add_argument("--cookies", type=json.loads, help = "Cookies from site", metavar= "\'{\"__utmz\":\"176859643.1432554849.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)\"}\'")
    args = parser.parse_args()
    
    url = args.url
    ultimo_char = url[len(url)-1]
    if '/' == ultimo_char:
        pass
    else:
        url = "%s/" % url
    user_agent = args.user_agent
    threads = args.threads
    data = args.data
    qtd = args.qtd
    cookie = args.cookies
    referer = args.referer
    retorno = args.response
    method = args.method

    MAX_CONEXOES = threads
    # Thread principal
    lista_threads = []
    for i in range(int(qtd)):
        while threading.active_count() > MAX_CONEXOES:
            print("Esperando 1s...")
            time.sleep(1)
        thread = threading.Thread(target=send_cmd, args=(qtd, url, data, user_agent, retorno, cookie, referer, method))
        lista_threads.append(thread)
        thread.start()
     
    # Esperando pelas threads abertas terminarem
    for thread in lista_threads:
        thread.join()
