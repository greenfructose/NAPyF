from NAPyF.App import App
from NAPyF.Types import Route, Method
from NAPyF.Admin.RequestFunctions import auth_post_user, auth_login_user, auth_logout_user


def profile(global_static_directory, base_directory):
    app = App('profile')
    app.default_route.html_templates = {
        'head': f'{global_static_directory}/templates/head.html',
        'content': f'{app.template_directory}/index.html',
        'foot': f'{global_static_directory}/templates/foot.html'
    }
    app.default_route.context = {'title': 'Profile', 'app_name': app.name}
    app.add_route(app.default_route)
    user_registration_get_route = Route(
        app_name=app.name,
        route_path=f'/{app.name}/register',
        file_path=f'{app.template_directory}/register.html',
        context={'title': 'Register', 'app_name': app.name},
        request_method=Method.GET.value,
        auth_level_required=0
    )
    user_registration_get_route.html_templates = {
        'head': f'{global_static_directory}/templates/head.html',
        'content': f'{app.template_directory}/index.html',
        'foot': f'{global_static_directory}/templates/foot.html'
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
        'head': f'{global_static_directory}/templates/head.html',
        'content': f'{app.template_directory}/index.html',
        'foot': f'{global_static_directory}/templates/foot.html'
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
        'head': f'{global_static_directory}/templates/head.html',
        'content': f'{app.template_directory}/login.html',
        'foot': f'{global_static_directory}/templates/foot.html'
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
        'head': f'{global_static_directory}/templates/head.html',
        'content': f'{app.template_directory}/login.html',
        'foot': f'{global_static_directory}/templates/foot.html'
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
        'head': f'{global_static_directory}/templates/head.html',
        'content': f'{app.template_directory}/login.html',
        'foot': f'{global_static_directory}/templates/foot.html'
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
        'head': f'{global_static_directory}/templates/head.html',
        'content': f'{app.template_directory}/login.html',
        'foot': f'{global_static_directory}/templates/foot.html'
    }
    user_logout_post_route.request_function = auth_logout_user.__name__
    user_logout_post_route.redirect = '/'
    app.add_route(user_logout_post_route)

    return app

