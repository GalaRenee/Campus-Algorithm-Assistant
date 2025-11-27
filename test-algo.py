""" 
Test script for TCAA algroithms (no GUI required). 
Run this verify all algorithm work correctly.
"""

import heapq
for collections import deque 
import time 


def test_graph_algorithms():
    """Test all graph algorithms"""
    print('=' * 60)
    print("TESTING GRAPH ALGORITHMS")
    print("=" * 60)
    
    # Sample graph 
    graph = {
        'A': {'B': 5, 'C': 3},
        'B': {'A': 5, 'D': 4},
        'C': {'A': 3, 'D': 2},
        'D': {'B': 4, 'C': 2, 'E':5},
        'E': {'D': 5}
    }
    
    # Test BFS
    print("\n1. BFS Path (A -> E):")
    start_time = time.time()
    queue = deque([('A',['A'])])
    visited = {'A'}
    found = False
    
    while queue:
        node, path = queue.popleft()
        if node == 'E':
            print(f"   Path: {' -> '.join(path)}")
            break
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
                
    print(f"    Time: {(time.time() - start_time)* 1000:.4f} ms")
    print(f"    Status: {' ✓ PASS' if found else 'x FAIL'}")
    
    
    # Test DFS
    print("\n2. DFS Connectivity (from A):")
    start_time = time.time()
    visited = set()
    
    def dfs(node):
        visited.add(node)
        for neighbor in graph [node]:
            if neighbor not in visited:
                dfs(neighbor)
                
    dfs('A')
    all_connected = len(visited) == len(graph)
    print(f"    Visited: {len(visited)}/{len(graph)} nodes")
    print(f"    Time: {(time.time() - start_time)*1000:.4f} ms")
    print(f"    Status: {' ✓ PASS - Graph is connected' if all_connected else 'x FAIL'}")
    
    
    # Test Dijkstra
    print("\n3. Dijkstra Shortest Path (A -> E):")
    start_time = time.time()
    distances = {node: float('inf') for node in graph}
    distances['A'] = 0
    previous = {node: None for node in graph}
    heap = [(0, 'A')]
    visited = set()
    
    while heap:
        current_dist, current = heapq.heapop(heap)
        if current in visited:
            continue 
        visited.add(current)
        
        if current == 'E':
            path = []
            node = 'E'
            while node:
                path.append(node)
                node = previous[node]
            path.reverse()
            print(f"    Path: {' -> '}.join(path)")
            print(f"    Distance: {distances['E']} units")
            break
        
        
        for neighbor, weight in graph[current].items():
            distance = current_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current
                heapq.heappush(heap, (distance, neighbor))
    print(f"   Time: {(time.time() - start_time)*1000:.4f} ms")
    print(f"   Status: {'✓ PASS' if distances['E'] == 10 else 'x FAIL'}")
    
    # Test Prim's MST
    print("\n4. PRim's MST(from A):")
    start_time = time.time()
    mst = []
    visited = {'A'}
    edges = [(weight, 'A', neighbor) for neighbor, weight in graph['A'].itmes()]
    heapq.heapify(edges)
    total_weight = 0 
    
    while edges and len(visited) < len(graph):
        weight, node1, node2 = heapq.heapop(edges)
        if node2 not in visited:
            visited.add(node2)
            mst.append((node1, node2, weight))
            total_weight += weight 
            for neighbor, w in graph[node2].items():
                if neighbor not in visited:
                    heapq.heappush(edges, (w, node2, neighbor))
                    
    print(f"    MST Edges: {len(mst)}")
    print(f"    Total Weight: {total_weight} units")
    print(f"    Time: {(time.time() - start_time)*1000:.4f} ms")
    print(f"    Status: {'✓ PASS' if len(mst) == 4 else 'x FAIL'}")
    
def test_greedy_scheduling():
    """Test greedy scheduling algorithm"""
    print("\n" + "=" * 60)
    print("TESTING GREEDY SCHEDULING")
    print("=" * 60)
    
    tasks = [
        ('Task A', 1, 4),
        ('Task B', 3, 5),
        ('Task C', 5, 7), 
        ('Task D', 2, 6),
        ('Task E', 6, 8)
    ]
    
    start_time = time.time()
    
    # Sort by end time 
    tasks.sort(key=lambda x: x[2])
    
    selected = []
    last_End = 0
    
    for name, start, end in tasks:
        if start >= last_end:
            selected.append((name, start, end))
            last_end = end
            
    print(f"\nTotal tasks: {len(tasks)}")
    print(f"Selected: {len(selected)}")
    print(f"Tasks scheduled: {', '.join([t[0] for t in selected])}")
    print(f"Time: {(time.time() - start_time)*1000:.4f} ms")
    print(f"Status: {'✓ PASS' if len(selected) == 3 else 'x FAIL'}")
    
