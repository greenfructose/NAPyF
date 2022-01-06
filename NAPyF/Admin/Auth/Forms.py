from NAPyF.Form import Form
from NAPyF.Admin.Auth.Models import User, Login, Logout
from Settings import PASSWORD_REQS, PASSWORD_ERROR_TEXT, USERNAME_REQS, USERNAME_ERROR_TEXT, NAME_REQS, NAME_ERROR_TEXT


class UserForm(Form):
    delete_button = ""
    fields = User.fields
    form_dict = {}
    submit_button_label = 'Register'
    for field in fields:
        input_type = ""
        if not field["visible"]:
            input_type = 'hidden'
        elif field["data_type"] == str or field["data_type"] == int or field["data_type"] == float:
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
            'display_name': field["display_name"],
            'data': field["data"],
            'visible': field["visible"]
        }
    form_dict["verify_password"] = {
        'label': "verify_password",
        'input_type': "password",
        'id': "verify_password",
        'name': "verify_password",
        'display_name': "Verify Password",
        'data': None,
        'visible': True
    }

    def new_user_form(self, action: str, css_mixin: dict = None):
        return generate_user_form(self, action, css_mixin)


class UserEditForm(Form):
    delete_button = '<form method="post" action="/admin/user/delete?id={%p(context[\'id\'])%}">'\
                    '<input type="hidden" name="null">'\
                    '<button type="submit" class="btn btn-danger">Delete User</button>' \
                    '</form>'
    fields = User.fields
    form_dict = {}
    submit_button_label = 'Submit'
    for field in fields:
        input_type = ""
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
            'display_name': field["display_name"],
            'data': None,
            'visible': True,
            'editable': True,
        }

    def edit_user_form(self, action: str, css_mixin: dict = None):
        return generate_user_form(self, action, css_mixin)


class UserLoginForm(Form):
    delete_button = ""
    fields = Login.fields
    form_dict = {}
    submit_button_label = 'Login'
    for field in fields:
        input_type = ""
        if not field["visible"]:
            input_type = 'hidden'
        elif field["data_type"] == str or field["data_type"] == int or field["data_type"] == float:
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
            'display_name': field["display_name"],
            'data': field["data"],
            'visible': field["visible"]
        }

        def new_login_form(self, action: str, css_mixin: dict = None):
            return generate_user_form(self, action, css_mixin)


class UserLogoutForm(Form):
    delete_button = ""
    fields = Logout.fields
    form_dict = {}
    submit_button_label = 'Logout'
    for field in fields:
        input_type = ""
        if not field["visible"]:
            input_type = 'hidden'
        elif field["data_type"] == str or field["data_type"] == int or field["data_type"] == float:
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
            'display_name': field["display_name"],
            'data': field["data"],
            'visible': field["visible"],
        }

        def new_logout_form(self, action: str, css_mixin: dict = None):
            return generate_user_form(self, action, css_mixin)


