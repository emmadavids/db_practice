class User:
    def __init__(self, id, email, name):
        self.id = id
        self.email = email
        self.name = name

    # # This method allows our tests to assert that the objects it expects
    # # are the objects we made based on the database records.
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    # This method makes it look nicer when we print an Artist
    def __repr__(self):
        return f"User({self.id}, {self.name}, {self.email})"
