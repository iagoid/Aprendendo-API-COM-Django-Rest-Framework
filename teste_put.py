import requests

headers = {'Authorization': 'Token 7db06996f551b69f08dad5b1942f63bb93ddf11f'}

url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'

curso_atualizado = {
    "titulo": "Curso atualizado",
    "url": "http://cursoatualizado.com"
}

# Buscanco curso com id 9
# curso = requests.get(url=f'{url_base_cursos}9/', headers=headers)
# print(curso.json())

resultado = requests.put(url=f'{url_base_cursos}9/', headers=headers, data=curso_atualizado)

# Testando código de status HTTP
assert resultado.status_code == 200

# Testando se título é igual
assert resultado.json()['titulo'] == curso_atualizado['titulo']

