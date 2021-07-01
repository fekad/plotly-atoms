from pymatgen import Lattice, Structure
from plotly_atoms import Figure


coords = [[0, 0, 0], [0.75, 0.5, 0.75]]
lattice = Lattice.from_parameters(a=3.84, b=3.84, c=3.84, alpha=120, beta=90, gamma=60)
struct = Structure(lattice, ["Si", "Si"], coords)
print(struct)


fig = Figure()
fig.add_structure(struct, supercell=[2, 2, 2])
fig.add_unitcell(struct)

fig.show()