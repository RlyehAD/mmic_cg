[//]: # (Badges)
[![GitHub Actions Build Status](https://github.com/molssi/mmic_cg/workflows/CI/badge.svg)](https://github.com/molssi/mmic_cg/actions?query=workflow%3ACI)
[![codecov](https://codecov.io/gh/molssi/mmic_cg/branch/main/graph/badge.svg)](https://codecov.io/gh/molssi/mmic_cg/branch/main)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/molssi-mint/mmic_cg.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/molssi/mmic_cg/context:python)

Forcefield param assignment component
========================================
This is part of the [MolSSI](http://molssi.org) Molecular Mechanics Interoperable Components ([MMIC](https://github.com/MolSSI/mmic)) project. This package provides a component for coarse-graining molecules.

<p align="center">
<img src="mmic_cg/data/cg_component.png">
</p>

# Basic Usage
```python
# Import main component for coarse-graining
from mmic_cg.components import CoarseComponent

# Import a molecule model that complies with MMSchema
from mmelemental.models import Molecule

# Create MMSchema molecule
mol = Molecule.from_file(path_to_file)

# Create input for coarse-graining a molecule with protoMD
cgIn = {
    "molecule": mol, 
    "method": "spacewarping",
    "keywords": {
        "kmax": 1,
        "polynomial": "legendre",
    },
}

# Execute coarse-graining
cgOut = CoarseComponent.compute(cgInput)

# Extract MMSchema CG mol
cgMol = cgOutput.mol
```
 
Project based on the 
[Computational Molecular Science Python Cookiecutter](https://github.com/molssi/cookiecutter-cms) version 1.1.
