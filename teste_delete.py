import requests

headers = {'Authorization': 'Token 7db06996f551b69f08dad5b1942f63bb93ddf11f'}

url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'

resultado = requests.delete(url=f'{url_base_cursos}9/', headers=headers)

# Testando o código HTTP
assert resultado.status_code == 204

# Testando se o tamanho do conteúdo retornado é 0
assert len(resultado.text) == 0

# Lembrando que só pode ser executado uma vez, depois mudar id