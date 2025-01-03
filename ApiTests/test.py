import random
import requests
from faker import Faker

URL = "http://localhost:5000/api/livros"
fake = Faker()

def get_books():
   return requests.get(URL)

def get_books_id(id):
   return requests.get(URL + f"/{id}")

def post_books(payload):
    return requests.post(URL, json=payload)

def delete_books(id):
    return requests.delete(URL + f"/{id}")

def generate_payload():
    return {
    "titulo": fake.sentence(nb_words=random.randint(2, 5)).strip("."),
    "autor": fake.name(),
    "editora": fake.company(),
    "anoPublicacao": fake.random_int(min=1900, max=2100),
    "numeroPaginas": fake.random_int(min=50, max=1000)
    }

def test_get_books():
    response = get_books()
    assert response.status_code == 200

def test_post_books():
    response_post = post_books(generate_payload())
    response_data = response_post.json()  # Converte a resposta JSON para um dicionário
    id = response_data["_id"]
    response_get_id = get_books_id(id)
    assert response_post.status_code == 201
    assert response_get_id.status_code == 200

def test_post_books_whith_custom_author():
    payload = generate_payload()
    payload["autor"] = "teste autor"
    response = post_books(payload)
    response_data = response.json()
    assert response.status_code == 201
    assert response_data["autor"] == "teste autor"


def test_delete_books():
    response_post = post_books(generate_payload())
    response_data_post = response_post.json()  # Converte a resposta JSON para um dicionário
    id = response_data_post["_id"]
   
    response_delete = delete_books(id)
    response_data_delete = response_delete.json()
    assert response_post.status_code == 201
    assert response_delete.status_code == 200
    assert response_data_delete["message"] == "Livro removido com sucesso"