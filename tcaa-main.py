"""TitanCampus Algorithmic Assitant (TCAA). A Comprehensive GUI application demonstrating various algorithms."""
    
import tkinter as tk 
from tkinter import ttk, messagebox, filedialog, scrolledtext, font as tkfont
import heapq
from collections import deque, defaultdict
import time
import os 

class TCAA(tk.Tk):
    """Main application class with styling. Implementing a purple/blue/pink aesthetic."""
    
    def __init__(self):
        """Initialize the styling with a custom theme."""
        super().__init__()
        
        # Color Palette - Blueberry Milk 
        self.colors = {
            'bg_dark': '#0F1729',
            'bg_medium': '#1A2332',
            'bg_light': '#243447',
            'accent_purple': '#B8A9FF',
            'accent_light': '#D4C5FF',
            'accent_blue': '#8B9FE8',
            'accent_pink': '#FFB5D5',
            'accent_peach': '#FFB5D5',
            'accent_mint': '#B5EAD7',
            'text_light': '#E8F0FF', 
            'text_mdeium': '#C8D6E5',
            'text_dark': '#1A1F2E',
            'success': '#7FE7B7',
            'highlight': '#A78BFA',
            'border': '#3D4B5E',
            'border_light': '#4A5A70',
            'card_bg': '#1E2D3E',
            'card_accent': '#2A3A4D',
            'glow': '#E0C3FC',
            'glow_pink': '#FFD6E8',
            'glow_blue': '#C3D9FF',     
        }
        
        
        # Configure main window 
        self.title("✨ Titan Campus Algorithmic Assistant (TCAA) ✨")
        self.geometry("1150x800")
        self.configure(bg=self.colors['bg_dark'])
        
        # Configure combox dropdown colors for better contrast
        self.option_add('*TCombobox*Listbox.background', self.colors['bg_light'])
        self.option_add('*TCombobox*Listbox.foreground', self.colors['text_light'])
        self.option_add('*TCombobox*Listbox.selectBackground', self.colors['accent_purple'])
        self.option_add('*TCombobox*Listbox.selectForeground', self.colors['text_dark'])
        self.option_add('*TCombobox*Listbox.font', ('Segoe UI', 10))
        
        # Apply custom styling 
        self.setup_styles()
        
        # Create notebook for tabs 
        self.notebook = ttk.Notebook(self, style='Custom.TNotebook')
        self.notebook.pack(fill='both', expand=True, padx=20, pady=(0, 20))
        
        # Initialize modules 
        self.campus_nav = CampusNavigator(self.notebook, self.colors)
        self.study_planner = StudyPlanner(self.notebook, self.colors)
        self.notes_Search = NotesSearchEngine(self.notebook, self.colors)
        self.algo_info = AlgorithmInfo(self.notebook, self.colors)
        
        # Add tabs 
        self.notebook.add(self.campus_nav, text="Campus Navigator")
        self.notebook.add(self.study_planner, text="Study Planner")
        self.notebook.add(self.notessearch, text="Notes Search")
        self.notebook.add(self.algo_info, text="Algorithm Info")
        
        # Add footer with personality
        self.create_footer()
        
        
