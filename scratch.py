from NAPyF.TemplateEngine import render

sample = './default/base/templates/index.html'
context = {'title': 'Default',
           'app_name': 'default'}
html_templates = {'head': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/default/base/templates/head.html',
                  'content': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/default/base/templates/index.html',
                  'foot': 'C:\\Users\\jturney\\PycharmProjects\\NAPyF/default/base/templates/foot.html'}
# results = re.findall('{%(.*?)%}', sample, re.MULTILINE)
# pattern = re.compile('{%(.*)%}', re.DOTALL)
# results = re.findall('{%((?:.*?\r?\n?)*)%}', sample)
# indices = [(m.start(0), m.end(0)) for m in re.finditer('{%((?:.*?\r?\n?)*)%}', sample)]
#
# for result in results:
#     print(result)
#
# print(results)
# print(indices)
# removed_code = ""
# chunk_start = 0
# block_count = 0
# for index in indices:
#     removed_code += sample[chunk_start:index[0]]
#     print(removed_code)
#     print(len(removed_code))
#     chunk_start = index[1]
# removed_code += sample[chunk_start:]
# print(removed_code)

# import black
#
# target = {black.TargetVersion.PY39}
#
# mode = black.Mode(target_versions=target)
#
# for result in results:
#     result = str(result).replace("    ", "   ")
#     result = black.format_str(result, mode=mode)
#     exec(result)
context["html_templates"] = html_templates
print(render(context["html_templates"]["content"], context))
