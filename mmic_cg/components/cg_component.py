"""
Components in mmic_cg.
"""

from typing import List, Tuple, Optional, Set

# Import the generic i.e. starting component from MMIC
from mmic.components.blueprints.generic_component import GenericComponent

#from mmic.components.blueprints import StrategyComponent
from ..models import CoarseInput, CoarseOutput

__all__ = ["CoarseComponent"]


class CoarseComponent(GenericComponent):
    """A sample component that defines the 3 required methods."""

    @classmethod
    def input(cls):
        return CoarseInput

    @classmethod
    def output(cls):
        return CoarseOutput

    @property
    def supported_comps(self) -> Set[str]:
        """Returns the supported components e.g. set(['mmic_mda',...]).
        Returns
        -------
        Set[str]
        """
        return set(["mmic_md_protomd"])
