import csv
import random
from BTrees.OOBTree import OOBTree
from timeit import timeit

def load_data_from_csv(filename):
    items = []
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            row["ID"] = int(row["ID"])
            row["Price"] = float(row["Price"])
            items.append(row)
    return items

tree = OOBTree()
dictionary = {}

def add_item_to_tree(item):
    tree[item["ID"]] = item

def add_item_to_dict(item):
    dictionary[item["ID"]] = item

def range_query_tree(min_price, max_price):
    return [item for _, item in tree.items() if min_price <= item["Price"] <= max_price]

def range_query_dict(min_price, max_price):
    return [item for item in dictionary.values() if min_price <= item["Price"] <= max_price]

def main():
    items = load_data_from_csv("generated_items_data.csv")
    
    # Додавання елементів до обох структур
    for item in items:
        add_item_to_tree(item)
        add_item_to_dict(item)
    
    # Генерація 100 випадкових запитів по ціні
    queries = [(random.uniform(5, 100), random.uniform(101, 500)) for _ in range(100)]

    # Вимірювання часу виконання запитів для OOBTree
    def tree_queries():
        for min_p, max_p in queries:
            range_query_tree(min_p, max_p)

    # Вимірювання часу виконання запитів для dict
    def dict_queries():
        for min_p, max_p in queries:
            range_query_dict(min_p, max_p)

    tree_time = timeit(tree_queries, number=1)
    dict_time = timeit(dict_queries, number=1)

    print(f"Total range_query time for OOBTree: {tree_time:.6f} seconds")
    print(f"Total range_query time for Dict: {dict_time:.6f} seconds")

if __name__ == "__main__":
    main()
