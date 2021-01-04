"""
Generates layouts and surface materials

TODO: To define "styles" object which includes all of the customizations options...
"""

# Layout
default_layout = {
    "scene_aspectmode": "data",
    "margin": dict(r=0, l=0, b=0, t=0),
    "scene_xaxis_showticklabels": False,
    "scene_yaxis_showticklabels": False,
    "scene_zaxis_showticklabels": False,
    "dragmode": "orbit",
    "template": "plotly_white",
    "showlegend": False,
    # "hovermode": False,
    "scene": {
        "xaxis": {
            "showgrid": False,
            "zeroline": False,
            "showline": False,
            "title": "",
            "ticks": "",
            "showticklabels": False,
            "showbackground": False,
            "showspikes": False,
        },
        "yaxis": {
            "showgrid": False,
            "zeroline": False,
            "showline": False,
            "title": "",
            "ticks": "",
            "showticklabels": False,
            "showbackground": False,
            "showspikes": False,
        },
        "zaxis": {
            "showgrid": False,
            "zeroline": False,
            "showline": False,
            "title": "",
            "ticks": "",
            "showticklabels": False,
            "showbackground": False,
            "showspikes": False,
        },
    },
}


# Materials
surface_materials = {
    "matte": {
        "ambient": 0.60,
        "diffuse": 0.35,
        "fresnel": 0.05,
        "specular": 0.03,
        "roughness": 0.05,
        "facenormalsepsilon": 1e-15,
        "vertexnormalsepsilon": 1e-15,
    },
    "shiny": {
        "ambient": 0.3,
        "diffuse": 0.85,
        "fresnel": 0.10,
        "specular": 0.70,
        "roughness": 0.05,
        "facenormalsepsilon": 1e-15,
        "vertexnormalsepsilon": 1e-15,
    },
    "orbs": {
        "ambient": 0.3,
        "diffuse": 0.6,
        "fresnel": 0.10,
        "specular": 0.70,
        "roughness": 0.9,
        "facenormalsepsilon": 1e-15,
        "vertexnormalsepsilon": 1e-15,
    },
    "glass": {
        "ambient": 0.3,
        "diffuse": 0.1,
        "fresnel": 0.45,
        "specular": 0.70,
        "roughness": 0.1,
        "facenormalsepsilon": 1e-15,
        "vertexnormalsepsilon": 1e-15,
    },
}
