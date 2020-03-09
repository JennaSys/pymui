lodash = require('lodash')

def deepcopy(obj):
    return lodash._.cloneDeep(obj)


def console_log(text):
    console.log(text)

def console_error(text):
    console.error(text)
