from typing import Callable


TOOLS: dict[str, Callable] = {}



def register_tool(
    name: str,
    function: Callable
):

    TOOLS[name] = function



def get_tool(
    name: str
):

    return TOOLS.get(name)