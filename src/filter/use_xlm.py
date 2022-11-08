import pymeshlab

ms = pymeshlab.MeshSet()
ms.load_new_mesh('./../../sample/2hole.stl')

ms.load_filter_script('filter.mlx')
ms.apply_filter_script()

ms.save_current_mesh('2hole_optimized_by_script_xlm.stl')