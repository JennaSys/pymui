from dataclasses import dataclass

from common.jsutils import console_error


@dataclass
class Customer:
    cust_id: int = None
    fname: str = ''
    lname: str = ''
    amount: float = 0
    status: bool = False

    @property
    def fullName(self):
        return ' '.join([self.fname, self.lname])

    def copy(self):
        return Customer(self.cust_id, self.fname, self.lname, self.amount, self.status)

    def update(self, updates):
        # return replace(self, **updates)
        new_object = self.copy()
        try:
            for key, val in updates.items():
                if hasattr(self, key):
                    setattr(new_object, key, val)
                else:
                    raise (Exception(''.join(["ERROR: Attempted to update invalid attribute key '", key, "' in class '", self.__name__, "'"])))
            return new_object
        except Exception as e:
            console_error(str(e))
            return None

    def _attributes(self):
        return [attr for attr in dir(self) if not attr.startswith('__') and not callable(getattr(self, attr))]

    def toDict(self):
        return {attr: getattr(self, attr) for attr in self._attributes()}

# customer = Customer(1,"Bob","Brady", 55.99, False)
