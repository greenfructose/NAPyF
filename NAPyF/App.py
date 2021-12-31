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
        self.app_dir = Settings.APPS_DIR + '/' + self.name
        self.app_base = self.app_dir + '/base'
        self.app_file = self.app_dir + '/App.py'
        self.app_request_func_file = self.app_dir + '/RequestFunctions.py'
        self.template_directory = self.app_base + '/templates'
        self.local_static_directory = self.app_base + '/local_static'
        self.relative_route_path = '/' + self.name
        self.html_templates = {
            'content': f'{self.template_directory}/index.html', }
        self.default_route = None
        self.routes = [

        ]
        self.app_file_contents = f'# Define app and routes below\n\n' \
                                 f'from NAPyF.App import App\n' \
                                 f'from NAPyF.Types import Route, Method\n' \
                                 f'from Settings import GLOBAL_STATIC_DIRECTORY\n\n\n' \
                                 f'def {self.name}():\n' \
                                 f'\tapp = App()\n' \
                                 f'\tapp.default_route = Route(\n' \
                                 f'\t\tapp_name=app.name,\n' \
                                 f'\t\troute_path=app.relative_route_path,\n' \
                                 f"\t\tfile_path=f'{{app.template_directory}}/index.html',\n" \
                                 f"\t\tcontext={{'title': app.name, 'app_name': app.name, }},\n" \
                                 f"\t\trequest_method=Method.GET.value,\n" \
                                 f"\t\tauth_level_required=0\n" \
                                 f"\t)\n" \
                                 f"\tapp.add_route(app.default_route)\n".expandtabs(4)

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
        if not os.path.isfile(route.file_path):
            file = open(route.file_path, 'w+')
            file.close()
        self.routes.append(route.__dict__)
