def name(**n):
    print(f"name is {n}")
    print(f"name is {n["name2"]}")

name(name3="abc", name1="cde", name2="hij")