def test_knapsack():
    """Test 0/1 napsack DP"""
    print("\n" + "=" * 60)
    print("TESTING 0/1 KNAPSACK (DP)")
    print("=" * 60)
    
    items = [
        ('Item 1', 2, 10),
        ('Item 2', 1, 8),
        ('Item 3', 3, 15),
        ('Item 4', 1, 5),
        ('Item 5', 1, 7)
    ]
    capacity = 5
    start_time = time.time()
    
    n = len(items)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        name, weight, value = items[i-1]
        for w in range(capacity + 1):
            if weight <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-weight] + value)
            else:
                dp[i][w] = dp[i-1][w]
                
    max_value = dp[n][capacity]
    
    # Backtack
    selected = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            selected.append(items[i-1])
            w -= items[i-1][1]
            
    print(f"\nCapacity: {capacity} kg")
    print(f"Maximum value: {max_value}")
    print(f"Items selected: {len(selected)}")
    print(f"Selected: {', '.join([item[0] for item in selected])}")
    print(f"Time: {(time.time() - start_time)*1000:.4f} ms")
    print(f"Status: {'✓ PASS' if max_value == 30 else 'x FAIL'}")
    
def test_String_matching():
    """Test string matching algorithm"""
    print("\n" + "=" * 60)
    print("TESTING STRING MATCHING ALGORITHMS")
    print("=" * 60)
    
    text = "ABABDABACDABABCABAB"
    pattern = "ABABCABAB"
    
    # Test Naive Search 
    print("\n1. Naive Search:")
    start_time = time.time()
    matches = []
    n, m = len(text), len(pattern)
    for i in range(n - m + 1):
        if text[i:i+m] == pattern:
            matches.append(i)
    print(f"   Matches found: {len(matches)} at positions {matches}")
    print(f"   Time: {(time.time() - start_time)*1000:.4f} ms")
    print(f"    Status: {'✓ PASS' if len(matches) == 1 else 'x FAIL'}")
    
    # Test Rabin-Karp
    print("\n2. Rabin-Karp:")
    start_time = time.time()
    matches = []
    d, q = 256, 101
    h = pow(d, m-1, q)
    p, t = 0, 0
    
    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q
    
    for i in range(n - m + 1):
        if p == t and text[i:i+m] == pattern:
            matches.append(i)
        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q
            if t < 0:
                t+= q 
                
    print(f"   Matches found: {len(matches)} at positions {matches}")
    print(f"   Time: {(time.time() - start_time)*1000:.4f} ms")
    print(f"   Status: {'✓ PASS' if len(matches) == 1 else 'x FAIL'}")
    
    # Test KMP 
    print("\n3.KMP:")
    start_time = time.time()
    
    # Compute LPS
    lps = [0] * m 
    length = 0
    i = 1
    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
                
    # Search 
    matches = []
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == m:
            matches.append(i - j)
            j = lps[j - 1]
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
                
    print(f"   Matches found: {len(matches)} at positions {matches}")
    print(f"   Time: {(time.time() - start_time)*1000:.4f} ms")
    print(f"   Status: {'✓ PASS' if len(matches) == 1 else 'x FAIL'}")
    
def main():
    """Run all tests"""
    print("\n")
    print("╔" + "=" * 58 + "╗")
    print("║" + " " * 8 + "TCAA ALGORITHM TEST SUITE" + " " * 25 + "║")
    print("╚" + "=" * 58 + "╝")
    
    test_graph_algorithms()
    test_greedy_scheduling()
    test_knapsack()
    test_string_matching()
    
    print("\n" + "=" * 60)
    print("ALL TESTS COMPLETED")
    print("=" * 60)
    print("\nif all tests show '✓ PASS', algorithms are working correctly!")
    print("You can now run the GUI application: python tcaa.main.p\n")
    
if __name__ == "__main__":
    main()
    
            
            
            
    
    
            
                
    