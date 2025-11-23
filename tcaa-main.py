"""TitanCampus Algorithmic Assitant (TCAA). A Comprehensive GUI application demonstrating various algorithms."""
    
import tkinter as tk 
from tkinter import ttk, messagebox, filedialog, scrolledtext
import heapq
from collections import deque, defaultdict
import time
import os 

class TCAA(tk.Tk):
    """Main application class"""
    
    def __init__(self):
        super().__init__()
        
        self.title("TitanCampus Algorithmic Assistant (TCAA)")
        self.geometry("1000x700")
        
        # Create notebook for tabs 
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Initialize modules 
        self.campus_nav = CampusNavigator(self.notebook)
        self.study_planner = StudyPlanner(self.notebook)
        self.notes_Search = NotesSearchEngine(self.notebook)
        self.algo_info = AlgorithmInfo(self.notebook)
        
        # Add tabs 
        self.notebook.add(self.campus_nav, text="Campus Navigator")
        self.notebook.add(self.study_planner, text="Study Planner")
        self.notebook.add(self.notessearch, text="Notes Search")
        self.notebook.add(self.algo_info, text="Algorithm Info")
        
class CampusNavigator(ttk.Frame):
    """Module 1: Graph Algorithms"""
    
    def __init__(self, parent):
        super().__init__(parent)
        
        # Sample CSUF campus graph 
        self.graph = {
            'Library': {'Student Union': 5, 'Engineering': 3, 'Parking A': 7},
            'Student Union': {'Library': 5, 'Gym': 4, 'Admin': 6},
            'Engineering': {'Library': 3, 'Computer Science': 2, 'Parking B': 5},
            'Computer Science': {'Engineering': 2, 'Student Union': 4},
            'Gym': {'Student Union': 4, 'Parking A': 3}, 
            'Admin': {'Student Union': 6, 'Parking B': 4},
            'Parking A': {'Library': 7, 'Gym': 3}, 
            'Parking B': {'Engineering': 5, 'Admin': 4}
        }
        
        self.locations = list(self.graph.keys())
        
        self.setup_ui()
    
    def setup_ui(self):
        # Title
        title = ttk.Label(self, text="Campus Navigator - Graph Algorithms", 
                          font=('Arial', 14, 'bold'))
        title.pack(pady=10)
    
    # Algorithm selection 
    algo_frame = ttk.LabelFrame(self, text="Select Algorithm")
    algo_frame.pack(fill='x', padx=20, pady=10)
    
    self.algo_var = tk.StringVar(value="BFS")
    algorithms = [
        ("BFS Path", "BFS"), 
        ("DFS + Connectivity", "DFS"), 
        ("Dijkstra Shortest Path", "DIJKSTRA"),
        ("Prim's MST", "PRIM")
    ]
    
    for i, (text, value) in enumerate(algorithms):
        ttk.Radiobutton(algo_frame, text=text, variable=self.algo_var,
                        value=value).grid(row=0, column=i, padx=10, pady=5)
        
    # Location selection 
    loc_frame = ttk.LabelFrame(self, text="Select Locations")
    loc_frame.pack(fill='x', padx=20, pady=10)
    
    ttk.Label(loc_frame, text="Start:").grid(row=0, column=0, padx=5, pady=5)
    self.start_var = tk.StringVar(value=self.locations[0])
    start_combo = ttk.Combobox(loc_frame, textvariable=self.start_var, 
                               values=self.locations, state='readonly', width=20)
    start_combo.grid(row=0, column=1, padx=5, pady=5)
    
    ttk.Label(loc_frame, text="End:").grid(row=0, column=2, padx=5, pady=5)
    self.end_var = tk.StringVar(value=self.locations[-1])
    end_combo = ttk.Combox(loc_frame, textvariable=self.end_var,
                           values=self.locations, state='readonly', width=20)
    end_combo.grid(row=0, column=3, padx=5, pady=5)
    
    # Run button 
    ttk.Button(self, text="Run Algorithm", command=self.run_algorithm,
               style='Accent.TButton').pack(pady=10)
    
    # Results
    result_frame = ttk.LabelFrame(self, text="Results")
    result_frame.pack(fill='both', expand=True, padx=20, pady=10)
    
    self.result_text = scrolledtext.ScrolledText(result_frame, height=15, width=80)
    self.result_text.pack(fill='both', expand=True, padx=5, pady=5)
    

