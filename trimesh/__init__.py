'''
trimesh.py
========
Python library for loading triangular meshes and doing simple operations on them. Included loaders are binary/ASCII STL and Wavefront (OBJ), included exporters are binary STL or COLLADA. If Assimp/pyassimp are available, meshes can be loaded using the assimp loaders.

Using
-----
    >>> import trimesh
    >>> m = trimesh.load_mesh('models/ballA.off')
    >>> m.show()

'''

from .base    import Trimesh
from .points  import unitize, transform_points
from .io.load import load_mesh, available_formats
from .        import transformations
