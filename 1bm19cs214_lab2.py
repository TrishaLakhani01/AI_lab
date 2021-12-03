def bfs(src,target):
    arr = []
    arr.append(src)
    exp=[]
    while len(arr) > 0:
        source=arr.pop(0)
        exp.append(source)
        print(source)
        if source==target:
            print('Done')
            return 
        moves_to_do = []
        moves_to_do = possible_moves(source,exp)
        for move in moves_to_do:
            if move not in exp and move not in arr:
                arr.append(move)

def possible_moves(state,visited):
    b=state.index(-1)
    d=[]
    pos_moves=[]
    if b in [0,1,2,3,4,5]:
        d.append('d')
    if b in [3,4,5,6,7,8]:
        d.append('u')
    if b in [1,2,4,5,7,8]:
        d.append('l')
    if b in [0,1,3,4,6,7]:
        d.append('r')
    for i in d:
        temp=gen(state,i,b)
        pos_moves.append(temp)
    return [move_can for move_can in pos_moves if move_can not in visited]

def gen(state,m,b):
    temp=state.copy()
    if m=='l':
        temp[b],temp[b-1] = temp[b-1],temp[b]
    if m=='r':
        temp[b],temp[b+1] = temp[b+1],temp[b]
    if m=='u':
        temp[b],temp[b-3] = temp[b-3],temp[b]
    if m=='d':
        temp[b],temp[b+3] = temp[b+3],temp[b]
    return temp
src = [1,2,3,-1,4,5,6,7,8]
target = [1,2,3,4,5,-1,6,7,8]


bfs(src, target) 
