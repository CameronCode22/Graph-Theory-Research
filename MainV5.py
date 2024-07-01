import tkinter as tk
import random

visited = {}

#each wall defined in matrix
cols = 15
rows = 15
maze = []
visited = {}

def dfs(current_node):
    x, y = current_node
    visited[current_node] = True
    neighbors = get_neighbors(current_node)
    random.shuffle(neighbors)

    for neighbor in neighbors:
        if not visited[neighbor]:
            remove_wall(current_node, neighbor)
            dfs(neighbor)

def remove_wall(current, next):
    #to determine if the wall is n,e,s,w

    x1, y1 = current
    x2, y2 = next

    if x1 == x2:
        #y because its vertical
        if y1 > y2:
            #up
            maze[x1][y1]['north'] = False
            maze[x2][y2]['south'] = False
        if y1 < y2:
            #down
            maze[x1][y1]['south'] = False
            maze[x2][y2]['north'] = False
    if y1 == y2:
        #because its horizontal
        if x1 > x2:
            #left
            maze[x1][y1]['west'] = False
            maze[x2][y2]['east'] = False
        if x1 < x2:
            #right
            maze[x1][y1]['east'] = False
            maze[x2][y2]['west'] = False

    #remove start and exit
    maze[0][0]['north'] = False
    maze[cols-1][rows-1]['south'] = False

def Initialise_Maze(root):
    canvas = tk.Canvas(root, width=800, height=600)
    canvas.pack()

    cell_size = 20
    for i in range(rows):
        for j in range(cols):

            #offset from the left
            offset = 30
            x1 = j * cell_size + offset
            y1 = i * cell_size + offset
            x2 = x1 + cell_size
            y2 = y1 + cell_size

            # Draw east and south walls based on maze grid
            if maze[j][i]['north']:
                canvas.create_line(x1, y1, x2, y1)
            if maze[j][i]['east']:
                canvas.create_line(x2, y1, x2, y2)
            if maze[j][i]['south']:
                canvas.create_line(x1, y2, x2, y2)
            if maze[j][i]['west']:
                canvas.create_line(x1, y1, x1, y2)

def get_neighbors(node):
    x, y = node
    neighbors = []
    if x > 0: neighbors.append((x-1, y))
    if x < rows - 1: neighbors.append((x+1, y))
    if y > 0: neighbors.append((x, y-1))
    if y < cols - 1: neighbors.append((x, y+1))

    #adding nodes to visited if not already there. set to FALSE
    for neighbor in neighbors:
        if neighbor not in visited:
            #appending to visited as False
            visited[neighbor] = False

    return neighbors

def reset_maze(cols, rows, start_node):
    global maze, visisted
    maze = [[{'north': True, 'east': True, 'south': True, 'west': True} for _ in range(cols)] for _ in range(rows)]
    visited[start_node] = False
    return maze, visited

def main():
    start_node = (0, 0)
    global maze, visited
    maze, visited = reset_maze(cols, rows, start_node)
    dfs(start_node)

    #Initilasing the canvas
    root = tk.Tk()
    Initialise_Maze(root)
    button = tk.Button(root, text= "New Maze", command=lambda: reset_maze(cols, rows, start_node))
    button.pack()
    root.mainloop()


#def create_grid():
if __name__ == "__main__":
    main()
    