import tkinter as tk
import random

class MazeGenerator:
    def __init__(self, root, rows, cols, cell_size=40):
        self.root = root
        self.root.title("Maze Generator")
        
        self.rows = rows
        self.cols = cols
        self.cell_size = cell_size
        
        self.canvas = tk.Canvas(self.root, width=cols * cell_size, height=rows * cell_size)
        self.canvas.pack()
        
        self.maze = self.initialize_maze(rows, cols)
        self.generate_maze()
        self.draw_maze()
        
    def initialize_maze(self, rows, cols):
        # Initialize maze grid with all walls
        maze = [[True for _ in range(cols)] for _ in range(rows)]
        return maze
    
    def generate_maze(self):
        # Generate maze using Prim's algorithm or any other method
        # Here's a simple example of generating a random maze
        visited = [[False for _ in range(self.cols)] for _ in range(self.rows)]
        stack = [(0, 0)]
        while stack:
            current = stack.pop()
            x, y = current
            visited[y][x] = True
            neighbors = []
            if x > 0 and not visited[y][x-1]: # left
                neighbors.append((x-1, y))
            if x < self.cols - 1 and not visited[y][x+1]: # right
                neighbors.append((x+1, y))
            if y > 0 and not visited[y-1][x]: # up
                neighbors.append((x, y-1))
            if y < self.rows - 1 and not visited[y+1][x]: # down
                neighbors.append((x, y+1))
            if neighbors:
                next_cell = random.choice(neighbors)
                nx, ny = next_cell
                if nx != x:
                    maze_y = min(y, ny)
                    self.maze[maze_y][x] = False
                else:
                    maze_x = min(x, nx)
                    self.maze[y][maze_x] = False
                stack.append(next_cell)
    
    def draw_maze(self):
        # Draw the maze on the canvas
        for y in range(self.rows):
            for x in range(self.cols):
                if self.maze[y][x]:
                    x1, y1 = x * self.cell_size, y * self.cell_size
                    x2, y2 = x1 + self.cell_size, y1 + self.cell_size
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="black", outline="")
                    
if __name__ == "__main__":
    root = tk.Tk()
    maze_app = MazeGenerator(root, 10, 10, 40)
    root.mainloop()
