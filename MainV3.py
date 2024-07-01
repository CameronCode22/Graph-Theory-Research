import tkinter as tk

visited = {}

#each wall defined in matrix
cols = 9
rows = 9
maze = [[{'north': True, 'east': True, 'south': True, 'west': True} for _ in range(cols)] for _ in range(rows)]
# Print maze with coordinates
for i in range(rows):
    for j in range(cols):
        print(f"Coordinates ({j}, {i}): {maze[j][i]}")


def dfs(current_node):
    x, y = current_node
    print("\visiting next: ", current_node)
    visited[current_node] = True

    for neighbor in get_neighbors(current_node):
        if not visited[neighbor]:
            remove_wall(current_node, neighbor)
            dfs(neighbor)

def remove_wall(current, next):
    #to determine if the wall is n,e,s,w

    x1, y1 = current
    x2, y2 = next
    print("\ current position",current)
    print("\ next position removal", next)

    print("before the removal change current posit:",maze[x1][y1])

    # if x1 == x2:
    #     #y because its vertical
    #     if y1 > y2:
    #         #up
    #         maze[x1][y1]['north'] = False
    #         maze[x2][y2]['south'] = False
    #     if y1 < y2:
    #         #down
    #         maze[x1][y1]['south'] = False
    #         maze[x2][y2]['north'] = False
    if y1 == y2:
        #because its horizontal
        if x1 > x2:
            print(" X1 is greater than X2 ")
            #left
            maze[x1][y1]['west'] = False
            maze[x2][y2]['east'] = False
        if x1 < x2:
            #right
            print("X2 is greater than X1")
            maze[x1][y1]['east'] = False
            maze[x2][y2]['west'] = False
            print("current position for maze",maze[x1][y1])
            print("next position for maze",maze[x2][y2])

def Initialise_Maze(root):
    canvas = tk.Canvas(root, width=800, height=600)
    canvas.pack()


    print(maze)
    cell_size = 40
    for i in range(rows):
        for j in range(cols):
            print(f"Coordinates ({j}, {i}): {maze[j][i]}")

            #offset from the left
            offset = 50
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
    

    print(f"Neighbors of ({x}, {y}): {neighbors}")

    #adding nodes to visited if not already there. set to FALSE
    for neighbor in neighbors:
        if neighbor not in visited:
            #appending to visited as False
            visited[neighbor] = False

    return neighbors

def main():

    #define start node and run algorithm
    start_node = (0, 0)
    visited[start_node] = False
    dfs(start_node)
    print("\ Maze once finished", maze)

    #Initilasing the canvas
    root = tk.Tk()
    Initialise_Maze(root)
    root.mainloop()
    print("\nVisited nodes:", visited)

    # Print maze with coordinates
    # for i in range(rows):
    #     for j in range(cols):
    #         print(f"Coordinates ({j}, {i}): {maze[i][j]}")


#def create_grid():
if __name__ == "__main__":
    main()
    