def generate_user_form(user, action: str, css_mixin: dict = None):
    form = f'<form class="was-validated" method="post" action="{action}">\n'
    if css_mixin:
        for key, value in user.form_dict.items():
            pattern = ""
            invalid_message = "Invalid Input"
            required = 'required'
            if user.form_dict[key]['name'] == 'password' or user.form_dict[key]['name'] == 'verify_password':
                pattern = f' pattern="{PASSWORD_REQS}"'
                invalid_message = PASSWORD_ERROR_TEXT
            if user.form_dict[key]['name'] == 'username':
                pattern = f' pattern="{USERNAME_REQS}"'
                invalid_message = USERNAME_ERROR_TEXT
            if user.form_dict[key]['name'] == 'first_name' or user.form_dict[key]['name'] == 'last_name':
                pattern = f' pattern="{NAME_REQS}"'
                invalid_message = NAME_ERROR_TEXT
            if user.form_dict[key]["visible"] and 'editable' not in user.form_dict[key]:
                field = f'\t<div class ="{css_mixin["div"]}">\n\t\t' \
                        f'<label class="{css_mixin["label"]}" for="{user.form_dict[key]["label"]}">' \
                        f'{user.form_dict[key]["display_name"]}' \
                        f'</label>\n\t\t' \
                        f'<input ' \
                        f'class="{css_mixin["input"]}" ' \
                        f'type="{user.form_dict[key]["input_type"]}" ' \
                        f'id="{user.form_dict[key]["id"]}"\n' \
                        f'name="{user.form_dict[key]["name"]}" ' \
                        f'required{pattern}>' \
                        f'\t<div class="valid-feedback">Valid.</div>\n' \
                        f'\t<div class="invalid-feedback">{invalid_message}</div>' \
                        f'\t</div>\n'
            elif 'editable'in user.form_dict[key]:
                required = ""
                checked = ''
                input_css = 'input'
                if user.form_dict[key]['input_type'] == 'checkbox':
                    input_css = 'checkbox'
                    if user.form_dict[key]['data'] == '1':
                        checked = 'checked'
                if user.form_dict[key]['name'] == 'password':
                    data = ""
                else:
                    data = '{%print(context["' + user.form_dict[key]["name"] + '"], end="")%}'
                field = f'\t<div class ="{css_mixin["div"]}">\n\t\t' \
                        f'<label class="{css_mixin["label"]}" for="{user.form_dict[key]["label"]}">' \
                        f'{user.form_dict[key]["display_name"]}' \
                        f'</label>\n\t\t' \
                        f'<input ' \
                        f'class="{css_mixin[input_css]}" ' \
                        f'type="{user.form_dict[key]["input_type"]}" ' \
                        f'id="{user.form_dict[key]["id"]}"\n' \
                        f'name="{user.form_dict[key]["name"]}" ' \
                        f'value="{data}" ' \
                        f'{checked}>\n' \
                        f'\t<div class="valid-feedback">Valid.</div>\n' \
                        f'\t<div class="invalid-feedback">{invalid_message}</div>' \
                        f'\t</div>\n'
            else:
                field = f'\t<input ' \
                        f'type="{user.form_dict[key]["input_type"]}"' \
                        f'id="{user.form_dict[key]["id"]}"' \
                        f'name="{user.form_dict[key]["name"]}"' \
                        f'value="{user.form_dict[key]["data"]}">'
            form += field
        form += f'\t<button type="submit" class="{css_mixin["button"]}">{user.submit_button_label}</button>\n' \
                f'</form>' \
                f'{user.delete_button}'
    else:
        for key, value in user.form_dict.items():
            pattern = ""
            if user.form_dict[key]['name'] == 'password' or user.form_dict[key]['name'] == 'verify_password':
                pattern = f' pattern="{PASSWORD_REQS}"'
            if user.form_dict[key]["visible"]:
                field = f'\t<div>\n\t\t' \
                        f'<label for="{user.form_dict[key]["label"]}">' \
                        f'{user.form_dict[key]["display_name"]}' \
                        f'</label>\n\t\t' \
                        f'<input ' \
                        f'type="{user.form_dict[key]["input_type"]}" ' \
                        f'id="{user.form_dict[key]["id"]}"\n' \
                        f'name="{user.form_dict[key]["name"]}" required{pattern}>\n' \
                        f'\t<div class="valid-feedback">Valid.</div>\n' \
                        f'\t<div class="invalid-feedback">Please fill out this field.</div>' \
                        f'\t</div>\n'
            else:
                field = f'\t<input ' \
                        f'type="{user.form_dict[key]["input_type"]}"' \
                        f'id="{user.form_dict[key]["id"]}"' \
                        f'name="{user.form_dict[key]["name"]}"' \
                        f'value="{user.form_dict[key]["data"]}">'
            form += field
        form += f'\t<button>Submit</button>\n' \
                f'</form>'
    return form


bootstrap_css_mixin = {
    "div": "mb-3 position-relative",
    "label": "form-label",
    "input": "form-control",
    "checkbox": "form-check-input",
    "button": "btn btn-primary"
}

# userform = UserForm()
# print(userform.new_user_form('/'))
