import heapq
maze = [
    [0, 0, -1, 0, 0, 0],
    [-1, 0, -1, 0, -1, 0],
    [0, 0, 0, 0, -1, 0],
    [0, -1, -1, 0, 0, 0],
    [0, 0, 0, -1, -1, 0],
    [-1, -1, 0, 0, 0, 0]
]
start=(0,0)
goal=(5,5)

moves=[
    (1,0),(0,1),(-1,0),(0,-1)
]

def heuristic(n):
    return abs(n[0]-goal[0])+abs(n[1]-goal[1])

def valid(r,c):
    return 0<=r<len(maze) and 0<=c<len(maze[0]) and maze[r][c]==0

def nextnode(node):
    r,c=node
    neighbor=[]

    for dr,dc in moves:
        nr=r+dr
        nc=c+dc

        if valid(nr,nc):
            neighbor.append((nr,nc))

    return neighbor


def cpath(par,node):
    path=[]

    while node is not None:
        path.append(node)
        node=par[node]
    return path[::-1]



def astar():
    pq=[(heuristic(start),0,start)]
    vis=set()

    par={start:None}
    while pq:
        _,cost,node=heapq.heappop(pq)#extra cost
        if node in vis:
            continue
        vis.add(node)

        if node==goal:
            return cpath(par,node)

        for nx in nextnode(node):
            if nx not in vis and nx not in par:
                newcost=cost+1
                f=newcost+heuristic(nx)
                #extra two lines^|^
                
                par[nx]=node
                heapq.heappush(pq,(f,newcost,nx))
    return None

path=astar()
print(path)
print("pathcost=",len(path)-1)


