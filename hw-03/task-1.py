from collections import deque


def bfs(capacity_matrix, flow_matrix, source, sink, parent):
    visited = [False] * len(capacity_matrix)
    queue = deque([source])
    visited[source] = True

    while queue:
        current_node = queue.popleft()

        for neighbor in range(len(capacity_matrix)):
            if (
                not visited[neighbor]
                and capacity_matrix[current_node][neighbor]
                - flow_matrix[current_node][neighbor]
                > 0
            ):
                parent[neighbor] = current_node
                visited[neighbor] = True
                if neighbor == sink:
                    return True
                queue.append(neighbor)

    return False


def edmonds_karp(capacity_matrix, source, sink):
    num_nodes = len(capacity_matrix)
    flow_matrix = [[0] * num_nodes for _ in range(num_nodes)]
    parent = [-1] * num_nodes
    max_flow = 0

    while bfs(capacity_matrix, flow_matrix, source, sink, parent):
        path_flow = float("Inf")
        current_node = sink

        while current_node != source:
            previous_node = parent[current_node]
            path_flow = min(
                path_flow,
                capacity_matrix[previous_node][current_node] - flow_matrix[previous_node][current_node],
            )
            current_node = previous_node

        current_node = sink
        while current_node != source:
            previous_node = parent[current_node]
            flow_matrix[previous_node][current_node] += path_flow
            flow_matrix[current_node][previous_node] -= path_flow
            current_node = previous_node

        max_flow += path_flow

    return max_flow


def generate_report(capacity_matrix, terminals, stores):
    terminal_header = "Terminal"
    store_header = "Store"
    flow_header = "Actual Flow"
    col1_width = max(len(terminal_header), max(len(label) for label in terminals.values()))
    col2_width = max(len(store_header), max(len(label) for label in stores.values()))
    report = f"| {terminal_header:^{col1_width}} | {store_header:^{col2_width}} | {flow_header:^{len(flow_header)}} |\n"
    report += "-" * len(report) + "\n"

    for terminal_id, terminal_name in terminals.items():
        for store_id, store_name in stores.items():
            max_flow = edmonds_karp(capacity_matrix, terminal_id, store_id)
            report += f"| {terminal_name:^{col1_width}} | {store_name:^{col2_width}} | {max_flow:^{len(flow_header)}} |\n"

    return report

if __name__ == "__main__":
    capacity_matrix = [
        # Terminals, Warehouses, and Stores (20 nodes in total)
        # Terminal 1, Terminal 2, Warehouses (1-4), Stores (1-14)
        # T1  T2  W1  W2  W3  W4  S1  S2  S3  S4  S5  S6  S7  S8  S9  S10 S11 S12 S13 S14
        [0,  0,  25, 20, 15,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],  # Terminal 1
        [0,  0,   0, 10, 15, 30,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],  # Terminal 2
        [0,  0,   0,  0,  0,  0, 15, 10, 20,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],  # Warehouse 1
        [0,  0,   0,  0,  0,  0,  0,  0,  0, 15, 10, 25,  0,  0,  0,  0,  0,  0,  0,  0],  # Warehouse 2
        [0,  0,   0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 20, 15, 10,  0,  0,  0,  0,  0],  # Warehouse 3
        [0,  0,   0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 20, 10, 15,  5, 10],  # Warehouse 4
        [0,  0,   0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],  # Store 1
        [0,  0,   0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],  # Store 2
        [0,  0,   0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],  # Store 3
        [0,  0,   0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],  # Store 4
        [0,  0,   0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],  # Store 5
        [0,  0,   0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],  # Store 6
        [0,  0,   0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],  # Store 7
        [0,  0,   0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],  # Store 8
        [0,  0,   0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],  # Store 9
        [0,  0,   0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],  # Store 10
        [0,  0,   0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],  # Store 11
        [0,  0,   0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],  # Store 12
        [0,  0,   0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],  # Store 13
        [0,  0,   0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],  # Store 14
    ]

    terminals = {0: "Terminal 1", 1: "Terminal 2"}
    stores = {i: f"Store {i - 5}" for i in range(6, 20)}

    report = generate_report(capacity_matrix, terminals, stores)
    print(report)
