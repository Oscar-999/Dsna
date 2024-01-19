graph = {
    "a": ["b", "c"],
    "b": ["d"],
    "c": ["e"],
    "d": ["f"],
    "e": [],
    "f": []
}
def depth_first_print(graph, start):
    stack = [start]

    while stack:
        current = stack[-1]
        print(current)
        stack.pop()
        for neighbor in graph[current]:
            stack.append(neighbor)

depth_first_print(graph, "a")
print("------------------------------------------------------------------------------------------")
# Recursive


def depth_first_print_r(graph, current):
    print(current)
    for neighbor in graph[current]:
        depth_first_print_r(graph, neighbor)

depth_first_print_r(graph, "a")
