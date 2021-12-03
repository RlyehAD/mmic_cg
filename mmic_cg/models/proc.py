""" Populate this file if your component requires its own models """

from cmselemental.models import InputProc, OutputProc
from mmelemental.models import Molecule
from pydantic import Field
from typing import Union, Optional, Dict, Any

__all__ = ["InputCoarse", "OutputCoarse"]


class InputCoarse(InputProc):
	"""An input model for mmic_cg."""

	molecule: Dict[str, Molecule] = Field(
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

	molecule: Dict[str, Molecule] = Field(
		None, description="Coarse-grained output molecule."
	)
