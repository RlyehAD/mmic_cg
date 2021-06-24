"""
Components in mmic_cg.
"""

from typing import List, Tuple, Optional
from mmic.components.blueprints import StrategyComponent
from ..models import CoarseInput, CoarseOutput

__all__ = ["CoarseComponent"]


class CoarseComponent(StrategyComponent):
    """A sample component that defines the 3 required methods."""

    @classmethod
    def input(cls):
        return CoarseInput

    @classmethod
    def output(cls):
        return CoarseOutput

    def execute(
        self,
        inputs: CoarseInput,
        extra_outfiles: Optional[List[str]] = None,
        extra_commands: Optional[List[str]] = None,
        scratch_name: Optional[str] = None,
        timeout: Optional[int] = None,
    ) -> Tuple[bool, CoarseOutput]:

        # Convert input dictionary to model
        if isinstance(inputs, dict):
            inputs = self.input()(**inputs)

        # Populate kwargs from inputs
        return True, self.output()(**kwargs)
