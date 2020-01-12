#!/bin/python3

import os
import sys

#
# Complete the swapNodes function below.
#
class Node:
    data = 0
    left = None
    right = None

def inOrderTraversal(node, arr):
    if(node == None):
        return 0
    inOrderTraversal(node.left, arr)
    arr.append(node.data)
    inOrderTraversal(node.right, arr)

def createTree(treeNodes):
    nodeQueue = []
    root = Node()
    root.data = treeNodes[0]
    nodeQueue.append(root)
    for index in range(1, len(treeNodes), 2):
        parentNode = nodeQueue.pop(0)
        if(treeNodes[index] != -1):
            nodeLeft = Node()
            nodeLeft.data = treeNodes[index]
            parentNode.left = nodeLeft
            nodeQueue.append(nodeLeft)
        if(treeNodes[index + 1] != -1):
            nodeRight = Node()
            nodeRight.data = treeNodes[index + 1]
            parentNode.right = nodeRight
            nodeQueue.append(nodeRight)
    return root

def swapNodes(query, root):
    stack1 = []
    stack2 = []
    inOrderPerQuery = []
    queryResult = []
    currentDepth = 1
    for depthDivisor in query:
        notDone = True
        stack1 = []
        stack2 = []
        stack1.append(root)
        currentDepth = 1
        while(notDone):
            parent = stack1.pop(0)
            if(currentDepth % depthDivisor == 0):
                temp = parent.left
                parent.left = parent.right
                parent.right = temp
            if(parent.left):
                stack2.append(parent.left)
            if(parent.right):
                stack2.append(parent.right)
            if(len(stack1) == 0 and len(stack2) != 0):
                stack1 = stack2
                stack2 = []
                currentDepth = currentDepth + 1
            if(len(stack1) == 0 and len(stack2) == 0):
                notDone = False
        inOrderTraversal(root, inOrderPerQuery)
        queryResult.append(list(inOrderPerQuery))
        inOrderPerQuery = [] 
    return queryResult
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    indexes = []

    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    nodeList = [1]
    for index in range(0, len(indexes)):
       for index1 in range(0, len(indexes[index])):
          nodeList.append(indexes[index][index1])  
    root = createTree(nodeList)
    queryResults = swapNodes(queries, root)
    fptr.write('\n'.join([' '.join(map(str, x)) for x in queryResults]))
    fptr.write('\n')
    
    fptr.close()
