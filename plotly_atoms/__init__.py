import numpy as np
import plotly.graph_objects as go

from .defaults import default_layout
from .data import atom_radiis, atom_colors, atom_sizes
from .shapes import get_sphere_mesh, get_line


class Figure:
    def __init__(self):
        self.fig = go.Figure()
        self.fig.update_layout(default_layout)

    def _add_ball_and_stick(self, coords, species):

        trace_list = []
        for coord, specie in zip(coords, species):

            mesh = get_sphere_mesh(
                coord,
                atom_sizes[specie],
                atom_colors[specie],
            )
            trace_list.append(mesh)

        self.fig.add_traces(trace_list)

    def _add_tubes(self, coords, species):

        trace_list = []
        for coord, specie in zip(coords, species):

            mesh = get_sphere_mesh(coord, 0.3, atom_colors[specie])
            trace_list.append(mesh)

        self.fig.add_traces(trace_list)

    def _add_spacefilling(self, coords, species):

        trace_list = []
        for coord, specie in zip(coords, species):
            # Uses van der waals radii
            mesh = get_sphere_mesh(
                coord,
                atom_radiis[specie],
                atom_colors[specie],
            )
            trace_list.append(mesh)

        self.fig.add_traces(trace_list)

    def _add_unitcell(self, cell):
        a, b, c = cell

        self.fig.add_traces(
            [
                get_line(
                    [0, 0, 0],
                    a,
                    mode="lines+text",
                    text=[None, "a"],
                    color="red",
                    width=4,
                ),
                get_line(
                    [0, 0, 0],
                    b,
                    mode="lines+text",
                    text=[None, "b"],
                    color="green",
                    width=4,
                ),
                get_line(
                    [0, 0, 0],
                    c,
                    mode="lines+text",
                    text=[None, "c"],
                    color="blue",
                    width=4,
                ),
                get_line(a, a + b),
                get_line(a, a + c),
                get_line(b, b + a),
                get_line(b, b + c),
                get_line(c, c + a),
                get_line(c, c + b),
                get_line(a + b, a + b + c),
                get_line(b + c, a + b + c),
                get_line(c + a, a + b + c),
            ]
        )

    def add_structure(self, structure, style="ball_and_stick", supercell=None):

        if supercell:
            structure = structure.copy()
            structure.make_supercell(supercell)

        coords = structure.cart_coords
        species = [site.specie.value for site in structure]

        if style == "ball_and_stick":
            self._add_ball_and_stick(coords, species)
        elif style == "tubes":
            self._add_tubes(coords, species)
        elif style == "spacefilling":
            self._add_spacefilling(coords, species)
        else:
            raise ValueError(
                'Only avaliable styles are "ball_and_stick", "tubes" and "spacefilling".'
            )

    def add_unitcell(self, structure):
        cell = structure.lattice.matrix
        self._add_unitcell(cell)

    def show(self):
        self.fig.show()
