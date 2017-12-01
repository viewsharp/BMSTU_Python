ivan = {
    "name": "ivan",
    "age": 34,
    "children": [{
        "name": "vasja",
        "age": 102,
    }, {
        "name": "petja",
        "age": 102,
    }]
}

darja = {
    "name": "darja",
    "age": 41,
    "children": [{
        "name": "kirill",
        "age": 211,
    }, {
        "name": "pavel",
        "age": 151,
    }]
}

emps = [ivan, darja]

for e in emps:
    for child in e["children"]:
        if child["age"] >= 18:
            print(e["name"])
            break
