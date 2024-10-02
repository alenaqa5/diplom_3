from faker import Faker

fake = Faker()

class UserPayloads:
    create_user = {
    "email": fake.free_email(),
    "password": fake.text(max_nb_chars=10),
    "name": fake.text(max_nb_chars=10)
    }