import numpy as np
import plotly.graph_objects as go

from .defaults import default_layout
from .data import atom_radiis, atom_colors, atom_sizes
from .shapes import get_sphere, get_line


class Figure(go.Figure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.update_layout(default_layout)

    def add_atoms(self, coords, species):

        trace_list = []
        for coord, specie in zip(coords, species):

            mesh = get_sphere(
                coord,
                atom_sizes[specie],
                atom_colors[specie],
            )
            trace_list.append(mesh)

        self.add_traces(trace_list)

    def add_tubes(self, coords, species):

        trace_list = []
        for coord, specie in zip(coords, species):

            mesh = get_sphere(coord, 0.3, atom_colors[specie])
            trace_list.append(mesh)

        self.add_traces(trace_list)

    def add_ball_and_stick(self, coords, species):

        trace_list = []
        for coord, specie in zip(coords, species):

            mesh = get_sphere(
                coord,
                atom_sizes[specie],
                atom_colors[specie],
            )
            trace_list.append(mesh)

        self.add_traces(trace_list)

    def add_spacefilling(self, coords, species):

        trace_list = []
        for coord, specie in zip(coords, species):
            # Uses van der waals radii
            mesh = get_sphere(
                coord,
                atom_radiis[specie],
                atom_colors[specie],
            )
            trace_list.append(mesh)

        self.add_traces(trace_list)

    def add_unitcell(self, cell):
        a, b, c = cell

        self.add_traces(
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
