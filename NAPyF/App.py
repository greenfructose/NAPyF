# Create a new application
import os
from glob import glob
from shutil import copyfile, rmtree
import Settings
from NAPyF.Types import Route, Method
import autopep8


class App:
    def __init__(self, name):
        self.name = name
        if self.name == 'Admin':
            self.app_dir = Settings.BASE_DIR + '/NAPyF/Admin'
        else:
            self.app_dir = Settings.APPS_DIR + '/' + self.name
        self.app_base = self.app_dir + '/base'
        self.app_file = self.app_dir + '/App.py'
        self.app_request_func_file = self.app_dir + '/RequestFunctions.py'
        self.template_directory = self.app_base + '/templates'
        self.local_static_directory = self.app_base + '/local_static'
        self.relative_route_path = '/' + self.name.lower()
        self.html_templates = {
            'content': f'{self.template_directory}/index.html', }
        self.default_route = Route(
            app_name=self.name,
            route_path=self.relative_route_path,
            request_method=Method.GET.value,
            file_path=self.html_templates["content"],
            context=None,
            auth_level_required=0,
        )
        self.routes = [

        ]
        self.app_file_contents = f'# Define app and routes below\n\n' \
                                 f'from NAPyF.App import App\n' \
                                 f'from NAPyF.Types import Route, Method\n\n\n' \
                                 f'def {self.name.lower()}(global_static_directory, base_directory):\n' \
                                 f"\tapp = App('{self.name.lower()}')\n" \
                                 f'\tapp.default_route.html_templates = {{\n' \
                                 f"\t\t'head': f'{{global_static_directory}}/templates/head.html',\n" \
                                 f"\t\t'content': f'{{app.template_directory}}/index.html',\n" \
                                 f"\t\t'foot': f'{{global_static_directory}}/templates/foot.html'\n" \
                                 f'\t}}\n' \
                                 "\tapp.default_route.context={'title': app.name, 'app_name': app.name, 'static': " \
                                 "global_static_directory,}\n" \
                                 f"\tapp.add_route(app.default_route)\n" \
                                 f'\treturn app\n'.expandtabs(4)

    def generate(self):
        """Generate new app files and routes"""
        os.mkdir(self.app_dir)
        os.mkdir(self.app_base)
        os.mkdir(self.template_directory)
        os.mkdir(self.local_static_directory)
        copyfile(Settings.APP_INDEX_TEMPLATE, self.template_directory + '/index.html')
        with open(self.app_file, 'w+') as f:
            f.write(self.app_file_contents)
        with open(self.app_request_func_file, 'w+') as f:
            f.write('# Define functions to run on requests below')
        autopep8.fix_file(self.app_file, Settings.CODE_FORMAT_OPTIONS)
        return True

    def kill(self):
        """Deletes app files and routes"""
        rmtree(self.app_dir)
        return True

    def add_route(self, route):
        """Adds route to app"""
        if not os.path.isfile(route.file_path) and '/static' not in route.route_path:
            file = open(route.file_path, 'w+')
            file.close()
        self.routes.append(route.__dict__)
