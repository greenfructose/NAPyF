import getopt
import os
import io
import sys
from contextlib import redirect_stdout
import autopep8
from NAPyF.Routes import route_builder
from Settings import TermColors, ROUTES_FILE, CODE_FORMAT_OPTIONS
from NAPyF.App import App
import NAPyF.Server


def main(argv):
    try:
        opts, args = getopt.getopt(argv, "rbn:k:", ["name=", "name="])
    except getopt.GetoptError:
        print('Some error occured')
        print('begin.py -r  ----- Run Existing App')
        print('begin.py -b -n <name>  ----- New app with name')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-r':
            try:
                NAPyF.Server.run()
            except KeyboardInterrupt:
                print("Keyboard Interrupt")
                sys.exit(0)
        elif opt in ('-n', '--name'):
            try:
                name = arg.strip()
                print(f'Generating files for {name}...')
                app = App(name)
                app.generate()
                route_builder()
                # autopep8.fix_file(ROUTES_FILE, CODE_FORMAT_OPTIONS)
                print('Done!')
            except KeyboardInterrupt:
                sys.exit()
        elif opt in ('-k', '--name'):
            try:
                name = arg.strip()
                print(f'{TermColors.WARNING}{TermColors.BOLD}All associated files and routes will be deleted.{TermColors.ENDC}')
                sure = input(f'Are you sure you want to delete {name}? \n(y/n)')
                if sure.lower().strip() == 'y':
                    print(f'Deleting {name}...')
                    app = App(name)
                    app.kill()
                    route_builder()
                    # autopep8.fix_file(ROUTES_FILE, CODE_FORMAT_OPTIONS)
                    print('Done!')
                elif sure.lower().strip() == 'n':
                    sys.exit()
                else:
                    print('Invalid input. Exiting now.')
                    sys.exit()
            except KeyboardInterrupt:
                sys.exit()


if __name__ == '__main__':
    main(sys.argv[1:])
