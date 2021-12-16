from NAPyF.App import App


default = App('default')
default.context = {'testkey1': 'one', 'testkey2': 'two'}


active_apps = [
    'default',
]
