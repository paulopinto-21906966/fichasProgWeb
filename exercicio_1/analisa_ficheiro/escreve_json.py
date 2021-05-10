import json

pessoa_dict = {
    "nome": "Pedro",
    "linguas": ["Portugues", "Espanhol"],
    "casado": True,
    "esposa": "Ines",
    "idade": 32,
    "filhos": {
        "Afonso": 12,
        "Beatriz": 10,
        "Joao": 7,
        "Diniz": 4
    }
}

with open('pessoa.json', 'w') as json_file:
    json.dump(pessoa_dict, json_file, indent=4)
