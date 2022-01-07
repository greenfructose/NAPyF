from NAPyF.Form import Form
from Apps.profile.Models import Profile
from Settings import PASSWORD_REQS, PASSWORD_ERROR_TEXT, USERNAME_REQS, USERNAME_ERROR_TEXT, \
    NAME_REQS, NAME_ERROR_TEXT, EMAIL_REQS, EMAIL_ERROR_TEXT


class ProfileForm(Form):
    delete_button = ""
    fields = Profile.fields
    form_dict = {}
    submit_button_label = 'Register'
    for field in fields:
        input_type = ""
        if not field["visible"]:
            input_type = 'hidden'
        elif field["data_type"] == str or field["data_type"] == int or field["data_type"] == float:
            if field["name"] == 'email':
                input_type = 'email'
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

    def new_profile_form(self, action: str, css_mixin: dict = None):
        return generate_profile_form(self, action, css_mixin)


def generate_profile_form(profile, action: str, css_mixin: dict = None):
    form = f'<form class="was-validated" method="post" action="{action}">\n'
    if css_mixin:
        for key, value in profile.form_dict.items():
            pattern = ""
            invalid_message = "Invalid Input"
            required = 'required'
            if profile.form_dict[key]['name'] == 'password' or profile.form_dict[key]['name'] == 'verify_password':
                pattern = f' pattern="{PASSWORD_REQS}"'
                invalid_message = PASSWORD_ERROR_TEXT
            if profile.form_dict[key]['name'] == 'username':
                pattern = f' pattern="{USERNAME_REQS}"'
                invalid_message = USERNAME_ERROR_TEXT
            if profile.form_dict[key]['name'] == 'first_name' or profile.form_dict[key]['name'] == 'last_name':
                pattern = f' pattern="{NAME_REQS}"'
                invalid_message = NAME_ERROR_TEXT
            if profile.form_dict[key]['name'] == 'email':
                pattern = f' pattern="{EMAIL_REQS}"'
                invalid_message = EMAIL_ERROR_TEXT
            if profile.form_dict[key]["visible"] and 'editable' not in profile.form_dict[key]:
                field = f'\t<div class ="{css_mixin["div"]}">\n\t\t' \
                        f'<label class="{css_mixin["label"]}" for="{profile.form_dict[key]["label"]}">' \
                        f'<p class="fs-3">{profile.form_dict[key]["display_name"]}</p>' \
                        f'</label>\n\t\t' \
                        f'<input ' \
                        f'class="{css_mixin["input"]}" ' \
                        f'type="{profile.form_dict[key]["input_type"]}" ' \
                        f'id="{profile.form_dict[key]["id"]}"\n' \
                        f'name="{profile.form_dict[key]["name"]}" ' \
                        f'required{pattern}>' \
                        f'\t<div class="valid-feedback">Valid.</div>\n' \
                        f'\t<div class="invalid-feedback">{invalid_message}</div>' \
                        f'\t</div>\n'
            elif 'editable' in profile.form_dict[key]:
                required = ""
                checked = ''
                input_css = 'input'
                if profile.form_dict[key]['input_type'] == 'checkbox':
                    input_css = 'checkbox'
                    if profile.form_dict[key]['data'] == '1':
                        checked = 'checked'
                if profile.form_dict[key]['name'] == 'password':
                    data = ""
                else:
                    data = '{%print(context["' + profile.form_dict[key]["name"] + '"], end="")%}'
                field = f'\t<div class ="{css_mixin["div"]}">\n\t\t' \
                        f'<label class="{css_mixin["label"]}" for="{profile.form_dict[key]["label"]}">' \
                        f'{profile.form_dict[key]["display_name"]}' \
                        f'</label>\n\t\t' \
                        f'<input ' \
                        f'class="{css_mixin[input_css]}" ' \
                        f'type="{profile.form_dict[key]["input_type"]}" ' \
                        f'id="{profile.form_dict[key]["id"]}"\n' \
                        f'name="{profile.form_dict[key]["name"]}" ' \
                        f'value="{profile}" ' \
                        f'{checked}>\n' \
                        f'\t<div class="valid-feedback">Valid.</div>\n' \
                        f'\t<div class="invalid-feedback">{invalid_message}</div>' \
                        f'\t</div>\n'
            else:
                field = f'\t<input ' \
                        f'type="{profile.form_dict[key]["input_type"]}"' \
                        f'id="{profile.form_dict[key]["id"]}"' \
                        f'name="{profile.form_dict[key]["name"]}"' \
                        f'value="{profile.form_dict[key]["data"]}">'
            form += field
        form += f'\t<button type="submit" class="{css_mixin["button"]}">{profile.submit_button_label}</button>\n' \
                f'</form>' \
                f'{profile.delete_button}'
    else:
        for key, value in profile.form_dict.items():
            pattern = ""
            if profile.form_dict[key]['name'] == 'password' or profile.form_dict[key]['name'] == 'verify_password':
                pattern = f' pattern="{PASSWORD_REQS}"'
            if profile.form_dict[key]["visible"]:
                field = f'\t<div>\n\t\t' \
                        f'<label for="{profile.form_dict[key]["label"]}">' \
                        f'{profile.form_dict[key]["display_name"]}' \
                        f'</label>\n\t\t' \
                        f'<input ' \
                        f'type="{profile.form_dict[key]["input_type"]}" ' \
                        f'id="{profile.form_dict[key]["id"]}"\n' \
                        f'name="{profile.form_dict[key]["name"]}" required{pattern}>\n' \
                        f'\t<div class="valid-feedback">Valid.</div>\n' \
                        f'\t<div class="invalid-feedback">Please fill out this field.</div>' \
                        f'\t</div>\n'
            else:
                field = f'\t<input ' \
                        f'type="{profile.form_dict[key]["input_type"]}"' \
                        f'id="{profile.form_dict[key]["id"]}"' \
                        f'name="{profile.form_dict[key]["name"]}"' \
                        f'value="{profile.form_dict[key]["data"]}">'
            form += field
        form += f'\t<button>Submit</button>\n' \
                f'</form>'
    return form
