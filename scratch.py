import re

sample = """
    <h1>Does this work?</h1>
    <p>Here it goes {% print("Hello, world!")
                        i = 0
                        while i <10:
                        print(i)
    %}</p>
    <p>Let's try here too {% print("Hello, world again!")%}</p>
    <p>And some more text for good measure</p>
"""

# results = re.findall('{%(.*?)%}', sample, re.MULTILINE)
# pattern = re.compile('{%(.*)%}', re.DOTALL)
results = re.findall('(?<={%).*(?=%})', sample, re.DOTALL)
indices = [(m.start(0), m.end(0)) for m in re.finditer('{%(.*)%}', sample)]

for result in results:
    print(result)

print(results)
print(indices)
removed_code = ""
chunk_start = 0
block_count = 0
# for index in indices:
#     removed_code += sample[chunk_start:index[0]]
#     print(removed_code)
#     print(len(removed_code))
#     chunk_start = index[1]
# removed_code += sample[chunk_start:]
# print(removed_code)

import black

mode = black.Mode(

)

for result in results:
    result = str(result)
    print(result)
    print(black.format_str(result, mode=mode))