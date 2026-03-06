# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["RunGetDetailsResponse", "Result", "ResultFinalResponse", "ResultLogs", "Step", "Usage"]


class ResultFinalResponse(BaseModel):
    """Compact agent-facing result summary and execution issues"""

    created_object_ids: Optional[List[str]] = FieldInfo(alias="createdObjectIds", default=None)

    issues: Optional[List[str]] = None

    summary: Optional[str] = None


class ResultLogs(BaseModel):
    """Sandbox execution logs (OpenCode server + runner script)"""

    opencode: Optional[str] = None
    """OpenCode server stdout/stderr"""

    runner: Optional[str] = None
    """Runner script stdout/stderr"""


class Result(BaseModel):
    """Final output from the agent"""

    final_response: Optional[ResultFinalResponse] = FieldInfo(alias="finalResponse", default=None)
    """Compact agent-facing result summary and execution issues"""

    logs: Optional[ResultLogs] = None
    """Sandbox execution logs (OpenCode server + runner script)"""

    output: Optional[str] = None

    output_object_ids: Optional[List[str]] = FieldInfo(alias="outputObjectIds", default=None)


class Step(BaseModel):
    id: Optional[str] = None

    content: Optional[str] = None

    duration_ms: Optional[int] = FieldInfo(alias="durationMs", default=None)

    timestamp: Optional[datetime] = None

    tool_input: Optional[object] = FieldInfo(alias="toolInput", default=None)

    tool_name: Optional[str] = FieldInfo(alias="toolName", default=None)

    tool_output: Optional[object] = FieldInfo(alias="toolOutput", default=None)

    type: Optional[Literal["output", "thinking", "tool_call", "tool_result"]] = None


class Usage(BaseModel):
    """Token usage statistics"""

    duration_ms: Optional[int] = FieldInfo(alias="durationMs", default=None)

    input_tokens: Optional[int] = FieldInfo(alias="inputTokens", default=None)

    model: Optional[str] = None

    output_tokens: Optional[int] = FieldInfo(alias="outputTokens", default=None)

    tool_calls: Optional[int] = FieldInfo(alias="toolCalls", default=None)


class RunGetDetailsResponse(BaseModel):
    id: Optional[str] = None

    agent_id: Optional[str] = FieldInfo(alias="agentId", default=None)

    completed_at: Optional[datetime] = FieldInfo(alias="completedAt", default=None)

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    guidance: Optional[str] = None

    modal_sandbox_id: Optional[str] = FieldInfo(alias="modalSandboxId", default=None)
    """Modal sandbox ID (available once sandbox is created)"""

    model: Optional[str] = None

    prompt: Optional[str] = None

    result: Optional[Result] = None
    """Final output from the agent"""

    started_at: Optional[datetime] = FieldInfo(alias="startedAt", default=None)

    status: Optional[Literal["queued", "running", "completed", "failed", "cancelled"]] = None

    steps: Optional[List[Step]] = None

    usage: Optional[Usage] = None
    """Token usage statistics"""

    workflow_id: Optional[str] = FieldInfo(alias="workflowId", default=None)
    """Durable workflow run ID"""
