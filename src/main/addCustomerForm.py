from common.pyreact import element as el
from common.pymui import Button, TextField, Box
from common.pymui import withSnackbar


@withSnackbar
def AddCustomer(props):
    # enqueueSnackbar, closeSnackbar = useSnackbar()

    def onAdd(event):
        success = props['onClick'](event)
        if success:
            props.enqueueSnackbar('Successfully added  the customer!', {'variant': 'success'})
        else:
            props.enqueueSnackbar('There was a problem adding the customer!', {'variant': 'error'})

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
              el(Box, {'display': 'flex', 'justifyContent': 'center'},
                 el(Button, {'onClick': onAdd}, "Add Customer")),
              )
