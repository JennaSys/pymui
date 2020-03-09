from common.pyreact import element as el
from common.pymui import TableContainer, Table, TableHead, TableBody, TableRow, TableCell, Box, Button, NumberFormat
from common.pymui import createMuiTheme, MuiThemeProvider, useTheme, styled

from common.customer import Customer


def AltTheme(props):
    theme = useTheme()
    new_theme = createMuiTheme({
        'palette': {
            'primary': theme.palette.altPrimary,
            'secondary': theme.palette.altSecondary,
        },
        'props': theme.props,
    })
    return el(MuiThemeProvider, {'theme': new_theme}, props.children)


def CustomerRowVu(props):
    customer: Customer = props['customer']

    def onEdit():
        props['editCustomer'](customer)

    def onDelete():
        props['deleteCustomer'](customer.cust_id)

    def onBought():
        props['paidCustomer'](customer)

    return el(TableRow, None,
              el(TableCell, None, customer.cust_id),
              el(TableCell, None, customer.fullName()),
              el(TableCell, None,
                 el(NumberFormat, {
                     'value': customer.amount,
                     'displayType': 'text',
                     'thousandSeparator': True,
                     'fixedDecimalScale': True,
                     'decimalScale': 2,
                     'prefix': '$',
                 })
                 ),
              el(TableCell, None,
                 el(Box, {'display': 'flex', 'flexWrap': 'wrap', 'justifyContent': 'center'},
                    el(AltTheme, None, el(Button, {'color': 'primary', 'onClick': onEdit}, "Edit")),
                    el(Button, {'color': 'secondary', 'onClick': onDelete}, "Delete"),
                    el(AltTheme, None, el(Button, {'color': 'secondary', 'onClick': onBought},
                                          "paid" if customer.status else "unpaid")),
                    )
                 )
              )


def CustomersVu(props):
    customers: [Customer] = props['customers']

    def customerToRow(customer: Customer):
        return el(CustomerRowVu, {'key': customer.cust_id,
                                  'customer': customer,
                                  'editCustomer': props['editCustomer'],
                                  'deleteCustomer': props['deleteCustomer'],
                                  'paidCustomer': props['paidCustomer']
                                  })

    if len(customers) > 0:
        return [customerToRow(cust) for cust in customers]
    else:
        return el(TableRow, {'key': '0'},
                  el(TableCell, {'colSpan': '4'},
                     el(Box, {'display': 'flex', 'flexWrap': 'wrap', 'justifyContent': 'center'},
                        "-- Add customers below --"))
                  )


def CustomerListVu(props):
    theme = useTheme()

    HeaderTableCell = styled(TableCell)({
        'backgroundColor': theme.palette.primary.dark,
        'color': theme.palette.primary.contrastText,
    })

    return el(TableContainer, None,
              el(Table, {'size': 'small', 'stickyHeader': True},
                 el(TableHead, None,
                    el(TableRow, None,
                       el(HeaderTableCell, None, "ID"),
                       el(HeaderTableCell, None, "Name"),
                       el(HeaderTableCell, None, "Amount"),
                       el(HeaderTableCell, {'align': 'center'}),
                       ),
                    ),
                 el(TableBody, None,
                    el(CustomersVu, props)
                    ),
                 )
              )
