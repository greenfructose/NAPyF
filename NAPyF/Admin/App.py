from NAPyF.Types import Route, Method
from NAPyF.App import App
from NAPyF.Admin.RequestFunctions import auth_list_admin_objects, auth_get_user, auth_update_user, auth_delete_user, \
    auth_logout_user, auth_login_user, get_sessions


def admin(global_static_directory, base_directory):
    app = App('Admin')
    app.default_route.html_templates = {
        'head': f'{global_static_directory}/templates/head.html',
        'content': f'{app.template_directory}/index.html',
        'foot': f'{global_static_directory}/templates/foot.html'
    }
    app.default_route.context = {'title': 'Admin',
                                 'app_name': app.name,
                                 'static': global_static_directory,
                                 'admin_objects': auth_list_admin_objects()}
    app.default_route.auth_level_required = 1
    app.add_route(app.default_route)
    user_edit_get_route = Route(
        app_name=app.name,
        route_path=f'/{app.name.lower()}/user',
        file_path=f'{app.template_directory}/user.html',
        context={'title': 'Edit User', 'app_name': app.name, 'static': global_static_directory, },
        request_method=Method.GET.value,
        auth_level_required=1
    )
    user_edit_get_route.html_templates = {
        'head': f'{global_static_directory}/templates/head.html',
        'content': f'{app.template_directory}/user.html',
        'foot': f'{global_static_directory}/templates/foot.html'
    }
    user_edit_get_route.request_function = auth_get_user.__name__
    app.add_route(user_edit_get_route)

    user_edit_post_route = Route(
        app_name=app.name,
        route_path=f'/{app.name.lower()}/user',
        file_path=f'{app.template_directory}/user.html',
        context={'title': 'Edit User', 'app_name': app.name, 'static': global_static_directory, },
        request_method=Method.POST.value,
        auth_level_required=1
    )
    user_edit_post_route.html_templates = {
        'head': f'{global_static_directory}/templates/head.html',
        'content': f'{app.template_directory}/user.html',
        'foot': f'{global_static_directory}/templates/foot.html'
    }
    user_edit_post_route.redirect = '/admin'
    user_edit_post_route.request_function = auth_update_user.__name__
    app.add_route(user_edit_post_route)

    user_delete_post_route = Route(
        app_name=app.name,
        route_path=f'/{app.name.lower()}/user/delete',
        file_path=f'{app.template_directory}/user.html',
        context={'title': 'Edit User', 'app_name': app.name, 'static': global_static_directory, },
        request_method=Method.POST.value,
        auth_level_required=1
    )
    user_delete_post_route.html_templates = {
        'head': f'{global_static_directory}/templates/head.html',
        'content': f'{app.template_directory}/user.html',
        'foot': f'{global_static_directory}/templates/foot.html'
    }
    user_delete_post_route.redirect = '/admin'
    user_delete_post_route.request_function = auth_delete_user.__name__
    app.add_route(user_delete_post_route)
    user_login_get_route = Route(
        app_name=app.name,
        route_path=f'/{app.name.lower()}/login',
        file_path=f'{app.template_directory}/login.html',
        context={'title': 'Login', 'app_name': app.name, 'static': global_static_directory, },
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
        route_path=f'/{app.name.lower()}/login',
        file_path=f'{app.template_directory}/login.html',
        context={'title': 'Login', 'app_name': app.name, 'static': global_static_directory, },
        request_method=Method.POST.value,
        auth_level_required=0
    )
    user_login_post_route.html_templates = {
        'head': f'{global_static_directory}/templates/head.html',
        'content': f'{app.template_directory}/login.html',
        'foot': f'{global_static_directory}/templates/foot.html'
    }
    user_login_post_route.request_function = auth_login_user.__name__
    user_login_post_route.redirect = '/admin'
    app.add_route(user_login_post_route)

    user_logout_get_route = Route(
        app_name=app.name,
        route_path=f'/{app.name.lower()}/logout',
        file_path=f'{app.template_directory}/logout.html',
        context={'title': 'Logout', 'app_name': app.name, 'static': global_static_directory, },
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
        route_path=f'/{app.name.lower()}/logout',
        file_path=f'{app.template_directory}/logout.html',
        context={'title': 'Logout', 'app_name': app.name, 'static': global_static_directory, },
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

    user_sessions_get_route = Route(
        app_name=app.name,
        route_path=f'/{app.name.lower()}/sessions',
        file_path=f'{app.template_directory}/sessions.html',
        context={'title': 'Logout', 'app_name': app.name, 'static': global_static_directory, },
        request_method=Method.GET.value,
        auth_level_required=9001
    )
    user_sessions_get_route.html_templates = {
        'head': f'{global_static_directory}/templates/head.html',
        'content': f'{app.template_directory}/sessions.html',
        'foot': f'{global_static_directory}/templates/foot.html'
    }
    user_sessions_get_route.request_function = get_sessions.__name__
    app.add_route(user_sessions_get_route)
    return app
