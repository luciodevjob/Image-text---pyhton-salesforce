import pytesseract
import cv2
import json
from simple_salesforce import Salesforce, SalesforceLogin, SFType

imagem = cv2.imread("lucio.png")

texto = pytesseract.image_to_string(imagem, lang="por")
#contato = texto.find("Contato")
texto = texto.splitlines()
res=[]
for abacaxi in texto:
    if abacaxi.strip():
        res.append(abacaxi)
#pre = texto.find("Contato")

nomePos = res.index('Process Automation')
contatoPos = res.index('Contato')

contato = res[contatoPos+1].replace(" ","@")
nome = res[nomePos+1].replace(" ",",")
nome = nome.split(',')
sobrenome = ' '.join(nome[1:])


loginInfo = json.load(open('login.json'))
username =   loginInfo['username'] 
password =   loginInfo['password']
security_token = loginInfo['security_token']
domain = 'login'

#sf = Salesforce(username=username, password=passowrd, security_token=security_token, domain=domain)
session_id, instance = SalesforceLogin(username=username, password=password, security_token=security_token, domain=domain)
sf = Salesforce(instance=instance, session_id=session_id)
print(sf)
Account = SFType('Python__c', session_id, instance)

data = {
    'Name': nome[0],
    'Sobrenome__c': sobrenome,
    'Email__c': contato
}

response = Account.create(data)
print(response)