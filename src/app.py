from common.pyreact import Component, render, element, deepcopy
from common.pymui import Box
from materialTheme import withMaterialTheme

from main.addCustomerForm import AddCustomerVu
from main.editCustomerForm import EditCustomerVu
from main.customerList import CustomerListVu

from common.customer import Customer


class App(Component):
    def __init__(self, props):
        super().__init__(props)

        self.state = {
            'cust_id': None,
            'fname': '',
            'lname': '',
            'amount': '',
            'status': False,
            'customer': None,
            'customers': [],
            'editing': False
        }

    def handleInputChange(self, event):
        event.preventDefault()
        target = event['target']
        value = target.value
        key = target['name']

        self.setState({
            key: value
        })

    def addCustomer(self, event):
        event.preventDefault()
        if not self.state['lname'] or not self.state['amount']:
            return False

        def getNextId():
            customers: [Customer] = self.state['customers']
            id_list = [cust.cust_id for cust in customers]
            return 1 if len(customers) == 0 else max(id_list) + 1

        try:
            new_id = getNextId()
            customer: Customer = Customer(
                cust_id=new_id,
                fname=self.state['fname'],
                lname=self.state['lname'],
                amount=self.state['amount'],
                status=self.state['status']
            )

            new_customers = deepcopy(self.state['customers'])
            new_customers.append(customer)

            self.setState({
                'lname': '',
                'fname': '',
                'amount': '',
                'customer': customer,
                'customers': new_customers
            })
            return True
        except Exception as e:
            print("ERROR:", e)
            return False

    def updateCustomer(self, source, event):
        event.preventDefault()
        customers: [Customer] = self.state['customers']
        if source == 'update':
            old_customer = self.state['customer']
            updated_fname = self.state['fname']
            updated_lname = self.state['lname']
            updated_amount = self.state['amount']
            updated_customer = old_customer.update(
                dict(fname=updated_fname, lname=updated_lname, amount=updated_amount))
            customers = [updated_customer if customer.cust_id == old_customer.cust_id else customer for customer in
                         customers]

        self.setState({'fname': '', 'lname': '', 'amount': '', 'customers': customers})
        self.setEditing(False)

    def deleteCustomer(self, id_):
        new_customers = [customer for customer in self.state['customers'] if customer.cust_id != id_]
        self.setState({'customers': new_customers})

    def paidCustomer(self, current_cust: Customer):
        updated_current_cust = current_cust.update(dict(status=True))
        customers = [updated_current_cust if customer.cust_id == current_cust.cust_id else customer for customer in
                     self.state['customers']]
        self.setState({'customers': customers})

    def editCustomer(self, customer: Customer):
        self.setEditing(True)
        self.setState({
            'fname': customer.fname,
            'lname': customer.lname,
            'amount': customer.amount,
            'customer': customer
        })

    def setEditing(self, value: bool):
        self.setState({'editing': value})

    @withMaterialTheme
    def render(self):
        return (element(Box, {'key': 'app-main', 'className': 'App', 'maxWidth': '800px'},
                        element(Box, None,
                                element(CustomerListVu, {
                                    'customers': self.state['customers'],
                                    'deleteCustomer': self.deleteCustomer,
                                    'paidCustomer': self.paidCustomer,
                                    'editCustomer': self.editCustomer,
                                }),
                                ),
                        element(Box, {'display': 'flex', 'justifyContent': 'center'}, self.editMode())
                        ),
                )

    def editMode(self):
        if self.state['editing']:
            return (element(EditCustomerVu, {
                'fname': self.state['fname'],
                'lname': self.state['lname'],
                'amount': self.state['amount'],
                'onChange': self.handleInputChange,
                'onClick': self.updateCustomer,
            }))
        else:
            return element(AddCustomerVu, {
                'fname': self.state['fname'],
                'lname': self.state['lname'],
                'amount': self.state['amount'],
                'onChange': self.handleInputChange,
                'onClick': self.addCustomer,
            })


render(App, None, 'root')
