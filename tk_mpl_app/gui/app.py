from gui.menu_bar import MenuBar 
from gui.nav_bar import NavigationBar
from gui.actions import toggle_avg, next_graph, prev_graph
from gui.graph_widget import GraphWidget
from graphs.graphs import get_graph_types


class App:
    def __init__(self, root) -> None:
        self.root = root
        self.menu: MenuBar | None = None
        self.nav: NavigationBar | None = None
        self.graph_widget: GraphWidget | None = None
        self.create_gui()

    def create_gui(self):
        button_config = [
            {"key": "prev", "text": "Previous", "side": "left", 
             "command": lambda: prev_graph(self, get_graph_types())},
            {"key": "avg", "text": "Toggle Avg", "side": "center", 
             "command": lambda: toggle_avg(self)},
            {"key": "next", "text": "Next", "side": "right", 
             "command": lambda: next_graph(self, get_graph_types())},
        ]

        self.menu = MenuBar(self.root, self)

        self.nav = NavigationBar(self.root, button_config)

        self.graph_widget = GraphWidget(self.root, self)
