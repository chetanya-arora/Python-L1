bookstore = {
    "New Arrivals": {
        "COOKING": ["Everyday Italian", "Giada De Laurentiis", "2005", "30.00"],
        "CHILDREN": ["Harry Potter", "J K. Rowling", "2005", "29.99"],
        "WEB": ["Learning XML", "Erik T. Ray", "2003", "39.95"],
    }
}
web = "".join(f"'{bookstore['New Arrivals']['WEB']}'")
cooking = "".join(f"'{bookstore['New Arrivals']['COOKING']}'")
children = "".join(f"'{bookstore['New Arrivals']['CHILDREN']}'")
print("BOOKSTORE")
print(web[2:-2])
print(cooking[2:-2])
print(children[2:-2])
