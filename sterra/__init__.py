from sterra.sterools import checkPaths
from sterra._outputs_ import _

if created_path := checkPaths():
    for path in created_path:
        _().p(path, logo="Python")