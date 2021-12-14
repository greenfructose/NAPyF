# Create a new application
import os
from glob import glob
from shutil import copyfile
import Settings


class App:
    def __init__(self, name):
        self.name = name
        self.app_dir = Settings.BASE_DIR + '/' + self.name
        self.app_base = self.app_dir + '/base'
        self.template_directory = self.app_base + '/templates'
        self.relative_route_path = '/' + self.name

    def generate(self):
        os.mkdir(self.app_dir)
        os.mkdir(self.app_base)
        os.mkdir(self.template_directory)
        copyfile(Settings.APP_INDEX_TEMPLATE, self.template_directory + '/index.html')
        route_string = ""
        with open(Settings.ROUTES_FILE, 'r') as f:
            route_string = f.read()
        end = route_string.find('}')
        new_route_string = (route_string[:end] + "\t'/" + self.name + "': '" + self.relative_route_path + "/base/templates/index.html',\n}\n").expandtabs(4)
        with open(Settings.ROUTES_FILE, 'w') as f:
            f.write(new_route_string)

    def kill(self):
        with open(Settings.ROUTES_FILE, 'r') as f:
            route_string = f.read()
        new_route_string = ""
        for line in route_string.splitlines():
            if '/' + self.name not in line:
                new_route_string += '\n' + line + '\n'
        with open(Settings.ROUTES_FILE, 'w') as f:
            f.write(new_route_string)
        filelist = glob(self.template_directory + '/*')
        for file in filelist:
            try:
                os.remove(file)
            except:
                print(f'Error occured while removing {file}')
        os.rmdir(self.template_directory)
        os.rmdir(self.app_base)
        os.rmdir(self.app_dir)

