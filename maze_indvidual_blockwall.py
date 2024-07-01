import tkinter as tk

class MazeApp:
    def __init__(self, root, rows, cols, cell_size=20):
        self.root = root
        self.root.title("Maze Example")

        self.rows = rows
        self.cols = cols
        self.cell_size = cell_size

        self.canvas = tk.Canvas(self.root, width=800, height=600)
        self.canvas.pack()

        # Initialize maze grid
        self.maze = [[{'north': True, 'east': True, 'south': True, 'west': True} for _ in range(cols)] for _ in range(rows)]

        # Draw the maze
        self.draw_maze()

    def draw_maze(self):
        for i in range(self.rows):
            for j in range(self.cols):


                offset = 50
                x1 = j * self.cell_size + offset
                y1 = i * self.cell_size + offset
                x2 = x1 + self.cell_size
                y2 = y1 + self.cell_size

                # Draw east and south walls based on maze grid
                if self.maze[i][j]['north']:
                    self.canvas.create_line(x1, y1, x2, y1)
                if self.maze[i][j]['east']:
                    self.canvas.create_line(x2, y1, x2, y2)
                if self.maze[i][j]['south']:
                    self.canvas.create_line(x1, y2, x2, y2)
                if self.maze[i][j]['west']:
                    self.canvas.create_line(x1, y1, x1, y2)

    # Other methods to manipulate maze structure, such as removing walls

if __name__ == "__main__":
    rows = 20
    cols = 20
    root = tk.Tk()
    app = MazeApp(root, rows, cols, 20)
    root.mainloop()
