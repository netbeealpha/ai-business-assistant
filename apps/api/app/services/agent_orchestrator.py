from app.services.llm_agent_brain import decide_with_llm

from app.services.agent_executor import (
    execute_agent_tool
)



def run_agent(
    query: str,
    **kwargs
):

    decision = decide_with_llm(
        query
    )


    result = execute_agent_tool(
        tool_name=decision.tool,
        query=decision.entity,
        **kwargs
    )


    return {
        "decision": decision,
        "result": result
    }