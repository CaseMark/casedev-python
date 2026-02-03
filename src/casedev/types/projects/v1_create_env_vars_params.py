# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["V1CreateEnvVarsParams", "EnvVar"]


class V1CreateEnvVarsParams(TypedDict, total=False):
    env_vars: Annotated[Iterable[EnvVar], PropertyInfo(alias="envVars")]


class EnvVar(TypedDict, total=False):
    environment: Required[Literal["production", "preview", "development", "shared"]]

    key: Required[str]

    value: Required[str]

    description: str

    is_secret: Annotated[bool, PropertyInfo(alias="isSecret")]
