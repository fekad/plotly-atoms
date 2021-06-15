from abc import ABCMeta



def view(structure, *args, **kwargs):
    pass


class Viewer(metaclass=ABCMeta):
    def __init__(self):
        pass

    def add_atoms(self, *args, **kwargs):
        pass

    def add_unitcell(self, *args, **kwargs):
        pass

    



