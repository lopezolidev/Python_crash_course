MAX_CONNECTIONS_PER_NODE = 5000
active_nodes, dropped_packets, total_packets = 12, 125, 14_000_000_000

total_connection_capacity = active_nodes * MAX_CONNECTIONS_PER_NODE

# form 1:
packet_loss_ratio = round((dropped_packets / total_packets) * 100, 10)
print(f"Form 1. \n packet loss ratio was: {packet_loss_ratio}%")

# form 2:
print(f"Form 2. \n packet loss ratio: {round((dropped_packets / total_packets) * 100, 10)}%")
