import tkinter as tk
from tkinter import LEFT, RIGHT

class SimpleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tkinter Convas Test")

        self.canvas = tk.Canvas(self.root, width=800, height=600)
        self.canvas.pack()

        self.button1 = tk.Button(self.root, text="Draw Square", command=self.draw_square)
        self.button1.pack()

        self.button2 = tk.Button(self.root, text= "Remove Square", command = self.remove_square)
        self.button2.pack()

    def draw_square(self):
        self.canvas.create_rectangle(50, 100, 350, 500, fill="blue")
    def remove_square(self):
        self.canvas.delete("all")
    def draw_triangle(self):
        #Giving the vertices
        self.canvas.create_polygon(2.0,2.0,
    100.0,100.0,200.0,50.0)

if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleApp(root)
    root.mainloop()