def run_algorithm(self):
    algo = self.algo_var.get()
    start = self.start_var.get()
    end = self.end_var.get()
    
    self.result_text.delete(1.0, tk.END)
    
    start_time = time.time()
    
    if algo == "BFS":
        result = self.bfs_path(start, end)
    elif algo == "DFS":
        result = self.dfs_connectivity(start)
    elif algo == "DIJKSTRA":
        result = self.djikstra_shortest_path(start, end)
    elif algo == "PRIM":
        result = self.prims_mst(start)
        
    elapsed = time.time() - start_time 
    
    self.result_text.insert(tk.END, result)
    self.result_text.insert(tk.END, f"\n\nExecution Time: {elapsed*1000:.4f} ms")
    
def bfs_path(self, start, end):
    """BFS pathfinding algorithm"""
    if start not in self.graph or end not in self.graph:
        return "Invalid locations selected"
    
    queue = deque([(start, [start])])
    visited = {start}
    
    while queue:
        node, path = queue.popleft()
        
        if node == end:
            return f"BFS Path Found!\n\nPath: {' -> '.join(path)}\n\nSteps: {len(path)}"
        
        for neighbor in self.graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
                
    return "No path found"
    
def dfs_connectivity(self, start):
    """DFS with connectivity check"""
    visited = set()
    
    def dfs(node, path):
        visited.add(node)
        path.append(node)
        
        for neighbor in self.graph[node]:
            if neighbor not in visited:
                dfs(neighbor, path)
                
    path = []
    dfs(start, path)
    
    all_nodes = set(self.graph.keys())
    connected = len(visited) == len(all_nodes)
    
    result = f"DFS Traversal from {start}:\n\n"
    result += f"Visited Order: {'->'.join(path)}\n\n"
    result += f"Nodes Reached: {len(visited)}/{len(all_nodes)}\n"
    result += f"Graph is {'CONNECTED' if connected else 'NOT CONNECTED'}"
    
    if not connected:
        unreached = all_nodes - visited 
        result += f"\n\nUnreachable nodes: {', '.join(unreached)}"
        
    return result 

def dijkstra_shortest_path(self, start, end):
    """Dijkstra's shortest path using heap"""
    if start not in self.graph or end not in self.graph:
        return "Invalid locations selected"
    
    distances = {node: float('inf') for node in self.graph}
    distances[start] = 0 
    previous = {node: None for node in self.graph}
    
    heap = [(0, start)]
    visited = set()
    
    while heap:
        current_dist, current = heapq.heappop(heap)
        
        if current in visited:
            continue 
        
        visited.add(current)
        
        if current == end:
            # Reconstruct path 
            path = []
            node = end
            while node:
                path.append(node)
                node = previous[node]
            path.reverse()
            
            return(f"Dijkstra's Shortest Path:\n\n"
                   f"Path: {' -> '.join(path)}\n"
                   f"Total Distance: {distances[end]} units\n"
                   f"Nodes Explored: {len(visited)}")
            
        for neighbor, weight in self.graph[current].items():
            distance = current_dist + weight 
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current 
                heapq.heappush(heap, (distance, neighbor))
                
    return "No path found"

