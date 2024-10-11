

class agent:
    def __init__(self):
        pass

    def list_methods(self):
        return [method for method in dir(self) if callable(getattr(self, method)) and not method.startswith('__') and not method.startswith('list_methods')]

