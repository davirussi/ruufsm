import requests

# Fill in your details here to be posted to the login form.
payload = {
    'j_username': '2911593', 'j_password': 'senha'
}

# Use 'with' to ensure the session context is closed after use.
with requests.Session() as s:
    s.post('http://portal.ufsm.br/ru/j_security_check', data=payload)
    # print the html returned or something more intelligent to see if it's a successful login page.
    #print s.text

    # An authorised request.
    r = s.get('http://portal.ufsm.br/ru/usuario/situacao.html')
    print r.text
