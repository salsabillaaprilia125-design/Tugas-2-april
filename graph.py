# Graph menggunakan dictionary

graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C"]
}

print("Graph:", graph)

print("Node A terhubung ke:", graph["A"])