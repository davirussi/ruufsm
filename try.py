# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup




# Fill in your details here to be posted to the login form.

payload = {'j_username': '2911212', 'j_password': 'senha'}


def getUsuario(html):
    soup = BeautifulSoup(html)
    tag='<br>'
    ftag='</br>'
    for linha in soup.find(id="usuarioTable").find_all('td'):
        nome_saldo = str(linha)[str(linha).find(tag)+len(tag):str(linha).find(ftag)]
        if nome_saldo.find('R$')!=-1:
            print (nome_saldo)
        else:
            print (nome_saldo)
            
def getCompra(html):
    soup = BeautifulSoup(html)
    tag='<td>'
    ftag='</td>'
    data=''

    for linha in soup.find(id="comprasTable").find_all('td'):
        dado = str(linha)[str(linha).find(tag)+len(tag):str(linha).find(ftag)]
        if dado.count('/')>1 and dado.find(':')!=-1: 
            data=dado
        if dado.find('R$')!=-1:
            if data!='':
                print (data+dado[dado.find('R$')+2:])#limpando coldspan do total
                data=''
            else:
                print ('Total '+dado[dado.find('R$')+2:])#limpando coldspan do total
    

    
def getRefeicao(html):
    soup = BeautifulSoup(html)
    tag='<td>'
    ftag='</td>'
    listatipo=['Almoço','Janta','Café']
    listaru=['RU - Refeitório 2','RU - Campus']
    
    
    blinha=True #caso encontre o total para de procurar por local
    data=''
    tipo=''
    valor=''
    ru=''

    #try
    for linha in soup.find(id="refeicoesTable").find_all('td'):
        dado = str(linha)[str(linha).find(tag)+len(tag):str(linha).find(ftag)]         
        if dado.find('Total')!=-1:
            blinha=False
        if blinha:
            if dado.count('/')>1 and dado.find(':')!=-1: 
                data=dado
            elif dado.find('R$')!=-1:
                valor=dado
            elif dado in listatipo:
                tipo=dado
            elif dado in listaru:
                ru=dado
                print (data+tipo+valor+ru)
        else:
            if dado.find('R$')!=-1:
                print ('Total'+dado[dado.find('R$')+2:])
                break
            

    
def getAgendamento(html):
    soup = BeautifulSoup(html)
    tag='<td>'
    ftag='</td>'
    for linha in soup.find(id="agendamentosTable").find_all('td'):
        print (str(linha)[str(linha).find(tag)+len(tag):str(linha).find(ftag)])    
        
def getUnidade(html):
    soup = BeautifulSoup(html)
    tag='<td>'
    ftag='</td>'
    listatipo=['Almoço','Janta','Café']
    listaru=['RU - Refeitório 2','RU - Campus']
    
    tipo=''
    ru=''
    
    for linha  in soup.find(id="autorizacoesUnidadeTable").find_all('td'):
        dado = str(linha)[str(linha).find(tag)+len(tag):str(linha).find(ftag)]
        if dado in listaru:
            ru=dado
        else:
            for t in listatipo:
                if dado.count(t)>0:
                    tipo=t
                    print (ru+tipo)
        
def getBeneficio(html):
    soup = BeautifulSoup(html)
    tag='<td colspan="3">'
    ftag='</td>'
    lbeneficio=['Sem benefício']
    
    for linha  in soup.find(id="beneficioTable").find_all('td'):
        dado=str(linha)[str(linha).find(tag)+len(tag):str(linha).find(ftag)]
        for b in lbeneficio:
            if dado.count(b)>0:
                print b
        


# Use 'with' to ensure the session context is closed after use.
with requests.Session() as s:
    s.post('http://portal.ufsm.br/ru/j_security_check', data=payload)
    # print the html returned or something more intelligent to see if it's a successful login page.
    #print s.text

    # An authorised request.
    r = s.get('http://portal.ufsm.br/ru/usuario/situacao.html')
    #print r.text
  
    try:  
        getBeneficio(r.text)
    
    except AttributeError:
        print 'Nenhuma refeicao nos últimos dias'
