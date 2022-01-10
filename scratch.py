admin_objects = {'profile': [{'email': 'justinclarkturney@gmail.com',
                              'first_name': 'Justin',
                              'last_name': 'Turney',
                              'picture': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/Apps/profile/base/profiles/default_profile_picture.png',
                              'profiles_id': 1,
                              'username': 'username'},
                             {'email': 'justinclarkturney@gmail.com',
                              'first_name': 'Justin',
                              'last_name': 'Turney',
                              'picture': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/Apps/profile/base/profiles/default_profile_picture.png',
                              'profiles_id': 2,
                              'username': 'username'},
                             {'email': 'justinclarkturney@gmail.com',
                              'first_name': 'Justin',
                              'last_name': 'Turney',
                              'picture': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/Apps/profile/base/profiles/default_profile_picture.png',
                              'profiles_id': 3,
                              'username': 'username'},
                             {'email': 'justinclarkturney@gmail.com',
                              'first_name': 'Justin',
                              'last_name': 'Turney',
                              'picture': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/Apps/profile/base/profiles/default_profile_picture.png',
                              'profiles_id': 4,
                              'username': 'username'}],
                 'user': [{'auth_level': 1,
                           'email': 1,
                           'first_name': 1,
                           'is_verified': 1,
                           'last_name': 1,
                           'username': 1,
                           'users_id': 1},
                          {'auth_level': 6,
                           'email': 6,
                           'first_name': 6,
                           'is_verified': 6,
                           'last_name': 6,
                           'username': 6,
                           'users_id': 6}]}

for key, item in admin_objects.items():
    print('<table class="table">')
    print('<thead>')
    for index, d in enumerate(item):
        print('<tr>')
        for k, v in d.items():
            if index == 0:
                print(f'<th scope="col">{k}</th>')
        print('</tr>')
        print('</thead>')
        print('<tbody>')
        print('<tr>')
        for k, v in d.items():
            if '_id' in k:
                print(f'<th scope="row"><a href="/{key}?id={v}">{v}</a></th>')
            else:
                print(f'<td>{v}</td>')
        print('</tr>')
    print('</tbody>')
    print('</table>')
