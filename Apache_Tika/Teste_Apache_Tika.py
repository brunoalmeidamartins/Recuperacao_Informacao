#!/usr/bin/python

import os
import json

import tika
from tika import parser
from tika import language
from tika import translate
from tika import detector

path_home = os.getenv("HOME") #Captura o caminho da pasta HOME do Usuario
path_pasta_arquivos = path_home + '/Recuperacao_Informacao/Apache_Tika/Arquivos_Para_Testes/'

#arquivos = os.listdir(path_pasta_arquivos) #Recebe lista de arquivos da pasta

arq0 = 'Example_Apache_Tika.docx'
arq1 = 'Example_Apache_Tika.odt'
arq2 = 'Example_Apache_Tika.pdf'
arq3 = 'Example_Apache_Tika.rtf'
arq4 = 'KALEO_Way_Down_We_Go.mp3'
arq5 = 'python.jpeg'
arq6 = 'Apache_Tika.html'
arq7 = 'Example_Apache_Tika.txt'

arquivos = [arq0, arq1, arq2, arq3, arq6, arq4, arq5, arq7]

tika.initVM()

print("--------------Metadados e o Conteudo dos arquivos--------------")
for i in range(0,5):
    print("--------------------------------------------------------------")
    print("Nome arquivo: " + arquivos[i])
    parsed = parser.from_file(path_pasta_arquivos + arquivos[i]) #Faz um parse do arquivo
    metadata = parsed["metadata"]
    print(json.dumps(metadata, indent=4)) #Imprime em um formato melhor

    print(parsed["content"]) #Imprime o conteudo do arquivo
    print("--------------------------------------------------------------")
    print("\n\n\n")

print("--------------Idioma do arquivo--------------")
print("O idioma do texto eh: ", language.from_file(path_pasta_arquivos + arq7), '\n\n') #Detecta o idioma do arquivo


print("--------------Traducao arquivo--------------")
print(translate.from_file(path_pasta_arquivos + arq7, 'en', 'es')) #Faz uma traducao do idioma de origem

print("\n\n")

print("--------------Classificacao dos arquivos--------------") #Tipos dos arquivos MIME
for arquivo in arquivos:
    print("Nome arquivo: %s \tTipo: %s" %(arquivo, detector.from_file(path_pasta_arquivos + arquivo)))

print("\n\n")
print("--------------Metadados Audio--------------")
parsed = parser.from_file(path_pasta_arquivos + arq4) #Faz um parse do arquivo
metadata = parsed["metadata"]
print(json.dumps(metadata, indent=4)) #Imprime em um formato melhor


print("\n\n")
print("--------------Metadados IMG--------------")
parsed = parser.from_file(path_pasta_arquivos + arq5) #Faz um parse do arquivo
metadata = parsed["metadata"]
print(json.dumps(metadata, indent=4)) #Imprime em um formato melhor


