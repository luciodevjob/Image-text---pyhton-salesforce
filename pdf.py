import PyPDF2

pdf = open('fatura.pdf', 'rb')

reader = PyPDF2.PdfFileReader(pdf)
texto = reader.getPage(0)
texto = texto.extractText()
nome = texto.find('pagador:')
texto = texto.splitlines()
res=[]
for abacaxi in texto:
    if abacaxi.strip():
        res.append(abacaxi)
#pre = texto.find("Contato")
print(res[nome+1])
