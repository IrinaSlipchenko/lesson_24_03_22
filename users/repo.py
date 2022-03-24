from users.user import User


class InMemoryUserRepo:
    def __init__(self):
        self.next_id = 1
        self.by_id = {}

    def request_create(self, username, password):
        if username in list(self.by_id.values()):
            # Если пользователь с таким именем есть
            return None
        new_user = User(id=self.next_id, username=username, password=password)
        self.by_id[new_user.id] = new_user
        self.next_id += 1
        return new_user
