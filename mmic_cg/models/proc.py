""" Populate this file if your component requires its own models """

from cmselemental.models import ProcInput, ProcOutput
from mmelemental.models import Molecule, Ensemble
from pydantic import Field
from typing import Union

__all__ = ["CoarseInput", "CoarseOutput"]


class CoarseInput(ProcInput):
    """An input model for mmic_cg."""

    molecule: Union[Molecule, Ensemble] = Field(...)
    method: str = Field(...)


class CoarseOutput(ProcOutput):
    """An output model for mmic_cg."""

    molecule: Union[Molecule, Ensemble] = Field(
        ..., description="Coarse-grained output molecule."
    )
