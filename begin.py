import getopt
import sys
from NAPyF.Routes import route_builder
from Settings import TermColors, GLOBAL_STATIC_DIRECTORY, BASE_DIR
from NAPyF.App import App
import NAPyF.Server


def main(argv):
    try:
        opts, args = getopt.getopt(argv, "rbn:k:", ["name=", "name="])
    except getopt.GetoptError:
        print('Some error occured')
        print('begin.py -r                  ----- Run Server')
        print('begin.py -n <app name>       ----- New app with name')
        print('begin.py -k <app name>       ----- Delete existing app')
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
                generated = app.generate()
                while not generated:
                    continue
                route_builder(GLOBAL_STATIC_DIRECTORY, BASE_DIR)
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
                    killed = app.kill()
                    while not killed:
                        continue
                    route_builder(GLOBAL_STATIC_DIRECTORY, BASE_DIR)
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
