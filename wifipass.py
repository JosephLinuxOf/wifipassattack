#!/usr/bin/python

import string, random
import sys
import os
import itertools

try:
    import requests
except:
    print "Os componentes necessarios nao foram encontradas. Instale para seguir adiante\n"
    sys.exit()


print "\n#################################################"
print "#     _              _     _                    #"
print "#    | | ___   ___  | |   (_)_ __  _   ___  __  #"
print "# _  | |/ _ \ / _ \ | |   | | '_ \| | | \ \/ /  #"
print "#| |_| | (_) |  __/ | |___| | | | | |_| |>  <   #"
print "# \___/ \___/ \___| |_____|_|_| |_|\__,_/_/\_\  #"
print "#                                               #"
print "# Desenvolvido por Joseph Linux                 #"
print "# Criando Wordlist numerica - wifipass attack   #"
print "# www.telegram.me/linuxteambr - TLB Sec         #"
print "#################################################\n\n"


minimum=input('Numero minimo de caracteres: ')
maximum=input('Numero maximo de caracteres ')
wmaximum=input('Quantidade de senhas que deseja gerar: ')


alphabet = string.digits

string=''
FILE = open("senhasgeradas.txt","w")
for count in xrange(0,wmaximum):
  for x in random.sample(alphabet,random.randint(minimum,maximum)):
      string+=x
  FILE.write(string+'\n')
  string=''
FILE.close()
print 'Processo terminado!'

