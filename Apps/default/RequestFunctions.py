from NAPyF.Admin.Auth.Models import User


def default_post(form=None, params=None):
    success = False
    return_data = {}
    if form is None:
        print('No form data posted')
    else:
        for field in form.keys():
            field_item = form[field]
            if field_item.filename:
                # The field contains an uploaded file
                file_data = field_item.file.read()
                file_len = len(file_data)
                del file_data
                return_data = f'Uploaded {field} as "{field_item.filename}" ({file_len} bytes)\n'
            else:
                # Regular form value
                # return_data += '\t%s=%s\n' % (field, form[field].value)
                return_data[field] = form[field].value
        print(return_data)
        user = User()
        user.create_user(**return_data)
        success = True
    return success
