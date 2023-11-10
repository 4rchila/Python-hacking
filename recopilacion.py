import requests
from os import path
import argparse #es usado para tomar dominios
import sys

parser = argparse.ArgumentParser()
parser.add_argument('-t','--target',help='indicar el dominio de la victima')#help
parser = parser.parse_args()

def main():
    if parser.target:
        if path.exists('subdominios.txt'):#este hace una comprobacion de que exista el archivo
           wordlist = open('subdominios.txt', 'r')
           wordlist = wordlist.read().split('\n')
           for subdominio in wordlist:
             url = "https://"+subdominio+"."+parser.target
             try:
               requests.get(url)
             except requests.ConnectionError:
               pass
             else:
               print(" (+) subdominio encontrado : " + url)
               
           for subdominio in wordlist:
               url = "http://"+subdominio+"."+parser.target
               try:
                requests.get(url)
               except requests.ConnectionError:
                 pass
               else:
                  print("(+) subdominio encontrado : " + url)
    
    else:
          print('(-) ingresa un dominio')
          
if __name__ == '__main__':
    try:
      main()
    except KeyboardInterrupt:#este termino nos ayuda a finalizar el programa sin presentar algun error raro
      sys.exit()
#con esto parser tendria el domino que nosotros estamos ingresando
#agregando el parametro y tomar el argumento de dicho parametro 







