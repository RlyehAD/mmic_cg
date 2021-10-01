"""
Components in mmic_cg.
"""

from typing import List, Tuple, Optional, Set

# Import the generic i.e. starting component from MMIC
from mmic.components.blueprints import GenericComponent

#from mmic.components.blueprints import StrategyComponent
from ..models import InputCoarse, OutputCoarse

__all__ = ["CoarseComponent"]


class CoarseComponent(GenericComponent):
    """A sample component that defines the 3 required methods."""

    @classmethod
    def input(cls):
        return InputCoarse

    @classmethod
    def output(cls):
        return OutputCoarse

    @property
    def supported_comps(self) -> Set[str]:
        """Returns the supported components e.g. set(['mmic_mda',...]).
        Returns
        -------
        Set[str]
        """
        return set(["mmic_md_protomd"])
