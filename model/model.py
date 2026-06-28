import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._graph = nx.Graph()
        self._nodes = DAO.getAllNodes()
        self._idMapAO = {}
        for n in self._nodes:
            self._idMapAO[n.object_id] = n   #dizionario che associa a ogni chiave primaria l'ggetto


    def buildGraph(self):
        #aggiunge i nodi per recuperarli li prendo dal database
        self._nodes = DAO.getAllNodes()
        self._graph.add_nodes_from(self._nodes)
        #aggiunge archi li prendo dal database
        self.addEdgesV2()

    def getInfoCompConnessa(self,id_oggetto):
        #cercare componente connessa che contiene id_oggetto
        if not self.hasNode(id_oggetto):  #se non ha questo nodo qui return None
            return None

        source = self._idMapAO[id_oggetto]
        #strategia 1
        dfsTree = nx.dfs_tree(self._graph,source)
        print("size connessa con dfs tree", len(dfsTree.nodes()))

        #strategia 2
        dfsPred = nx.dfs_predecessors(self._graph,source)
        print("size connessa con predecessors", len(dfsPred.values()))

        #strategia 3
        conn = nx.node_connected_component(self._graph,source)
        print("size connessa con connected componente", len(conn))

        return len(conn)

    def hasNode(self,id_oggetto):
        return id_oggetto in self._idMapAO

    def addEdges(self):     #pero questo metodo è molto lwnto quindi devo lavorare sylla query
        for u in self._nodes:           #ciclo su tutti i nodi
            for v in self._nodes:
                peso = DAO.getEdgePeso(u, v)       #recupero peso
                if peso is not None:     #se non è none aggiungo arco
                    self._graph.add_edge(u, v, weight=peso)
                    print(f"Aggiungo acrco fra {u} e {v} con peso {peso}")

    def addEdgesV2(self):
        allEdges = DAO.getAllEdges(self._idMapAO)
        for e in allEdges:
            self._graph.add_edge(e.o1, e.o2, weight=e.peso)

    def getNumNodes(self):
        return len(self._graph.nodes)

    def getNumEdges(self):
        return len(self._graph.edges)