def setup_styles(self):
    """Configure custom ttk styles for modern, cute appearance"""
    style = ttk.Style()
    
    # Using 'clam' theme as the base - most customizable 
    style.theme_use('clam')
    
    # Notebook tabs styling 
    style.configure('Custom.TNotebook',
                    background=self.colors['bg_dark'],
                    borderwidth=0,
                    tabmargins=[5, 5, 5, 0])
    
    style.configure('Custom.TNotebook.Tab',
                    background=self.colors['bg_light'],
                    foreground=self.colors['text_medium'],
                    padding=[24, 12],
                    borderwidth=0,
                    font=('Segoe UI', 10, 'bold'))
    
    style.map('Custom.TNotebook.Tab',
             background=[('selected', self.colors['accent_purple'])],
             foreground=[('selected', self.colors['text_dark'])],
             expand=[('selected', [1, 1, 1, 0])],
             padding=[('selected, [24, 14]')])
    
    # Frame styling 
    style.configure('Card.TFrame',
             background=self.colors['card_bg'],
             borderwidth=2,
             relief='flat')
    
    # LabelFrame styling - enhanced borders
    style.configure('Custom.TLabelframe',
                    background=self.colors['card_bg'],
                    foreground=self.colors['text_light'],
                    borderwidth=2,
                    relief='flat',
                    bordercolor=self.colors['border_light'])
    
    style.configure('Custom.TLabelframe.Label',
                    background=self.colors['card_bg'],
                    foreground=self.colors['accent_purple'],
                    font=('Segoe UI', 11, 'bold'))
    
    # Button styling 
    style.configure('Accent.TButton', 
                    background=self.colors['accent_purple'],
                    borderwidth=0,
                    focuscolor='none',
                    padding=[24, 12],
                    font=('Segoe UI', 10, 'bold'))
    
    style.map('Accent.TButton', 
              background=[('active', self.colors['accent_pink']),
                          ('presed', self.colors['accent_blue'])],
              foreground=[('active', self.colors['text_dark'])])
    
    # Secondary button - with border accent
    style.configure('Secondary.TButton',
                    background=self.colors['bg_medium'],
                    foreground=self.colors['text_light'],
                    borderwidth=2, 
                    bordercolor=self.colors['accent_purple'],
                    focuscolor='none',
                    padding=[18, 18],
                    font=('Segoe UI', 9, 'bold'))
    
    style.map('Secondary.TButton',
              background=[('active', self.colors['accent_light'])],
              foreground=[('active', self.colors['text_dark'])],
              bordercolor=[('active', self.colors['accent_pink'])])
    
    # Special action button 
    style.configure('Special.TButton',
                    background=self.colors['accent_pink'],
                    foreground=self.colors['text_dark'],
                    borderwidth=0,
                    focuscolor='none',
                    padding=[20, 20],
                    font=('Segoe UI', 10, 'bold'))
    
    style.map('Special.TButton',
              background=[('active', self.colors['accent_peach']),
                          ('pressed', self.colors['accent_mint'])])
    
    # Label styling 
    style.configure('Custom.TLabel', 
                    background=self.colors['card_bg'], 
                    foreground=self.colors['text_light'],
                    font=('Segoe UI', 10))
    
    style.configure('Title.TLabel',
                    background=self.colors['bg_dark'],
                    foreground=self.colors['accent_purple'],
                    font=('Segoe UI', 16, 'bold'))
    
    style.configure('Subtitle.TLabel',
                    background=self.colors['bg_dark'],
                    foreground=self.colors['accent_light'],
                    font=('Segoe UI', 10))
    
    # Radio button styling 
    style.configure('Custom.TRadiobutton',
                    background=self.colors['card_bg'],
                    foreground=self.colors['text_light'],
                    font=('Segoe UI', 10), 
                    borderwidth=0, 
                    focuscolor=self.colors['accent_purple'])
    
    style.map('Custom.TRadiobutton', 
              background=[('active', self.colors['card_bg'])],
              indicatorcolor=[('selected', self.colors['accent_pink'])],
              foreground=[('active', self.colors['accent_purple'])])
    
    # Combobox styling - improved contrast
    style.configure('Custom.TCombobox', 
                    fieldbackground=self.colors['bg_light'],
                    background=self.colors['accent_purple'],
                    foreground=self.colors['text_light'], 
                    arrowcolor=self.colors['text_light'], 
                    arrowcolor=self.colors['text_light'], 
                    arrowcolor=self.colors['text_light'],
                    arrowcolor=self.colors['text_light'], 
                    borderwidth=2, 
                    relief='flat')
    
    style.map('custom.TCombobox', 
              fieldbackground=[('readonly', self.colors['bg_light'])], 
              foreground=[('readonly', self.colors['text_light'])], 
              selectbackground=[('readonly', self.colors['accent_purple'])],
              selectforeground=[('readonly', self.colors['text_dark'])])
    
    # Addional combobox dropdown styling 
    self.option_add('*TCombobox*Listbox.font', ('Segoe UI', 10))
    self.option_add('*TCombobox*Listbox.background', self.colors['bg_light'])
    self.option_add('*TCombobox*Listbox.foreground', self.colors['text_light'])
    self.option_add('*TCombobox*Listbox.selectBackground', self.colors['accent_purple'])
    self.option_add('*TCombobox*Listbox.selectForeground', self.colors['text_dark'])
    
