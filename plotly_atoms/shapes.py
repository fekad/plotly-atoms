import numpy as np
import plotly.graph_objects as go
from .defaults import surface_materials


def build_sphere(r=1.0, points=12):

    phi = np.linspace(0, 2 * np.pi, 2 * points, endpoint=False)
    theta = np.linspace(-np.pi / 2, np.pi / 2, points)

    # The mesh of the sphere
    phi, theta = np.meshgrid(phi, theta)

    xsphere = r * (np.cos(theta) * np.sin(phi)).flatten()
    ysphere = r * (np.cos(theta) * np.cos(phi)).flatten()
    zsphere = r * (np.sin(theta)).flatten()

    return xsphere, ysphere, zsphere


def get_line(point1, point2, width=1, color="black", mode="lines", **kwargs):
    return go.Scatter3d(
        mode=mode,
        x=[point1[0], point2[0]],
        y=[point1[1], point2[1]],
        z=[point1[2], point2[2]],
        line=dict(color=color, width=width),
        **kwargs
    )


def get_sphere_mesh(point, size, color):

    lightning = surface_materials["matte"]

    return go.Mesh3d(
        x=size * SPHERE[0] + point[0],
        y=size * SPHERE[1] + point[1],
        z=size * SPHERE[2] + point[2],
        alphahull=0,
        color=color,
        flatshading=False,
        cmin=-7,  # a trick to get a nice plot (z.min()=-3.31909)
        lighting=lightning,
        lightposition=dict(x=100, y=100, z=0),
    )


SPHERE = build_sphere()
