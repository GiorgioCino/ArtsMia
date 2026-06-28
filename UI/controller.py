import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleAnalizzaOggetti(self, e):
        self._model.buildGraph()
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text("Grafo ok"))
        self._view.txt_result.controls.append(ft.Text(f"Il grafo contiene {self._model.getNumNodes()}nodi e {self._model.getNumEdges()} archi"))
        self._view.update_page()


    def handleCompConnessa(self,e):
        txtIdOggetto = self._view._txtIdOggetto.value  #recupera input
        if txtIdOggetto== "":
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text("inserire vslore nel campo id"))

            self._view.update_page()
            return

        try:
            idOggetto = int(txtIdOggetto)
        except ValueError:
                self._view.txt_result.controls.clear()
                self._view.txt_result.controls.append(ft.Text("inserire vslore numerico"))

                self._view.update_page()
                return

        if not self._model.hasNode(idOggetto):
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text("id non presente nel grafo"))

            self._view.update_page()
            return

        sizeCompConn = self._model.getInfoCompConnessa(idOggetto)
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text(f"componente connessa contente oggetto {idOggetto} è composta di {sizeCompConn} nodi"))

        self._view.update_page()