def create_header(self):
    """Create a styled header with decorative elements"""
    # Header container with border accent 
    header_container = tk.Frame(self, bg=self.colors['bg_dark'])
    header_container.pack(fill='x', padx=20, pady=(20, 10))
    
    # Top decorative line 
    top_border = tk.Frame(header_container, bg=self.colors['accent_purple'], height=3)
    top_border.pack(fill='x')
    
    # Main header frame 
    header_frame = tk.Frame(header_container, bg=self.colors['bg_medium'], height=100)
    header_frame.pack(fill='x', pady=3)
    header_frame.pack_propagrate(False)
    
    # Left decorative accent 
    left_accent = tk.Frame(header_frame, bg=self.colors['accent_pink'], width=5)
    left_accent.pack(side='left', fill='y')
    
    # Content frame 
    content_frame = tk.Frame(header_frame, bg=self.colors['bg_medium'])
    content_frame.pack(side='left', fill='both', expand=True, padx=20)
    
    # Title with gradient effect 
    title_frame = tk.Frame(content_frame, bg=self.colors['bg_medium'])
    title_frame.pack(pady=(15, 5))
    
    title_font = tk.font.Font(family='Segoe UI', size=22, weight='bold')
    title = tk.Label(title_frame, 
                     text="✨ Titan Campus Algorithmic Assistant ✨",
                     font=title_font,
                     bg=self.colors['bg_medium'],
                     fg=self.colors['accent_purple'])
    title.pack()
    
    # Decorative subtitle divider 
    divider_frame = tk.Frame(content_frame, bg=self.colors['bg_medium'])
    divider_frame.pack(pady=3)
    
    tk.Frame(divider_frame, bg=self.colors['accent_pink'], width=40, height=2).pack(side='left', padx=3)
    tk.Frame(divider_frame, bg=self.colors['accent_purple'], width=40, height=2).pack(side='left', padx=3)
    tk.Frame(divider_frame, bg=self.colors['accent_blue'], width=40, height=2).pack(side='left', padx=3)
    tk.Frame(divider_frame, bg=self.colors['accent_mint'], width=40, height=2).pack(side='left', padx=3)
    
    # Subtitle with icons 
    subtitle = tk.Label(content_frame, 
                        text=" Graph Algorithms • Dynamic Programming • String Matching • Complexity Analysis", 
                        font=('Segoe UI', 9), 
                        bg=self.colors['bg_medium'],
                        fg=self.colors['text_medium'])
    subtitle.pack()
    
    # Right decorative accent 
    right_accent = tk.Frame(header_frame, bg=self.colors['accent_mint'], width=5)
    right_accent.pack(side='right', fill='y')
    
    # Bottom decorative line (gradient effect)
    bottom_frame = tk.Frame(header_container, bg=self.colors['bg_dark'], height=3)
    bottom_frame.pack(fill='x')
    
    graident_colors = [self.colors['accent_mint'], self.colors['accent_blue'],
                       self.colors['accent_purple'], self.colors['accent_pink']]
    for color in gradient_colors:
        tk.Frame(bottom_frame, bg=color, height=3).pack(side='left', fill='both', expand=True)
        
def create_footer(self):
    """Create a cute footer with more info"""
    footer_frame = tk.Frame(self, bg=self.colors['bg_dark'], height=30)
    footer_frame.pack(fill='x', padx=20, pady=(0, 15))
    footer_frame.pack_propagate(False)
    
    # Decorative top line 
    top_line = tk.Frame(footer_frame, bg=self.colors['border'], height=1)
    top_line.pack(fill='x', pady=(0, 8))
    
    # Decorative top line 
    top_line = tk.Frame(footer_frame, bg=self.colors['border'], height=1)
    top_line.pack(fill='x', pady=(0, 8))
    
    # Footer content 
    footer_text = tk.Label(footer_frame, 
        text="💫 Made with algorithms & aesthetic vibes ✨ CPSC 335 Final Project 🎓 ",
        font=('Segoe UI', 8),
        bg=self.colors['bg_dark'],
        fg=self.colors['text_medium'])
    footer_text.pack()
    
    
