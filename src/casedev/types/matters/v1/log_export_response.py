# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from ...._models import BaseModel

__all__ = ["LogExportResponse"]


class LogExportResponse(BaseModel):
    data: Optional[List[Dict[str, object]]] = None
