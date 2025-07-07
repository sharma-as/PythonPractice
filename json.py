import json
data = '{"var1":"ashu","var2":"ashu2", "var3":"ashu3"}'
print(data)

parsed = json.loads(data)
print(parsed['var1'])