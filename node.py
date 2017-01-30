#!/usr/bin/python3.5

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

    def add_node(self,name,value,couleur="black"):
        if name not in self.nodes :
            new = Node(name,value,couleur)
            self.nodes[name] = new
            return new
        else :
            return self.nodes[name]


    def add_edge(self ,src , dest ,data):
        S = Node(src,black)
        D = Node(dest,black)
        self.add_node(S)
        self.add_node(N)
        S.add_neighbor(D)
        self.edges.add(Edge(src,dest,data))


if __name__ == '__main__' :
    n= Node(name="bachir",color="red",value=23)
    n2 =Node(name="vero",color="green",value=233)
    n3=Node(name="boris",color="pink",value=78)
    n3. add_neighbor(n)
    edge = Edge("a" , "b" , "23" , color="black")
    edge2 = Edge("c" , "e" , "89" , color="red")
    print(edge2)
    
