from NAPyF.App import App
from NAPyF.Types import Route, Method
from NAPyF.Admin.RequestFunctions import auth_login_user, auth_logout_user
from Apps.profile.RequestFunctions import create_user, get_profile, request_update_profile


def profile(global_static_directory, base_directory):
    app = App('profile')
    app.default_route.html_templates = {
        'head': f'{global_static_directory}/templates/head.html',
        'content': f'{app.template_directory}/index.html',
        'foot': f'{global_static_directory}/templates/foot.html',
        'css': f'{app.local_static_directory}/css/profile.css',
    }
    app.default_route.context = {'title': 'Profile', 'app_name': app.name, 'static': global_static_directory, }
    app.default_route.request_function = get_profile.__name__
    app.add_route(app.default_route)

    app.local_static_route = Route(
        app_name=app.name,
        route_path=f'{app.relative_route_path}/local_static',
        request_method=Method.GET.value,
        file_path=app.local_static_directory,
        context=None,
        auth_level_required=0,
    )
    app.add_route(app.local_static_route)

    profile_edit_get_route = Route(
        app_name=app.name,
        route_path=f'/{app.name.lower()}/edit',
        file_path=f'{app.template_directory}/profile.html',
        context={'title': 'Edit Profile', 'app_name': app.name, 'static': global_static_directory, },
        request_method=Method.GET.value,
        auth_level_required=1
    )
    profile_edit_get_route.html_templates = {
        'head': f'{global_static_directory}/templates/head.html',
        'content': f'{app.template_directory}/profile.html',
        'foot': f'{global_static_directory}/templates/foot.html'
    }
    profile_edit_get_route.request_function = get_profile.__name__
    app.add_route(profile_edit_get_route)

    profile_edit_post_route = Route(
        app_name=app.name,
        route_path=f'/{app.name.lower()}/edit',
        file_path=f'{app.template_directory}/profile.html',
        context={'title': 'Edit Profile', 'app_name': app.name, 'static': global_static_directory, },
        request_method=Method.POST.value,
        auth_level_required=1
    )
    profile_edit_post_route.html_templates = {
        'head': f'{global_static_directory}/templates/head.html',
        'content': f'{app.template_directory}/profile.html',
        'foot': f'{global_static_directory}/templates/foot.html'
    }
    profile_edit_post_route.redirect = '/profile'
    profile_edit_post_route.request_function = request_update_profile.__name__
    app.add_route(profile_edit_post_route)

    user_registration_get_route = Route(
        app_name=app.name,
        route_path=f'/{app.name.lower()}/register',
        file_path=f'{app.template_directory}/register.html',
        context={'title': 'Register', 'app_name': app.name, 'static': global_static_directory, },
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
        route_path=f'/{app.name.lower()}/register',
        file_path=f'{app.template_directory}/register.html',
        context={'title': 'Register', 'app_name': app.name, 'static': global_static_directory, },
        request_method=Method.POST.value,
        auth_level_required=0
    )
    user_registration_post_route.html_templates = {
        'head': f'{global_static_directory}/templates/head.html',
        'content': f'{app.template_directory}/index.html',
        'foot': f'{global_static_directory}/templates/foot.html'
    }
    user_registration_post_route.request_function = create_user.__name__
    user_registration_post_route.redirect = '/'
    app.add_route(user_registration_post_route)

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
    user_login_post_route.redirect = '/profile'
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

    return app
