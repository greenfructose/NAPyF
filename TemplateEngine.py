# Dead simple template engine. Run Python code in HTML.
import io
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
    def __init__(self, loc):
        self.loc = loc
    def format(self, parsed_code):
        return blac

class TemplateParser:
    """
    Parse templates for code blocks
    """
    def parse(self, pattern, template_string):
        code_block_strings = re.findall(pattern, template_string)
        indices = [(m.start(0), m.end(0)) for m in re.finditer('{%(.*)%}', template_string)]


