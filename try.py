import requests
from bs4 import BeautifulSoup


# Fill in your details here to be posted to the login form.
payload = {
    'j_username': '2911212', 'j_password': 'senha'
}



def gettabelausuario(html):
    soup = BeautifulSoup(html)
    tag='<br>'
    ftag='</br>'
    for linha in soup.find(id="usuarioTable").find_all('td'):
        print (str(linha)[str(linha).find(tag)+len(tag):str(linha).find(ftag)])
        
#nao testado
def getcompras(html):
    soup = BeautifulSoup(html)
    tag='<td>'
    ftag='</td>'
    for linha in soup.find(id="comprasTable").find_all('td'):
        print (str(linha)[str(linha).find(tag)+len(tag):str(linha).find(ftag)])
    
def getrefeicoes(html):
    soup = BeautifulSoup(html)
    tag='<td>'
    ftag='</td>'
    for linha in soup.find(id="refeicoesTable").find_all('td'):
        print (str(linha)[str(linha).find(tag)+len(tag):str(linha).find(ftag)])
    
def getagendamento(html):
    soup = BeautifulSoup(html)
    tag='<td>'
    ftag='</td>'
    for linha in soup.find(id="agendamentosTable").find_all('td'):
        print (str(linha)[str(linha).find(tag)+len(tag):str(linha).find(ftag)])    
        
def getunidade(html):
    soup = BeautifulSoup(html)
    tag='<td>'
    ftag='</td>'
    for linha  in soup.find(id="autorizacoesUnidadeTable").find_all('td'):
        print (str(linha)[str(linha).find(tag)+len(tag):str(linha).find(ftag)])    
        
        
def getbeneficio(html):
    soup = BeautifulSoup(html)
    tag='<td colspan="3">'
    ftag='</td>'
    for linha  in soup.find(id="beneficioTable").find_all('td'):
        print (str(linha)[str(linha).find(tag)+len(tag):str(linha).find(ftag)])     
        


# Use 'with' to ensure the session context is closed after use.
with requests.Session() as s:
    s.post('http://portal.ufsm.br/ru/j_security_check', data=payload)
    # print the html returned or something more intelligent to see if it's a successful login page.
    #print s.text

    # An authorised request.
    r = s.get('http://portal.ufsm.br/ru/usuario/situacao.html')
    #print r.text
    
    getbeneficio(r.text)
    

