"""Top-level package for Infinite AI Array."""

__author__ = """Ian Bicking"""
__email__ = "ian@ianbicking.org"
__version__ = "0.1.0"

import sys

from .infinite_ai_array import InfiniteAIArray, InfiniteAIDict
from .magicmodule import MagicModule

magic = sys.modules[__name__ + ".magic"] = MagicModule()


def set_verbose(verbose=True):
    """Set verbose mode for all clients."""
    from .engine_ollama import llm_engine

    llm_engine.verbose = verbose