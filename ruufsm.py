# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

class MyClass:
    """A simple example class"""
    i = 12345
    def f(self):
        return 'hello world'
        
    def __init__(self):
        print ('estou sendo estanciado ')
        self.data = []
        
class Complex:
    def __init__(self, real, imag):
        self.r=real
        self.i=imag
 

    def __g(self):
        return 'lol'
                
    def f(self):
   
        return 'hello world'+ self.__g()

        



class RuUfsm:
    def __init__(self, nome, senha):
        self.nome=nome
        self.senha=senha
        self.online=False
        self.soup=''
        self.nomecompleto=''
        self.saldo=''
        self.compra=[]
        self.refeicao=[]
        self.agendamento=[]
        self.unidade=[]
        self.beneficio=''
        self.__fetch()
          
    def __fetch(self):
        payload =  dict()
        payload['j_username'] = self.nome
        payload['j_password'] = self.senha
        
        with requests.Session() as sessao:
            sessao.post('http://portal.ufsm.br/ru/j_security_check', data=payload)
            # print the html returned or something more intelligent to see if it's a successful login page.
            #print s.text
            # An authorised request.
            retorno = sessao.get('http://portal.ufsm.br/ru/usuario/situacao.html')
            self.soup=BeautifulSoup(retorno.text)
            self.online=True
            #print r.text
        if self.online:
            print('\nUSUARIO SALDO')
            #self.__getUsuario()
            print('\nULTIMAS COMPRAS')
            #self.__getCompra()
            print('\nULTIMAS REFEICOES')
            self.__getRefeicao()
            print('\nULTIMOS AGENDAMENTOS')
            #self.__getAgendamento()
            print('\nRUs')
            #self.__getUnidade()
            print('\nBENEFICIOS')
            #sself.__getBeneficio()
            
    def __getUsuario(self):
        tag='<br>'
        ftag='</br>'
        for linha in self.soup.find(id="usuarioTable").find_all('td'):
            nome_saldo = str(linha)[str(linha).find(tag)+len(tag):str(linha).find(ftag)]
            print (nome_saldo)
            if nome_saldo.find('R$')!=-1:
                self.nomecompleto = nome_saldo
            else:
                self.saldo = nome_saldo
                    
    def __getCompra(self):
        tag='<td>'
        ftag='</td>'
        data=''
        try:
            for linha in self.soup.find(id="comprasTable").find_all('td'):
                dado = str(linha)[str(linha).find(tag)+len(tag):str(linha).find(ftag)]
                if dado.count('/')>1 and dado.find(':')!=-1: 
                    data=dado
                if dado.find('R$')!=-1:
                    if data!='':
                        print (data+dado[dado.find('R$')+2:])#limpando coldspan do total
                        self.compra.append((data,dado[dado.find('R$')+2:]))
                        data=''
                    else:
                        print ('Total '+dado[dado.find('R$')+2:])#limpando coldspan do total
                        self.compra.append(('Total',dado[dado.find('R$')+2:]))
        except AttributeError:
            print 'Nenhuma compra nos últimos dias'
        
    def __getRefeicao(self):
        tag='<td>'
        ftag='</td>'
        #listatipo=['Almoço','Janta','Café','Distribuição']
        listatipo=['Almoço','Janta','Café']
        listaru=['RU - Refeitório 2','RU - Campus']
        
        blinha=True #caso encontre o total para de procurar por todas as variaveis
        data=''
        tipo=''
        valor=''
        ru=''    
        
        try:
            for linha in self.soup.find(id="refeicoesTable").find_all('td'):
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
        except:
            print ('Nenhuma refeição realizada nos últimos 10 dias')
 

 
 
    #nao implementado        
    def __getAgendamento(self):
#        tag='<td>'
#        ftag='</td>'
#        for linha in self.soup.find(id="agendamentosTable").find_all('td'):
#            print (str(linha)[str(linha).find(tag)+len(tag):str(linha).find(ftag)])    
        pass
            
    def __getUnidade(self):
        tag='<td>'
        ftag='</td>'
        listatipo=['Almoço','Janta','Café']
        listaru=['RU - Refeitório 2','RU - Campus']
        
        tipo=''
        ru=''
        
        try:
            for linha  in self.soup.find(id="autorizacoesUnidadeTable").find_all('td'):
                dado = str(linha)[str(linha).find(tag)+len(tag):str(linha).find(ftag)]
                if dado in listaru:
                    ru=dado
                else:
                    for t in listatipo:
                        if dado.count(t)>0:
                            tipo=t
                            print (ru+tipo) 
                            self.unidade.append((ru,tipo))
                             
        except:
            print ('Nenhum local encontrado')
                 
    def __getBeneficio(self):
        tag='<td colspan="3">'
        ftag='</td>'
        lbeneficio=['Sem benefício']
        beneficio=''
        try:
            for linha  in soup.find(id="beneficioTable").find_all('td'):
                dado = str(linha)[str(linha).find(tag)+len(tag):str(linha).find(ftag)]
                for b in lbeneficio:
                    if dado.count(b)>0:
                        beneficio = b
                        self.beneficio=beneficio

        except:
            print ('Nenhum beneficio encontrado')
            
 



