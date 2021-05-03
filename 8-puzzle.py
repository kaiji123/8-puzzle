## a star algorithm
import random
import copy
arr= [x for x in range(9)]
random.shuffle(arr)
d = [arr[:3],arr[3:6],arr[6:9]]
print(d)
print(arr)
print(d)
def check_tiles(array):
    cost=0
    for i in range(3):
        for x in range(3):
            correct= i*3 + x+1
            if array[i][x] == 0:## if its zero then continue
                continue
            if array[i][x] != correct :
                cost = cost +1
    return cost

def find_zero(d):
    for i in range(len(d)):
        for x in range(len(d[i])):
            if d[i][x] == 0 :
              return (i,x)
sequence= []
while True :
    position = find_zero(d)
    temp =copy.deepcopy(d)
    print(temp)
    d[position[0]][position[1]]
    cost = []
    
    states= []
    try:
        d[position[0]][position[1]]=temp[position[0]][position[1]+1]
        d[position[0]][position[1]+1]=temp[position[0]][position[1]]
        if d not in sequence:
            states.append(d)
            cost.append(check_tiles(d))
    except:
        pass
    d = copy.deepcopy(temp)
    try:
        if position[1]!=0:
            d[position[0]][position[1]]=temp[position[0]][position[1]-1]
            d[position[0]][position[1]-1]=temp[position[0]][position[1]]
        if d not in sequence:
            states.append(d)
            cost.append(check_tiles(d))
    except:
        pass
    d = copy.deepcopy(temp)
    try:
        d[position[0]][position[1]]=temp[position[0]+1][position[1]]
        d[position[0]+1][position[1]]=temp[position[0]][position[1]]
        if d not in sequence:
            states.append(d)
            cost.append(check_tiles(d))
    except:
        pass
    d = copy.deepcopy(temp)
    try:
        if position[0] !=0:
                
            d[position[0]][position[1]]=temp[position[0]-1][position[1]]
            d[position[0]-1][position[1]]=temp[position[0]][position[1]]
        if d not in sequence:
            states.append(d)
            cost.append(check_tiles(d))
    except:
        pass
    d = copy.deepcopy(temp)
#     print(states)
    print(cost)
    minimum = min(cost)
    index = cost.index(minimum)
    sequence.append(states[index])
    d = copy.deepcopy(states[index])
    print(sequence)
    print(d)
    if minimum ==0:
        break
print(find_zero(d))
print(check_tiles(d))

###
#predefine the moves
corners = [(0,0),(2,0),(0,2),(2,2)]
moves= [[(0,1),(1,0)],[(2,1),(1,0)],[(1,2),(0,1)]]
#
# class Node:
#     def __init__(self,data,level,fval):
#         """ Initialize the node with the data, level of the node and the calculated fvalue """
#         self.data = data
#         self.level = level
#         self.fval = fval
# 
#     def generate_child(self):
#         """ Generate child nodes from the given node by moving the blank space
#             either in the four directions {up,down,left,right} """
#         x,y = self.find(self.data,'_')
#         """ val_list contains position values for moving the blank space in either of
#             the 4 directions [up,down,left,right] respectively. """
#         val_list = [[x,y-1],[x,y+1],[x-1,y],[x+1,y]]
#         children = []
#         for i in val_list:
#             child = self.shuffle(self.data,x,y,i[0],i[1])
#             if child is not None:
#                 child_node = Node(child,self.level+1,0)
#                 children.append(child_node)
#         return children
#         
#     def shuffle(self,puz,x1,y1,x2,y2):
#         """ Move the blank space in the given direction and if the position value are out
#             of limits the return None """
#         if x2 >= 0 and x2 < len(self.data) and y2 >= 0 and y2 < len(self.data):
#             temp_puz = []
#             temp_puz = self.copy(puz)
#             temp = temp_puz[x2][y2]
#             temp_puz[x2][y2] = temp_puz[x1][y1]
#             temp_puz[x1][y1] = temp
#             return temp_puz
#         else:
#             return None
#             
# 
#     def copy(self,root):
#         """ Copy function to create a similar matrix of the given node"""
#         temp = []
#         for i in root:
#             t = []
#             for j in i:
#                 t.append(j)
#             temp.append(t)
#         return temp    
#             
#     def find(self,puz,x):
#         """ Specifically used to find the position of the blank space """
#         for i in range(0,len(self.data)):
#             for j in range(0,len(self.data)):
#                 if puz[i][j] == x:
#                     return i,j
# 
# 
# class Puzzle:
#     def __init__(self,size):
#         """ Initialize the puzzle size by the specified size,open and closed lists to empty """
#         self.n = size
#         self.open = []
#         self.closed = []
# 
#     def accept(self):
#         """ Accepts the puzzle from the user """
#         puz = []
#         for i in range(0,self.n):
#             temp = input().split(" ")
#             puz.append(temp)
#         return puz
# 
#     def f(self,start,goal):
#         """ Heuristic Function to calculate hueristic value f(x) = h(x) + g(x) """
#         return self.h(start.data,goal)+start.level
# 
#     def h(self,start,goal):
#         """ Calculates the different between the given puzzles """
#         temp = 0
#         for i in range(0,self.n):
#             for j in range(0,self.n):
#                 if start[i][j] != goal[i][j] and start[i][j] != '_':
#                     temp += 1
#         return temp
#         
# 
#     def process(self):
#         """ Accept Start and Goal Puzzle state"""
#         print("Enter the start state matrix \n")
#         start = self.accept()
#         print("Enter the goal state matrix \n")        
#         goal = self.accept()
# 
#         start = Node(start,0,0)
#         start.fval = self.f(start,goal)
#         """ Put the start node in the open list"""
#         self.open.append(start)
#         print("\n\n")
#         while True:
#             cur = self.open[0]
#             print("")
#             print("  | ")
#             print("  | ")
#             print(" \\\'/ \n")
#             for i in cur.data:
#                 for j in i:
#                     print(j,end=" ")
#                 print("")
#             """ If the difference between current and goal node is 0 we have reached the goal node"""
#             if(self.h(cur.data,goal) == 0):
#                 break
#             for i in cur.generate_child():
#                 i.fval = self.f(i,goal)
#                 self.open.append(i)
#             self.closed.append(cur)
#             del self.open[0]
# 
#             """ sort the opne list based on f value """
#             self.open.sort(key = lambda x:x.fval,reverse=False)
# 
# 
# puz = Puzzle(3)
# puz.process()
                
    