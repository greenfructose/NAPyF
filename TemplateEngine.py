# Dead simple template engine. Run Python code in HTML.
import sys
from io import StringIO
import contextlib
import re
import black


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
    Format string in code as Python code
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

    def execute(self):
        with self.stdoutIO() as s:
            try:
                exec(self.code)
            except:
                print('Something wrong with template code')
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
            formatted_code = black.format_str(i, mode=black.Mode())
            formatted_code_strings.append(formatted_code)
        return formatted_code_strings


class TemplateRebuilder:
    """
    Rebuilds template with executed code
    """

    def __init__(self, original_template, code_list, locs):
        self.original_template = original_template
        self.code_list = code_list
        self.locs = locs

    def rebuild(self):
        temp_template = self.original_template
        rebuilt_template = ""
        oi = 0
        for i, block in enumerate(self.code_list):
            codeblock = CodeBlock(self.locs[i], block)
            # print(self.original_template[oi:self.locs[i][0]])
            rebuilt_template = rebuilt_template + self.original_template[oi:codeblock.loc[0]]
            rebuilt_template = rebuilt_template + str(codeblock.execute())
            oi = codeblock.loc[1]
        rebuilt_template = rebuilt_template + self.original_template[oi:]
        return rebuilt_template
