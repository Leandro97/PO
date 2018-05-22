from collections import defaultdict

class Graph:
  def __init__(self,vertices):
    self.V= vertices #número de vértices
    self.graph = defaultdict(list) #dicionário que armazena o grafo
    self.Time = 0
    self.path = []
  
  #adiciona uma aresta
  def addEdge(self,u,v):
      self.graph[u].append(v)
      self.graph[v].append(u)
 
  #remove uma aresta do grafo 
  def rmvEdge(self, u, v):
    for index, key in enumerate(self.graph[u]):
      if key == v:
        self.graph[u].pop(index)
    for index, key in enumerate(self.graph[v]):
      if key == u:
        self.graph[v].pop(index)
 
  #Algoritmo DFS que conta quantos vértices são alcançados a partir de v
  def DFSCount(self, v, visited):
      count = 1
      visited[v] = True
      for i in self.graph[v]:
          if visited[i] == False:
              count = count + self.DFSCount(i, visited)         
      return count
 
  #Checa se a próxima aresta pode ser usada
  def isValidNextEdge(self, u, v):
    #Se for o único caminho, retorna true
    if len(self.graph[u]) == 1:
        return True
    else:
      #conta os vértices alcançáveis através de u  
      visited =[False]*(self.V)
      count1 = self.DFSCount(u, visited)
  
      #remove a aresta (u, v) e conta os vértices alcançáveis através de u  
      self.rmvEdge(u, v)
      visited =[False]*(self.V)
      count2 = self.DFSCount(u, visited)
 
      #Recoloca aresta no grafo
      self.addEdge(u,v)
 
      #Se mais nós eram alcançados antes da remoção, temos uma ponte, então a aresta é uma ponte e não pode ser usada
      return False if count1 > count2 else True
 
 
  #função que monta o caminho 
  def findPathUtil(self, u):
    #Verifica rodos os filhos de u
    for v in self.graph[u]:
        #verifica se a aresta u,v pode ser usada
        if self.isValidNextEdge(u, v):
          self.path.append((u,v))
          self.rmvEdge(u, v)
          self.findPathUtil(v)
 
  #função que verifica todos os nós
  def findPath(self):
    u = 0
    for i in range(self.V):
      #buscando nó com grau ímpar
      if len(self.graph[i]) %2 != 0 :
        u = i
        break
    self.findPathUtil(u)

def main(): 
  g1 = Graph(4)
  g1.addEdge(0, 1)
  g1.addEdge(0, 2)
  g1.addEdge(1, 2)
  g1.addEdge(2, 3)
  g1.findPath()
  print(g1.path)
  
  
  g2 = Graph(3)
  g2.addEdge(0, 1)
  g2.addEdge(1, 2)
  g2.addEdge(2, 0)
  g2.findPath()
  print(g2.path)
  
  g3 = Graph (5)
  g3.addEdge(1, 0)
  g3.addEdge(0, 2)
  g3.addEdge(2, 1)
  g3.addEdge(0, 3)
  g3.addEdge(3, 4)
  g3.addEdge(3, 2)
  g3.addEdge(3, 1)
  g3.addEdge(2, 4)
  g3.findPath()
  print(g3.path)

main()