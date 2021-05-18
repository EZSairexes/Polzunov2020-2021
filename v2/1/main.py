from collections import defaultdict


start_list = [["A", "B", 9], ["A", "C", 5], ["A", "D", 2], ["C", "B", 8], ["B", "F", 1], ["D", "C", 4], ["C", "E", 5], ["C", "F", 16], ["D", "E", 7], ["F", "E", 3]]
abc = {
    "A" : 1,
    "B" : 2,
    "C" : 3,
    "D" : 4,
    "E" : 5,
    "F" : 6,
}
input_list = [ [0 for j in range(3)] for i in range(len(start_list))]

for i in range(len(start_list)):
    for j in range(len(start_list[i])):
        if start_list[i][j] in abc:
            input_list[i][j] = abc.get(start_list[i][j])
        else:
            input_list[i][j] = start_list[i][j]

number_of_elements = 6
source = 1
target = 3


graph = defaultdict(list)
for a, b, cost in input_list:
    graph[a] += [(cost, b)]


nodes_to_visit = []
nodes_to_visit.append((0, source))

visited = set()
min_dist = {i: float('inf') for i in range(1, number_of_elements + 1)}
min_dist[source] = 0

while len(nodes_to_visit):
    cost, node = min(nodes_to_visit)
    nodes_to_visit.remove((cost, node))
    if node in visited:
        continue

    visited.add(node)

    for n_cost, n_node in graph[node]:
       
        if cost + n_cost < min_dist[n_node] and n_node not in visited:
            min_dist[n_node] = cost + n_cost
            nodes_to_visit.append((cost + n_cost, n_node))
            

print(min_dist[target])