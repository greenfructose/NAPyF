from NAPyF.Form import Form
from NAPyF.Auth.Models import User


class UserForm(Form):
    fields = User.fields
    form_dict = {}
    for field in fields:
        input_type = ""
        if field["data_type"] == str or field["data_type"] == int or field["data_type"] == float:
            input_type = "text"
        elif field["data_type"] == bool:
            input_type = "checkbox"
        form_dict[field["name"]] = {
            'label': field["name"],
            'input_type': input_type,
            'id': field["name"],
            'name': field["name"],
            'display_name': field["display_name"]
        }

form = UserForm()
print(form.form_dict)

