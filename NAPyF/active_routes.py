routes = [{'app_name': 'Admin',
           'route_path': '/admin',
           'request_method': 1,
           'file_path': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/NAPyF/Admin/base/templates/index.html',
           'context': {'title': 'Admin',
                       'app_name': 'Admin',
                       'static': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/global_static',
                       'admin_objects': {'admin-user': [{'user_id': 1,
                                                         'first_name': 'Justin',
                                                         'last_name': 'Turney',
                                                         'email': 'info@napyf.com',
                                                         'username': 'admin',
                                                         'auth_level': 9001,
                                                         'is_verified': 1}],
                                         'profile': [{'profile_id': 1,
                                                      'first_name': 'Justin',
                                                      'last_name': 'Turney',
                                                      'email': 'info@napyf.com',
                                                      'username': 'admin',
                                                      'picture': 'default_profile_picture.png',
                                                      'user_id': 1}]}},
           'auth_level_required': 1,
           'html_templates': {'head': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/global_static/templates/head.html',
                              'content': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/NAPyF/Admin/base/templates/index.html',
                              'foot': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/global_static/templates/foot.html'}},
          {'app_name': 'Admin',
           'route_path': '/admin/user',
           'request_method': 1,
           'file_path': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/NAPyF/Admin/base/templates/user.html',
           'context': {'title': 'Edit User',
                       'app_name': 'Admin',
                       'static': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/global_static'},
           'auth_level_required': 1,
           'html_templates': {'head': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/global_static/templates/head.html',
                              'content': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/NAPyF/Admin/base/templates/user.html',
                              'foot': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/global_static/templates/foot.html'},
           'request_function': 'auth_get_user'},
          {'app_name': 'Admin',
           'route_path': '/admin/user',
           'request_method': 2,
           'file_path': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/NAPyF/Admin/base/templates/user.html',
           'context': {'title': 'Edit User',
                       'app_name': 'Admin',
                       'static': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/global_static'},
           'auth_level_required': 1,
           'html_templates': {'head': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/global_static/templates/head.html',
                              'content': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/NAPyF/Admin/base/templates/user.html',
                              'foot': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/global_static/templates/foot.html'},
           'redirect': '/admin',
           'request_function': 'auth_update_user'},
          {'app_name': 'Admin',
           'route_path': '/admin/user/delete',
           'request_method': 2,
           'file_path': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/NAPyF/Admin/base/templates/user.html',
           'context': {'title': 'Edit User',
                       'app_name': 'Admin',
                       'static': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/global_static'},
           'auth_level_required': 1,
           'html_templates': {'head': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/global_static/templates/head.html',
                              'content': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/NAPyF/Admin/base/templates/user.html',
                              'foot': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/global_static/templates/foot.html'},
           'redirect': '/admin',
           'request_function': 'auth_delete_user'},
          {'app_name': 'Admin',
           'route_path': '/admin/login',
           'request_method': 1,
           'file_path': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/NAPyF/Admin/base/templates/login.html',
           'context': {'title': 'Login',
                       'app_name': 'Admin',
                       'static': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/global_static'},
           'auth_level_required': 0,
           'html_templates': {'head': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/global_static/templates/head.html',
                              'content': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/NAPyF/Admin/base/templates/login.html',
                              'foot': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/global_static/templates/foot.html'}},
          {'app_name': 'Admin',
           'route_path': '/admin/login',
           'request_method': 2,
           'file_path': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/NAPyF/Admin/base/templates/login.html',
           'context': {'title': 'Login',
                       'app_name': 'Admin',
                       'static': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/global_static'},
           'auth_level_required': 0,
           'html_templates': {'head': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/global_static/templates/head.html',
                              'content': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/NAPyF/Admin/base/templates/login.html',
                              'foot': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/global_static/templates/foot.html'},
           'request_function': 'auth_login_user',
           'redirect': '/admin'},
          {'app_name': 'Admin',
           'route_path': '/admin/logout',
           'request_method': 1,
           'file_path': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/NAPyF/Admin/base/templates/logout.html',
           'context': {'title': 'Logout',
                       'app_name': 'Admin',
                       'static': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/global_static'},
           'auth_level_required': 0,
           'html_templates': {'head': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/global_static/templates/head.html',
                              'content': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/NAPyF/Admin/base/templates/login.html',
                              'foot': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/global_static/templates/foot.html'}},
          {'app_name': 'Admin',
           'route_path': '/admin/logout',
           'request_method': 2,
           'file_path': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/NAPyF/Admin/base/templates/logout.html',
           'context': {'title': 'Logout',
                       'app_name': 'Admin',
                       'static': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/global_static'},
           'auth_level_required': 0,
           'html_templates': {'head': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/global_static/templates/head.html',
                              'content': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/NAPyF/Admin/base/templates/login.html',
                              'foot': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/global_static/templates/foot.html'},
           'request_function': 'auth_logout_user',
           'redirect': '/'},
          {'app_name': 'Admin',
           'route_path': '/admin/sessions',
           'request_method': 1,
           'file_path': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/NAPyF/Admin/base/templates/sessions.html',
           'context': {'title': 'Logout',
                       'app_name': 'Admin',
                       'static': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/global_static'},
           'auth_level_required': 9001,
           'html_templates': {'head': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/global_static/templates/head.html',
                              'content': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/NAPyF/Admin/base/templates/sessions.html',
                              'foot': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/global_static/templates/foot.html'},
           'request_function': 'get_sessions'},
          {'app_name': 'static',
           'route_path': '/static',
           'request_method': 1,
           'file_path': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/global_static',
           'context': None,
           'auth_level_required': 0},
          {'app_name': 'default',
           'route_path': '/default',
           'request_method': 1,
           'file_path': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/Apps/default/base/templates/index.html',
           'context': {'title': 'Default',
                       'app_name': 'default'},
           'auth_level_required': 0,
           'html_templates': {'head': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/global_static/templates/head.html',
                              'content': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/Apps/default/base/templates/index.html',
                              'foot': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/global_static/templates/foot.html'}},
          {'app_name': 'default',
           'route_path': '/',
           'request_method': 1,
           'file_path': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/Apps/default/base/templates/index.html',
           'context': {'title': 'Default',
                       'app_name': 'default',
                       'static': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/global_static'},
           'auth_level_required': 0,
           'html_templates': {'head': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/global_static/templates/head.html',
                              'content': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/Apps/default/base/templates/index.html',
                              'foot': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/global_static/templates/foot.html'}},
          {'app_name': 'default',
           'route_path': '/',
           'request_method': 2,
           'file_path': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/Apps/default/base/templates/index.html',
           'context': {'title': 'Default',
                       'app_name': 'default',
                       'static': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/global_static'},
           'auth_level_required': 0,
           'html_templates': {'head': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/global_static/templates/head.html',
                              'content': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/Apps/default/base/templates/index.html',
                              'foot': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/global_static/templates/foot.html'},
           'request_function': 'default_post'},
          {'app_name': 'profile',
           'route_path': '/profile',
           'request_method': 1,
           'file_path': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/Apps/profile/base/templates/index.html',
           'context': {'title': 'Profile',
                       'app_name': 'profile',
                       'static': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/global_static'},
           'auth_level_required': 0,
           'html_templates': {'head': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/global_static/templates/head.html',
                              'content': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/Apps/profile/base/templates/index.html',
                              'foot': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/global_static/templates/foot.html',
                              'css': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/Apps/profile/local_static/css/profile.css'},
           'request_function': 'get_profile'},
          {'app_name': 'profile',
           'route_path': '/profile/local_static',
           'request_method': 1,
           'file_path': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/Apps/profile/local_static',
           'context': None,
           'auth_level_required': 0},
          {'app_name': 'profile',
           'route_path': '/profile/edit',
           'request_method': 1,
           'file_path': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/Apps/profile/base/templates/profile.html',
           'context': {'title': 'Edit Profile',
                       'app_name': 'profile',
                       'static': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/global_static'},
           'auth_level_required': 1,
           'html_templates': {'head': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/global_static/templates/head.html',
                              'content': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/Apps/profile/base/templates/profile.html',
                              'foot': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/global_static/templates/foot.html'},
           'request_function': 'get_profile'},
          {'app_name': 'profile',
           'route_path': '/profile/edit',
           'request_method': 2,
           'file_path': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/Apps/profile/base/templates/profile.html',
           'context': {'title': 'Edit Profile',
                       'app_name': 'profile',
                       'static': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/global_static'},
           'auth_level_required': 1,
           'html_templates': {'head': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/global_static/templates/head.html',
                              'content': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/Apps/profile/base/templates/profile.html',
                              'foot': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/global_static/templates/foot.html'},
           'redirect': '/profile',
           'request_function': 'request_update_profile'},
          {'app_name': 'profile',
           'route_path': '/profile/register',
           'request_method': 1,
           'file_path': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/Apps/profile/base/templates/register.html',
           'context': {'title': 'Register',
                       'app_name': 'profile',
                       'static': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/global_static'},
           'auth_level_required': 0,
           'html_templates': {'head': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/global_static/templates/head.html',
                              'content': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/Apps/profile/base/templates/index.html',
                              'foot': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/global_static/templates/foot.html'}},
          {'app_name': 'profile',
           'route_path': '/profile/register',
           'request_method': 2,
           'file_path': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/Apps/profile/base/templates/register.html',
           'context': {'title': 'Register',
                       'app_name': 'profile',
                       'static': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/global_static'},
           'auth_level_required': 0,
           'html_templates': {'head': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/global_static/templates/head.html',
                              'content': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/Apps/profile/base/templates/index.html',
                              'foot': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/global_static/templates/foot.html'},
           'request_function': 'create_user',
           'redirect': '/'},
          {'app_name': 'profile',
           'route_path': '/profile/login',
           'request_method': 1,
           'file_path': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/Apps/profile/base/templates/login.html',
           'context': {'title': 'Login',
                       'app_name': 'profile',
                       'static': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/global_static'},
           'auth_level_required': 0,
           'html_templates': {'head': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/global_static/templates/head.html',
                              'content': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/Apps/profile/base/templates/login.html',
                              'foot': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/global_static/templates/foot.html'}},
          {'app_name': 'profile',
           'route_path': '/profile/login',
           'request_method': 2,
           'file_path': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/Apps/profile/base/templates/login.html',
           'context': {'title': 'Login',
                       'app_name': 'profile',
                       'static': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/global_static'},
           'auth_level_required': 0,
           'html_templates': {'head': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/global_static/templates/head.html',
                              'content': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/Apps/profile/base/templates/login.html',
                              'foot': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/global_static/templates/foot.html'},
           'request_function': 'auth_login_user',
           'redirect': '/profile'},
          {'app_name': 'profile',
           'route_path': '/profile/logout',
           'request_method': 1,
           'file_path': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/Apps/profile/base/templates/logout.html',
           'context': {'title': 'Logout',
                       'app_name': 'profile',
                       'static': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/global_static'},
           'auth_level_required': 0,
           'html_templates': {'head': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/global_static/templates/head.html',
                              'content': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/Apps/profile/base/templates/login.html',
                              'foot': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/global_static/templates/foot.html'}},
          {'app_name': 'profile',
           'route_path': '/profile/logout',
           'request_method': 2,
           'file_path': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/Apps/profile/base/templates/logout.html',
           'context': {'title': 'Logout',
                       'app_name': 'profile',
                       'static': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/global_static'},
           'auth_level_required': 0,
           'html_templates': {'head': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/global_static/templates/head.html',
                              'content': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/Apps/profile/base/templates/login.html',
                              'foot': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/global_static/templates/foot.html'},
           'request_function': 'auth_logout_user',
           'redirect': '/'}]