class CampusNavigator(ttk.Frame):
    """Module 1: Graph Algorithms"""
    
    def __init__(self, parent, colors):
        """Initialize Campus Navigator"""
        super().__init__(parent)
        self.colors = colors
        self.configure(style='Card.TFrame')
        
        # Campus graph 
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
        
        self.setup_ui()
    
    def setup_ui(self):
        """ Styled UI components with enhanced visuals"""
        # Main container with padding 
        main_container = tk.Frame(self, bg=self.colors['bg_dark'])
        main_container.pack(fill='both', xpand=True, padx=25, pady=25)
        
        
        # Title
        title_frame = tk.Frame(main_container, bg=self.colors['bg_dark'])
        title_frame.pack(fill='x', pady=(0, 20))
        
        
        title = ttk.Label(title_frame, 
            text=" Campus Navigation System",
            font=('Segoe UI', 15, 'bold'),
            bg=self.colors['bg_dark'],
            fg=self.colors['accent_purple'])
        title.pack(side='left')
        
        # Cute subtitle 
        subtitle = tk.Label(title_frame, 
            text=" Find your way around campus!", 
            font=('Segoe UI', 9),
            bg=self.colors['bg_dark'],
            fg=self.colors['accent_pink'])
        subtitle.pack(side='left', padx=(10, 0))
        
        # Controls frame with glow effect
        glow_outer = tk.Frame(main_container, bg=self.colors['glow_pink'], padx=1, pady=1)
        glow_outer.pack(fill='x', pady=(0, 15))
        
        controls_outer = tk.Frame(glow_outer, bg=self.colors['accent_purple'], padx=2, pady=2)
        controls_outer.pack(fill='x')
        
        controls_frame = ttk.LabelFrame(controls_outer, 
            text=" 🎯 Select Locations", 
            style='Custom.TLabelframe',
            padding=20)
        controls_frame.pack(fill='x')
        
        # Use grid layout for perfect alignment 
        controls_frame.grid_columnconfigure(1, weight=1)
        
        # Start location 
        start_label = tk.Label(controls_frame, 
            text="📍 Starting Point:",
            font=('Segoe UI', 10, 'bold'),
            bg=self.colors['card_bg'],
            fg=self.colors['accent_pink'],
            width=18,
            anchor='w')
        start_label.grid(row=0, column=0, sticky='w', padx=(0, 10), pady=8)
        
        # End location 
        end_label = tk.Label(controls_frame, 
            text=" 🎯 Destination:",
            font=('Segoe UI', 10, 'bold'),
            bg=self.colors['card_bg'], 
            fg=self.colors['accent_mint'],
            width=18,
            anchor='w')
        end_label.grid(row=1, column=0, sticky='w', padx=(0, 10), pady=8)
        
        self.end_var = tk.StringVar(value=self.locations[-1])
        end_menu = ttk.Combobox(controls_frame, 
            textvariable=self.end_var, 
            values=self.locations, 
            state='readonly',
            width=30, 
            font=('Segoe UI', 10),
            style='Custom.TCombobox')
        end_menu.grid(row=1, column=1, sticky='ew', pady=8)
            
    
    # Algorithm selection with buttons 
    algo_frame = ttk.LabelFrame(main_container, 
        text=" Choose Your Algorithm",
        style='Custom.TButtonframe',
        padding=15)
    algo_frame.pack(fill='x', pady=(0, 15))
    
    self.algo_var = tk.StringVar(value="BFS")
    
    # Create radio button frame with decorative elements 
    radio_container = tk.Frame(algo_frame, bg=self.colors['card_bg'])
    radio_container.pack(fill='x')
    
    algorithms = [
        (' 🔵 BFS - Breadth-First Search', 'bfs', self.colors['accent_blue']),
        (' 🌳 DFS - Depth-First Search', 'dfs', self.colors['accent_mint']),
        (' ⚡ Dijkstra - Shortest Weighted Path', 'dijkstra', self.colors['accent_purple']),
        (' 🌉 Prim\'s MST - Minimum Spanning Tree', 'prim', self.colors['accent_pink'])   
    ]
    
    
    for i, (text, value, color) in enumerate(algorithms):
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
    
    def __init__(self, parent):
        super().__init__(parent)
        self.document_text = ""
        self.setup_ui()
        
    def setup_ui(self):
        # Title
        title = ttk.Label(self, text="Notes Search Engine - String Pattern Matching",
                          font=('Arial', 14, 'bold'))
        title.pack(pady=10)
        
        # File upload
        upload_frame = ttk.LabelFrame(self, text="Document Upload")
        upload_frame.pack(fill='x', padx=20, pady=10)
        
        ttk.Button(upload_frame, text="Upload TXT/PDF/DOCX",
                   command=self.upload_file).pack(side='left', padx=10, pady=5)
        self.file_label = ttk.Label(upload_frame, text="No file loaded")
        self.file_label.pack(side='left', padx=10)
        
        # Search input 
        search_frame = ttk.LabelFrame(self, text="Search Pattern")
        search_frame.pack(side='left', padx=10)
        
        ttk.Button(upload_frame, text="Upload TXT/PDF/DOCX",
                   command=self.upload_file).pack(side='left', padx=10, pady=5)
        self.file_label = ttk.Label(upload_frame, text="No file loaded")
        self.file_label.pack(side='left', padx=10)
        
        
        # Search input 
        search_frame = ttk.LabelFrame(self, text="Search Pattern")
        search_frame.pack(fill='x', padx=20, pady=10)
        
        ttk.Label(search_frame, text="Pattern to search:").pack(side='left', padx=5)
        self.pattern_var = tk.StringVar()
        ttk.Entry(search_frame, textvariable=self.pattern_var, width=30).pack(side='left', padx=5)
        
        
        # Algorithm selection
        algo_frame = ttk.LabelFrame(self, text="Search Algorithm")
        algo_frame.pack(fill='x', padx=20, pady=10)
        
        self.algo_var = tk.StringVar(value="NATIVE")
        ttk.Radiobutton(algo_frame, text="Native Search",
                        variable=self.algo_var, value="NAIVE").pack(side='left', padx=15, pady=5)
        ttk.Radiobutton(algo_frame, text="Rabin-Karp",
                        variable=self.algo_var, value="RABIN").pack(side='left', padx=15, pady=5)
        ttk.Radiobutton(algo_frame, text="KMP",
                        variable=self.algo_var, value="KMP").pack(side='left', padx=15, pady=5)
        ttk.Radiobutton(algo_frame, text="Compare All", 
                        variable=self.algo_var, value="COMPARE").pack(side='left', padx=15, pady=5)
        
        # Search button 
        ttk.Button(self, text="Search", command=self.search).pack(pady=10)
        
        # Results 
        result_frame = ttk.LabelFrame(self, text="Search Results")
        result_frame.pack(fill='both', expand=True, padx=20, pady=10)
        
        self.result_text = scrolledtext.ScrolledText(result_frame, height=15, width=80)
        self.result_text.pack(fill='both', expand=True, padx=5, pady=5)
        
