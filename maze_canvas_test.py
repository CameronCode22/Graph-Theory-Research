import tkinter as tk

class MazeApp:
    def __init__(self, root, rows, cols, cell_size=20):
        #initialise the canvas
        self.root = root
        self.root.title("Maze Grid Example")

        self.rows = rows
        self.cols = cols
        self.cell_size = cell_size

        self.canvas = tk.Canvas(self.root, width=800, height= 600)
        self.canvas.pack()

        self.draw_grid()

    def draw_grid(self):
        #draw grid set-up
        for i in range(self.rows):
            for j in range(self.cols):
                x1 = j * self.cell_size
                y1 = i * self.cell_size
                x2 = x1 + self.cell_size
                y2 = y1 + self.cell_size
                if j == 2 and i == 1:
                    fill_color = "white"
                    continue
                if i % 2 == 0 and j % 2 == 0:
                    fill_color = "black"
                elif i % 2 == 0:
                    fill_color = "black"
                elif j % 2 == 0:
                    fill_color = "black"
                else:
                    fill_color = "white"

                self.canvas.create_rectangle(x1,y1,x2,y2, fill=fill_color, outline="white")
        
    
if __name__ == "__main__":
    root = tk.Tk()
    app = MazeApp(root, 9, 9, 20)
    root.mainloop()