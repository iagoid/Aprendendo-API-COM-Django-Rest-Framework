import requests

# GET AVALIAÇÕES

# avaliacoes = requests.get('http://localhost:8000/api/v2/avaliacoes/')
# ACESSANDO O CÓDIGO DE STATUS HTTP
# print(avaliacoes.status_code)

# Acessando os dados da resposta
# Retorna os dados em um dicionário
# print(avaliacoes.json())

# Acessando a quantidade de registro
# print(avaliacoes.json()['count'])

# Acessando a próxima página de resultados
# print(avaliacoes.json()['next'])

# Acessoando os resultados dessa página
# Retorna os dados em uma lista
# print(avaliacoes.json()['results'])

# Acessando o primeiro elemento da lista de resultados
# print(avaliacoes.json()['results'][0])

# Acessando o ultimo elemento da lista de resultados
# print(avaliacoes.json()['results'][-1])

# Acessando o nome da pessoa que fez a ultima avaliação
# print(avaliacoes.json()['results'][-1]['nome'])

# GET AVALIAÇÃO
# avaliacao = requests.get('http://localhost:8000/api/v2/avaliacoes/5/')
# print(avaliacao.json())

#GET CURSOS
# Para acessar os cursos é necessário ser um usuário autenticado
headers = {'Authorization': 'Token 7db06996f551b69f08dad5b1942f63bb93ddf11f'}

cursos = requests.get(url='http://localhost:8000/api/v2/cursos/', headers=headers)
print(cursos.status_code)
print(cursos.json())


