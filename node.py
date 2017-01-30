#!/usr/bin/python3.4

""" dot -Tpng -0 ou -o fichier.dot"""


class Node :

    def __init__(self,name,value,color="black") :
        self.name = name
        self.value = value
        self.col = color
        self.in_neighbors = []
        self.out_neighbors = []

    def add_neighbor(self,neighbor):
        self.out_neighbors.append(neighbor)
        neighbor.in_neighbors.append(self)

    def __str__(self):
        return "name : "+self.name+", value : "+str(self.value)+", color : "\
            +self.col+ "\n"+" in : "+" ".join([node.name for node in self.in_neighbors])\
            +" \n out : "+" ".join([node.name for node in self.out_neighbors])

    
class Edge :
    def __init__(self ,src , dest , data , color="black") :
        self.src = src
        self.dest = dest
        self.data = data
        self.color = color

    def __str__(self):
        return "src : "+self.src+" ,dest : "+self.dest+" ,data : "+self.data+" ,color :"+self.color
 
        
class Graph :
    def __init__(self,name=None):
        self.nodes = dict()
        self.edges = set()
        self.name = name

   
    def add_node(self,node):
        if node.name not in self.nodes :
            self.nodes[node.name]=node
        else :
            return node

    def add_edge(self ,src , dest ,data):
        S = Node(src,black)
        D = Node(dest,black)
        self.add_node(S)
        self.add_node(N)
        S.add_neighbor(D)
        self.edges.add(Edge(src,dest,data))

    def __str__(self):
        return "Nodes : "+" , ".join([key for key in self.nodes])\
            +"\nedgs : "+" , ".join([edge.src+" "+edge.dest  for edge in self.edges])
        

if __name__ == '__main__' :
    n1= Node(name="bachir",color="red",value=23)
    n2= Node(name="chelbi",color="pink",value=56)
    edge = Edge("a" , "b" , "23" , color="black")

    graphe = Graph("graphe")
    graphe.add_node(n1)
    graphe.add_node(n2)
    graphe.add_edge()
    print(graphe)
