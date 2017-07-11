import json



s_dict = '{"name": "jim", "age": 23}' # 注意：字典里的字符串必须是双引号

# loads() 用于将字典、列表、元组形式的字符串，转换成相应的字典、列表、元组
result = json.loads(s_dict)

print result

# dumps() 将基本数据类型转换成字符串