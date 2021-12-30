# Dead simple template engine. Run Python code in HTML.
import sys
from io import StringIO
import contextlib
import re
import autopep8
from Settings import CODE_FORMAT_OPTIONS
from NAPyF.Auth.Forms import *
from NAPyF.Auth.Models import auth_level


class TemplateReader:
    """
    Read the template and return string for parsing
    """

    def __init__(self, template):
        self.template = template

    def get_string(self):
        with open(self.template, 'r') as f:
            return f.read()


class CodeTag:
    """
    Define code tags for template
    """
    begin, end = "{%", "%}"

class CodeBlock:
    """
    Format string in code as Python code and execute it
    """

    def __init__(self, loc, code):
        self.loc = loc
        self.code = code

    @contextlib.contextmanager
    def stdoutIO(self, stdout=None):
        old = sys.stdout
        if stdout is None:
            stdout = StringIO()
        sys.stdout = stdout
        yield stdout
        sys.stdout = old

    def execute(self, context=None, session=None):
        if context is None:
            context = {}
        if session is None:
            session = {}
        with self.stdoutIO() as s:
            try:
                user_logout_form = UserLogoutForm().new_logout_form
                user_login_form = UserLoginForm().new_login_form
                new_user_form = UserForm().new_user_form
                user_edit_form = UserEditForm().edit_user_form
                css_mixin = bootstrap_css_mixin
                _globals = {}
                _locals = context, session
                exec(self.code, {
                    'p': print,
                    'session': session,
                    'context': context,
                    'block': context['html_templates'],
                    'r': render,
                    'new_user_form': new_user_form,
                    'user_login_form': user_login_form,
                    'user_logout_form': user_logout_form,
                    'user_edit_form': user_edit_form,
                    'auth_level': auth_level,
                    'css_mixin': css_mixin
                })
            except SyntaxError as e:
                print(f'Something wrong with template code: {e}')
            return s.getvalue()


class TemplateParser:
    """
    Parse templates for code blocks
    """

    def __init__(self, template_string):
        self.template_string = template_string

    def get_code_list(self):
        return re.findall('{%((?:.*?\r?\n?)*)%}', self.template_string)

    def get_loc_list(self):
        indices = [(m.start(0), m.end(0)) for m in re.finditer('{%((?:.*?\r?\n?)*)%}', self.template_string)]
        locs = []
        for i in indices:
            locs.append(i)
        return locs

    def format_code(self):
        formatted_code_strings = []
        for i in self.get_code_list():
            formatted_code = autopep8.fix_code(i, CODE_FORMAT_OPTIONS)
            formatted_code_strings.append(formatted_code)
        return formatted_code_strings


class TemplateRenderer:
    """
    Rebuilds template with executed code
    """

    def __init__(self, original_template, code_list, code_locs):
        self.original_template = original_template
        self.code_list = code_list
        self.code_locs = code_locs

    # Takes context dictionary as optional argument
    def render(self, context=None, session=None):
        if context is None:
            context = {}
        rebuilt_template = ""
        oi = 0
        for i, block in enumerate(self.code_list):
            codeblock = CodeBlock(self.code_locs[i], block)
            # print(self.original_template[oi:self.locs[i][0]])
            rebuilt_template = rebuilt_template + self.original_template[oi:codeblock.loc[0]]
            rebuilt_template = rebuilt_template + str(codeblock.execute(context=context, session=session))
            oi = codeblock.loc[1]
        rebuilt_template = rebuilt_template + self.original_template[oi:]

        return rebuilt_template


def render(template=None, context=None, session=None, template_string=None):
    if template_string is None:
        template_string = TemplateReader(template).get_string()
    parsed_template = TemplateParser(template_string)
    code_list = parsed_template.format_code()
    loc_list = parsed_template.get_loc_list()
    template_rebuilder = TemplateRenderer(template_string, code_list, loc_list)
    return template_rebuilder.render(context=context, session=session)
