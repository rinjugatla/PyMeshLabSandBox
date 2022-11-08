import pymeshlab

ms = pymeshlab.MeshSet()
ms.load_new_mesh('./../../sample/2hole.stl')

# If the path contains double-byte characters, saving will fail.
# NG
ms.save_current_mesh('./あ/2hole.stl')

# NG
ms.save_current_mesh('./い_2hole.stl')