graph = {
  'A' : ['B','G'],
  'B' : ['C', 'D', 'E'],
  'C' : [],
  'D' : [],
  'E' : ['F'],
  'F' : [],
  'G' : ['H'],
  'H' : ['I'],
  'I' : [], 
}

#Pass the graph and starting at node A to the function
def dfs(graph, node):
    #create an array for visited nodes the stack
    #stack will hold list of what is priority to pop
    #pop meaning which one is most recent, and next to be visited
    visited = []
    stack = []

    #set Visited and popped next to A
    visited.append(node)
    stack.append(node)

    while stack:
        #stack.pop gets A and the adjacent dictionary so in this case B & G
        s = stack.pop()
        print(s, end = "")

        #The loop makes reverse order G n and then tests if its visited. if it is not
        #the visited and stack are added
        #the stack is essentially managing the order in which they should be visited
        for n in reversed(graph[s]):
            if n not in visited:
                visited.append(n)
                stack.append(n)

def main():
    dfs(graph, 'A')

main()