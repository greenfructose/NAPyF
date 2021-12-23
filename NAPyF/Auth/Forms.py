from pprint import pprint

from NAPyF.Form import Form
from NAPyF.Auth.Models import User


class UserForm(Form):
    fields = User.fields
    form_dict = {}
    for field in fields:
        input_type = ""
        if field["visible"]:
            if field["data_type"] == str or field["data_type"] == int or field["data_type"] == float:
                if field["name"] == 'email':
                    input_type = 'email'
                elif field["name"] == 'password':
                    input_type = 'password'
                else:
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

    def new_user_form(self, action: str, css_mixin: dict = None):
        form = f'<form method="post" action="{action}">\n'
        if css_mixin:
            for key, value in self.form_dict.items():
                field = f'\t<div class ="{css_mixin["div"]}">\n\t\t' \
                        f'<label class="{css_mixin["label"]}" for="{self.form_dict[key]["label"]}">' \
                        f'{self.form_dict[key]["display_name"]}' \
                        f'</label>\n\t\t' \
                        f'<input ' \
                        f'class="{css_mixin["input"]}" ' \
                        f'type="{self.form_dict[key]["input_type"]}" ' \
                        f'id="{self.form_dict[key]["id"]}"\n' \
                        f'name="{self.form_dict[key]["name"]}">\n' \
                        f'\t</div>\n'
                form += field
            form += f'\t<button type="submit" class="{css_mixin["button"]}">Submit</button>\n' \
                    f'</form>'
        else:
            for key, value in self.form_dict.items():
                field = f'\t<div>\n\t\t' \
                        f'<label for="{self.form_dict[key]["label"]}">' \
                        f'{self.form_dict[key]["display_name"]}' \
                        f'</label>\n\t\t' \
                        f'<input ' \
                        f'type="{self.form_dict[key]["input_type"]}" ' \
                        f'id="{self.form_dict[key]["id"]}"\n' \
                        f'name="{self.form_dict[key]["name"]}">\n' \
                        f'\t</div>\n'
                form += field
            form += f'\t<button>Submit</button>\n' \
                    f'</form>'
        return form


bootstrap_css_mixin = {
    "div": "mb-3",
    "label": "form-label",
    "input": "form-control",
    "button": "btn btn-primary"
}

# userform = UserForm()
# print(userform.new_user_form('/'))