def upload_file(self):
    """Upload and read document"""
    filename = filedialog.askopenfilename(
        title="Select a file",
        filetypes=[("Text files", "*.txt"), ("PDF files", "*.pdf"),
                   ("Word files", "*.docx"), ("All files", "*.*")]
    )
    
    if filename:
        try: 
            if filename.endswith('.txt'):
                with open(filename, 'r', encoding='utf-8') as f:
                    self.document_text = f.read()
            elif filename.endswith('.pdf'):
                self.document_text = "PDF support: Use sample text for demo."
                self.document_text = """Sample course notes for Algorithm Engineering. 
                Topics include: sorting algorithms, graph algorithms, dynamic programming,
                greedy algorithms, string matching, and complexity analysis."""
            else:
                self.document_text = "DOCX support: use sample text for demo."
                self.document_text = """Algorithm Engineering Course Notes
                Chapter 1: Introduction to Algorithms
                Chapter 2: Sorting and Searching
                Chapter 3: Graph Algorithms"""
                
            self.file_label.config(text=f"Loaded: {os.path.basename(filename)}")
            messagebox.showinfo("Success", "File loaded successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load file: {str(e)}")
            
def search(self):
    """Run selected search algorithm"""
    if not self.document_text:
        messagebox.showwarning("No Document", "Please upload a document first!")
        return 
    
    pattern = self.pattern_var.get()
    if not pattern:
        messagebox.showwarning("No Pattern", "Please enter a search pattern!")
        return 
    
    self.result_text.delete(1.0, tk.END)
    
    if self.algo_var.get() == "COMPARE":
        self.compare_algorithms(pattern)
    else:
        start_time = time.time()
        
        if self.algo_var.get() == "NATIVE":
            matches = self.naive_search(self.document_text, pattern)
            algo_name = "Naive Search"
        elif self.algo_var.get() == "RABIN":
            matches = self.rabin_karp_search(self.document_text, pattern)
            algo_name = "Rabin-Karp"
        else: # KMP
            matches = self.kmp_search(self.document_text, pattern)
            algo_name = "KMP (Knuth-Morris-Pratt)"
            
        elapsed = time.time() - start_time
        
        result = f"{algo_name} Results:\n\n"
        result += f"Pattern: '{pattern}'\n"
        result += f"Matches found: {len(matches)}\n"
        result += f"Execution time: {elapsed*1000:.4f} ms\n\n"
        
        if matches:
            result += "Match positions:\n"
            for i, pos in enumerate(matches[:10], 1): # Shows first 10
                context_start = max(0, pos - 20)
                context_end = min(len(self.document_text), pos + len(pattern) + 20)
                context = self.document_text[context_start:context_end]
                result += f"{i}. Position {pos}: ...{context}...\n"
                
            if len(matches) > 10:
                result += f"\n... and {len(matches) - 10} more matches"
                
        self.result_text.insert(tk.END, result)
        