def prims_mst(self, start):
    """Prim's Minimum Spanning Tree algorithm"""
    mst = []
    visited = {start}
    total_weight = 0 
    
    # Edges from start node 
    edges = [(weight, start, neighbor)
             for neighbor, weight in self.graph[start].items()]
    heapq.heapify(edges)
    
    while edges and len(visited) < len(self.graph):
        weight, node1, node2 = heapq.heappop(edges)
        
        if node2 not in visited:
            visited.add(node2)
            mst.append((node1, node2, weight))
            total_weight += weight
            
            # Add new edges 
            for neighbor, w in self.graph[node2].items():
                if neighbor not in visited:
                    heapq.heappush(edges, (w, node2, neighbor))
                    
    result = f"Prim's Minimum Spanning Tree (starting from {start})\n\n"
    result += "Edges in MST:\n"
    for node1, node2, weight in mst:
        result += f" {node1} ↔ {node2}: {weight} units\n"
    result += f"\nTotal Weight: {total_weight} units\n"
    result += f"Nodes in MST: {len(visited)}/{len(self.graph)}"
    
    return result 

class StudyPlanner(ttk.Frame):
    """Module 2: Greedy Scheduling and Dynamic Programming"""
    
    def __init__(self, parent):
        super().__init__(parent)
        self.setup_ui()
        
        
    def setup_ui(self):
        # Title
        title = ttk.Label(self, text="Study Planner - Scheduling & optimization",
                          font=('Arial', 14, 'bold'))
        title.pack(pady=10)
        
        # Algorithm selection 
        algo_frame = ttk.LabelFrame(self, text="Select Algorithm")
        algo_frame.pack(fill='x', padx=20, pady=10)
        
        self.algo_var = tk.StringVar(value="GREEDY")
        ttk.Radiobutton(algo_frame, text="Greedy Scheduling",
                        variable=self.algo_var, value="GREEDY").pack(side='left', padx=20, pady=5)
        ttk.Radiobutton(algo_frame, text="0/1 Knapsack (DP)",
                        variable=self.algo_var,value="KNAPSACK").pack(side='left', padx=20, pady=5)
        
        # Input frame
        input_frame = ttk.LabelFrame(self, text="Input Data")
        input_frame.pack(fill='x', padx=20, pady=10)
        
        # Greedy scheduling inputs 
        self.greedy_frame = ttk.Frame(input_frame)
        self.greedy_frame.pack(fill='x', padx=5, pady=5)
        
        ttk.Label(self.greedy_frame,
                  text="Tasks(format: name, start, end per line):").pack(anchor='w')
        self.tasks_text = scrolledtext.ScrolledText(self.greedy_frame, height=5, width=60)
        self.tasks_text.pack(fill='x', pady=5)
        self.tasks_text.insert(1.0, 
            "Study CPSC335,1,4\nGym,3,5\nProject Meeting,5,7\nRead Chapter5,2,6\nLunch,6,8")
        
        # Knapsack inputs 
        self.knapsak_frame = ttk.Frame(input_frame)
        
        ttk.Label(self.knapsack_frame, 
                  text="Items (format: name, weight, value per line):").pack(anchor='w')
        self.items_text = scrolledtext.ScrolledText(self.knapsack_frame, height=5, width=60)
        self.items_text.pack(fill='x', pady=5)
        self.items_text.insert(1.0, 
            "Algorithms Textbook,2,10\nCalculus Notes,1\nLaptop, 3,15\nNotebook,1,5\nCalculator,1,7")
        
        ttk.Label(self.knapsack_frame, text="Backpack Capacity:").pack(anchor='w', pady=(5,0))
        self.capacity_var = tk.StringVar(value="5")
        ttk.Entry(self.knapsack_frame,textvariable=self.capacity_var, width=10).pack(anchor='w')
        
        # Run button
        ttk.Button(self, text="Run Algorithm", command=self.run_algorithm).pack(pady=10)
        
        # Results
        result_frame = ttk.LabelFrame(self, text="Results")
        result_frame.pack(fill='both', expand=True, padx=20, pady=10)
        
        self.result_text = scrolledtext.ScrolledText(result_frame, height=15, width=80)
        self.result_text.pack(fill='both', expand=True, padx=20, pady=10)
        
        # Show/hide appropriate input frames
        self.algo_var.trace('w', self.toggle_inputs)
        self.toggle_inputs()
        
        
