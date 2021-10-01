""" Populate this file if your component requires its own models """

from cmselemental.models import InputProc, OutputProc
from mmelemental.models import Molecule
from mmelemental.models.collect import Ensemble
from pydantic import Field
from typing import Union, Optional, Dict, Any

__all__ = ["InputCoarse", "OutputCoarse"]


class InputCoarse(InputProc):
	"""An input model for mmic_cg."""

	molecule: Optional[Dict[str, Molecule]] = Field(
		None,
		description="The selected molecules used for coarse-graining"
		)

	ensemble: Optional[Dict[str, Ensemble]] = Field(
		None,
		description="The selected molecules used for coarse-graining"
		)

	method: str = Field(
		...,
		description="The name of the cg method. Example: 'spacewarping'"
		)

	method_keywords: Optional[Dict[str, Any]] = Field(
		None,
		description="The args used to specifi details in different cg method."
		)

class OutputCoarse(OutputProc):
	"""An output model for mmic_cg."""

	proc_input: InputCoarse = Field(
		...,
		description="Input schema used to compute cg variables"
		)

	molecule: Optional[Dict[str, Molecule]] = Field(
		None, description="Coarse-grained output molecule."
	)

	ensemble: Optional[Dict[str, Ensemble]] = Field(
		None,
		description="Ensemble output for a series of microstates of molecules. "
		"See the :class:``Ensemble`` class.",
	)