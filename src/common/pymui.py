from common.pyreact import console_log

MaterialUI = require('@material-ui/core')
notistack = require('notistack')

react_number_format = require('react-number-format')
NumberFormat = react_number_format['default']


# Basic components
Button = MaterialUI.Button
ButtonGroup = MaterialUI.ButtonGroup
InputLabel = MaterialUI.InputLabel
TextField = MaterialUI.TextField
Box = MaterialUI.Box
Toolbar = MaterialUI.Toolbar
Grid = MaterialUI.Grid

# Tables
TableContainer = MaterialUI.TableContainer
Table = MaterialUI.Table
TableHead = MaterialUI.TableHead
TableBody = MaterialUI.TableBody
TableRow = MaterialUI.TableRow
TableCell = MaterialUI.TableCell


# Theme-ing
MuiThemeProvider = MaterialUI.MuiThemeProvider


def createMuiTheme(props):
    return MaterialUI.createMuiTheme(props)


def withStyles(props):
    return MaterialUI.withStyles(props)


useTheme = MaterialUI.useTheme

styled = MaterialUI.styled

colors = MaterialUI.colors
# class Colors:
#     common = MaterialUI.colors.common
#     red = MaterialUI.colors.red
#     pink = MaterialUI.colors.pink
#     purple = MaterialUI.colors.purple
#     deepPurple = MaterialUI.colors.deepPurple
#     indigo = MaterialUI.colors.indigo
#     blue = MaterialUI.colors.blue
#     lightBlue = MaterialUI.colors.lightBlue
#     cyan = MaterialUI.colors.cyan
#     teal = MaterialUI.colors.teal
#     green = MaterialUI.colors.green
#     lightGreen = MaterialUI.colors.lightGreen
#     lime = MaterialUI.colors.lime
#     yellow = MaterialUI.colors.yellow
#     amber = MaterialUI.colors.amber
#     orange = MaterialUI.colors.orange
#     deepOrange = MaterialUI.colors.deepOrange
#     brown = MaterialUI.colors.brown
#     grey = MaterialUI.colors.grey
#     blueGrey = MaterialUI.colors.blueGrey


# notistack
SnackbarProvider = notistack.SnackbarProvider


def useSnackbar():
    return notistack.useSnackbar().enqueueSnackbar, notistack.useSnackbar().closeSnackbar


def withSnackbar(component):
    return notistack.withSnackbar(component)
