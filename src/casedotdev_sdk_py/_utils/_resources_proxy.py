from __future__ import annotations

from typing import Any
from typing_extensions import override

from ._proxy import LazyProxy


class ResourcesProxy(LazyProxy[Any]):
    """A proxy for the `casedotdev_sdk_py.resources` module.

    This is used so that we can lazily import `casedotdev_sdk_py.resources` only when
    needed *and* so that users can just import `casedotdev_sdk_py` and reference `casedotdev_sdk_py.resources`
    """

    @override
    def __load__(self) -> Any:
        import importlib

        mod = importlib.import_module("casedotdev_sdk_py.resources")
        return mod


resources = ResourcesProxy().__as_proxied__()
