from matplotlib.image import pil_to_array
import numpy as np
import plotly.graph_objects as go
from .defaults import surface_materials


def rotation_matrix_from_vectors(vec1, vec2):
    """Find the rotation matrix that aligns vec1 to vec2
    :param vec1: A 3d "source" vector
    :param vec2: A 3d "destination" vector
    :return mat: A transform matrix (3x3) which when applied to vec1, aligns it with vec2.
    """
    a = vec1 / np.linalg.norm(vec1)
    b = vec2 / np.linalg.norm(vec2)

    v = np.cross(a, b)
    print(v)

    if any(v):  # if not all zeros then
        c = np.dot(a, b)
        s = np.linalg.norm(v)
        kmat = np.array([[0, -v[2], v[1]], [v[2], 0, -v[0]], [-v[1], v[0], 0]])
        return np.eye(3) + kmat + kmat.dot(kmat) * ((1 - c) / (s ** 2))
    else:
        # cross of all zeros only occurs on identical directions
        if np.allclose(a, b):
            return np.eye(3)
        else:
            return -np.eye(3)


def build_sphere(point, radius=1.0, npoints=12):

    phi = np.linspace(0, 2 * np.pi, 2 * npoints, endpoint=False)
    theta = np.linspace(-np.pi / 2, np.pi / 2, npoints)

    # The mesh of the sphere
    phi, theta = np.meshgrid(phi, theta)
    phi, theta = phi.flatten(), theta.flatten()

    x = radius * np.cos(theta) * np.sin(phi) + point[0]
    y = radius * np.cos(theta) * np.cos(phi) + point[1]
    z = radius * np.sin(theta) + point[2]

    return x, y, z


def build_cylinder(point1, point2, radius=1.0, npoints=12):

    point1, point2 = np.array(point1), np.array(point2)
    vec = point2 - point1

    phi = np.linspace(0, 2 * np.pi, 2 * npoints)
    v = np.linspace(0, np.linalg.norm(vec), 2)

    phi, v = np.meshgrid(phi, v)
    phi, v = phi.flatten(), v.flatten()

    x = radius * np.cos(phi)
    y = radius * np.sin(phi)
    z = v

    # Rotate cilinder
    R = rotation_matrix_from_vectors(np.array([0, 0, 1]), vec)
    x, y, z = np.dot(R, np.array([x, y, z]))

    x += point1[0]
    y += point1[1]
    z += point1[2]

    return x, y, z


def get_line(point1, point2, width=1, color="black", mode="lines", **kwargs):
    return go.Scatter3d(
        mode=mode,
        x=[point1[0], point2[0]],
        y=[point1[1], point2[1]],
        z=[point1[2], point2[2]],
        line=dict(color=color, width=width),
        **kwargs
    )


def get_sphere(point, radius, color, surface="matte"):

    lightning = surface_materials[surface]
    x, y, z = build_sphere(point, radius)

    return go.Mesh3d(
        x=x,
        y=y,
        z=z,
        alphahull=0,
        color=color,
        flatshading=False,
        cmin=-7,  # a trick to get a nice plot (z.min()=-3.31909)
        lighting=lightning,
        lightposition=dict(x=100, y=100, z=0),
    )


def get_cylinder(point1, point2, radius, color, surface="matte"):

    lighting = surface_materials[surface]
    x, y, z = build_cylinder(point1, point2, radius)

    mesh = go.Mesh3d(
        x=x,
        y=y,
        z=z,
        color=color,
        alphahull=0,
        flatshading=True,
        cmin=-7,
        lighting=lighting,
        lightposition=dict(x=100, y=200, z=0),
    )

    return mesh
