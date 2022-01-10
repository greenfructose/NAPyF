def unslug(string):
    string = string.replace('_', " ")
    string = string.replace('-', " ")
    space_indexes = [i for i, ltr in enumerate(string) if ltr == ' ']
    string = string[0].upper() + string[1:]
    for index in space_indexes:
        string = string[:index + 1] + string[index + 1].upper() + string[index + 2:]
    return string


def slug_to_path(slug):
    slug = slug.replace('-', '/')
    slug = slug.replace('_', '/')
    return slug
