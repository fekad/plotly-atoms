import numpy as np
import plotly.graph_objects as go

from .defaults import default_layout
from .data import colors, atomic_radii
from .shapes import get_sphere_mesh, get_line


class Figure:
    def __init__(self):
        self.fig = go.Figure()
        self.fig.update_layout(default_layout)

    def add_structure(self, structure, style="ball_and_stick", supercell=None):

        if supercell:
            structure = structure.copy()
            structure.make_supercell(supercell)

        trace_list = []

        if style == "ball_and_stick":
            for site in structure:

                mesh = get_sphere_mesh(
                    site.coords,
                    site.specie.number / 40 + 0.2,
                    colors[site.specie.value],
                )
                trace_list.append(mesh)

        elif style == "tubes":
            for site in structure:

                mesh = get_sphere_mesh(site.coords, 0.3, colors[site.specie.value])
                trace_list.append(mesh)

        elif style is "spacefilling":
            for site in structure:
                # Uses van der waals radii
                mesh = get_sphere_mesh(
                    site.coords,
                    atomic_radii[site.specie.value],
                    colors[site.specie.value],
                )
                trace_list.append(mesh)

        else:
            raise ValueError(
                'Only avaliable styles are "ball_and_stick", "tubes" and "spacefilling".'
            )

        self.fig.add_traces(trace_list)

    def add_unitcell(self, lattice):
        a, b, c = lattice.matrix

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

    def show(self):
        self.fig.show()
