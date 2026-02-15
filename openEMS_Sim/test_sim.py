import sys
import os
import numpy as np

# path setup for CSXCAD and openEMS
csxcad_path = '/home/dhanushkramesh/opt/openEMS/local/lib/python3.12/dist-packages/CSXCAD-0.6.3-py3.12-linux-x86_64.egg'
openems_path = '/home/dhanushkramesh/opt/openEMS/local/lib/python3.12/dist-packages/openEMS-0.0.36-py3.12-linux-x86_64.egg'

if csxcad_path not in sys.path:
    sys.path.append(csxcad_path)
if openems_path not in sys.path:
    sys.path.append(openems_path)

from CSXCAD import ContinuousStructure
from openEMS import openEMS

# path for simulation results
print("--- Initializing Official Microstrip Example (Fixed) ---")
Sim_Path = os.path.join(os.getcwd(), 'Sim_Results_MSL')
if not os.path.exists(Sim_Path):
    os.mkdir(Sim_Path)

# FDTD setup
FDTD = openEMS(EndCriteria=1e-4)
FDTD.SetGaussExcite(10e9, 5e9)
FDTD.SetBoundaryCond(['MUR', 'MUR', 'MUR', 'MUR', 'PEC', 'MUR'])

# Geometry setup
CSX = ContinuousStructure()
FDTD.SetCSX(CSX)
mesh = CSX.GetGrid()
mesh.SetDeltaUnit(1e-3) # Units are mm

# defining geometry parameters
trace_width = 2.0
sub_height  = 1.0
sub_eps     = 3.66 

# Building the geometry (materials and objects)

# Substrate
sub = CSX.AddMaterial('FR4', epsilon=sub_eps)
sub.AddBox(priority=0, start=[-10, -10, 0], stop=[30, 10, sub_height])

# Ground Plane (PEC at z=0) - We make it larger than the trace to ensure good grounding
gnd = CSX.AddMetal('Ground')
gnd.AddBox(priority=10, start=[-10, -10, 0], stop=[30, 10, 0])

# Microstrip Trace (PEC at z=1)
trace = CSX.AddMetal('Trace')
trace.AddBox(priority=10, start=[-10, -trace_width/2, sub_height], stop=[30, trace_width/2, sub_height])

# Excitation 
# Port is at x=-10 (Start of the line)
start = [-10,  -trace_width/2, 0]
stop  = [-10,   trace_width/2, sub_height]
port = FDTD.AddLumpedPort(1, 50, start, stop, 'z', 1.0, priority=20, ExciteAmp=1)

# Mesh setup
# We add "Air Padding" so the boundary is NOT at -10.
# We move the mesh boundary to -20 and +40.
mesh.AddLine('x', [-20, 40]) 
mesh.AddLine('y', [-20, 20])
mesh.AddLine('z', [0, sub_height, 10]) # Add air above trace

# Add specific lines for the geometry edges to keep them sharp
mesh.AddLine('x', [-10, 30])
mesh.AddLine('y', [-trace_width/2, trace_width/2])

# Smooth the mesh to reduce staircasing effects, especially around the trace edges
mesh.SmoothMeshLines('x', 1.0, ratio=1.4)
mesh.SmoothMeshLines('y', 1.0, ratio=1.4)
mesh.SmoothMeshLines('z', 0.3, ratio=1.4)

# Run the simulation
print("Writing XML file...")
CSX.Write2XML(os.path.join(Sim_Path, 'msl.xml'))

print("Running openEMS Solver...")
FDTD.Run(Sim_Path, cleanup=True)

print("--- SUCCESS! Simulation Finished ---")