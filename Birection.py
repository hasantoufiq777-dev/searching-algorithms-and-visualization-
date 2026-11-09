from collections import deque
def makepath(vis1,vis2,meet):
    path1=[]
    node=meet

    while node is not None:
        path1.append(node)#
        node=vis1[node]#upadate the node
    path1.reverse()

    path2=[]
    node=vis2[meet]

    while node is not None:
        path2.append(node)
        node=vis2[node]

    return path2+path1
    
def bidir(graph,start,goal):
    if start==goal:
        return [start]

    q1=deque([start])
    q2=deque([goal])

    vis1={start:None}
    vis2={goal:None}

    while q1 and q2:
        node=q1.popleft()

        for child in graph[node]:
            if child not in vis1:
                vis1[child]=node
                q1.append(child)
            if child in vis2:
                return makepath(vis1,vis2,child)
        node=q2.popleft()
        for child in graph[node]:
            if child not in vis2:
                vis2[child]=node
                q2.append(child)
            if child in vis1:
                return makepath (vis1,vis2,child)
    return None    

        
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'E'],
    'D': ['B', 'F'],
    'E': ['C', 'F'],
    'F': ['D', 'E', 'G'],
    'G': ['F']
}

start = 'A'
goal = 'G'

result = bidir(graph, start, goal)



print(result)