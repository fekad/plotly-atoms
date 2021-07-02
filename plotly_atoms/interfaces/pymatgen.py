from .. import Figure as BaseFigure

try:
    import pymatgen
except ImportError:
    raise ImportError('Please install `pymatgen` first!')

class Figure(BaseFigure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def add_structure(self, structure, style="ball_and_stick", supercell=None):

        if supercell:
            structure = structure.copy()
            structure.make_supercell(supercell)

        if style == "ball_and_stick":
            self.add_ball_and_stick(structure)
        elif style == "tubes":
            self.add_tubes(structure)
        elif style == "spacefilling":
            self.add_spacefilling(structure)
        else:
            raise ValueError(
                'Only avaliable styles are "ball_and_stick", "tubes" and "spacefilling".'
            )

    def add_ball_and_stick(self, structure):

        coords = structure.cart_coords
        species = [site.specie.value for site in structure]

        super().add_ball_and_stick(coords, species)


    def add_tubes(self, structure):

        coords = structure.cart_coords
        species = [site.specie.value for site in structure]

        super().add_tubes(coords, species)

    def add_spacefilling(self, structure):

        coords = structure.cart_coords
        species = [site.specie.value for site in structure]

        super().add_spacefilling(coords, species)


    def add_unitcell(self, structure):
        cell = structure.lattice.matrix
        super().add_unitcell(cell)
