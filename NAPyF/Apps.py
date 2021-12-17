from NAPyF.App import App
from NAPyF.RequestHandler import RequestHandler
from NAPyF.Types import Route, Method


def default():
    app = App('default')
    return app

