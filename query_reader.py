import json
def read_search_queries(filename):
    with open(filename, 'r') as file:
        queries = json.load(file)
    return queries
