def no_function():
    pass


def default_post(form=None):
    if form is None:
        form = {'value': ''}
        for field in form.keys():
            print(f'Field: {field}')
