from common.pyreact import element as el
from common.pymui import Button, TextField, Box


def EditCustomerVu(props):
    def onUpdate(event):
        props['onClick']('update', event)

    def onCancel(event):
        props['onClick']('cancel', event)

    return el('form', None,
              el('div', None,
                 el(TextField, {'label': "First Name",
                                'type': 'text',
                                'name': 'fname',
                                'value': props['fname'],
                                'onChange': props['onChange']
                                }),
                 ),
              el('div', None,
                 el(TextField, {'label': "Last Name",
                                'type': 'text',
                                'name': 'lname',
                                'value': props['lname'],
                                'onChange': props['onChange']
                                }),
                 ),
              el('div', None,
                 el(TextField, {'label': "Amount",
                                'type': 'number',
                                'name': 'amount',
                                'value': props['amount'],
                                'onChange': props['onChange']
                                }),
                 ),
              el(Box, None,
                 el(Button, {'color': 'primary', 'onClick': onUpdate}, "Update"),
                 el(Button, {'color': 'secondary', 'onClick': onCancel}, "Cancel"),
                 )
              )
