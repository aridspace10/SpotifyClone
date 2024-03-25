
class Model():
    def __init__(self) -> None:
        pass

class View():
    def __init__(self) -> None:
        pass
class Controller():
    def __init__(self) -> None:
        self.model = Model()
        self.view = View()
        self.run()
    
    def run(self) -> None:
        pass