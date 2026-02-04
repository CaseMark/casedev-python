# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["V1GetUsageResponse", "Period", "Pricing", "Project", "ProjectCosts", "Totals"]


class Period(BaseModel):
    end: Optional[datetime] = None
    """End of the billing period"""

    start: Optional[datetime] = None
    """Start of the billing period"""


class Pricing(BaseModel):
    """Current pricing rates"""

    branch_per_month: Optional[float] = FieldInfo(alias="branchPerMonth", default=None)
    """Cost per branch per month in dollars"""

    compute_per_cu_hour: Optional[float] = FieldInfo(alias="computePerCuHour", default=None)
    """Cost per compute unit hour in dollars"""

    free_branches: Optional[int] = FieldInfo(alias="freeBranches", default=None)
    """Number of free branches included"""

    storage_per_gb_month: Optional[float] = FieldInfo(alias="storagePerGbMonth", default=None)
    """Cost per GB of storage per month in dollars"""

    transfer_per_gb: Optional[float] = FieldInfo(alias="transferPerGb", default=None)
    """Cost per GB of data transfer in dollars"""


class ProjectCosts(BaseModel):
    branches: Optional[str] = None

    compute: Optional[str] = None

    storage: Optional[str] = None

    total: Optional[str] = None

    transfer: Optional[str] = None


class Project(BaseModel):
    id: Optional[str] = None

    branch_count: Optional[int] = FieldInfo(alias="branchCount", default=None)

    compute_cu_hours: Optional[float] = FieldInfo(alias="computeCuHours", default=None)

    costs: Optional[ProjectCosts] = None

    last_updated: Optional[datetime] = FieldInfo(alias="lastUpdated", default=None)

    project_id: Optional[str] = FieldInfo(alias="projectId", default=None)

    project_name: Optional[str] = FieldInfo(alias="projectName", default=None)

    storage_gb_months: Optional[float] = FieldInfo(alias="storageGbMonths", default=None)

    transfer_gb: Optional[float] = FieldInfo(alias="transferGb", default=None)


class Totals(BaseModel):
    """Aggregated totals across all projects"""

    branch_cost_dollars: Optional[str] = FieldInfo(alias="branchCostDollars", default=None)
    """Total branch cost formatted as dollars"""

    compute_cost_dollars: Optional[str] = FieldInfo(alias="computeCostDollars", default=None)
    """Total compute cost formatted as dollars"""

    compute_cu_hours: Optional[float] = FieldInfo(alias="computeCuHours", default=None)
    """Total compute unit hours"""

    storage_cost_dollars: Optional[str] = FieldInfo(alias="storageCostDollars", default=None)
    """Total storage cost formatted as dollars"""

    storage_gb_months: Optional[float] = FieldInfo(alias="storageGbMonths", default=None)
    """Total storage in GB-months"""

    total_branches: Optional[int] = FieldInfo(alias="totalBranches", default=None)
    """Total number of branches"""

    total_cost_dollars: Optional[str] = FieldInfo(alias="totalCostDollars", default=None)
    """Total cost formatted as dollars"""

    transfer_cost_dollars: Optional[str] = FieldInfo(alias="transferCostDollars", default=None)
    """Total transfer cost formatted as dollars"""

    transfer_gb: Optional[float] = FieldInfo(alias="transferGb", default=None)
    """Total data transfer in GB"""


class V1GetUsageResponse(BaseModel):
    period: Optional[Period] = None

    pricing: Optional[Pricing] = None
    """Current pricing rates"""

    project_count: Optional[int] = FieldInfo(alias="projectCount", default=None)
    """Total number of projects with usage"""

    projects: Optional[List[Project]] = None
    """Usage breakdown by project"""

    totals: Optional[Totals] = None
    """Aggregated totals across all projects"""
