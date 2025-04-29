


class Service:
    def __init__(self):
        self._repository = None


    def get_all(self):
        return self._repository.get_all()


    def get_by_id(self, *keys):
        return self._repository.get_by_id(*keys)


    def insert(self, model):
        self._repository.insert(model)


    def update(self, model):
        self._repository.update(model)


    def delete(self, model):
        self._repository.delete(model)
