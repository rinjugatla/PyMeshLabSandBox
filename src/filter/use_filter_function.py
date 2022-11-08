import pymeshlab

ms = pymeshlab.MeshSet()
ms.load_new_mesh('./../../sample/2hole.stl')

ms.meshing_decimation_quadric_edge_collapse(
    targetperc = 0.5, 
    qualitythr = 0.9, 
    preserveboundary = True)

ms.save_current_mesh('2hole_optimized_by_script_function.stl')