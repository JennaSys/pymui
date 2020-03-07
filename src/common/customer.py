class Customer:
    def __init__(self, cust_id: int = None, fname: str = '', lname: str = '', amount: float = 0, status: bool = False):
        self.cust_id = cust_id
        self.fname = fname
        self.lname = lname
        self.amount = amount
        self.status = status

    def update(self, updates: dict):
        new_customer = self.copy()
        for key, val in updates.items():
            setattr(new_customer, key, val)
        return new_customer

    def copy(self):
        new_customer = Customer(self.cust_id, self.fname, self.lname, self.amount, self.status)
        return new_customer

    def fullName(self):
        return ' '.join([self.fname, self.lname])

# customer = Customer(1,"Bob","Brady", 55.99, False)
