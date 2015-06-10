# SAWEF - Send Attack Web Forms
===============
```
Danilo Vaz - UNK
danilovazb@gmail.com
http://unk-br.blogspot.com
https://twitter.com/unknownantisec
```
=== DESCRIPTION
```
The purpose of this tool is to be a Swiss army knife 
for anyone who works with HTTP, so far it she is basic, 
bringing only some of the few features that want her to have, 
but we can already see in this tool:

- Email Crawler in sites
- Crawler forms on the page
- Sending POST and GET
- Support for USER-AGENT
- Support for THREADS
- Support for COOKIES
```

=== REQUERIMENTS
```
 ----------------------------------------------------------
threading
time
argparse
requests
json
BeautifulSoap
permission          Reading & Writing
User                root privilege, or is in the sudoers group
Operating system    LINUX
Python              2.7
 ----------------------------------------------------------
```
=== INSTALL
```
git clone http://github.com/danilovazb/SAWEF

sudo apt-get install python-bs4 python-requests
```
=== HELP
```
usage: tool [-h] --url http://url.com/
            [--user_agent '{"User-agent": "Mozilla/5.0 Windows; U; Windows NT 5.1; hu-HU; rv:1.7.8 Gecko/20050511 Firefox/1.0.4"}"]
            [--threads 10] [--data '{"data":"value","data1":"value"}']
            [--qtd 5] [--method post|get]
            [--referer '{"referer": "http://url.com"}']
            [--response status_code|headers|encoding|html|json|form]
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
  --method post|get
                    Method sends requests
  --referer '{"referer": "http://url.com"}'
                    Referer
  --response status_code|headers|encoding|html|json|form
                    Status return
  --cookies '{"__utmz":"176859643.1432554849.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)"}'
                    Cookies from site

```
=== EXAMPLE
```
*Send 1 SMS anonymous to POST [in BR]:
-------------
$:> python sawef.py --url "https://smsgenial.com.br/forms_teste/enviar.php" --data '{"celular":"(11) XXXX-XXXXX","mensagem":"Teste","Testar":"Enviar"}' --threads 10 --qtd 1 --user_agent '{"User-agent":"Mozilla/5.0 Windows; U; Windows NT 5.1; hu-HU; rv:1.7.8) Gecko/20050511 Firefox/1.0.4"}'

*List Form attributes:
-------------
$:> python sawef.py --url "https://smsgenial.com.br/ --method post --response form
OUTPUT:

--------------------------------
NOME_FORM[None]
URL[http://paineldeenvios.com/painel/app/login/login.php]
METHOD[post]

email:Digite Seu Login        (text)
passwd:Senha        (password)
Entrar:Entrar        (submit)

--------------------------------
NOME_FORM[form1]
URL[/forms_teste/criaruser.php]
METHOD[post]

action:criarconta        (hidden)
nome:<NONE>        (text)
celular:<NONE>        (text)
email:<NONE>        (text)
Testar:Criar        (submit)
Testar:Enviar        (hidden)

--------------------------------
NOME_FORM[None]
URL[/forms_teste/enviar.php]
METHOD[post]

celular:<NONE>        (text)
Testar:Enviar        (submit)


```
=== SCREENSHOT
![Screenshot](https://unknownsec.files.wordpress.com/2015/06/screenshot.png)
