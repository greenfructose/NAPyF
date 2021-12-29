from functools import wraps
from NAPyF.App import App
from NAPyF.Types import Route, Method
from NAPyF.RequestFunctions import default_post, auth_post_user, auth_list_users, auth_login_user, auth_logout_user
from Settings import GLOBAL_STATIC_DIRECTORY


def default():
    app = App('default')
    default_get_route = Route(
        app_name=app.name,
        route_path='/',
        file_path=f'{app.template_directory}/index.html',
        context={'title': 'Default', 'app_name': app.name},
        request_method=Method.GET.value,
        auth_level_required=0
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
        auth_level_required=0
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
    app.default_route["auth_level_required"] = 1
    user_edit_get_route = Route(
        app_name=app.name,
        route_path=f'/{app.name}/admin/user/',
        file_path=f'{app.template_directory}/user.html',
        context={'title': 'Edit User', 'app_name': app.name},
        request_method=Method.GET.value,
        auth_level_required=1
    )
    user_edit_get_route.html_templates = {
        'head': f'{GLOBAL_STATIC_DIRECTORY}/templates/head.html',
        'content': f'{app.template_directory}/user.html',
        'foot': f'{GLOBAL_STATIC_DIRECTORY}/templates/foot.html'
    }
    app.add_route(user_edit_get_route)
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
        context={'title': 'Register', 'app_name': app.name},
        request_method=Method.GET.value,
        auth_level_required=0
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
        context={'title': 'Register', 'app_name': app.name},
        request_method=Method.POST.value,
        auth_level_required=0
    )
    user_registration_post_route.html_templates = {
        'head': f'{GLOBAL_STATIC_DIRECTORY}/templates/head.html',
        'content': f'{app.template_directory}/index.html',
        'foot': f'{GLOBAL_STATIC_DIRECTORY}/templates/foot.html'
    }
    user_registration_post_route.request_function = auth_post_user.__name__
    user_registration_post_route.redirect = '/profile'
    app.add_route(user_registration_post_route)

    user_login_get_route = Route(
        app_name=app.name,
        route_path=f'/{app.name}/login',
        file_path=f'{app.template_directory}/login.html',
        context={'title': 'Login', 'app_name': app.name},
        request_method=Method.GET.value,
        auth_level_required=0
    )
    user_login_get_route.html_templates = {
        'head': f'{GLOBAL_STATIC_DIRECTORY}/templates/head.html',
        'content': f'{app.template_directory}/login.html',
        'foot': f'{GLOBAL_STATIC_DIRECTORY}/templates/foot.html'
    }
    app.add_route(user_login_get_route)

    user_login_post_route = Route(
        app_name=app.name,
        route_path=f'/{app.name}/login',
        file_path=f'{app.template_directory}/login.html',
        context={'title': 'Login', 'app_name': app.name},
        request_method=Method.POST.value,
        auth_level_required=0
    )
    user_login_post_route.html_templates = {
        'head': f'{GLOBAL_STATIC_DIRECTORY}/templates/head.html',
        'content': f'{app.template_directory}/login.html',
        'foot': f'{GLOBAL_STATIC_DIRECTORY}/templates/foot.html'
    }
    user_login_post_route.request_function = auth_login_user.__name__
    user_login_post_route.redirect = '/profile'
    app.add_route(user_login_post_route)

    user_logout_get_route = Route(
        app_name=app.name,
        route_path=f'/{app.name}/logout',
        file_path=f'{app.template_directory}/logout.html',
        context={'title': 'Logout', 'app_name': app.name},
        request_method=Method.GET.value,
        auth_level_required=0
    )
    user_logout_get_route.html_templates = {
        'head': f'{GLOBAL_STATIC_DIRECTORY}/templates/head.html',
        'content': f'{app.template_directory}/login.html',
        'foot': f'{GLOBAL_STATIC_DIRECTORY}/templates/foot.html'
    }
    app.add_route(user_logout_get_route)

    user_logout_post_route = Route(
        app_name=app.name,
        route_path=f'/{app.name}/logout',
        file_path=f'{app.template_directory}/logout.html',
        context={'title': 'Logout', 'app_name': app.name},
        request_method=Method.POST.value,
        auth_level_required=0
    )
    user_logout_post_route.html_templates = {
        'head': f'{GLOBAL_STATIC_DIRECTORY}/templates/head.html',
        'content': f'{app.template_directory}/login.html',
        'foot': f'{GLOBAL_STATIC_DIRECTORY}/templates/foot.html'
    }
    user_logout_post_route.request_function = auth_logout_user.__name__
    user_logout_post_route.redirect = '/'
    app.add_route(user_logout_post_route)

    return app


active_apps = [
    default,
    admin,
    profile,
]
