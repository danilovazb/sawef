# SAWEF - Send Attack Web Forms
===============
```
Danilo Vaz - UNK
danilovazb@gmail.com
http://unk-br.blogspot.com
https://twitter.com/unknownantisec
```
- REQUERIMENTS
```
 ----------------------------------------------------------
threading
time
argparse
requests
json
permission          Reading & Writing
User                root privilege, or is in the sudoers group
Operating system    LINUX
Python              2.7
 ----------------------------------------------------------
```
- HELP
```
usage: tool [-h] --url http://url.com/
            [--user_agent '{"User-agent": "Mozilla/5.0 Windows; U; Windows NT 5.1; hu-HU; rv:1.7.8 Gecko/20050511 Firefox/1.0.4"}"]
            [--threads 10] --data '{"data":"value","data1":"value"}' [--qtd 5]
            [--referer '{"referer": "http://url.com"}']
            [--response status_code|headers|encoding|html|json]
            [--cookies '{"__utmz":"176859643.1432554849.1.1.utmcsr=direct|utmccn=direct|utmcmd=none"}']

optional arguments:
  -h, --help        show this help message and exit
  --url http://url.com/
                    URL to request
  --user_agent '{"User-agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; hu-HU; rv:1.7.8) Gecko/20050511 Firefox/1.0.4"}"
                    For a longer list, visit:
                    http://www.useragentstring.com/pages/useragentstring.php
  --threads 10      Threads
  --data '{"data":"value","data1":"value"}'
                    Data to be transmitted by post
  --qtd 5           Quantity requests
  --referer '{"referer": "http://url.com"}'
                    Referer
  --response status_code|headers|encoding|html|json
                    Status return
  --cookies '{"__utmz":"176859643.1432554849.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)"}'
                    Cookies from site
```
- EXAMPLE
```
Send 1 SMS anonymous to POST [in BR]:
-------------
$:> python sawef.py --url "https://smsgenial.com.br/forms_teste/enviar.php" --data '{"celular":"(11) XXXX-XXXXX","mensagem":"Teste","Testar":"Enviar"}' --threads 10 --qtd 1 --user_agent '{"User-agent":"Mozilla/5.0 Windows; U; Windows NT 5.1; hu-HU; rv:1.7.8) Gecko/20050511 Firefox/1.0.4"}'
```
