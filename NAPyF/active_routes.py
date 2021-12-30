routes = [{'app_name': 'default',
           'route_path': '/default',
           'request_method': 1,
           'file_path': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/default/base/templates/index.html',
           'context': {'title': 'default',
                       'app_name': 'default'},
           'auth_level_required': 0,
           'html_templates': {'head': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/global_static/templates/head.html',
                              'content': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/default/base/templates/index.html',
                              'foot': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/global_static/templates/foot.html'}},
          {'app_name': 'default',
           'route_path': '/',
           'request_method': 1,
           'file_path': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/default/base/templates/index.html',
           'context': {'title': 'Default',
                       'app_name': 'default'},
           'auth_level_required': 0,
           'html_templates': {'head': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/global_static/templates/head.html',
                              'content': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/default/base/templates/index.html',
                              'foot': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/global_static/templates/foot.html'}},
          {'app_name': 'default',
           'route_path': '/',
           'request_method': 2,
           'file_path': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/default/base/templates/index.html',
           'context': {'title': 'Default',
                       'app_name': 'default'},
           'auth_level_required': 0,
           'html_templates': {'head': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/global_static/templates/head.html',
                              'content': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/default/base/templates/index.html',
                              'foot': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/global_static/templates/foot.html'},
           'request_function': 'default_post'},
          {'app_name': 'admin',
           'route_path': '/admin',
           'request_method': 1,
           'file_path': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/admin/base/templates/index.html',
           'context': {'title': 'admin',
                       'app_name': 'admin',
                       'users': [(1,
                                  'Justin',
                                  'Turney',
                                  'justinclarkturney@gmail.com',
                                  '4172309931',
                                  'jturney',
                                  2,
                                  1),
                                 (2,
                                  'Debo',
                                  'Brown',
                                  'H@ell.com',
                                  '4',
                                  'ju',
                                  0,
                                  1),
                                 (3,
                                  'Jerry',
                                  'Fallwell',
                                  't@A',
                                  '333',
                                  'h',
                                  2,
                                  1),
                                 (4,
                                  'Another',
                                  'Test',
                                  't@h',
                                  '45',
                                  'h',
                                  1,
                                  0),
                                 (5,
                                  'Username',
                                  'IsValid',
                                  'a@t',
                                  '4',
                                  'username',
                                  1,
                                  0),
                                 (6,
                                  'Justin',
                                  'Turney',
                                  'justinclarkturney@gmail.com',
                                  '4172309931',
                                  'greenfructose1',
                                  9000,
                                  1),
                                 (7,
                                  'Justin',
                                  'Turney',
                                  'justinclarkturney@gmail.com',
                                  '4172309931',
                                  'a882014',
                                  0,
                                  0),
                                 (8,
                                  'Justin',
                                  'Turney',
                                  'justinclarkturney@gmail.com',
                                  '4172309931',
                                  'a882014',
                                  0,
                                  0),
                                 (9,
                                  'Justin',
                                  'Turney',
                                  'justinclarkturney@gmail.com',
                                  '4172309931',
                                  'joi',
                                  0,
                                  0),
                                 (10,
                                  'Justin',
                                  'Turney',
                                  'justinclarkturney@gmail.com',
                                  '4172309931',
                                  'admin',
                                  0,
                                  0)]},
           'auth_level_required': 1,
           'html_templates': {'head': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/global_static/templates/head.html',
                              'content': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/admin/base/templates/index.html',
                              'foot': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/global_static/templates/foot.html'}},
          {'app_name': 'admin',
           'route_path': '/admin/user/',
           'request_method': 1,
           'file_path': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/admin/base/templates/user.html',
           'context': {'title': 'Edit User',
                       'app_name': 'admin'},
           'auth_level_required': 1,
           'html_templates': {'head': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/global_static/templates/head.html',
                              'content': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/admin/base/templates/user.html',
                              'foot': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/global_static/templates/foot.html'},
           'request_function': 'auth_get_user'},
          {'app_name': 'admin',
           'route_path': '/admin/user/',
           'request_method': 2,
           'file_path': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/admin/base/templates/user.html',
           'context': {'title': 'Edit User',
                       'app_name': 'admin'},
           'auth_level_required': 1,
           'html_templates': {'head': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/global_static/templates/head.html',
                              'content': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/admin/base/templates/user.html',
                              'foot': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/global_static/templates/foot.html'},
           'redirect': '/admin',
           'request_function': 'auth_update_user'},
          {'app_name': 'profile',
           'route_path': '/profile',
           'request_method': 1,
           'file_path': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/profile/base/templates/index.html',
           'context': {'title': 'profile',
                       'app_name': 'profile'},
           'auth_level_required': 0,
           'html_templates': {'head': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/global_static/templates/head.html',
                              'content': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/profile/base/templates/index.html',
                              'foot': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/global_static/templates/foot.html'}},
          {'app_name': 'profile',
           'route_path': '/profile/register',
           'request_method': 1,
           'file_path': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/profile/base/templates/register.html',
           'context': {'title': 'Register',
                       'app_name': 'profile'},
           'auth_level_required': 0,
           'html_templates': {'head': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/global_static/templates/head.html',
                              'content': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/profile/base/templates/index.html',
                              'foot': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/global_static/templates/foot.html'}},
          {'app_name': 'profile',
           'route_path': '/profile/register',
           'request_method': 2,
           'file_path': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/profile/base/templates/register.html',
           'context': {'title': 'Register',
                       'app_name': 'profile'},
           'auth_level_required': 0,
           'html_templates': {'head': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/global_static/templates/head.html',
                              'content': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/profile/base/templates/index.html',
                              'foot': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/global_static/templates/foot.html'},
           'request_function': 'auth_post_user',
           'redirect': '/profile'},
          {'app_name': 'profile',
           'route_path': '/profile/login',
           'request_method': 1,
           'file_path': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/profile/base/templates/login.html',
           'context': {'title': 'Login',
                       'app_name': 'profile'},
           'auth_level_required': 0,
           'html_templates': {'head': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/global_static/templates/head.html',
                              'content': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/profile/base/templates/login.html',
                              'foot': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/global_static/templates/foot.html'}},
          {'app_name': 'profile',
           'route_path': '/profile/login',
           'request_method': 2,
           'file_path': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/profile/base/templates/login.html',
           'context': {'title': 'Login',
                       'app_name': 'profile'},
           'auth_level_required': 0,
           'html_templates': {'head': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/global_static/templates/head.html',
                              'content': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/profile/base/templates/login.html',
                              'foot': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/global_static/templates/foot.html'},
           'request_function': 'auth_login_user',
           'redirect': '/profile'},
          {'app_name': 'profile',
           'route_path': '/profile/logout',
           'request_method': 1,
           'file_path': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/profile/base/templates/logout.html',
           'context': {'title': 'Logout',
                       'app_name': 'profile'},
           'auth_level_required': 0,
           'html_templates': {'head': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/global_static/templates/head.html',
                              'content': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/profile/base/templates/login.html',
                              'foot': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/global_static/templates/foot.html'}},
          {'app_name': 'profile',
           'route_path': '/profile/logout',
           'request_method': 2,
           'file_path': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/profile/base/templates/logout.html',
           'context': {'title': 'Logout',
                       'app_name': 'profile'},
           'auth_level_required': 0,
           'html_templates': {'head': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/global_static/templates/head.html',
                              'content': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/profile/base/templates/login.html',
                              'foot': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/global_static/templates/foot.html'},
           'request_function': 'auth_logout_user',
           'redirect': '/'}]
