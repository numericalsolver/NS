# Take Pixel Data Input from User
pixel_data = []
n = int(input("Enter the number of wire connections: "))
for _ in range(n):
    x1, y1, x2, y2 = map(int, input("Enter x1, y1, x2, y2 for wire connection (separated by space): ").split())
    pixel_data.append((x1, y1, x2, y2))

# Take Components Data Input from User
components_data = []
m = int(input("Enter the number of components: "))
for _ in range(m):
    symbol = input("Enter symbol for component (e.g., cap, voltage, res): ")
    x, y = map(int, input("Enter x, y coordinates for component (separated by space): ").split())
    rotation = int(input("Enter rotation in degrees for component: "))
    inst_name = input("Enter instance name for component: ")
    value = input("Enter value for component: ")
    components_data.append((symbol, x, y, rotation, inst_name, value))

# Initialize Graph and Components Dictionary
graph = {}
components = {}

# Process Pixel Data
for (x1, y1, x2, y2) in pixel_data:
    node1 = f"({x1},{y1})"
    node2 = f"({x2},{y2})"
    
    if node1 not in graph:
        graph[node1] = []
    if node2 not in graph:
        graph[node2] = []
    
    graph[node1].append(node2)
    graph[node2].append(node1)

# Process Components Data
for (symbol, x, y, rotation, inst_name, value) in components_data:
    node = f"({x},{y})"
    components[node] = {
        "symbol": symbol,
        "rotation": rotation,
        "inst_name": inst_name,
        "value": value
    }

# Apply Kirchhoff's Voltage Law (KVL)
def apply_kvl(graph, components):
    loops = find_loops(graph)
    
    for idx, loop in enumerate(loops):
        print(f"Loop {idx + 1}:")
        voltage_sources = [node for node in loop if components.get(node, {}).get("symbol") == "voltage"]
        
        if not voltage_sources:
            print("No voltage source found in this loop.")
            continue
        
        total_voltage = sum(components[node]["value"] for node in voltage_sources)
        total_voltage -= sum(components[node]["value"] for node in loop if components.get(node, {}).get("symbol") == "res")
        
        print(f"Total Voltage in Loop {idx + 1}: {total_voltage}V")

def find_loops(graph):
    visited = set()
    loops = []

    def dfs(node, start_node, path):
        visited.add(node)
        path.append(node)

        for neighbor in graph[node]:
            if neighbor == start_node and len(path) > 2:
                loops.append(path.copy())
            elif neighbor not in visited:
                dfs(neighbor, start_node, path)
        
        path.pop()
        visited.remove(node)

    for node in graph:
        dfs(node, node, [])

    return loops

apply_kvl(graph, components)
