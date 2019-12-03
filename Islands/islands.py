# Islands

def main():
    matrix = [1, 0, 0, 0, 0,
              0, 0, 1, 1, 0,
              0, 1, 1, 0, 0,
              0, 0, 0, 0, 0,
              1, 1, 0, 0, 1,
              1, 1, 0, 0, 1]
    return islands(matrix)

def islands(matrix):
    isles = [] # list of Nodes
    for i in range(len(matrix)):
        if (matrix[i] == 1):
            for isle in isles:
                if (isle.index != i and i not in isle.adj_list):
                    new_node = Node(i)
                    isles.append(new_node)
                else:
                    return

class Node:
    def __init__(self, index):
        self.index = index
        self.adj_list = []

    def add_adj(self, adj):
        self.adj_list.append(adj)

if __name__ == '__main__':
    main()