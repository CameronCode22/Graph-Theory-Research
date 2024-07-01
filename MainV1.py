import tkinter as tk

visited = {}

def dfs(current_node):
    x, y = current_node
    visited[current_node] = True
    for neighbor in get_neighbors(current_node):
        if not visited[neighbor]:
            dfs(neighbor)


def Initialise_Maze(root):
    canvas = tk.Canvas(width=800, height=600)
    canvas.pack()

def get_neighbors(node):
    x, y = node
    neighbors = []
    if x > 0: neighbors.append((x-1, y))
    if x < 7: neighbors.append((x+1, y))
    if y > 0: neighbors.append((x, y-1))
    if y < 7: neighbors.append((x, y+1))

    #adding nodes to visited if not already there. set to FALSE
    for neighbor in neighbors:
        if neighbor not in visited:
            #appending to visited as False
            visited[neighbor] = False

    return neighbors
def main():
    #Initilasing the canvas
    root = tk.Tk()
    Initialise_Maze(root)
    root.mainloop()

    #define start node and run algorithm
    start_node = (0, 0)
    dfs(start_node)

#def create_grid():

if __name__ == "__main__":
    main()
    