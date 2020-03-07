from common.pyreact import element
from common.pymui import createMuiTheme, MuiThemeProvider
from common.pymui import colors
from common.pymui import SnackbarProvider


_material_theme = createMuiTheme({
    'palette': {
        'primary': colors.teal,
        'secondary': colors.pink,
        'altPrimary': {
            'main': colors.cyan[700],
            'contrastText': colors.common.white,
        },
        'altSecondary': {
            'main': colors.cyan[400],
            'contrastText': colors.common.white,
        },
        'warning': colors.yellow,
        'error': colors.red,
    },
    'props': {
        'MuiButton': {
            'variant': "contained",
            'color': "primary",
            'style': {'minWidth': '6rem', 'margin': '0.3rem'},
        },
        'MuiTextField': {
            'variant': "outlined",
            'InputLabelProps': {'shrink': True},
            'InputProps': {'margin': 'dense'},
            'margin': 'normal',
        }
    }
})


def withMaterialTheme(old_element):
    def newElement(*args):
        # return element(MuiThemeProvider, {'theme': _material_theme}, old_element(*args))
        return element(MuiThemeProvider, {'theme': _material_theme},
                       element(SnackbarProvider, {'maxSnack': 3},
                               old_element(*args)
                               )
                       )

    return newElement
