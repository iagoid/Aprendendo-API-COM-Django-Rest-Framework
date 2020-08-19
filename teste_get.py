import requests

headers = {'Authorization': 'Token 7db06996f551b69f08dad5b1942f63bb93ddf11f'}

url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'

resultado = requests.get(url=url_base_cursos, headers=headers)

print(resultado.json()['results'][-1]['id'])

# Testando se o endpoint está correto
assert resultado.status_code == 200

# Testando a quantidade de registros
# Útil quando espero resultados fixos
# assert resultado.json()['count'] == 3

# Testando se o titulo do primeiro curso está correto
# Teste de valores iguais
assert resultado.json()['results'][0]['titulo'] == 'Teste v2'












