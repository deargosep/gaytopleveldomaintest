from tinydb import TinyDB, Query
import json
db = TinyDB('db.json')

with open('ok_list.json', 'w', encoding='utf-8') as f:
    data = db.all()
    json.dump(data, f, ensure_ascii=False, indent=4)
