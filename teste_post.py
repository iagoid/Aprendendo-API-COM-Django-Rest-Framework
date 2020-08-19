import requests

headers = {'Authorization': 'Token 7db06996f551b69f08dad5b1942f63bb93ddf11f'}

url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'

novo_curso = {
    "titulo": "Curso criado através de teste5",
    "url": "http://www.cursoteste5.com"
}

resultado = requests.post(url=url_base_cursos, headers=headers, data=novo_curso)

# Testando o código de estatus HTTP 201
assert resultado.status_code == 201

# Testando se o título retornado é o mesmo que o informado
assert resultado.json()['titulo'] == novo_curso['titulo']

# Lembrando que é necessário mudar o titulo e url em cada envio
