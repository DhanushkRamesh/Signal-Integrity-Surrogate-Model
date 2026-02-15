import sys
import os

#Pth setup - explicitly defining the path just in case
csxcad_path = '/home/dhanushkramesh/opt/openEMS/local/lib/python3.12/dist-packages/CSXCAD-0.6.3-py3.12-linux-x86_64.egg'
openems_path = '/home/dhanushkramesh/opt/openEMS/local/lib/python3.12/dist-packages/openEMS-0.0.36-py3.12-linux-x86_64.egg'

if csxcad_path not in sys.path:
    sys.path.append(csxcad_path)
if openems_path not in sys.path:
    sys.path.append(openems_path)

try:
    import CSXCAD
    from openEMS import openEMS
except ImportError as e:
    print(f"CRITICAL ERROR: {e}")
    sys.exit(1)

# Simulation Setup
print("Starting OpenEMS Simulation for Testing...")
Sim_Path = os.path.join(os.getcwd(), 'Sim_Results')
if not os.path.exists(Sim_Path):
    os.mkdir(Sim_Path)

# FDTD Setup
FDTD = openEMS(EndCriteria=1e-4)
FDTD.SetGaussExcite(10e9, 5e9)
FDTD.SetBoundaryCond(['MUR', 'MUR', 'MUR', 'MUR', 'PEC', 'MUR'])

# Geometry Setup
CSX = CSXCAD.ContinuousStructure()
FDTD.SetCSX(CSX)
mesh = CSX.GetGrid()
mesh.SetDeltaUnit(1e-3)

# Creating Geometry - A simple microstrip line on a substrate
# Substrate
substrate_prop = CSX.AddMaterial('Substrate', epsilon=4.4)
substrate_prop.AddBox(priority=1, start=[-10, -10, 0], stop=[10, 10, 1])

# Metal Trace (Top) - A simple strip
metal_prop = CSX.AddMetal('Trace')
metal_prop.AddBox(priority=10, start=[-10, -1.0, 1], stop=[10, 1.0, 1])

# Adding Excitation
# We add a source voltage between the ground (z=0) and the trace (z=1)
# located at x=0.
exc_prop = CSX.AddExcitation('Source', exc_type=0, exc_val=1) # 0 = E-field excitation
exc_prop.AddBox(start=[-0.5, -1.0, 0], stop=[0.5, 1.0, 1]) 
# Note: The box defines the volume where the E-field is applied (vertical z-field)

# Mesh Setup
mesh.AddLine('x', [-10, 10])
mesh.AddLine('y', [-10, 10])
mesh.AddLine('z', [0, 1])
# Refined mesh
mesh.SmoothMeshLines('x', 1.0, ratio=1.4)
mesh.SmoothMeshLines('y', 1.0, ratio=1.4)
mesh.SmoothMeshLines('z', 0.3, ratio=1.4) 

# Run Simulation
print("Writing XML file...")
CSX.Write2XML(os.path.join(Sim_Path, 'test.xml'))

print("Running Solver...")
FDTD.Run(Sim_Path, cleanup=True)

print("--- SUCCESS! Simulation Complete ---")

