from NAPyF.Types import Route, Method
from NAPyF.App import App
from NAPyF.Admin.RequestFunctions import auth_list_users, auth_get_user, auth_update_user, auth_delete_user


def admin(global_static_directory):
    app = App('Admin')
    app.default_route['html_templates'] = {
        'head': f'{global_static_directory}/templates/head.html',
        'content': f'{app.template_directory}/index.html',
        'foot': f'{global_static_directory}/templates/foot.html'
    }
    app.default_route["context"]['users'] = auth_list_users()
    app.default_route["auth_level_required"] = 1
    user_edit_get_route = Route(
        app_name=app.name,
        route_path=f'/{app.name}/user/',
        file_path=f'{app.template_directory}/user.html',
        context={'title': 'Edit User', 'app_name': app.name},
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
        route_path=f'/{app.name}/user/',
        file_path=f'{app.template_directory}/user.html',
        context={'title': 'Edit User', 'app_name': app.name},
        request_method=Method.POST.value,
        auth_level_required=1
    )
    user_edit_post_route.html_templates = {
        'head': f'{global_static_directory}/templates/head.html',
        'content': f'{app.template_directory}/user.html',
        'foot': f'{global_static_directory}/templates/foot.html'
    }
    user_edit_post_route.redirect = '/Admin'
    user_edit_post_route.request_function = auth_update_user.__name__
    app.add_route(user_edit_post_route)

    user_delete_post_route = Route(
        app_name=app.name,
        route_path=f'/{app.name}/user/delete/',
        file_path=f'{app.template_directory}/user.html',
        context={'title': 'Edit User', 'app_name': app.name},
        request_method=Method.POST.value,
        auth_level_required=1
    )
    user_delete_post_route.html_templates = {
        'head': f'{global_static_directory}/templates/head.html',
        'content': f'{app.template_directory}/user.html',
        'foot': f'{global_static_directory}/templates/foot.html'
    }
    user_delete_post_route.redirect = '/Admin'
    user_delete_post_route.request_function = auth_delete_user.__name__
    app.add_route(user_delete_post_route)
    return app
