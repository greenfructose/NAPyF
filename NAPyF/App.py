# Create a new application
import os
from glob import glob
from shutil import copyfile
import Settings
from NAPyF.Types import Route, Method
# from NAPyF.Routes import route_builder
import autopep8
from pathlib import Path


class App:
    def __init__(self, name):
        self.name = name
        self.app_dir = Settings.BASE_DIR + '/' + self.name
        self.app_base = self.app_dir + '/base'
        self.template_directory = self.app_base + '/templates'
        self.local_static_directory = self.app_base + '/local_static'
        self.relative_route_path = '/' + self.name
        self.routes = [
            Route(
                app_name=self.name,
                route_path=self.relative_route_path,
                file_path=f'{self.template_directory}/index.html',
                context={'title': self.name, 'app_name': self.name},
                method=Method.GET.value
            )
        ]

    """Generate new app files and routes"""

    def generate(self):
        os.mkdir(self.app_dir)
        os.mkdir(self.app_base)
        os.mkdir(self.template_directory)
        os.mkdir(self.local_static_directory)
        copyfile(Settings.APP_INDEX_TEMPLATE, self.template_directory + '/index.html')
        app_string = ""
        with open(Settings.APPS_FILE, 'r') as f:
            app_string = f.read()
        end_app_def = app_string.find('active_apps')
        active_apps = app_string[end_app_def:]
        new_app_string = (app_string[
                          :end_app_def] + "def " + self.name + "():\n\t" +
                          "app = App('" + self.name + "')\n\t" +
                          "return app\n\n\n"
                          ).expandtabs(4)
        end_active_apps = active_apps.find(']\n')
        new_active_apps = (active_apps[
                           :end_active_apps] + "\t" + self.name + ",\n]").expandtabs(4)
        # new_app_string = autopep8.fix_code(new_app_string, Settings.CODE_FORMAT_OPTIONS)
        # new_active_apps = autopep8.fix_code(new_active_apps, Settings.CODE_FORMAT_OPTIONS)
        with open(Settings.APPS_FILE, 'w') as f:
            f.write(new_app_string)
            f.write(new_active_apps)
        autopep8.fix_file(Settings.APPS_FILE, Settings.CODE_FORMAT_OPTIONS)
        return True
        # black.format_file_in_place(Path(Settings.ROUTES_FILE), fast=True, mode=black.Mode())

    """Deletes app files and routes"""

    def kill(self):
        with open(Settings.APPS_FILE, 'r') as f:
            app_string = f.read()
        new_app_string = ""
        start_of_app_def = app_string.find("def " + self.name)
        end_of_app_def = app_string[start_of_app_def:].find("return app") + start_of_app_def + 10
        new_app_string += app_string[:start_of_app_def] + app_string[end_of_app_def:]
        new_app_string = new_app_string.replace(self.name + ',\n', "")
        new_app_string = autopep8.fix_code(new_app_string, Settings.CODE_FORMAT_OPTIONS)
        with open(Settings.APPS_FILE, 'w') as f:
            f.write(new_app_string)
        # autopep8.fix_file(Settings.APPS_FILE, Settings.CODE_FORMAT_OPTIONS)
        filelist = glob(self.template_directory + '/*')
        for file in filelist:
            try:
                os.remove(file)
            except:
                print(f'Error occured while removing {file}')
        os.rmdir(self.template_directory)
        os.rmdir(self.local_static_directory)
        os.rmdir(self.app_base)
        os.rmdir(self.app_dir)
        return True
        # black.format_file_in_place(Path(Settings.ROUTES_FILE), fast=True, mode=black.Mode())

    """Adds route to app"""

    def add_route(self, route):
        self.routes.append(route)
