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
    
        
    