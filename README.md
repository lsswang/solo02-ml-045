# Small grid motion and object rearrangement

Python 3.11 standard library; run `python demo.py`.

The existing motion routine returns a four-neighbour point path among static
blocked cells. The abstract task routine can move between named sites and
pick/place identified objects, but has no orientation, carried footprint, door
or grid execution model. Both ordinary entries are runnable. New physical
snapshots and goals use the contracts in the question. Fixtures are synthetic
finite grids and do not represent continuous collision or real robot safety.
