# Name: Gala Ferdoaus 
# Date: 11/23/25

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
        self.notebook.add(self.notes_Search, text="Notes Search")
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
    
    gradient_colors = [self.colors['accent_mint'], self.colors['accent_blue'],
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
           radio_frame = tk.Frame(radio_container, bg=self.colors['card_bg'])
           radio_frame.pack(side='left', fill='x', expand=True, padx=5)
        
           # Decorative accent bar with glow 
           accent_container = tk.Frame(radio_frame, bg=color, width=4, height=22)
           accent_container.pack(side='left', padx=(0, 8))
        
        
           ttk.Radiobutton(radio_frame,
               text=text,
               variable=self.algo_var,
               value=value,
               style='Custom.TRadiobutton').pack(side='left')
        
        button_frame = tk.Frame(main_container, bg=self.colors['bg_dark'])
        button_frame.pack(fill='x', pady=(0, 15))
        # Location selection 
    
        # Main action button with glow 
        main_btn_glow = tk.Frame(button_frame, bg=self.colors['glow_pink'], padx=2, pady=2)
        main_btn_glow.pack(side='left', padx=5)
    
        ttk.Button(main_btn_glow,
           text="🚀 Find Path!",
           command=self.reset_display,
           style='Secondary.TButton').pack()
    
        # Secondary buttons 
        ttk.Button(main_btn_glow,
           text= " Reset",
           command=self.reset_display,
           style='Accent.TButton').pack()
    
        # Decorative sparkles 
        sparkle_frame = tk.Frame(button_frame, bg=self.colors['bg_dark'])
        sparkle_frame.pack(side='left', padx=(20, 0))
    
        sparkles = ['✨', '💫', '⭐']
        for sparkle in sparkles:
            tk.Label(sparkle_frame:
                text=sparkle,
                font=('Segoe UI', 10), 
                bg=self.colors['bg_dark'],
                fg=self.colors['accent_light']).pack(side='left', padx=2)
        
        # Results display with gradient border 
        results_gradient = tk.Frame(main_container, bg=self.colors['bg_dark'], height=3)
        results_gradient.pack(fill='x')
    
        gradient_colors = [self.colors['accent_mint'], self.colors['accent_blue'], 
                           self.colors['accent_purple'], self.colors['accent_pink']]
        for color in gradient_colors:
             tk.Frame(results_gradient, bg=color, height=3).pack(side='left', fill='both', expand=True)
    
        results_outer = tk.Frame(main_container, bg=self.colors['accent_light'], padx=2, pady=2)
        results_outer.pack(fill='both', expand=True)
        
        results_inner = tk.Frame(main_container, bg=self.colors['accent_light'], padx=2, pady=2)
        results_inner.pack(fill='both', expand=True)
    
        results_label = tk.Label(results_label, 
            text= " Results & Path Visualization", 
            font=('Segoe UI', 11, 'bold'), 
            bg=self.colors['card_bg'], 
            fg=self.colors['accent_purple'])
        results_label.pack(side='left')
    
        # Decorative dots 
        dots_frame = tk.Frame(results_label, bg=self.colors['card_bg'])
        dots_frame.pack(side='right')
    
        dots_colors = [self.colors['accent_pink'], self.colors['accent_purple'], self.colors['accent_mint']]
        for color in dots_colors:
            tk.Label(dots_frame, 
                    text="●", 
                    font=('Segoe UI', 12),
                    bg=self.colors['card_bg'],
                    fg=color).pack(side='left', padx=3)
        
            self.results_text = scrolledtext.ScrolledText(results_inner,
                wrap=tk.WORD, 
                font=('Consolas', 10),
                bg=self.colors['bg_light'],
                fg=self.colors['text_light'],
                relief='flat', 
                padx=20, 
                pady=20,
                insertbackground=self.colors['accent_purple'])
            self.results_text.pack(fill='both', expand=True, padx=15, pady=(0, 15))
        
            # Add welcome message 
            welcome_msg = """
╔═════════════════════════════════════════════════════╗
║          ✨ Welcome to Campus Navigator! ✨          ║
╚═════════════════════════════════════════════════════╝
        
     Choose your starting point and destination above 
   Select an algorithm to use for pathfinding
      Click "Find Path!" to discover the best route 
            
Available Algorithms:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔵 BFS     - Finds shortest path (unweighted)
🌳 DFS     - Explores depth-first through graph
⚡ Dijkstra - Optimal weighted shortest path 
🌉 Prim      - Creates minimum spanning tree 
               
Ready to navigate? Let's go! 💫
        """
        self.results_text.insert(1.0, welcome_msg)
    
        def find_path(self):
            """Execute selected pathfinding algorithm with styling output"""
            start = self.start_var.get()
            end = self.end_var.get()
            algo = self.algo_var.get()
        
            if start == end:
                messagebox.showwarning("⚠️ Same Location",
                        "You're already at your destination!🎯")
                return 
        
                self.results_text.delete(1.0, tk.END)
        
            # Header with cute formatting 
            header = f"""
╔═════════════════════════════════════════════════════╗
║          🗺️ PATHFINDING RESULTS 🗺️                   ║
╚═════════════════════════════════════════════════════╝

📍  Start: {start}
🎯  Goal: {end}
⚡   Algorithm: {algo.upper()}
               
"""
        self.results_text.insert(tk.END, header)
          
        start_time = time.time()
          
        if algo == 'bfs':
            result = self.bfs(start, end)
        elif algo == 'dfs':
            result = self.dfs(start, end)
        elif algo == 'dijkstra':
            result = self.dijkstra(start, end)
        else: # prim
            result = self.prim_mst(start)
        
        elapsed = (time.time() - start_time) * 1000
    
        self.results_text.insert(tk.END, result)
        self.results_text.insert(tk.END, f"\n{'━'*59}\n")
        self.results_text.insert(tk.END, f"⏱️  Execution Time:{elapsed:.2f}ms\n")
        self.results_text.insert(tk.END, f"{'━'*59}\n")
    
    def bts(self, start, goal):
       """BFS algorithm with styled output"""
       queue = deque([(start, [start])])
       visited = {start}
    
       result = "🔵 BREADTH-FIRST SEARCH (BFS)\n"
       result += "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
       result += "🔍  Exploration Order:\n"
    
       step = 1
       while queue:
           current, path = queue.popleft()
           result += f"    Step {step}: {current}\n"
           step += 1
        
           if current == goal:
               result += f"\n✅ PATH FOUND!\n\n"
               result += "🛤️  Route:\n"
               for i, location in enumerate(path, 1):
                   if i < len(path):
                       result += f"    {i}. {location}📍\n"
                       result += f"        ↓\n"
                   else:
                       result += f"    {i}. {location} 🎯\n"
                    
               total_dist = sum(self.graph[path[i]][path[i+1]] for i in range(len(path-1)))
               result += f"\n  Total Distance: {total_dist} units\n"
               result += f"  Nodes Visited: {len(visited)}\n"
               return result 
        
           for neighbor in sorted(self.graph[current].keys()):
               if neighbor not in visited:
                   visited.add(neighbor)
                   queue.append((neighbor, path + [neighbor]))
                
       return " ❌ No path found between locations.\n"

    def dfs(self, start, goal):
       """DFS algorithm with styled output"""
       result = "🌳 DEPTH_FIRST SEARCH (DFS)\n"
       result+= "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
       result += "🔍 Exploration Order (Deep Dive):\n"
    
       visited = set()
       path = []
       found = [False]
       step = [1]
       output = [""]
    
    def dfs_recursive(node, target, current_path):
        visited.add(node)
        current_path.append(node)
        output[0] += f"   Step {step[0]}: {node}, (depth: {len(current_path)})\n"
        step[0] += 1
    
        if node == target:
            found[0] = True
            path.extend(current_path)
            return True 
    
        for neighbor in sorted(self.graph[node].keys()):
             if neighbor not in visited:
                 if dfs_recursive(neighbor, target, current_path):
                     return True 
            
        current_path.pop()
        return False
    
    defs_recursive(start, goal, [])
    result += output[0]
    
    if found[0]:
        result += f"\n✅ PATH FOUND!\n\n"
        result += "🛤️ Route:\n"
        for i, location in enumerate(path, 1):
            if i < len(path):
                result += f"   {i}. {location} 📍 \n"
                result += f"       ↓\n"
            else:
                result += f"   {i}. {location} 🎯\n"
                
        total_dist = sum(self.graoh[path[i]][path[i+1]] for i in range(len(path)-1))
        result += f"\n  Total Distance: {total_dist} units\n"
        result += f" Nodes Visited: {len(visited)}\n"
    else:
        result += " No path between locations.\n"
        
        return result 

def dijkstra(self, start, goal):
    """Dijkstra's algorithm with styled output"""
    result = " DIJKSTRA'S SHORTEST PATH ALGORITHM\n"
    result += "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
    
    distances = {node: float('inf') for node in self.graph}
    distances[start] = 0
    previous = {node: None for node in self.graph}
    pq = [(0, start)]
    visited = set()
    
    result += "🔍 Processing Nodes (by distance):\n"
    step = 1
    
    while pq:
        current_dist, current = heapq.heappop(pq)
        
        if current in visited:
            continue 
        
        visited.add(current)
        result += f"   Step{step}: {current} (distance: {current_dist})\n"
        step += 1
        
        if current == goal:
            break 
        
        for neighbor, weight in self.graph[current].itmes():
            distance = current_dist + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance 
                previous[neighbor] = current 
                heapq.heappush(pq, (distance, neighbor))
            
    # Reconstruct path 
    if distances[goal] != float('inf'):
        path = []
        current = goal
        while current is not None:
            path.append(current)
            current = previous[current]
        path.reverse()
        
        result += f"\n✅ OPTIMAL PATH FOUND!\n\n"
        result += "    Shortest Route:\n"
        for i, location in enumerate(path, 1):
            if i < len(path):
                dist = self.graph[path[i-1]][path[i]]
                result += f"    {i}. {location}  📍\n"
                result += f"        ↓ ({dist} units)\n"
            else: 
                result += f"    {i}. {location}  🎯\n"
                
        result += f"\n📏  Optimal Distance: {distances[goal]} units\n"
        result += f"🔢  Nodes Processed: {len(visited)}\n"
    else:
        result += "❌  No path exists between locations.\n"
        
    return result

def prim_mst(self, start):
    """Prim's MST algorithm with styled output"""
    result = "🌉 PRIM'S MINIMUM SPANNING TREE\n"
    result += "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
    result += "Building MST to connect all campus locations efficiently!\n\n"
    result += "🔍 Edge Selection Process:\n"
    
    visited = {start}
    edges = []
    pq = []
    
    for neighbor, weight in self.graph[start].items():
        heapq.heappush(pq, (weight, start, neighbor))
        
    total_weight = 0
    step = 1
    
    while pq and len(visited) < len(self.graph):
        weight, u, v = heapq.heapop(pq)
        
        if v in visited:
            continue
        
        visited.add(v)
        edges.append((u, v, weight))
        total_weight += weight
        
        result += f"    Step {step}: Add edges {u} ↔ {v} (weight: {weight}) ✨\n"
        step += 1
        
        for neighbor, w in self.graph[v].items():
            if neighbor not in visited:
                heapq.heappush(pq, (w, v, neighbor))
                
    result += f"\n✅  MINIMUM SPANNING TREE COMPLETE!\n\n"
    result += "🌉  All Edges in MST:\n"
    for u, v, weight in edges:
        result += f"   • {u} ↔ {v} ({weight} units)\n"
        
    result += f"\n📏  Total MST Weight: {total_weight} units\n"
    result += f"🔢  Edges in Tree: {len(edges)}\n"
    result += f"🌳  Nodes Connected: {len(visited)}\n"
    
    return result 

def reset_display(self):
    """Reset the display to intial state"""
    self.results_text.delete(1.0, tk.END)
    welcome_msg = """
╔═════════════════════════════════════════════════════╗
║       ✨   Welcome to Campus Navigator! ✨           ║
╚═════════════════════════════════════════════════════╝   

🗺️ Choose your starting point and destination above
⚡ Select an algorithm to use for pathfinding
🚀 Click "Find Path!" to discover the best route 

Available: Algorithms:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔵 BFS    - Finds shortest path (unweighted)
 🌳 DFS    - Explores depth-first through path
 ⚡ Dijkstra - Optimal weighted shortest path
 🌉 Prim     - Creates minimum spanning tree
    
Ready to navigate? Let's go! 
        """
        
    def save_results(self):
        """Save current results to a file"""
        content = self.results_text.get(1.0, tk.END)
        
        if content.strip():
            filename = filedialog.asksaveasfilename(
                defaultextension=".txt",
                filetypes=[("Text files", "*.txt"), ("All files", "*.*")],
                title="Save Navigation Results"
            )
            
            if filename:
                try:
                    with open(filename, 'w', encoding='utf-8') as f:
                        f.write(content)
                    messagebox.showinfo("💾 Success",
                                        f"Results saved successfully! ✨\n\n{filename}")
                except Exception as e:
                    messagebox.showerror("❌ Error",
                                         f"Could not save file:\n{str(e)}")
                    
class StudyPlanner(ttk.Frame):
    """Study Planner module with greedy and DP scheduling"""
    
    def __init__(self, parent, colors):
        """Initalize Study Planner with custom colors"""
        super().__init__(parent)
        self.colors = colors
        self.configure(style='Card.TFrame')
        self.tasks = []
        self.setup_ui()
        
    def setup_ui(self):
        """Create styled UI components"""
        main_container = tk.Frame(self, bg=self.colors['bg_dark'])
        main_container.pack(fill='both', expand=True, padx=25, pady=25)
        
        # Decorative title
        title_frame = tk.Frame(main_container, bg=self.colors['bg_dark'])
        title_frame.pack(fill='x', pady=(0, 20))
        
        title = tk.Label(title_frame, 
            text="✨ Study Session Planner",
            font=('Segoe UI', 15, 'bold'),
            bg=self.colors['bg_dark'],
            fg=self.colors['acent_purple'])
        title.pack(side='left')
        
        subtitle = tk.Label(title_frame,
            text="📚 Optimize your study scheduke!",
            font=('Segoe UI', 9),
            bg=self.colors['bg_dark'],
            fg=self.colors['accent_peach'])
        subtitle.pack(side='left', padx=(10, 0))
        
        
        # Task input frame with decorative border 
        input_outer = tk.Frame(main_container, bg=self.colors['accent_purple'], padx=2, pady=2)
        input_outer.pack(fill='x', pady=(0, 15))
        
        input_frame = ttk.LabelFrame(input_outer,
            text="➕ Add Study Task",
            style='Custom.TLabelframe',
            padding=20)
        input_frame.pack(fill='x')
        
        # Task name
        name_frame = tk.Frame(input_frame, bg=self.colors['card_bg'])
        name_frame.pack(fill='x', pady=5)
        
        tk.Label(name_frame,
                 text="📝  Task Name:",
                 font=('Segoe Ui', 10, 'bold'),
                 bg=self.colors['card_bg'],
                 fg=self.colors['accent_pink']).pack(side='left', padx=(0, 10))
        
        self.task_name = tk.Entry(name_frame,
            font=('Segoe UI', 10),
            bg=self.colors['bg_light'],
            fg=self.colors['text_light'],
            relief='flat',
            insertbackground=self.colors['accent_purple'])
        self.tasks_name.pack(side='left', fill='x', expand=True, ipady=5)
        
        # Time inputs 
        time_frame = tk.Frame(input_frame, bg=self.colors['card_bg'])
        time_frame.pack(fill='x', pady=5)
        
        tk.Label(time_frame,
            text="⏰  Start:",
            font=('Segoe UI', 10, 'bold'),
            bg=self.colors['card_bg'],
            fg=self.colors['accent_mint']).pack(side='left', padx=(0, 10))
        
        self.start_time = tk.Entry(time_frame, 
            font=('Segoe UI', 10),
            width=10,
            bg=self.colors['bg_light'],
            fg=self.colors['text_light'],
            relief='flat')
        self.start_time.pack(side='left', ipady=5)
        
        tk.Label(time_frame,
            text="⏰  End:",
            font=('Segoe UI', 10, 'bold'),
            bg=self.colors['card_bg'],
            fg=self.colors['accent_blue']).pack(side='left', padx=(20, 10))
        
        self.end_time = tk.Entry(time_frame, 
            font=('Segoe UI', 10), 
            width=10, 
            bg=self.colors['bg_light'],
            relief='flat')
        self.end_time.pack(side='left', ipady=5)
        
        tk.Label(time_frame, 
            text="⭐ Priority:",
            font=('Segoe UI', 10, 'bold'),
            bg=self.colors['card_bg'],
            fg=self.colors['accent_peach']).pack(side='left', padx=(20, 10))
        
        self.priority = tk.Entry(time_frame, 
            font=('Segoe UI', 10),
            width=10,
            bg=self.colors['bg_light'],
            fg=self.colors['text_light'],
            relief='flat')
        self.priority.pack(side='left', ipady=5)
        
        # Buttons 
        btn_frame = tk.Frame(input_frame, bg=self.colors['card_bg'])
        btn_frame.pack(fill='x', pady=(10, 0))
        
        ttk.Button(btn_frame, 
            text="➕ Add Task",
            command=self.add_task,
            style='Accent.TButton').pack(side='left', padx=5)
        
        ttk.Button(btn_frame, 
            text="🗑️  Clear All",
            command=self.clear_tasks,
            style='Secondary.TButton').pack(side='left', padx=5)
        
        # Algorithm selection
        algo_frame = ttk.LabelFrame(main_container,
            text="⚡ Select Scheduling Algorithm",
            style='Custom.TLabelframe', 
            padding=15)
        algo_frame.pack(fill='x', pady=(0, 15))
        
        self.schedule_algo = tk.StringVar(value='greedy')
        
        radio_container = tk.Frame(algo_frame, bg=self.colors['card_bg'])
        radio_container.pack(fill='x')
        
        algorithms = [
            (' Greedy - Maximize Tasks', 'greedy', self.colors['accent_mint']),
            ('  Dynamic Programming - Maximize Priority', 'dp', self.colors['accent_pink'])
        ]
        
        for text, value, color in algorithms:
            radio_frame = tk.Frame(radio_container, bg=self.colors['card_bg'])
            radio_frame.pack(side='left', fill='x', expand=True, padx=10)
            
            tk.Frame(radio_frame, bg=color, width=3, height=20).pack(side='left', padx=(0, 5))
            
            ttk.Radiobutton(radio_frame, 
                text=text,
                variable=self.schedule_algo,
                value=value,
                style='Custom.TRadiobutton').pack(side='left')
            
        # Schedule button 
        ttk.Button(main_container, 
            text="   Generate Schedule!",
            command=self.generate_schedule,
            style='Special.TButton').pack(pady=(0, 15))
        
        # Results display 
        results_outer = tk.Frame(main_container, bg=self.colors['accent_light'], padx=2, pady=2)
        results_outer.pack(fill='both', expand=True)
        
        results_inner = tk.Frame(main_container, bg=self.colors['accent_light'], padx=2, pady=2)
        results_inner.pack(fill='both', expand=True)
        
        
        results_label = tk.Label(results_inner,
            text="  Schedule Results",
            font=('Segoe UI', 11, 'bold'),
            bg=self.colors['card_bg'],
            fg=self.colors['accent_purple'])
        results_label.pack(anchor='w', padx=15, pady=(15, 10))
        
        self.schedule_text = scrolledtext.ScrolledText(results_inner, 
            wrap=tk.WORD,
            font=('Consolas', 10),
            bg=self.colors['bg_light'],
            fg=self.colors['text_light'],
            relief='flat',
            padx=20, 
            pady=20)
        self.schedule_text.pack(fill='both', expand=True, padx=15, pady=(0, 15))
        
        welcome_msg = """
╔═════════════════════════════════════════════════════╗
║       ✨   Welcome to Study Planner! ✨              ║
╚═════════════════════════════════════════════════════╝   

 📝 Add your study tasks with:
   - Task name 
   - Start time (e.g., 9)     
   - End time (e.g., 11)
   - Priority score (e.g., 10)
   
⚡ Choose an algorithm:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
⚡ Greedy - Schedules maximum number of non-overlapping tasks 
🎯 DP     - Maximizes total priority value (weighted scheduling)
   
       
Ready to ptimize your study time? Add tasks to begin! 💫
        """
        
        self.schedule_text.insert(1.0, welcome_msg)
    def add_task(self):
        """Add a study task with validation"""
        name = self.task_name.get().strip()
        
        try:
            start = int(self.start_time.get())
            end = int(self.end_time.get())
            priority = int(slef.priority.get())
            
            if not name:
                messagebox.shwowarning("⚠️  Invalid Input", "Please enter a task name! 📝")
                return
            
            if start >= end:
                messagebox.showwarning("⚠️  Invalid Time",
                    "Start time must be before end time! ⏰")
                return
            
            self.tasks.append({
                'name': name, 
                'start': start, 
                'end': end, 
                'priority': priority
            })
            
            # Clear inputs 
            self.task_name.delete(0, tk.END)
            self.start_time.delete(0, tk.END)
            self.end_time.delete(0, tk.END)
            self.priority.delete(0, tk.END)
            
            messagebox.showinfo("✅ Success",
                f"Task  '{name}' added successfully!  ✨\nTotal tasks: {len(self.tasks)}")
            
        except ValueError:
            messagebox.showerror("❌ Error",
                "Please enter valid numbers for time and priority! 🔢")
            
    def clear_tasks(self):
        """Clear all tasks"""
        if self.tasks:
            if messagebox.askyesno("🗑️ Confirm", 
                "Clear all tasks? This cannot be undone"):
                self.tasks.clear()
                messagebox.showinfo("✅ Cleared", "All tasks removed! 🧹")
        else:
            messagebox.showinfo("ℹ️ Info", "No tasks to clear! 📝")
            
    def generate_schedule(self):
        """Generate schedule using selected algorithm"""
        if not self.tasks:
            messagebox.showwarning("  No Tasks",
                "Please add some tasks first! 📝")
            return 
        
        algo = self.schedule_algo.get()
        self.schedule_text.delete(1.0, tk.END)
        
        header = f"""
╔═════════════════════════════════════════════════════╗
║         📅  STUDY SCHEDULE GENERATED  📅             ║
╚═════════════════════════════════════════════════════╝     

⚡ Algorithm: {algo.upper()} 
📝 Total Tasks Available: {len(self.tasks)}
       
"""
        self.schedule_text.insert(tk.END, header)
               
        start_time = time.time()
               
        if algo == 'greedy':
            result = self.greedy_schedule()
        else:
            result = self.dp_schedule()
            
        elapsed = (time.time() - start_time) * 1000
        
        self.schedule_text.insert(tk.END, result)
        self.schedule_text.insert(tk.END, f"\n{'━'*59}\n")
        self.schedule_text.insert(tk.END, f"⏱️   Execution Time: {elapsed:.2f}ms\n")
        self.schedule_text.insert(tk.END, f"{'━'*59}\n")
        
        def greedy_schedule(self, start):
            """Greedy interval scheduling algorithm"""
            result = "⚡ GREEDY INTERVAL SCHEDULING\n"
            result += "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
            result += "Strategy: Sort by end time, pick non-overlapping tasks!\n\n"
            
            # Sort by end time 
            sorted_tasks = sorted(self.tasks, key=lambda x: x['end'])
            
            result += " 📋  Tasks Sorted by End Time:\n"
            for i, task in enumerate(sorted_tasks, 1):
                result += f"   {i}. {task['name']} ({tasks['start']} → {task['end']})  ⭐{task['priority']}\n"
    
            result += "\n🔍 Selection Process:\n"
            
            scheduled = []
            last_end = -1
            step = 1
            
            for task in sorted_tasks:
                if task['start'] >= last_end:
                    scheduled.append(task)
                    result += f"    Step {step}: ✅ Selected '{task['name']}' "
                    result += f"({task['start']} → {task['end']})\n"
                    last_end = task['end']
                else:
                    result += f"    Step{step}:  ⏭️  Skipped '{task['name']}' "
                    result += f"(conflits with previous task)\n"
                step += 1
                
            result += f"\n✨ OPTIMAL SCHEDULE\n\n"
            result += "📅 Selected Tasks:\n"
            total_priority = 0
            total_time = 0 
            
            for i, task in enumerate(scheduled, 1):
                duration = task['end'] - task['start']
                total_time += duration
                total_priority += task['priority']
                result += f"   {i}. {task['name']}\n"
                result += f"       ⏰ Time: {task['start']}:80 - {task['end']}: 80 ({duration}h)\n"
                result += f"       ⭐ Priority: {task['priority']}\n\n"
                
            result += f"📊  Statistics:\n"
            result += f"   ✅ Tasks Scheduled: {len(scheduled)}/{len(self.tasks)}\n"
            result += f"   ⏰ Total Study Time: {total_time} hours\n"
            result += f"   ⭐ Total Priority: {total_priority}\n"
            
            return result 
        
        def dp_schedule(self):
            """Dynamic programming weighted scheduling"""
            result = "🎯 DYNAMIC PROGRAMMING SCHEDULER\n"
            result += "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
            result += "Strategy: Maximize total priority using 0/1 Knapsack approach!\n\n"
            
            # Sort by end time for DP
            sorted_tasks = sorted(self.tasks, key=lambda x: x['end'])
            n = len(sorted_tasks)
            
            # Find latest non-conflicting task 
            def find_latest_non_conflict(i):
                for j in range(i - 1, -1, -1):
                    if sorted_tasks[j]['end'] <= sorted_tasks[i]['start']:
                        return j 
                return -1 
            
            # DP table
            dp = [0] * n
            dp[0] = sorted_tasks[0]['priority']
            
            result += "📊 DP Table Construction:\n"
            
            for i in range(1, n):
                # Include current task 
                include_priority = sorted_tasks[i]['priority']
                latest = find_latest_non_conflict(i)
                if latest != -1:
                    include_priority += dp[latest]
                    
                # Exclude current task 
                exclude_priority = dp[i -1]
                
                dp[i] = max(include_priority, exclude_priority)
                
                result += f"    Task {i+1} ({sorted_tasks[i]['name']}): "
                result += f"Include={include_priority}, Exclude={exclude_priority} → "
                result += f"Max={dp[i]}\n"
                
            # Backtrack to find solution 
            scheduled = []
            i = n - 1
            while i >= 0:
                if i == 0:
                    scheduled.append(sorted_tasks[0])
                    break
                
                latest = find_latest_non_conflict(i)
                include_priority = sorted_tasks[i]['priority']
                if latest != -1:
                    include_priority += dp[latest]
                    
                if include_priority > dp[i - 1]:
                    scheduled.append(sorted_tasks[i])
                    i = latest
                else:
                    i -= 1
                    
            scheduled.reverse()
            
            result += f"\n✨ OPTIMAL WEIGHTED SCHEDULE\n\n"
            result += "📅 Selected Tasks (Priority-Optimized):\n"
            total_priority = 0
            total_time = 0
            
            for i, task in enumerate(scheduled, 1):
                duration = task['end'] - task['start']
                total_time += duration
                total_priority += task['priority']
                result += f"   {i}. {task['name']}\n"
                result += f"       ⏰ Time: {task['start']}:00 - {task['end']}: 00 ({duration}h)\n"
                result += f"       ⭐ Priority: {task['priority']}\n\n"
                
            result += f"📊 Statistics:\n"
            result += f"   ✅ Tasks Scheduled: {len(scheduled)}/{len(self.tasks)}\n"
            result += f"   ⏰ Total Study Time: {total_time} hours\n"
            result += f"   ⭐ Maximum Priority Achieved: {total_priority}\n"
            result += f"   🎯 DP Table Final Value: {dp[n-1]}\n"
            
            return result 
        
        def toggle_graph(self):
            """Toggle betwen custom and default graph"""
        if not self.custom_graph:
            messagebox.showwarning("⚠️  No Custom Graph"),
            "Please build a custom graph first! 🏗️ \n\nAdd nodes and edges using the builder above."
            return
        
        self.using_custom = not self.using_custom
        
        if self.using_custom:
            self.graph = self.custom_graph.copy()
            self.use_custom_btn.config(text="🏛️ Use Default Graph")
            self.graph_status.config(text="📊 Using: Custom ")
            status_msg = "Custom Graph"
        else:
            self.graph = self.default_graph.copy()
            self.use_custom_btn.config(text="🎨 Use Custom Graph")
            self.graph_status.config(text="📊 Using: Default")
            status_msg = "Default Graph"
            
        # Update locations list
        self.locations = list(self.graph.keys())
        
        # Update combox values
        self.start_menu['values'] = self.locations
        self.end_menu['values'] = self.locations
        
        # Set default selections
        self.start_var.set(self.locations[0] if self.locations else "")
        self.end_var.set(self.locations[-1] if len(self.locations) > 1 else (self.locations[0] if self.locations else ""))
        
        messagebox.showinfo("🔄 Graph Switched", 
            f"Now using: {status_msg}!🎉 \n\nNodes: {len(self.graph)}") 
        
    def clear_custom_graph(self):
        """Clear the custom graph"""
        if not self.custom_graph:
            messagebox.showinfo("  Info", 
                "Custom graph is already empty!  ")
            return 
        
        if messagebox.askyesno("  Confirm", 
            "Clear all custom nodes and edges? This cannot be undone!"):
            self.custom_graph.clear()
            self.node_positions.clear()
            
            # Clear listbox
            if hasattr(self, 'node_listbox'):
                self.node_listbox.delete(0, tk.END)
                
            # Clear canvas
            if hasattr(self, 'builder_canvas'):
                self.draw_graph()
                
            # Update combos
            self.update_builder_combos()
            
            # Reset selection
            self.selected_node = None
            if hasattr(self, 'selected_node_label'):
                self.slected_node_label.config(text="None")
                
            # If currently using custom graph, switch back to default
            if self.using_custom:
                self.using_custom = False
                self.graph = self.default_graph.copy()
                self.locations = list(self.graph.keys())
                self.use_custom_btn.config(text="🎨 Use Custom Graph")
                self.graph_status.config(text="📊 Using: Default")
                
                # Update combobox values list
                self.start_menu['values'] = self.locations
                self.end_menu['values'] = self.locations
                
                # Update combox selections
                self.start_var.set(self.locations[0])
                self.end_var.set(self.locations[-1])
                
            messagebox.showinfo("✅ Cleared",
                "Custom graph cleared! 🧹 ")
            
    def view_graph_structure(self):
        """Display the current graph structure"""
        graph_to_view = self.custom_graph if self.custom else self.graph
        graph_name = "Custom Graph" if (self.custom_graph and self.using_custom) else ("Custom Graph (Not Active)" if self.custom_graph else "Default Campus Graph")
        
        if not graph_to_view:
            messagebox.showinfo(" ℹ️ Info",
                "No graph to display! 📊\n\nBuild a custom graph first.")
            return 
        
        # Build display text
        display_text = f"""
╔═══════════════════════════════════════════════════════════╗
║          🏗️  GRAPH STRUCTURE: {graph_name.upper()}          
╚═══════════════════════════════════════════════════════════╝

  📊 Total Nodes: {len(graph_to_view)}      
  🔗 Graph Edges:
  
"""


        total_edges = 0
        for node in sorted(graph_to_view.keys()):
            display_text += f"\n📍  {node}:\n"
            if graph_to_view[node]:
                for neighbor, weight in sorted(graph_to_view[node].items()):
                    display_text += f"   <-> {neighbor} (weight: {weight})\n"
                    total_edges += 1
            else:
                display_text += f"    (No connections)\n"
                
        display_text += f"\n{'━'*59}\n"
        display_text += f"Total Edges: {total_edges // 2} (undirected)\n"
        display_text += f"{'━'*59}\n"
        
        # Show in main view area only 
        self.results_text.delete(1.0, tk.END)
        self.results_text.insert(1.0, display_text)
        
        
class NotesSearchEngine(ttk.Frame):
    """Module 3: Notes Search Engine with String Pattern Matching"""
    
    def __init__(self, parent, colors):
        """Initialize Notes Search Engine"""
        super().__init__(parent)
        self.colors = colors
        self.configure(style='Card.TFrame')
        self.notes_content = ""
        self.setup_ui()
        
    def setup_ui(self):
        """Stylized UI components"""
        main_container = tk.Frame(self, bg=self.colors['bg_dark'])
        main_container.pack(fill='both', expand=True, padx=25, pady=25)
        
        # Title
        title_frame = tk.Frame(main_container, bg=self.colors['bg_dark'])
        title_frame.pack(fill='x', pady=(0, 20))
        
        
        title = tk.Label(title_frame, 
            text="🔍  Notes Search Engine",
            font=('Segoe UI', 15, 'bold'), 
            bg=self.colors['bg_dark'],
            fg=self.colors['accent_purple'])
        title.pack(side='left')
        
        subtitle = tk.Label(title_frame, 
            text="💡  Find patterns in your notes!", 
            font=('Segoe UI', 9),
            bg=self.colors['bg_dark'],
            fg=self.colors['accent_blue'])
        subtitle.pack(side='left', padx=(10, 0))
        
        # Notes input with decorative border
        notes_outer = tk.Frame(main_container, bg=self.colors['accent_purple'], padx=2, pady=2)
        notes_outer.pack(fill='both', expand=True, pady=(0, 15))
        
        notes_frame = ttk.LabelFrame(notes_outer, 
             text="📝  Your Notes",
             style='Custom.TLabelframe',
             padding=15)
        notes_frame.pack(fill='both', expand=True)
        
        # File operations
        file_btn_frame = tk.Frame(notes_frame, bg=self.colors['card_bg'])
        file_btn_frame.pack(fill='x', pady=(0, 10))
        
        ttk.Button(file_btn_frame,
            text="📂 Load File",
            command=self.load_file,
            style='Secondary.TButton').pack(side='Left', padx=5)
        
        ttk.Button(file_btn_frame, 
            text="🧹 Clear",
            command=self.clear_notes,
            style='Secondary.TButton').pack(side='left', padx=5)
        
        # Text area
        self.notes_text = scrolledtext.ScrolledText(notes_frame,
            wrap=tk.WORD,
            font=('Segoe UI', 10),
            bg=self.colors['bg_light'],
            fg=self.colors['text_light'],
            relief='flat',
            padx=15,
            pady=15,
            height=8)
        self.notes_text.pack(fill='both', expand=True)
        
        # Search controls
        search_frame = ttk.LabelFrame(main_container, 
            text="🔍 Search Pattern", 
            style='Custom.TLabelframe',
            padding=15)
        search_frame.pack(fill='x', pady=(0, 15))
        
        pattern_frame = tk.Frame(search_frame, bg=self.colors['card_bg'])
        pattern_frame.pack(fill='x', pady=5)
        
        tk.Label(pattern_frame, 
            text=" Pattern:",
            font=('Segoe UI', 10, 'bold'),
            bg=self.colors['card_bg'],
            fg=self.colors['accent_pink']).pack(side='left', padx=(0, 10))
        
        self.pattern_entry = tk.Entry(pattern_frame, 
            font=('Segoe UI', 10),
            bg=self.colors['bg_light'],
            fg=self.colors['text_light'],
            relief='flat',
            insertbackground=self.colors['accent_purple'])
        self.pattern_entry.pack(side='left', fill='x', expand=True, ipady=6)
        
        # Algorithm selection
        algo_frame = tk.Frame(search_frame, bg=self.colors['card_bg'])
        algo_frame.pack(fill='x', pady=(10, 0))
        
        self.search_algo = tk.StringVar(value='native')
        
        algorithms = [
            ('🔄 Naive Search', 'naive', self.colors['accent_blue']),
            ('🎲 Rabin-Karp', 'rabin-karp', self.colors['accent_mint']),
            ('⚡ KMP Algorithm', 'kmp', self.colors['accent_pink'])
        ]
        
        for text, value, color in algorithms:
            radio_frame = tk.Frame(algo_frame, bg=self.colors['card_bg'])
            radio_frame.pack(side='left', fill='x', expand=True, padx=5)
            
            tk.Frame(radio_frame, bg=color, width=3, height=20).pack(side='left', padx=(0, 5))
            
            ttk.Radiobutton(radio_frame, 
                text=text,
                variable=self.search_algo,
                value=value,
                style='Custom.TRadiobutton').pack(side='left')
            
            # Search button 
            ttk.Button(main_container,
                text="🔍 Search Now!",
                command=self.search_pattern,
                style='Accent.TButton').pack(pady=(0, 15))
            
            # Results 
            results_outer = tk.Frame(main_container, bg=self.colors['accent_light'], padx=2, pady=2)
            results_outer.pack(fill='both', expand=True)
            
            results_inner = tk.Frame(results_outer, bg=self.colors['card_bg'], padx=2, pady=2)
            results_inner.pack(fill='both', expand=True)
            
            results_label = tk.Label(results_inner, 
                text="📊 Search Results",
                font=('Segoe UI', 11, 'bold'),
                bg=self.colors['card_bg'],
                fg=self.colors['accent_purple'])
            results_label.pack(anchor='w', padx=15, pady=(15, 10))
            
            self.results_text = scrolledtext.ScrolledText(results_inner,
                wrap=tk.WORD, 
                font=('Consolas', 10),
                bg=self.colors['bg_light'],
                fg=self.colors['text_light'],
                relief='flat',
                padx=20,
                pady=20)
            self.results_text.pack(fill='both', expand=True, padx=15, pady=(0, 15))
            
            welcome_msg = """
╔═════════════════════════════════════════════════════╗
║           🔍 Welcome to Notes Search! 🔍             ║
╚═════════════════════════════════════════════════════╝               
 
 📝 How to use:
   1. Load a file or type your notes above 
   2. Enter a pattern to search for 
   3. Choose a search algorithm 
   4. Click "Search Now!" to find matches 
   
 ⚡ Available Algorithms:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔄 Naive        - Simple brute-force search 
 🎲 Rabin-Karp   - Hash-based pattern matching 
 ⚡ KMP           - Efficient with preprocessing 
       
Ready to search? Load your notes to begin!💫            
            """
            self.results_text.insert(1.0, welcome_msg)
            
        def load_file(self):
            """Load notes from a file"""
            filename = filedialog.askopenfilename(
                filetypes=[("Text files", "*, txt"), ("All files", "*.*")],
                title="Load Notes File"
            )
            if filename:
                try: 
                    with open(filename, 'r', encoding='utf-8'):
                    content = f.read()
                    self.notes_text.delete(1.0, tk.END)
                    self.notes_text.insert(1.0, content)
                    messagebox.showinfo("✅ Success", 
                                        f"File loaded successfully! ✨\n\n{filename}")
                except Exception as e:
                    messagebox.showerror("❌ Error",
                        f"Could not load file:\n{str(e)}")
                    
        def clear_notes(self):
            """Clear the notes text area"""
            if self.notes_text.get(1.0, tk.END).strip():
                if messagebox.askyesno("🗑️ Confirm", 
                    "Clear all notes? This cannot be undone!"):
                    self.notes_text.delete(1.0, tk.END)
                    messagebox.showinfo("✅ Cleared", "Notes cleared! 🧹")
                    
        def search_pattern(self):
            """Search for pattern using selected algorithm"""
            text = self.notes_text.get(1.0, tk.END).strip()
            pattern = self.pattern_entry.get().strip()
            
            if not text:
                messagebox.showwarning("⚠️  No Notes",
                    "Please load or enter some notes first! 📝")
                return 
            
            if not pattern:
                messagebox.showwarning("⚠️ No Pattern",
                    "Please enter a pattern to search for! 🔍")
                return 
            
            algo = self.search_algo.get()
            self.results_text.delete(1.0, tk.END)
            
            header = f"""
╔═════════════════════════════════════════════════════╗
║            🔍  PATTERN SEARCH RESULTS 🔍             ║
╚═════════════════════════════════════════════════════╝   

 🎯 Pattern: "{pattern} "
 ⚡ Algorithm: {algo.upper().replace('_', '-')}
 📝 Text Length: {len(text)} characters 
            
"""
            self.results_text.insert(tk.END, header)
            
            start_time = time.time()
            
            if algo == 'naive':
                result = self.naive_search(text, pattern)
            elif algo == 'rabin-karp':
                result = self.rabin_karp(text, pattern)
            else: # kmp 
                result = self.kmp_search(text, pattern)
                
            elapsed = (time.time() - start_time) * 1000
            
            self.results_text.insert(tk.END, result)
            self.results_text.insert(tk.END, f"\n{'━'*59}\n")
            self.results_text.insert(tk.END, f"⏱️   Execution Time: {elapsed:.3f}ms\n")
            self.results_text.insert(tk.END, f"{'━'*59}\n")
            
        def naive_search(self, text, pattern):
            """Naive string matching algorithm"""
            result = "🔄 NAIVE STRING SEARCH\n"
            result += "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
            results += "Stratgey: Check every position in text\n\n"
            
            matches = []
            n = len(text)
            m = len(pattern)
            comparisons = 0
            
            result += "🔍 Search Progress:\n"
            
            for i in range(n - m + 1):
                j = 0 
                while j < m and text[i + j] == pattern[j]:
                    j += 1
                    comparisons += 1
                    
                if j == m:
                    matches.append(i)
                    result += f"    ✅ Match found at position {i}\n"
                else:
                    comparisons += 1 # Count the failed comparisons
                    
            result += f"\n📊 SEARCH COMPLETE\n\n"
            result += f"✨ Matches Found: {len(matches)}\n"
            result += f"🔢 Total Comparisons: {comparisons}\n\n"
            
            if matches:
                result += "📍 Match Positions:\n"
                for pos in matches:
                    context_start = max(0, pos - 20)
                    context_end = min(len(text), pos + len(pattern) + 20)
                    context = text[context_start:context_end]
                    result += f"   Position {pos}: ...{context}...\n"
            else:
                result += "❌ No matches found in the text.\n"
                
            return result 
        
        def rabin_karp(self, text, pattern):
            """Rabin-Karp string matching algorithm"""
            result = "  RABIN_KARP ALGORITHM\n"
            result += "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
            result += "Strategy: Use rolling hash for efficient comparisons\n\n"
            
            matches = []
            n = len(text)
            m = len(pattern)
            d = 256 # Number of characters 
            q = 101 # Prime number 
            
            # Calculate hash values
            h = pow(d, m - 1, q)
            p = 0 # Pattern hash
            t = 0 # Text hash
            
            # Calculate intial hash values 
            for i in range(m):
                p = (d * p + ord(pattern[i])) % q
                t = (d * t + ord(text[i])) % q
                
            result += f"🔢  Pattern Hash: {p}\n\n"
            result += "🔍  Searching with Rolling Hash:\n"
            
            comparisons = 0
            hash_matches = 0
            
            # Slide pattern over text
            for i in range(n - m + 1):
                if p == t:
                    hash_matches += 1
                    # Verify match character by character 
                    match = True 
                    for j in range(m):
                        comparisons += 1
                        if text[i + j] != pattern[j]:
                            match = False
                            break
                        
                    if match: 
                        matches.append(i)
                        result += f"   ✅ Hash match & verified at position {i}\n"
                    else:
                        result += f"   ⚠️  Hash collision at position {i}\n"
                        
                # Calculate rolling hash for next window
                if i < n - m:
                    t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q
                    if t < 0:
                        t += q
                        
                        
            result += f"\n📊  SEARCH COMPLETE\n\n"
            result += f"✨   Matches Found: {len(matches)}\n"
            result += f"🔢  Hash Matches: {hash_matches}\n"
            result += f"🔢  Character Comparisons: {comparisons}\n\n"
            
            if matches:
                result += "📍 Match Positions:\n"
                for pos in matches:
                    context_start = max(0, pos - 20)
                    context_end = min(len(text), pos + len(pattern) + 20)
            else:
                result += "❌  No matches found in the text.\n"
                
            return result 
        
    def kmp_search(self, text, pattern):
        """KMP string matching algorithm."""
        result = "⚡ KNUTH-MORRIS-PRATT (KMP) ALGORITHM\n"
        result += "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        
        # Compute LPS (Longest Proper Prefix which is also Suffix) array
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
                    
        result += "📊   LPS Array (preprocessing): \n"
        result += f"     Pattern: {pattern}\n"
        result += f"     LPS:      {lps}\n\n"
        
        # Search for pattern 
        matches = []
        n = len(text)
        i = 0 # Index for text 
        j = 0 # Index for pattern 
        comparisons = 0 
        
        result += "🔍 Searching with KMP:\n"
        
        while i < n:
            comparisons += 1
            
            if pattern[j] == text[i]:
                i += 1
                j += 1
                
            if j == m:
                matches.append(i - j)
                result += f"   ✅ Match found at position {i - j}\n"
                j = lps[j - 1]
            elif i < n and pattern[j] != text[i]:
                if j != 0:
                    j = lps[j - 1]
                    result += f"    ⏭️   Skip using LPS[{j}] at position {i}\n"
                else:
                    i += 1
                    
        result += f"\n📊   SEARCH COMPLETE\n\n"
        result += f"✨  Matches Found: {len(matches)}\n"
        result += f"🔢  Total Comparisons: {comparisons}\n"
        result += f"⚡  Efficiency Gain: {((n * m - comparisons) / (n * m) * 100):.f}%\n\n"
        
        
        if matches:
            result += "📍  Match Positions: \n"
            for pos in matches:
                context_start = max(0, pos - 20)
                context_end = min(len(text), pos + len(pattern) + 20)
                context = text[context_start:context_end]
                result += f"    Position {pos}: ...{context}...\n"
        else:
            result += "❌  No matches found in the text.\n"
        return result 
    
class AlgorithmInfo(ttk.Frame):
    """Algorithm Information module with complexity analysis."""
                
        
    def __init__(self, parent, colors):
        """Initialize Algorithm Info module"""
        super().__init__(parent)
        self.colors = colors
        self.configure(style='Card.TFrame')
        self.setup_ui()
        
    def setup_ui(self):
        """Create styled UI omponents"""
        main_container = tk.Frame(self, bg=self.colors['bg_dark'])
        main_container.pack(fill='both', expand=True, padx=25, pady=25)
        
        # Title 
        title_frame = tk.Frame(main_container, bg=self.colors['bg_dark'])
        title_frame.pack(fill='x', pady=(0, 20))
        
        title = tk.Label(title_frame, 
            text="💡  Algorithm Knowledge Base",
            font=('Segoe UI', 15, 'bold'),
            bg=self.colors['bg_dark'],
            fg=self.colors['accent_purple'])
        title.pack(side='left')
        
        subtitle = tk.Label(title_frame,
            text="📊  Complexity & Theory",
            font=('Segoe UI', 9),
            bg=self.colors['bg_dark'],
            fg=self.colors['accent_mint'])
        subtitle.pack(side='left', padx=(10, 0))
        
        # Sub-notebook for tabs 
        notebook = ttk.Notebook(main_container, style='Custom.TNotebook')
        notebook.pack(fil='both', expand=True)
        
        # Time Complexities tab 
        complexity_frame = tk.Frame(notebook, bg=self.colors['card_bg'])
        notebook.add(complexity_frame, text=" ⏱️  Time Complexities  ")
        
        complexity_text = scrolledtext.ScrolledText(complexity_frame,
            wrap=tk.WORD,
            font=('Consolas', 10),
            bg=self.colors['bg_light'],
            fg=self.colors['text_light'],
            relief='flat',
            padx=15, 
            pady=15)
        complexity_text.pack(fill='both', expand=True, padx=10, pady=10)
        
        complexity_info = """⏱️  TIME COMPLEXITY ANALYSIS ✨
        
╔═════════════════════════════════════════════════════╗
║                   GRAPH ALGORITHMS  🗺️               ║
╚═════════════════════════════════════════════════════╝     

🔵 BFS (Breadth-First Search)  
   Time: O(V + E)
   SPACE: O(V)
   Use:   Shortest path in unweighted graphs
   ✨      Level-by-level exploration
   
🌳 DFS (Depth-First Search)
   Time:  O(V + E)
   Space: O(V) recursion stack 
   Use: Connectivity, cycle detection
   ✨    Deep exploration first
   
⚡ Dijkstra's Algorithm (heap-based)
   Time: O((V + E) log V)
   Space: O(V)
   Use:   Shortest weighted path (non-negative weights)
   ✨      Greedy shortest path selection
   
🌉 Prim's MST (heap-based)
Time: O((V + E) log V)
Space: O(V)
Use:   Minimum spanning tree
✨     Greedy edges selection

╔═════════════════════════════════════════════════════╗
║         GREEDY & DYNAMIC PROGRAMMING  📚             ║
╚═════════════════════════════════════════════════════╝   

⚡ Greedy Interval Scheduling 
   Time:  O(n log n) - sorting dominates 
   Space: O(1)
   Use:   Maximize number of non-overlapping activities 
   ✨     Sorting by end time, pick greedily
   
╔═════════════════════════════════════════════════════╗
║            STRING MATCHING ALGORITHM 🔍              ║
╚═════════════════════════════════════════════════════╝  

🔄 Naive Search 
  Time: O(n x m)
  Space: O(1)
  Use:   Simple cases, small patterns 
  ✨     Check every position 
  
🎲 Rabin-Karp
  Time: O(n + m) average, O(n x m) worst
  Space: O(1)
  Use: Multiple pattern search 
  ✨   Rolling hash for efficiency 
  
⚡ KMP (Knuth-Morris-Pratt)
   Time: O(n + m) guaranteed 
   Space: O(m) for LPS array
   Use: Single pattermn, linear time guarentee
   ✨   LPS array prevents backtraacking 
   
╔═════════════════════════════════════════════════════╗
║            COMPLEXITY CLASSES 📊                     ║
╚═════════════════════════════════════════════════════╝ 

O(1)        Constant     ⚡ Instant - array access 
O(log n)    Logarithmic  ⚡ Very fast - binary search 
O(n)        Linear       ✅ Acceptable - single pass
O( n log n) Linearithmic ✅ Efficient - merge sort 
O(n^2)      Quadratic    ⚠️ Slow for large n - nested loops 
O(n^3)      Cubic        ⚠️ Very slow - triple nested 
O(2^n)      Exponential  ❌ Impractical - subsets
O(n!)       Factorial    ❌ Impossible - permutations   
        
💡  Pro Tip: Always aim for O(n log n) or better for large inputs!
"""
        complexity_text.insert(1.0, complexity_info)
        complexity_text.config(state='disabled')
        
        # P vs NP tab 
        pnp_frame = tk.Frame(notebook, bg=self.colors['card_bg'])
        notebook.add(pnp_frame, text="  🧠  P vs NP")
        
        pnp_text = scrolledtext.ScrolledText(pnp_frame, 
            wrap=tk.WORD,
            font=('Consolas', 10),
            bg=self.colors['bg_light'],
            fg=self.colors['text_light'],
            relief='flat',
            padx=15, 
            pady=15)
        pnp_text.pack(fill='both', expand=True, padx=10, pady=10)
        
        pnp_info = """🧠  P vs NP: THE MILLION DOLLAR QUESTION  ✨
        
╔═════════════════════════════════════════════════════╗
║                    NAVIGATION  💡                    ║
╚═════════════════════════════════════════════════════╝

The P vs NP question asks:

    "If we can quickly VERIFY a solution,
     can we also quickly FIND it?"
     
 💰 Millennium Prize Problem: $1,000,000 reward
 🤔 Unsolved for 50+ years
 📊 Most computer scientists believe P ≠ NP
 ✨ One of the most important questions in CS
    

╔═════════════════════════════════════════════════════╗
║                   WHAT IS P? ⚡                      ║
╚═════════════════════════════════════════════════════╝  

P = Problems solvable in POLYNOMIAL time 

✅  Examples from TCAA:
- BFS Pathfining             O( V + E)
- Dijkstra Shortest Path     O((V+E) log V)
- All sorting algorithms     O(n log n)
- String matching (KMP)      O(n + m)

✨ These problems are "tractable" - we can solve them efficiently!

╔═════════════════════════════════════════════════════╗
║                   WHAT IS NP? 🔍                     ║
╚═════════════════════════════════════════════════════╝  

NP = Problems where solutions can be VERIFIED in polynomial time 

❓  Examples NOT in TCAA:
    - Boolean SAT (satisfiability)
    - Traveling Salesman (decision version)
    - Graph Coloring
    - Hamiltonian Cycle 
    - Subset Sum 
    
✨  Key insight: Verification is easier than finding!
    
Example: Sudoku
- Finding solution: Could take very long ❌
- Checking solution: Quick and easy ✅

╔═════════════════════════════════════════════════════╗
║                   NP-COMPLETE 🔴                    ║
╚═════════════════════════════════════════════════════╝  

The HARDEST problems in NP

if ANY NP-Complete problem can be solved in P time, 
then P = NP (all NP problems become easy!)

Famous NP-Complete problems:
    🔴 SAT (first proven NP-Complete)
    🔴 3-SAT
    🔴 Vertex Cover
    🔴 Clique
    🔴 Independent Set
    🔴 Hamiltonian Path
      
 ✨ All NP-Complete problems can be reduced to each other!
 
╔═════════════════════════════════════════════════════╗
║                   NP-HARD ⚠️                         ║
╚═════════════════════════════════════════════════════╝ 

At least as hard as Np-Complete, maybe harder

⚠️  0/1 Knapsack (optimization) - NP-Hard
  Our DP solution: O(nW) pseudo-polynomial
  Works well when W is reasonable!
  
⚠️  Traveling Salesman (optimization) - NP-Hard
  Finding shortest tour is harder than yes/no question 
  
✨ NP-Hard problems aren't necessarily in NP!

╔═════════════════════════════════════════════════════╗
║               WHY IT MATTERS 🌟                      ║
╚═════════════════════════════════════════════════════╝ 

🔐 Cryptography
   RSA encryption relies on P ≠ NP
   if P = NP, most encryption breaks!
   
🎯  Real-World Optimzation
   Scheduling, routing, packing all NP-Hard
   Need approximations, not perfect solutions
   
🧠  Undertsanding Computation 
   Fundamental limits of what's computable 
   Shapes how we approach problem-solving
   
💰  Career Impact 
   Understanding complexity helps choose right approach 
   Don't waste time looking for polyminal solutions!
    
╔═════════════════════════════════════════════════════╗
║        STRATEGIES FOR NP-HARD PROBLEMS  💡           ║
╚═════════════════════════════════════════════════════╝ 

1. 📈 Approxiation Algorithms 
Get "good enough" solutions quickly
Example: 2-approximation for Vertex Cover 

2. 🎲 Heuristics 
Greedy algorithms, local search, genetic algorithms
No guarantees, but often work well in practice

3. 📊 Dynamic Programming 
Like our knapsack! Works for reaonable inputs 
Pseudo-polyminal for some problems 

4. 🎯 Special Cases
Restrict problem to make tractable 
Example: 2-SAT is in P (but 3-SAT is NP-Complete)

5. 🔧 Parameterized Complexity 
Efficient when some parameter is small 
Example: Tree width, vertex cover size

✨ Remember: If a problem is NP-Hard, don't waste time 
looking for a perfect polynomial algorithm! Be smart,
use approximations and heuristics instead!
              
"""
        pnp_text.insert(1.0, pnp_info)
        pnp_text.config(state='disabled')
              
def main():
    """Main entry point for the enhanced style application"""
    app = TCAA()
    app.mainloop()
    
if __name__ == "__main__":
    main()
    
    