def toggle_inputs(self, *args):
    if self.algo_var.get() == "GREEDY":
        self.greedy_frame.pack(fill='x', padx=5, pady=5)
        self.knapsack_frame.pack_forget()
    else:
        self.greedy_frame.pack_forget()
        self.knapsack_frame.pack(fill='x', padx=5, pady=5)
        
def run_algorithm(self):
    self.result_text.delete(1.0, tk.END)
    
    start_time = time.time()
    
    if self.algo_var.get() == "GREEDY":
        result = self.greedy_scjeduling()
    else:
        result = self.knapsack_dp()
        
    elapsed = time.time() - start_time 
    
    self.result_text.insert(tk.END, result)
    self.result_text.insert(tk.END, f"\n\nExecution Time: {elapsed*1000:.4f} ms")

def greedy_scheduling(self):
    """Greedy interval scheduling algorithm"""
    try: 
        task = []
        for like in self.tasks_text.get(1.0, tk.END).strip().split('\n'):
            if line.strip():
                parts = line.split(',')
                name = parts[0].strip()
                start = int(parts[1].strip())
                end = int(parts[2].strip())
                tasks.append((name, start, end))
                
                
        # Sort by end time (greedy choice)
        tasks.sort(key=lambda x: x[2])
        
        selected = []
        last_end = 0
        
        for name, start, end in tasks:
            if start >= last_end:
                selected.append((name, start, end))
                last_end = end 
                
        result = "Greedy Scheduling (Maximum Non-Overlapping Tasks:\n\n"
        result += f"Total tasks submitted: {len(tasks)}\n"
        result += f"Maximum tasks scheduled: {len(selected)}\n\n"
        result += "Scheduled Tasks:\n"
        for i, (name, start, end) in enumerate(selected, 1):
            result += f"{i}. {name}: {start}:00 - {end}:00\n"
            
        if len(selected) < len(tasks):
            unscheduled = [t[0] for t in tasks if t not in selected]
            result += f"\nUnscheduled (conflicts): {','.join(unscheduled)}"
            
        return result 
    except Exception as e:
        return f"Error parsing input: {str(e)}"
    
def knapsack_dp(self):
    """0/1 Knapsack using Dynamic Programming"""
    try: 
        items = []
        for line in self.items_text.get(1.0, tk.END).strip().split('\n'):
            if line.strip():
                parts = line.split(',')
                name = parts[0].strip()
                weight = int(parts[1].strip())
                value = int(parts[2].strip())
                items.append((name, weight, value))
                
        capacity = int(self.capacity_var.get())
        n = len(items)
        
        # DP table 
        dp = [[0] * (capacity + 1) for _ in range(n + 1)]
        
        # Fill DP table 
        for i in range(1, n + 1):
            name, weight, value = items[i-1]
            for w in range(capacity + 1):
                if weight <= w:
                    dp[i][w] = max(dp[i-1][w], dp[i-1][w-weight] + value)
                else:
                    dp[i][w] = dp[i-1][w]
                    
        # Backtrack to find items 
        selected = []
        w = capacity
        for i in range(n, 0, -1):
            if dp[i][w] != dp[i-1][w]:
                selected.append(items[i-1])
                w -= items[i-1][1]
                
        selected.reverse()
        
        result = "0/1 Knapsack Dynamic Programming:\n\n"
        result += f"Backpack Capacity: {capacity} kg\n"
        result += f"Total items available: {n}\n"
        result += f"Items selected: {len(selected)}\n"
        result += f"Maximum value: {dp[n][capacity]}\n\n"
        total_weight = 0
        for name, weight, value in selected:
            result += f"   • {name}: {weight} kg, value {value}\n"
            total_weight += weight
        result += f"\nTotal Weight: {total_weight}/{capacity} kg"
        
        return result 
    
    except Exception as e:
        return f"Error: {str(e)}"
    
    
class NotesSearchEngine(ttk.Frame):
    """Module 3: String Pattern Matching"""
            
            
        
        
        
        
        
        
        
                
    
        
    