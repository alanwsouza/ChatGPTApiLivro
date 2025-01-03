from books import Books
import pytest

base_url = "http://localhost:5000/api/livros"

books = Books(base_url)

def test_get_books():
    response = books.get_books()
    assert response.status_code == 200

def test_post_books():
    response_post = books.post_books(books.generate_payload())
    response_data = response_post.json()  # Converte a resposta JSON para um dicionário
    id = response_data["_id"]
    response_get_id = books.get_books_id(id)
    assert response_post.status_code == 201
    assert response_get_id.status_code == 200

def test_post_books_whith_custom_author():
    payload = books.generate_payload()
    payload["autor"] = "teste autor"
    response = books.post_books(payload)
    response_data = response.json()
    assert response.status_code == 201
    assert response_data["autor"] == "teste autor"


def test_delete_books():
    response_post = books.post_books(books.generate_payload())
    response_data_post = response_post.json()  # Converte a resposta JSON para um dicionário
    id = response_data_post["_id"]
   
    response_delete = books.delete_books(id)
    response_data_delete = response_delete.json()
    assert response_post.status_code == 201
    assert response_delete.status_code == 200
    assert response_data_delete["message"] == "Livro removido com sucesso"