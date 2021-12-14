import getopt
import io
import sys
from contextlib import redirect_stdout
from NAPyF.AppGenerator import App
import NAPyF.Server


def main(argv):
    try:
        opts, args = getopt.getopt(argv, "rbn:", ["name="])
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
                name = arg
                app = App(name)
                app.generate()
            except KeyboardInterrupt:
                sys.exit()


if __name__ == '__main__':
    main(sys.argv[1:])
