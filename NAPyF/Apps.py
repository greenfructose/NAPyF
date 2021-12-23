from functools import wraps
from NAPyF.App import App
from NAPyF.Types import Route, Method
from NAPyF.RequestFunctions import default_post, auth_post_user, auth_list_users
from Settings import GLOBAL_STATIC_DIRECTORY


def default():
    app = App('default')
    default_get_route = Route(
        app_name=app.name,
        route_path='/',
        file_path=f'{app.template_directory}/index.html',
        context={'title': 'Default', 'app_name': app.name},
        request_method=Method.GET.value,
    )
    app.default_route["html_templates"] = {
        'head': f'{GLOBAL_STATIC_DIRECTORY}/templates/head.html',
        'content': f'{app.template_directory}/index.html',
        'foot': f'{GLOBAL_STATIC_DIRECTORY}/templates/foot.html'
    }
    default_get_route.html_templates = {
        'head': f'{GLOBAL_STATIC_DIRECTORY}/templates/head.html',
        'content': f'{app.template_directory}/index.html',
        'foot': f'{GLOBAL_STATIC_DIRECTORY}/templates/foot.html'
    }
    app.add_route(default_get_route)
    default_post_route = Route(
        app_name=app.name,
        route_path='/',
        file_path=f'{app.template_directory}/index.html',
        context={'title': 'Default', 'app_name': app.name},
        request_method=Method.POST.value,
    )
    default_post_route.html_templates = {
        'head': f'{GLOBAL_STATIC_DIRECTORY}/templates/head.html',
        'content': f'{app.template_directory}/index.html',
        'foot': f'{GLOBAL_STATIC_DIRECTORY}/templates/foot.html'
    }
    default_post_route.request_function = default_post.__name__
    app.add_route(default_post_route)
    return app


# Active apps will have routes automatically generated for them


def admin():
    app = App('admin')
    app.default_route['html_templates'] = {
        'head': f'{GLOBAL_STATIC_DIRECTORY}/templates/head.html',
        'content': f'{app.template_directory}/index.html',
        'foot': f'{GLOBAL_STATIC_DIRECTORY}/templates/foot.html'
    }
    app.default_route["context"]['users'] = auth_list_users()
    return app


def profile():
    app = App('profile')
    app.default_route['html_templates'] = {
        'head': f'{GLOBAL_STATIC_DIRECTORY}/templates/head.html',
        'content': f'{app.template_directory}/index.html',
        'foot': f'{GLOBAL_STATIC_DIRECTORY}/templates/foot.html'
    }
    user_registration_get_route = Route(
        app_name=app.name,
        route_path=f'/{app.name}/register',
        file_path=f'{app.template_directory}/register.html',
        context={'title': 'Default', 'app_name': app.name},
        request_method=Method.GET.value,
    )
    user_registration_get_route.html_templates = {
        'head': f'{GLOBAL_STATIC_DIRECTORY}/templates/head.html',
        'content': f'{app.template_directory}/index.html',
        'foot': f'{GLOBAL_STATIC_DIRECTORY}/templates/foot.html'
    }
    app.add_route(user_registration_get_route)
    user_registration_post_route = Route(
        app_name=app.name,
        route_path=f'/{app.name}/register',
        file_path=f'{app.template_directory}/register.html',
        context={'title': 'Default', 'app_name': app.name},
        request_method=Method.POST.value,
    )
    user_registration_post_route.html_templates = {
        'head': f'{GLOBAL_STATIC_DIRECTORY}/templates/head.html',
        'content': f'{app.template_directory}/index.html',
        'foot': f'{GLOBAL_STATIC_DIRECTORY}/templates/foot.html'
    }
    user_registration_post_route.request_function = auth_post_user.__name__
    user_registration_post_route.redirect = '/profile'
    app.add_route(user_registration_post_route)
    return app


active_apps = [
    default,
    admin,
    profile,
]
