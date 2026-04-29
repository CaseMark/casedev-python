# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = [
    "RunGetDetailsResponse",
    "Result",
    "ResultFinalResponse",
    "ResultLogs",
    "Step",
    "Usage",
    "UsageEntry",
    "UsageSummary",
]


class ResultFinalResponse(BaseModel):
    """Compact agent-facing result summary and execution issues"""

    created_object_ids: Optional[List[str]] = FieldInfo(alias="createdObjectIds", default=None)

    issues: Optional[List[str]] = None

    summary: Optional[str] = None


class ResultLogs(BaseModel):
    """Sandbox execution logs (runtime server + runner script)"""

    opencode: Optional[str] = None
    """Legacy runtime server stdout/stderr"""

    runner: Optional[str] = None
    """Runner script stdout/stderr"""

    runtime: Optional[str] = None
    """Runtime server stdout/stderr"""


class Result(BaseModel):
    """Final output from the agent"""

    final_response: Optional[ResultFinalResponse] = FieldInfo(alias="finalResponse", default=None)
    """Compact agent-facing result summary and execution issues"""

    logs: Optional[ResultLogs] = None
    """Sandbox execution logs (runtime server + runner script)"""

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


class UsageEntry(BaseModel):
    id: Optional[str] = None

    completion_tokens: Optional[int] = FieldInfo(alias="completionTokens", default=None)

    cost_micros: Optional[int] = FieldInfo(alias="costMicros", default=None)

    endpoint: Optional[str] = None

    kind: Optional[Literal["llm", "api"]] = None

    metadata: Optional[object] = None

    method: Optional[str] = None

    model: Optional[str] = None

    prompt_tokens: Optional[int] = FieldInfo(alias="promptTokens", default=None)

    service: Optional[str] = None

    status_code: Optional[int] = FieldInfo(alias="statusCode", default=None)

    timestamp: Optional[datetime] = None

    total_tokens: Optional[int] = FieldInfo(alias="totalTokens", default=None)


class UsageSummary(BaseModel):
    cost_micros: Optional[int] = FieldInfo(alias="costMicros", default=None)

    total_input_tokens: Optional[int] = FieldInfo(alias="totalInputTokens", default=None)

    total_output_tokens: Optional[int] = FieldInfo(alias="totalOutputTokens", default=None)

    total_tokens: Optional[int] = FieldInfo(alias="totalTokens", default=None)


class Usage(BaseModel):
    """Token usage statistics"""

    duration_ms: Optional[int] = FieldInfo(alias="durationMs", default=None)

    entries: Optional[List[UsageEntry]] = None

    input_tokens: Optional[int] = FieldInfo(alias="inputTokens", default=None)

    model: Optional[str] = None

    output_tokens: Optional[int] = FieldInfo(alias="outputTokens", default=None)

    summary: Optional[UsageSummary] = None

    tool_calls: Optional[int] = FieldInfo(alias="toolCalls", default=None)


class RunGetDetailsResponse(BaseModel):
    id: Optional[str] = None

    agent_id: Optional[str] = FieldInfo(alias="agentId", default=None)

    completed_at: Optional[datetime] = FieldInfo(alias="completedAt", default=None)

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    guidance: Optional[str] = None

    modal_sandbox_id: Optional[str] = FieldInfo(alias="modalSandboxId", default=None)
    """Deprecated legacy Modal sandbox ID. Prefer `provider` and `runtimeId`."""

    model: Optional[str] = None

    prompt: Optional[str] = None

    provider: Optional[Literal["daytona", "vercel"]] = None
    """Runtime provider for this run"""

    result: Optional[Result] = None
    """Final output from the agent"""

    runtime_id: Optional[str] = FieldInfo(alias="runtimeId", default=None)
    """Provider-specific runtime identifier"""

    runtime_state: Optional[Literal["running", "stopped", "archived", "ended", "error"]] = FieldInfo(
        alias="runtimeState", default=None
    )
    """Current runtime state, when available"""

    started_at: Optional[datetime] = FieldInfo(alias="startedAt", default=None)

    status: Optional[Literal["queued", "running", "completed", "failed", "cancelled"]] = None

    steps: Optional[List[Step]] = None

    usage: Optional[Usage] = None
    """Token usage statistics"""

    workflow_id: Optional[str] = FieldInfo(alias="workflowId", default=None)
    """Durable workflow run ID"""
