import random
import requests
from faker import Faker

class Books:
    
    def __init__(self, base_url):
        self.base_url = base_url
        self.fake = Faker()


    def get_books(self):
        #url = self.base_url
        return requests.get(self.base_url)

    def get_books_id(self,id):
        return requests.get(self.base_url + f"/{id}")

    def post_books(self,payload):
        return requests.post(self.base_url, json=payload)

    def delete_books(self,id):
        return requests.delete(self.base_url + f"/{id}")

    def generate_payload(self):
        return {
        "titulo": self.fake.sentence(nb_words=random.randint(2, 5)).strip("."),
        "autor": self.fake.name(),
        "editora": self.fake.company(),
        "anoPublicacao": self.fake.random_int(min=1900, max=2100),
        "numeroPaginas": self.fake.random_int(min=50, max=1000)
        }