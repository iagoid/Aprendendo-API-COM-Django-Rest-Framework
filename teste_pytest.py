import requests


class TestCursos:
    headers = {'Authorization': 'Token 7db06996f551b69f08dad5b1942f63bb93ddf11f'}

    url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
    url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'

    # É necessário ser test_
    def test_get_cursos(self):
        resposta = requests.get(url=self.url_base_cursos, headers=self.headers)

        assert resposta.status_code == 200

    def test_get_curso(self):
        resposta = requests.get(url=f'{self.url_base_cursos}21/', headers=self.headers)

        assert resposta.status_code == 200

    def test_post_curso(self):
        novo_curso = {
            "titulo": "Curso criado através de Pytest",
            "url": "http://www.cursopytest.com"
        }
        resposta = requests.post(url=self.url_base_cursos, headers=self.headers, data=novo_curso)

        assert resposta.status_code == 201
        assert resposta.json()['titulo'] == novo_curso['titulo']

    def test_put_curso(self):
        curso_atualizado = {
            "titulo": "Curso atualizado Pytest",
            "url": "http://cursoatualizado.com"
        }
        resposta = requests.put(url=f'{self.url_base_cursos}24/', headers=self.headers, data=curso_atualizado)

        assert resposta.status_code == 200

    def test_put_titulo_curso(self):
        curso_atualizado = {
            "titulo": "Curso atualizado Pytest",
            "url": "http://cursoatualizado.com"
        }
        resposta = requests.put(url=f'{self.url_base_cursos}24/', headers=self.headers, data=curso_atualizado)

        assert resposta.json()['titulo'] == curso_atualizado['titulo']

    def test_delete_curso(self):
        resposta = requests.delete(url=f'{self.url_base_cursos}24/', headers=self.headers)

        assert resposta.status_code == 204 and len(resposta.text) == 0

# LEMBRAR DE MUDAR ID's E TOKEN DE USUÁRIO