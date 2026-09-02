from app.services.tools.registry import get_tool



def execute_agent_tool(
    tool_name: str,
    **kwargs
):

    tool = get_tool(
        tool_name
    )


    if not tool:

        raise ValueError(
            f"Tool '{tool_name}' not found"
        )


    return tool(
        **kwargs
    )