def naive_search(self, text, pattern):
    """Naive string search"""
    matches = []
    n, m = len(text), len(pattern)
    
    for i in range(n - m + 1):
        if text[i:i+m] == pattern:
            matches.append(i)
            
    return matches 

def rabin_karp_search(self, text, pattern):
    """Rabin-Karp string search"""
    matches = []
    n, m = len(text), len(pattern)
    d = 256 # number of characters
    q = 101 # prime number 
    
    h = pow(d, m-1, q)
    p = 0 # hash of pattern
    t = 0 # hash of text
    
    # Calculate initial hash
    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q
        
    # Slide pattern over text
    for i in range(n - m + 1):
        if p == t:
            # Hash match, verify actual string 
            if text[i:i+m] == pattern:
                matches.append(i)
                
        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q
            if t < 0:
                t += q
                
    return matches 

def kmp_search(self, text, pattern):
    """KMP string search"""
    matches = []
    n, m = len(text), len(pattern)
    
    # Compute LPS array
    lps = self.compute_lps(pattern)
    
    i = 0 # index for text
    j = 0 # index for pattern 
    
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
                
    return matches 

def compute_lps(self, pattern):
    """Compute Longest Proper Prefix which is also Suffix"""
    m = len(pattern)
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
                
    return lps

def compare_algorithms(self, pattern):
    """Compare all three algorithms"""
    results = []
    
    for algo_name, search_func in [
        ("Naive Search", self.naive_search),
        ("Rabin-Karp", self.rabin_karp_search),
        ("KMP", self.kmp_search)
    ]:
        start_time = time.time()
        matches = search_func(self.document_text, pattern)
        elapsed = time.time() - start_time
        results.append((algo_name, len(matches), elapsed))
        
    output = "Algorithm Comparison:\n\n"
    output += f"Pattern: '{pattern}'\n"
    output += f"Document length: {len(self.document_text)} characters\n\n"
    output += f"{'Algorithm':<20} {'Matches':<10} {'Time (ms)':<15}\n"
    output += "-" * 50 + "\n"
    
    for name, matches, time_taken in results:
        output += f"{name:<20} {matches:<10} {time_taken*1000:>10.4f} ms\n"
        
        # Find fastest
        fastest = min(results, key=lambda x: x[2])
        output += f"{name:<20} {matches:<10} {time_taken*1000:>10.4f} ms\n"
        
        self.result_text.insert(tk.END, output)
        
class AlgorithmInfo(ttk.Frame):
    """Module 4: Algorithm Information and Complexity Analysis"""
    
    def __init__(self, parent):
        super().__init__(parent)
        self.setup_ui()
        
    def setup_ui(self):
        
        # Title
        title = ttk.Label(self, text="Algorithm Information & Complexity Analysis",
                          font=('Arial', 14, 'bold'))
        title.pack(pady=10)
        
        # Create notebook for sub-sections
        notebook = ttk.Notebook(self)
        notebook.pack(fill='both', expand=True, padx=20, pady=10)
        
        # Time Complexities tab 
        complexity_frame = ttk.Frame(notebook)
        notebook.add(complexity_frame, text="Time Complexities")
        
        complexities_text = scrolledtext.ScrolledText(complexity_frame, wrap=tk.WORD)
        complexity_text.pack(fill='both', expand=True, padx=10, pady=10)
        
        complexity_info = """TIME COMPLEXITY ANALYSIS"""
        


        
        
        
        
        
        
                
    
        
    