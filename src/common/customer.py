class Customer:
    def __init__(self, cust_id: int = None, fname: str = '', lname: str = '', amount: float = 0, status: bool = False):
        self.cust_id = cust_id
        self.fname = fname
        self.lname = lname
        self.amount = amount
        self.status = status

    def fullName(self):
        return ' '.join([self.fname, self.lname])

    def copy(self):
        return Customer(self.cust_id, self.fname, self.lname, self.amount, self.status)

    def update(self, updates: dict):
        new_object = self.copy()
        try:
            for key, val in updates.items():
                if not hasattr(self, key):
                    print(''.join(["ERROR: Attempted to update invalid attribute key '", key, "' in class '", self.__name__, "'"]))
                    raise KeyError
                setattr(new_object, key, val)
            return new_object
        except KeyError as e:
            print(e)
            return None

    def _attributes(self):
        return [attr for attr in dir(self) if not attr.startswith('__') and not callable(getattr(self, attr))]

    def toDict(self):
        return {attr: getattr(self, attr) for attr in self._attributes()}

# customer = Customer(1,"Bob","Brady", 55.99, False)
