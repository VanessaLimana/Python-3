import json

data = {
    'nome' : 'vanessa',
    'idade' : 30,
    'peso' : 70
}
json_str = json.dumps(data)
print(json_str) # transormação da estrutura de dados em json
print(type(json_str))
data = json.loads(json_str) # # transormação da estrutura de json de volta para estutura de dados py
print(data)
print(type(data))