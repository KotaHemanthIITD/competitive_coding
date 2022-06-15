"""

Given a binary tree and given number N, and a distance K, find the sum of all the nodes that are present at K distance from the node of N


Input: target = 9, K = 1,  

                                  1
                                /   \
                               2      9
                             /      /   \
                            4      5     7
                          /  \          /  \
                         8    19      20   11
                             /      /   \
                            30     40   50
Output: 22

9 + 5 + 7 + 1 = 22

Input: target = 40,  K = 2,  
                                  1
                                /   \
                               2     9
                             /      /   \
                            4      5     7
                           /  \         /  \
                          8    19      20   11
                              /      /   \
                             30     40   50
Output: 97
40 + 7 + 50 = 97
"""

# wrong mod(curr_depth-found_depth) + parent_depth+1

# find node in binary : O(n)
# find sum at K : O(n)

# 4 3
# 4 4 
#k=1 res = n->left.val+n->right.val+prev.val
#k = 2 find_sum(n.left,k-1)+find_sum(n.right,k-1) +find_sum(prev.val,k-1)
# k find_sum(n.left,k-1)+find_sum(n.right,k-1)+find_sum(prev.val,k-1)

# depth variable at each node mod(curr_dep-found_depth) == k

class Node:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val
        self.parent = None

def find_node(root,n):
    if root.val == n:
        return root
    else:
        left_ret = None
        right_ret = None
        if root.left != None:
            left_ret = find_node(root.left,n)
        if root.right != None:
            right_ret = find_node(root.right,n)
        if left_ret != None:
            return left_ret
        if right_ret != None:
            return right_ret
        return None

def find_sum(root,n,k):
    f_node = find_node(root,n)
    # print("node",f_node.val)
    res = n
    queue = [f_node]
    visited = {}
    new_queue = []
    while len(queue) != 0 and k >=0:
        vals = []
        for i in queue:
            vals.append(i.val)
        print("queue",vals)
        front = queue[0]
        queue.pop(0)
        visited[front] = True
        print("front",front.val)
        if front.parent != None and front.parent not in visited:
            new_queue.append(front.parent)
        if front.left != None and front.left not in visited:
            print("left",front.left.val)
            new_queue.append(front.left)
        if front.right != None and front.right not in visited:
            print("right")
            new_queue.append(front.right)
         
        if len(queue) == 0:
            queue = new_queue
            new_queue = []
            k = k-1
            print("k",k)

        if k == 0:
            vals = []
            print(res)
            for i in queue:
                res += i.val
                vals.append(i.val)
            print("when 0",len(queue),vals,res)
            k = k-1

    return res


# def find_sum( root, n, k, prev, incl):
#     if k == 0 and incl == False:
#         return root.val
#     if root.val == n:
#         if incl:
#             res += root.val
#         right_val = 0
#         left_val = 0
#         ances_val = 0
#         if prev != None:
#             ances_val = find_sum(prev,n,k-1,prev.parent)
#         if root.left != None:
#             left_val = find_sum(root.left,n,k-1,root)
#         if right != None:
#             right_val = right_val = find_sum(root.left,n,k-1,root)
#         tot_sum = ances_val + left_val + right_val
#         res += tot_sum
#     return res
inp1 = Node(1)

leaf_1 = Node(30)
leaf_2 = Node(40)
leaf_3 = Node(50)
################

lb_1 = Node(8)
lb_2 = Node(19)
lb_3 = Node(20)
lb_4 = Node(11)

llb_1 = Node(4)
llb_2 = Node(5)
llb_3 = Node(7)

ub_1 = Node(2)
ub_2 = Node(9)
###################
leaf_1.parent = lb_2 
leaf_2.parent = lb_3
leaf_3.parent = lb_3
lb_2.left=leaf_1
lb_3.left = leaf_2
lb_3.right = leaf_3
#####################
lb_1.parent = llb_1
lb_2.parent = llb_1

lb_3.parent = llb_3
lb_4.parent = llb_3

llb_1.left = lb_1
llb_1.right=lb_2
llb_3.left = lb_3
llb_3.right=lb_4
################
llb_1.parent = ub_1
llb_2.parent = ub_2
llb_3.parent = ub_2

ub_1.left = llb_1
ub_2.left = llb_2
ub_2.right = llb_3
################
ub_1.parent=inp1
ub_2.parent=inp1
inp1.left=ub_1
inp1.right=ub_2

# print(inp1.left.left.left.val)
# Input: target = 9, K = 1,  

#                                   1
#                                 /   \
#                                2      9
#                              /      /   \
#                             4      5     7
#                           /  \          /  \
#                          8    19      20   11
#                              /      /   \
#                             30     40   50
# Output: 22


n = 1
k = 4
out1 = find_sum(inp1,n,k)
print("inp1: ",out1)

