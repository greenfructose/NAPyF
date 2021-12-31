from NAPyF.App import App
from NAPyF.Types import Route, Method
from Apps.default.RequestFunctions import default_post


def default(global_static_directory, base_directory):
    app = App('default')
    app.default_route.context = {'title': 'Default', 'app_name': app.name}
    app.add_route(app.default_route)
    default_get_route = Route(
        app_name=app.name,
        route_path='/',
        file_path=f'{app.template_directory}/index.html',
        context={'title': 'Default', 'app_name': app.name},
        request_method=Method.GET.value,
        auth_level_required=0
    )
    app.default_route.html_templates = {
        'head': f'{global_static_directory}/templates/head.html',
        'content': f'{app.template_directory}/index.html',
        'foot': f'{global_static_directory}/templates/foot.html'
    }
    default_get_route.html_templates = {
        'head': f'{global_static_directory}/templates/head.html',
        'content': f'{app.template_directory}/index.html',
        'foot': f'{global_static_directory}/templates/foot.html'
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
        'head': f'{global_static_directory}/templates/head.html',
        'content': f'{app.template_directory}/index.html',
        'foot': f'{global_static_directory}/templates/foot.html'
    }
    default_post_route.request_function = default_post.__name__
    app.add_route(default_post_route)
    return app
