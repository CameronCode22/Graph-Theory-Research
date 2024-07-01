import tkinter as tk

visited = {}

#each wall defined in matrix
cols = 9
rows = 9
maze = [[{'north': True, 'east': True, 'south': True, 'west': True} for _ in range(cols)] for _ in range(rows)]

def dfs(current_node):
    x, y = current_node
    visited[current_node] = True
    for neighbor in get_neighbors(current_node):
        if not visited[neighbor]:
            dfs(neighbor)


def Initialise_Maze(root):
    canvas = tk.Canvas(width=800, height=600)
    canvas.pack()

    cell_size = 40
    for i in range(rows):
        for j in range(cols):

            #offset from the left
            offset = 50
            x1 = j * cell_size + offset
            y1 = i * cell_size + offset
            x2 = x1 + cell_size
            y2 = y1 + cell_size

            # Draw east and south walls based on maze grid
            if maze[i][j]['north']:
                canvas.create_line(x1, y1, x2, y1)
            if maze[i][j]['east']:
                canvas.create_line(x2, y1, x2, y2)
            if maze[i][j]['south']:
                canvas.create_line(x1, y2, x2, y2)
            if maze[i][j]['west']:
                canvas.create_line(x1, y1, x1, y2)


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
    