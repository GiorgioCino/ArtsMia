from model.model import Model

mdl = Model()
mdl.buildGraph()
print(f"Grafo creato contiene {mdl.getNumNodes()} nodes e {mdl.getNumEdges()} archi")

mdl.getInfoCompConnessa(1224)