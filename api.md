# Agent

## V1

### Agents

Types:

```python
from casedev.types.agent.v1 import (
    AgentCreateResponse,
    AgentRetrieveResponse,
    AgentUpdateResponse,
    AgentListResponse,
    AgentDeleteResponse,
)
```

Methods:

- <code title="post /agent/v1/agents">client.agent.v1.agents.<a href="./src/casedev/resources/agent/v1/agents.py">create</a>(\*\*<a href="src/casedev/types/agent/v1/agent_create_params.py">params</a>) -> <a href="./src/casedev/types/agent/v1/agent_create_response.py">AgentCreateResponse</a></code>
- <code title="get /agent/v1/agents/{id}">client.agent.v1.agents.<a href="./src/casedev/resources/agent/v1/agents.py">retrieve</a>(id) -> <a href="./src/casedev/types/agent/v1/agent_retrieve_response.py">AgentRetrieveResponse</a></code>
- <code title="patch /agent/v1/agents/{id}">client.agent.v1.agents.<a href="./src/casedev/resources/agent/v1/agents.py">update</a>(id, \*\*<a href="src/casedev/types/agent/v1/agent_update_params.py">params</a>) -> <a href="./src/casedev/types/agent/v1/agent_update_response.py">AgentUpdateResponse</a></code>
- <code title="get /agent/v1/agents">client.agent.v1.agents.<a href="./src/casedev/resources/agent/v1/agents.py">list</a>() -> <a href="./src/casedev/types/agent/v1/agent_list_response.py">AgentListResponse</a></code>
- <code title="delete /agent/v1/agents/{id}">client.agent.v1.agents.<a href="./src/casedev/resources/agent/v1/agents.py">delete</a>(id) -> <a href="./src/casedev/types/agent/v1/agent_delete_response.py">AgentDeleteResponse</a></code>

### Run

Types:

```python
from casedev.types.agent.v1 import (
    RunCreateResponse,
    RunCancelResponse,
    RunExecResponse,
    RunGetDetailsResponse,
    RunGetStatusResponse,
    RunWatchResponse,
)
```

Methods:

- <code title="post /agent/v1/run">client.agent.v1.run.<a href="./src/casedev/resources/agent/v1/run.py">create</a>(\*\*<a href="src/casedev/types/agent/v1/run_create_params.py">params</a>) -> <a href="./src/casedev/types/agent/v1/run_create_response.py">RunCreateResponse</a></code>
- <code title="post /agent/v1/run/{id}/cancel">client.agent.v1.run.<a href="./src/casedev/resources/agent/v1/run.py">cancel</a>(id) -> <a href="./src/casedev/types/agent/v1/run_cancel_response.py">RunCancelResponse</a></code>
- <code title="post /agent/v1/run/{id}/exec">client.agent.v1.run.<a href="./src/casedev/resources/agent/v1/run.py">exec</a>(id) -> <a href="./src/casedev/types/agent/v1/run_exec_response.py">RunExecResponse</a></code>
- <code title="get /agent/v1/run/{id}/details">client.agent.v1.run.<a href="./src/casedev/resources/agent/v1/run.py">get_details</a>(id) -> <a href="./src/casedev/types/agent/v1/run_get_details_response.py">RunGetDetailsResponse</a></code>
- <code title="get /agent/v1/run/{id}/status">client.agent.v1.run.<a href="./src/casedev/resources/agent/v1/run.py">get_status</a>(id) -> <a href="./src/casedev/types/agent/v1/run_get_status_response.py">RunGetStatusResponse</a></code>
- <code title="post /agent/v1/run/{id}/watch">client.agent.v1.run.<a href="./src/casedev/resources/agent/v1/run.py">watch</a>(id, \*\*<a href="src/casedev/types/agent/v1/run_watch_params.py">params</a>) -> <a href="./src/casedev/types/agent/v1/run_watch_response.py">RunWatchResponse</a></code>

# System

Types:

```python
from casedev.types import SystemListServicesResponse
```

Methods:

- <code title="get /services">client.system.<a href="./src/casedev/resources/system.py">list_services</a>() -> <a href="./src/casedev/types/system_list_services_response.py">SystemListServicesResponse</a></code>

# Applications

## V1

### Deployments

Methods:

- <code title="post /applications/v1/deployments">client.applications.v1.deployments.<a href="./src/casedev/resources/applications/v1/deployments.py">create</a>(\*\*<a href="src/casedev/types/applications/v1/deployment_create_params.py">params</a>) -> None</code>
- <code title="get /applications/v1/deployments/{id}">client.applications.v1.deployments.<a href="./src/casedev/resources/applications/v1/deployments.py">retrieve</a>(id, \*\*<a href="src/casedev/types/applications/v1/deployment_retrieve_params.py">params</a>) -> None</code>
- <code title="get /applications/v1/deployments">client.applications.v1.deployments.<a href="./src/casedev/resources/applications/v1/deployments.py">list</a>(\*\*<a href="src/casedev/types/applications/v1/deployment_list_params.py">params</a>) -> None</code>
- <code title="post /applications/v1/deployments/{id}/cancel">client.applications.v1.deployments.<a href="./src/casedev/resources/applications/v1/deployments.py">cancel</a>(id, \*\*<a href="src/casedev/types/applications/v1/deployment_cancel_params.py">params</a>) -> None</code>
- <code title="post /applications/v1/deployments/from-files">client.applications.v1.deployments.<a href="./src/casedev/resources/applications/v1/deployments.py">create_from_files</a>() -> None</code>
- <code title="get /applications/v1/deployments/{id}/logs">client.applications.v1.deployments.<a href="./src/casedev/resources/applications/v1/deployments.py">get_logs</a>(id, \*\*<a href="src/casedev/types/applications/v1/deployment_get_logs_params.py">params</a>) -> None</code>
- <code title="get /applications/v1/deployments/{id}/status">client.applications.v1.deployments.<a href="./src/casedev/resources/applications/v1/deployments.py">get_status</a>(id) -> None</code>
- <code title="get /applications/v1/deployments/{id}/stream">client.applications.v1.deployments.<a href="./src/casedev/resources/applications/v1/deployments.py">stream</a>(id, \*\*<a href="src/casedev/types/applications/v1/deployment_stream_params.py">params</a>) -> None</code>

### Projects

Types:

```python
from casedev.types.applications.v1 import ProjectListResponse
```

Methods:

- <code title="post /applications/v1/projects">client.applications.v1.projects.<a href="./src/casedev/resources/applications/v1/projects.py">create</a>(\*\*<a href="src/casedev/types/applications/v1/project_create_params.py">params</a>) -> None</code>
- <code title="get /applications/v1/projects/{id}">client.applications.v1.projects.<a href="./src/casedev/resources/applications/v1/projects.py">retrieve</a>(id) -> None</code>
- <code title="get /applications/v1/projects">client.applications.v1.projects.<a href="./src/casedev/resources/applications/v1/projects.py">list</a>() -> <a href="./src/casedev/types/applications/v1/project_list_response.py">ProjectListResponse</a></code>
- <code title="delete /applications/v1/projects/{id}">client.applications.v1.projects.<a href="./src/casedev/resources/applications/v1/projects.py">delete</a>(id, \*\*<a href="src/casedev/types/applications/v1/project_delete_params.py">params</a>) -> None</code>
- <code title="post /applications/v1/projects/{id}/deployments">client.applications.v1.projects.<a href="./src/casedev/resources/applications/v1/projects.py">create_deployment</a>(id, \*\*<a href="src/casedev/types/applications/v1/project_create_deployment_params.py">params</a>) -> None</code>
- <code title="post /applications/v1/projects/{id}/domains">client.applications.v1.projects.<a href="./src/casedev/resources/applications/v1/projects.py">create_domain</a>(id, \*\*<a href="src/casedev/types/applications/v1/project_create_domain_params.py">params</a>) -> None</code>
- <code title="post /applications/v1/projects/{id}/env">client.applications.v1.projects.<a href="./src/casedev/resources/applications/v1/projects.py">create_env</a>(id, \*\*<a href="src/casedev/types/applications/v1/project_create_env_params.py">params</a>) -> None</code>
- <code title="delete /applications/v1/projects/{id}/domains/{domain}">client.applications.v1.projects.<a href="./src/casedev/resources/applications/v1/projects.py">delete_domain</a>(domain, \*, id) -> None</code>
- <code title="delete /applications/v1/projects/{id}/env/{envId}">client.applications.v1.projects.<a href="./src/casedev/resources/applications/v1/projects.py">delete_env</a>(env_id, \*, id) -> None</code>
- <code title="get /applications/v1/projects/{id}/runtime-logs">client.applications.v1.projects.<a href="./src/casedev/resources/applications/v1/projects.py">get_runtime_logs</a>(id, \*\*<a href="src/casedev/types/applications/v1/project_get_runtime_logs_params.py">params</a>) -> None</code>
- <code title="get /applications/v1/projects/{id}/deployments">client.applications.v1.projects.<a href="./src/casedev/resources/applications/v1/projects.py">list_deployments</a>(id, \*\*<a href="src/casedev/types/applications/v1/project_list_deployments_params.py">params</a>) -> None</code>
- <code title="get /applications/v1/projects/{id}/domains">client.applications.v1.projects.<a href="./src/casedev/resources/applications/v1/projects.py">list_domains</a>(id) -> None</code>
- <code title="get /applications/v1/projects/{id}/env">client.applications.v1.projects.<a href="./src/casedev/resources/applications/v1/projects.py">list_env</a>(id, \*\*<a href="src/casedev/types/applications/v1/project_list_env_params.py">params</a>) -> None</code>

### Workflows

Methods:

- <code title="get /applications/v1/workflows/{id}/status">client.applications.v1.workflows.<a href="./src/casedev/resources/applications/v1/workflows.py">get_status</a>(id, \*\*<a href="src/casedev/types/applications/v1/workflow_get_status_params.py">params</a>) -> None</code>

# Compute

## V1

Types:

```python
from casedev.types.compute import V1GetUsageResponse
```

Methods:

- <code title="get /compute/v1/pricing">client.compute.v1.<a href="./src/casedev/resources/compute/v1/v1.py">get_pricing</a>() -> None</code>
- <code title="get /compute/v1/usage">client.compute.v1.<a href="./src/casedev/resources/compute/v1/v1.py">get_usage</a>(\*\*<a href="src/casedev/types/compute/v1_get_usage_params.py">params</a>) -> <a href="./src/casedev/types/compute/v1_get_usage_response.py">V1GetUsageResponse</a></code>

### Environments

Types:

```python
from casedev.types.compute.v1 import (
    EnvironmentCreateResponse,
    EnvironmentRetrieveResponse,
    EnvironmentListResponse,
    EnvironmentDeleteResponse,
    EnvironmentSetDefaultResponse,
)
```

Methods:

- <code title="post /compute/v1/environments">client.compute.v1.environments.<a href="./src/casedev/resources/compute/v1/environments.py">create</a>(\*\*<a href="src/casedev/types/compute/v1/environment_create_params.py">params</a>) -> <a href="./src/casedev/types/compute/v1/environment_create_response.py">EnvironmentCreateResponse</a></code>
- <code title="get /compute/v1/environments/{name}">client.compute.v1.environments.<a href="./src/casedev/resources/compute/v1/environments.py">retrieve</a>(name) -> <a href="./src/casedev/types/compute/v1/environment_retrieve_response.py">EnvironmentRetrieveResponse</a></code>
- <code title="get /compute/v1/environments">client.compute.v1.environments.<a href="./src/casedev/resources/compute/v1/environments.py">list</a>() -> <a href="./src/casedev/types/compute/v1/environment_list_response.py">EnvironmentListResponse</a></code>
- <code title="delete /compute/v1/environments/{name}">client.compute.v1.environments.<a href="./src/casedev/resources/compute/v1/environments.py">delete</a>(name) -> <a href="./src/casedev/types/compute/v1/environment_delete_response.py">EnvironmentDeleteResponse</a></code>
- <code title="post /compute/v1/environments/{name}/default">client.compute.v1.environments.<a href="./src/casedev/resources/compute/v1/environments.py">set_default</a>(name) -> <a href="./src/casedev/types/compute/v1/environment_set_default_response.py">EnvironmentSetDefaultResponse</a></code>

### InstanceTypes

Types:

```python
from casedev.types.compute.v1 import InstanceTypeListResponse
```

Methods:

- <code title="get /compute/v1/instance-types">client.compute.v1.instance_types.<a href="./src/casedev/resources/compute/v1/instance_types.py">list</a>() -> <a href="./src/casedev/types/compute/v1/instance_type_list_response.py">InstanceTypeListResponse</a></code>

### Instances

Types:

```python
from casedev.types.compute.v1 import (
    InstanceCreateResponse,
    InstanceRetrieveResponse,
    InstanceListResponse,
    InstanceDeleteResponse,
)
```

Methods:

- <code title="post /compute/v1/instances">client.compute.v1.instances.<a href="./src/casedev/resources/compute/v1/instances.py">create</a>(\*\*<a href="src/casedev/types/compute/v1/instance_create_params.py">params</a>) -> <a href="./src/casedev/types/compute/v1/instance_create_response.py">InstanceCreateResponse</a></code>
- <code title="get /compute/v1/instances/{id}">client.compute.v1.instances.<a href="./src/casedev/resources/compute/v1/instances.py">retrieve</a>(id) -> <a href="./src/casedev/types/compute/v1/instance_retrieve_response.py">InstanceRetrieveResponse</a></code>
- <code title="get /compute/v1/instances">client.compute.v1.instances.<a href="./src/casedev/resources/compute/v1/instances.py">list</a>() -> <a href="./src/casedev/types/compute/v1/instance_list_response.py">InstanceListResponse</a></code>
- <code title="delete /compute/v1/instances/{id}">client.compute.v1.instances.<a href="./src/casedev/resources/compute/v1/instances.py">delete</a>(id) -> <a href="./src/casedev/types/compute/v1/instance_delete_response.py">InstanceDeleteResponse</a></code>

### Secrets

Types:

```python
from casedev.types.compute.v1 import (
    SecretCreateResponse,
    SecretListResponse,
    SecretDeleteGroupResponse,
    SecretRetrieveGroupResponse,
    SecretUpdateGroupResponse,
)
```

Methods:

- <code title="post /compute/v1/secrets">client.compute.v1.secrets.<a href="./src/casedev/resources/compute/v1/secrets.py">create</a>(\*\*<a href="src/casedev/types/compute/v1/secret_create_params.py">params</a>) -> <a href="./src/casedev/types/compute/v1/secret_create_response.py">SecretCreateResponse</a></code>
- <code title="get /compute/v1/secrets">client.compute.v1.secrets.<a href="./src/casedev/resources/compute/v1/secrets.py">list</a>(\*\*<a href="src/casedev/types/compute/v1/secret_list_params.py">params</a>) -> <a href="./src/casedev/types/compute/v1/secret_list_response.py">SecretListResponse</a></code>
- <code title="delete /compute/v1/secrets/{group}">client.compute.v1.secrets.<a href="./src/casedev/resources/compute/v1/secrets.py">delete_group</a>(group, \*\*<a href="src/casedev/types/compute/v1/secret_delete_group_params.py">params</a>) -> <a href="./src/casedev/types/compute/v1/secret_delete_group_response.py">SecretDeleteGroupResponse</a></code>
- <code title="get /compute/v1/secrets/{group}">client.compute.v1.secrets.<a href="./src/casedev/resources/compute/v1/secrets.py">retrieve_group</a>(group, \*\*<a href="src/casedev/types/compute/v1/secret_retrieve_group_params.py">params</a>) -> <a href="./src/casedev/types/compute/v1/secret_retrieve_group_response.py">SecretRetrieveGroupResponse</a></code>
- <code title="put /compute/v1/secrets/{group}">client.compute.v1.secrets.<a href="./src/casedev/resources/compute/v1/secrets.py">update_group</a>(group, \*\*<a href="src/casedev/types/compute/v1/secret_update_group_params.py">params</a>) -> <a href="./src/casedev/types/compute/v1/secret_update_group_response.py">SecretUpdateGroupResponse</a></code>

# Database

## V1

Types:

```python
from casedev.types.database import V1GetUsageResponse
```

Methods:

- <code title="get /database/v1/usage">client.database.v1.<a href="./src/casedev/resources/database/v1/v1.py">get_usage</a>() -> <a href="./src/casedev/types/database/v1_get_usage_response.py">V1GetUsageResponse</a></code>

### Projects

Types:

```python
from casedev.types.database.v1 import (
    ProjectCreateResponse,
    ProjectRetrieveResponse,
    ProjectListResponse,
    ProjectDeleteResponse,
    ProjectCreateBranchResponse,
    ProjectGetConnectionResponse,
    ProjectListBranchesResponse,
)
```

Methods:

- <code title="post /database/v1/projects">client.database.v1.projects.<a href="./src/casedev/resources/database/v1/projects.py">create</a>(\*\*<a href="src/casedev/types/database/v1/project_create_params.py">params</a>) -> <a href="./src/casedev/types/database/v1/project_create_response.py">ProjectCreateResponse</a></code>
- <code title="get /database/v1/projects/{id}">client.database.v1.projects.<a href="./src/casedev/resources/database/v1/projects.py">retrieve</a>(id) -> <a href="./src/casedev/types/database/v1/project_retrieve_response.py">ProjectRetrieveResponse</a></code>
- <code title="get /database/v1/projects">client.database.v1.projects.<a href="./src/casedev/resources/database/v1/projects.py">list</a>() -> <a href="./src/casedev/types/database/v1/project_list_response.py">ProjectListResponse</a></code>
- <code title="delete /database/v1/projects/{id}">client.database.v1.projects.<a href="./src/casedev/resources/database/v1/projects.py">delete</a>(id) -> <a href="./src/casedev/types/database/v1/project_delete_response.py">ProjectDeleteResponse</a></code>
- <code title="post /database/v1/projects/{id}/branches">client.database.v1.projects.<a href="./src/casedev/resources/database/v1/projects.py">create_branch</a>(id, \*\*<a href="src/casedev/types/database/v1/project_create_branch_params.py">params</a>) -> <a href="./src/casedev/types/database/v1/project_create_branch_response.py">ProjectCreateBranchResponse</a></code>
- <code title="get /database/v1/projects/{id}/connection">client.database.v1.projects.<a href="./src/casedev/resources/database/v1/projects.py">get_connection</a>(id, \*\*<a href="src/casedev/types/database/v1/project_get_connection_params.py">params</a>) -> <a href="./src/casedev/types/database/v1/project_get_connection_response.py">ProjectGetConnectionResponse</a></code>
- <code title="get /database/v1/projects/{id}/branches">client.database.v1.projects.<a href="./src/casedev/resources/database/v1/projects.py">list_branches</a>(id) -> <a href="./src/casedev/types/database/v1/project_list_branches_response.py">ProjectListBranchesResponse</a></code>

# Format

## V1

Methods:

- <code title="post /format/v1/document">client.format.v1.<a href="./src/casedev/resources/format/v1/v1.py">create_document</a>(\*\*<a href="src/casedev/types/format/v1_create_document_params.py">params</a>) -> BinaryAPIResponse</code>

### Templates

Types:

```python
from casedev.types.format.v1 import (
    TemplateCreateResponse,
    TemplateRetrieveResponse,
    TemplateListResponse,
)
```

Methods:

- <code title="post /format/v1/templates">client.format.v1.templates.<a href="./src/casedev/resources/format/v1/templates.py">create</a>(\*\*<a href="src/casedev/types/format/v1/template_create_params.py">params</a>) -> <a href="./src/casedev/types/format/v1/template_create_response.py">TemplateCreateResponse</a></code>
- <code title="get /format/v1/templates/{id}">client.format.v1.templates.<a href="./src/casedev/resources/format/v1/templates.py">retrieve</a>(id) -> <a href="./src/casedev/types/format/v1/template_retrieve_response.py">TemplateRetrieveResponse</a></code>
- <code title="get /format/v1/templates">client.format.v1.templates.<a href="./src/casedev/resources/format/v1/templates.py">list</a>(\*\*<a href="src/casedev/types/format/v1/template_list_params.py">params</a>) -> <a href="./src/casedev/types/format/v1/template_list_response.py">TemplateListResponse</a></code>

# Legal

## V1

Types:

```python
from casedev.types.legal import (
    V1FindResponse,
    V1GetCitationsResponse,
    V1GetCitationsFromURLResponse,
    V1GetFullTextResponse,
    V1ListJurisdictionsResponse,
    V1PatentSearchResponse,
    V1ResearchResponse,
    V1SimilarResponse,
    V1TrademarkSearchResponse,
    V1VerifyResponse,
)
```

Methods:

- <code title="post /legal/v1/find">client.legal.v1.<a href="./src/casedev/resources/legal/v1.py">find</a>(\*\*<a href="src/casedev/types/legal/v1_find_params.py">params</a>) -> <a href="./src/casedev/types/legal/v1_find_response.py">V1FindResponse</a></code>
- <code title="post /legal/v1/citations">client.legal.v1.<a href="./src/casedev/resources/legal/v1.py">get_citations</a>(\*\*<a href="src/casedev/types/legal/v1_get_citations_params.py">params</a>) -> <a href="./src/casedev/types/legal/v1_get_citations_response.py">V1GetCitationsResponse</a></code>
- <code title="post /legal/v1/citations-from-url">client.legal.v1.<a href="./src/casedev/resources/legal/v1.py">get_citations_from_url</a>(\*\*<a href="src/casedev/types/legal/v1_get_citations_from_url_params.py">params</a>) -> <a href="./src/casedev/types/legal/v1_get_citations_from_url_response.py">V1GetCitationsFromURLResponse</a></code>
- <code title="post /legal/v1/full-text">client.legal.v1.<a href="./src/casedev/resources/legal/v1.py">get_full_text</a>(\*\*<a href="src/casedev/types/legal/v1_get_full_text_params.py">params</a>) -> <a href="./src/casedev/types/legal/v1_get_full_text_response.py">V1GetFullTextResponse</a></code>
- <code title="post /legal/v1/jurisdictions">client.legal.v1.<a href="./src/casedev/resources/legal/v1.py">list_jurisdictions</a>(\*\*<a href="src/casedev/types/legal/v1_list_jurisdictions_params.py">params</a>) -> <a href="./src/casedev/types/legal/v1_list_jurisdictions_response.py">V1ListJurisdictionsResponse</a></code>
- <code title="post /legal/v1/patent-search">client.legal.v1.<a href="./src/casedev/resources/legal/v1.py">patent_search</a>(\*\*<a href="src/casedev/types/legal/v1_patent_search_params.py">params</a>) -> <a href="./src/casedev/types/legal/v1_patent_search_response.py">V1PatentSearchResponse</a></code>
- <code title="post /legal/v1/research">client.legal.v1.<a href="./src/casedev/resources/legal/v1.py">research</a>(\*\*<a href="src/casedev/types/legal/v1_research_params.py">params</a>) -> <a href="./src/casedev/types/legal/v1_research_response.py">V1ResearchResponse</a></code>
- <code title="post /legal/v1/similar">client.legal.v1.<a href="./src/casedev/resources/legal/v1.py">similar</a>(\*\*<a href="src/casedev/types/legal/v1_similar_params.py">params</a>) -> <a href="./src/casedev/types/legal/v1_similar_response.py">V1SimilarResponse</a></code>
- <code title="post /legal/v1/trademark-search">client.legal.v1.<a href="./src/casedev/resources/legal/v1.py">trademark_search</a>(\*\*<a href="src/casedev/types/legal/v1_trademark_search_params.py">params</a>) -> <a href="./src/casedev/types/legal/v1_trademark_search_response.py">V1TrademarkSearchResponse</a></code>
- <code title="post /legal/v1/verify">client.legal.v1.<a href="./src/casedev/resources/legal/v1.py">verify</a>(\*\*<a href="src/casedev/types/legal/v1_verify_params.py">params</a>) -> <a href="./src/casedev/types/legal/v1_verify_response.py">V1VerifyResponse</a></code>

# Llm

Types:

```python
from casedev.types import LlmGetConfigResponse
```

Methods:

- <code title="get /llm/config">client.llm.<a href="./src/casedev/resources/llm/llm.py">get_config</a>() -> <a href="./src/casedev/types/llm_get_config_response.py">LlmGetConfigResponse</a></code>

## V1

Types:

```python
from casedev.types.llm import V1CreateEmbeddingResponse, V1ListModelsResponse
```

Methods:

- <code title="post /llm/v1/embeddings">client.llm.v1.<a href="./src/casedev/resources/llm/v1/v1.py">create_embedding</a>(\*\*<a href="src/casedev/types/llm/v1_create_embedding_params.py">params</a>) -> <a href="./src/casedev/types/llm/v1_create_embedding_response.py">V1CreateEmbeddingResponse</a></code>
- <code title="get /llm/v1/models">client.llm.v1.<a href="./src/casedev/resources/llm/v1/v1.py">list_models</a>() -> <a href="./src/casedev/types/llm/v1_list_models_response.py">V1ListModelsResponse</a></code>

### Chat

Types:

```python
from casedev.types.llm.v1 import ChatCreateCompletionResponse
```

Methods:

- <code title="post /llm/v1/chat/completions">client.llm.v1.chat.<a href="./src/casedev/resources/llm/v1/chat.py">create_completion</a>(\*\*<a href="src/casedev/types/llm/v1/chat_create_completion_params.py">params</a>) -> <a href="./src/casedev/types/llm/v1/chat_create_completion_response.py">ChatCreateCompletionResponse</a></code>

# Memory

## V1

Types:

```python
from casedev.types.memory import (
    V1CreateResponse,
    V1RetrieveResponse,
    V1ListResponse,
    V1DeleteResponse,
    V1DeleteAllResponse,
    V1SearchResponse,
)
```

Methods:

- <code title="post /memory/v1">client.memory.v1.<a href="./src/casedev/resources/memory/v1.py">create</a>(\*\*<a href="src/casedev/types/memory/v1_create_params.py">params</a>) -> <a href="./src/casedev/types/memory/v1_create_response.py">V1CreateResponse</a></code>
- <code title="get /memory/v1/{id}">client.memory.v1.<a href="./src/casedev/resources/memory/v1.py">retrieve</a>(id) -> <a href="./src/casedev/types/memory/v1_retrieve_response.py">V1RetrieveResponse</a></code>
- <code title="get /memory/v1">client.memory.v1.<a href="./src/casedev/resources/memory/v1.py">list</a>(\*\*<a href="src/casedev/types/memory/v1_list_params.py">params</a>) -> <a href="./src/casedev/types/memory/v1_list_response.py">V1ListResponse</a></code>
- <code title="delete /memory/v1/{id}">client.memory.v1.<a href="./src/casedev/resources/memory/v1.py">delete</a>(id) -> <a href="./src/casedev/types/memory/v1_delete_response.py">V1DeleteResponse</a></code>
- <code title="delete /memory/v1">client.memory.v1.<a href="./src/casedev/resources/memory/v1.py">delete_all</a>(\*\*<a href="src/casedev/types/memory/v1_delete_all_params.py">params</a>) -> <a href="./src/casedev/types/memory/v1_delete_all_response.py">V1DeleteAllResponse</a></code>
- <code title="post /memory/v1/search">client.memory.v1.<a href="./src/casedev/resources/memory/v1.py">search</a>(\*\*<a href="src/casedev/types/memory/v1_search_params.py">params</a>) -> <a href="./src/casedev/types/memory/v1_search_response.py">V1SearchResponse</a></code>

# Ocr

## V1

Types:

```python
from casedev.types.ocr import V1RetrieveResponse, V1DownloadResponse, V1ProcessResponse
```

Methods:

- <code title="get /ocr/v1/{id}">client.ocr.v1.<a href="./src/casedev/resources/ocr/v1.py">retrieve</a>(id) -> <a href="./src/casedev/types/ocr/v1_retrieve_response.py">V1RetrieveResponse</a></code>
- <code title="get /ocr/v1/{id}/download/{type}">client.ocr.v1.<a href="./src/casedev/resources/ocr/v1.py">download</a>(type, \*, id) -> str</code>
- <code title="post /ocr/v1/process">client.ocr.v1.<a href="./src/casedev/resources/ocr/v1.py">process</a>(\*\*<a href="src/casedev/types/ocr/v1_process_params.py">params</a>) -> <a href="./src/casedev/types/ocr/v1_process_response.py">V1ProcessResponse</a></code>

# Privilege

## V1

Types:

```python
from casedev.types.privilege import V1DetectResponse
```

Methods:

- <code title="post /privilege/v1/detect">client.privilege.v1.<a href="./src/casedev/resources/privilege/v1.py">detect</a>(\*\*<a href="src/casedev/types/privilege/v1_detect_params.py">params</a>) -> <a href="./src/casedev/types/privilege/v1_detect_response.py">V1DetectResponse</a></code>

# Search

## V1

Types:

```python
from casedev.types.search import (
    V1AnswerResponse,
    V1ContentsResponse,
    V1ResearchResponse,
    V1RetrieveResearchResponse,
    V1SearchResponse,
    V1SimilarResponse,
)
```

Methods:

- <code title="post /search/v1/answer">client.search.v1.<a href="./src/casedev/resources/search/v1.py">answer</a>(\*\*<a href="src/casedev/types/search/v1_answer_params.py">params</a>) -> <a href="./src/casedev/types/search/v1_answer_response.py">V1AnswerResponse</a></code>
- <code title="post /search/v1/contents">client.search.v1.<a href="./src/casedev/resources/search/v1.py">contents</a>(\*\*<a href="src/casedev/types/search/v1_contents_params.py">params</a>) -> <a href="./src/casedev/types/search/v1_contents_response.py">V1ContentsResponse</a></code>
- <code title="post /search/v1/research">client.search.v1.<a href="./src/casedev/resources/search/v1.py">research</a>(\*\*<a href="src/casedev/types/search/v1_research_params.py">params</a>) -> <a href="./src/casedev/types/search/v1_research_response.py">V1ResearchResponse</a></code>
- <code title="get /search/v1/research/{id}">client.search.v1.<a href="./src/casedev/resources/search/v1.py">retrieve_research</a>(id, \*\*<a href="src/casedev/types/search/v1_retrieve_research_params.py">params</a>) -> <a href="./src/casedev/types/search/v1_retrieve_research_response.py">V1RetrieveResearchResponse</a></code>
- <code title="post /search/v1/search">client.search.v1.<a href="./src/casedev/resources/search/v1.py">search</a>(\*\*<a href="src/casedev/types/search/v1_search_params.py">params</a>) -> <a href="./src/casedev/types/search/v1_search_response.py">V1SearchResponse</a></code>
- <code title="post /search/v1/similar">client.search.v1.<a href="./src/casedev/resources/search/v1.py">similar</a>(\*\*<a href="src/casedev/types/search/v1_similar_params.py">params</a>) -> <a href="./src/casedev/types/search/v1_similar_response.py">V1SimilarResponse</a></code>

# Superdoc

## V1

Methods:

- <code title="post /superdoc/v1/annotate">client.superdoc.v1.<a href="./src/casedev/resources/superdoc/v1.py">annotate</a>(\*\*<a href="src/casedev/types/superdoc/v1_annotate_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="post /superdoc/v1/convert">client.superdoc.v1.<a href="./src/casedev/resources/superdoc/v1.py">convert</a>(\*\*<a href="src/casedev/types/superdoc/v1_convert_params.py">params</a>) -> BinaryAPIResponse</code>

# Translate

## V1

Types:

```python
from casedev.types.translate import V1DetectResponse, V1ListLanguagesResponse, V1TranslateResponse
```

Methods:

- <code title="post /translate/v1/detect">client.translate.v1.<a href="./src/casedev/resources/translate/v1.py">detect</a>(\*\*<a href="src/casedev/types/translate/v1_detect_params.py">params</a>) -> <a href="./src/casedev/types/translate/v1_detect_response.py">V1DetectResponse</a></code>
- <code title="get /translate/v1/languages">client.translate.v1.<a href="./src/casedev/resources/translate/v1.py">list_languages</a>(\*\*<a href="src/casedev/types/translate/v1_list_languages_params.py">params</a>) -> <a href="./src/casedev/types/translate/v1_list_languages_response.py">V1ListLanguagesResponse</a></code>
- <code title="post /translate/v1/translate">client.translate.v1.<a href="./src/casedev/resources/translate/v1.py">translate</a>(\*\*<a href="src/casedev/types/translate/v1_translate_params.py">params</a>) -> <a href="./src/casedev/types/translate/v1_translate_response.py">V1TranslateResponse</a></code>

# Vault

Types:

```python
from casedev.types import (
    VaultCreateResponse,
    VaultRetrieveResponse,
    VaultUpdateResponse,
    VaultListResponse,
    VaultDeleteResponse,
    VaultConfirmUploadResponse,
    VaultIngestResponse,
    VaultSearchResponse,
    VaultUploadResponse,
)
```

Methods:

- <code title="post /vault">client.vault.<a href="./src/casedev/resources/vault/vault.py">create</a>(\*\*<a href="src/casedev/types/vault_create_params.py">params</a>) -> <a href="./src/casedev/types/vault_create_response.py">VaultCreateResponse</a></code>
- <code title="get /vault/{id}">client.vault.<a href="./src/casedev/resources/vault/vault.py">retrieve</a>(id) -> <a href="./src/casedev/types/vault_retrieve_response.py">VaultRetrieveResponse</a></code>
- <code title="patch /vault/{id}">client.vault.<a href="./src/casedev/resources/vault/vault.py">update</a>(id, \*\*<a href="src/casedev/types/vault_update_params.py">params</a>) -> <a href="./src/casedev/types/vault_update_response.py">VaultUpdateResponse</a></code>
- <code title="get /vault">client.vault.<a href="./src/casedev/resources/vault/vault.py">list</a>() -> <a href="./src/casedev/types/vault_list_response.py">VaultListResponse</a></code>
- <code title="delete /vault/{id}">client.vault.<a href="./src/casedev/resources/vault/vault.py">delete</a>(id, \*\*<a href="src/casedev/types/vault_delete_params.py">params</a>) -> <a href="./src/casedev/types/vault_delete_response.py">VaultDeleteResponse</a></code>
- <code title="post /vault/{id}/upload/{objectId}/confirm">client.vault.<a href="./src/casedev/resources/vault/vault.py">confirm_upload</a>(object_id, \*, id, \*\*<a href="src/casedev/types/vault_confirm_upload_params.py">params</a>) -> <a href="./src/casedev/types/vault_confirm_upload_response.py">VaultConfirmUploadResponse</a></code>
- <code title="post /vault/{id}/ingest/{objectId}">client.vault.<a href="./src/casedev/resources/vault/vault.py">ingest</a>(object_id, \*, id) -> <a href="./src/casedev/types/vault_ingest_response.py">VaultIngestResponse</a></code>
- <code title="post /vault/{id}/search">client.vault.<a href="./src/casedev/resources/vault/vault.py">search</a>(id, \*\*<a href="src/casedev/types/vault_search_params.py">params</a>) -> <a href="./src/casedev/types/vault_search_response.py">VaultSearchResponse</a></code>
- <code title="post /vault/{id}/upload">client.vault.<a href="./src/casedev/resources/vault/vault.py">upload</a>(id, \*\*<a href="src/casedev/types/vault_upload_params.py">params</a>) -> <a href="./src/casedev/types/vault_upload_response.py">VaultUploadResponse</a></code>

## Events

### Subscriptions

Methods:

- <code title="post /vault/{id}/events/subscriptions">client.vault.events.subscriptions.<a href="./src/casedev/resources/vault/events/subscriptions.py">create</a>(id, \*\*<a href="src/casedev/types/vault/events/subscription_create_params.py">params</a>) -> None</code>
- <code title="patch /vault/{id}/events/subscriptions/{subscriptionId}">client.vault.events.subscriptions.<a href="./src/casedev/resources/vault/events/subscriptions.py">update</a>(subscription_id, \*, id, \*\*<a href="src/casedev/types/vault/events/subscription_update_params.py">params</a>) -> None</code>
- <code title="get /vault/{id}/events/subscriptions">client.vault.events.subscriptions.<a href="./src/casedev/resources/vault/events/subscriptions.py">list</a>(id) -> None</code>
- <code title="delete /vault/{id}/events/subscriptions/{subscriptionId}">client.vault.events.subscriptions.<a href="./src/casedev/resources/vault/events/subscriptions.py">delete</a>(subscription_id, \*, id) -> None</code>
- <code title="post /vault/{id}/events/subscriptions/{subscriptionId}/test">client.vault.events.subscriptions.<a href="./src/casedev/resources/vault/events/subscriptions.py">test</a>(subscription_id, \*, id, \*\*<a href="src/casedev/types/vault/events/subscription_test_params.py">params</a>) -> None</code>

## Graphrag

Types:

```python
from casedev.types.vault import (
    GraphragGetStatsResponse,
    GraphragInitResponse,
    GraphragProcessObjectResponse,
)
```

Methods:

- <code title="get /vault/{id}/graphrag/stats">client.vault.graphrag.<a href="./src/casedev/resources/vault/graphrag.py">get_stats</a>(id) -> <a href="./src/casedev/types/vault/graphrag_get_stats_response.py">GraphragGetStatsResponse</a></code>
- <code title="post /vault/{id}/graphrag/init">client.vault.graphrag.<a href="./src/casedev/resources/vault/graphrag.py">init</a>(id) -> <a href="./src/casedev/types/vault/graphrag_init_response.py">GraphragInitResponse</a></code>
- <code title="post /vault/{id}/graphrag/{objectId}">client.vault.graphrag.<a href="./src/casedev/resources/vault/graphrag.py">process_object</a>(object_id, \*, id) -> <a href="./src/casedev/types/vault/graphrag_process_object_response.py">GraphragProcessObjectResponse</a></code>

## Groups

Methods:

- <code title="post /vault/groups">client.vault.groups.<a href="./src/casedev/resources/vault/groups.py">create</a>() -> None</code>
- <code title="patch /vault/groups/{groupId}">client.vault.groups.<a href="./src/casedev/resources/vault/groups.py">update</a>(group_id) -> None</code>
- <code title="get /vault/groups">client.vault.groups.<a href="./src/casedev/resources/vault/groups.py">list</a>() -> None</code>
- <code title="delete /vault/groups/{groupId}">client.vault.groups.<a href="./src/casedev/resources/vault/groups.py">delete</a>(group_id) -> None</code>

## Multipart

Types:

```python
from casedev.types.vault import MultipartGetPartURLsResponse
```

Methods:

- <code title="post /vault/{id}/multipart/abort">client.vault.multipart.<a href="./src/casedev/resources/vault/multipart.py">abort</a>(id, \*\*<a href="src/casedev/types/vault/multipart_abort_params.py">params</a>) -> None</code>
- <code title="post /vault/{id}/multipart/part-urls">client.vault.multipart.<a href="./src/casedev/resources/vault/multipart.py">get_part_urls</a>(id, \*\*<a href="src/casedev/types/vault/multipart_get_part_urls_params.py">params</a>) -> <a href="./src/casedev/types/vault/multipart_get_part_urls_response.py">MultipartGetPartURLsResponse</a></code>

## Objects

Types:

```python
from casedev.types.vault import (
    ObjectRetrieveResponse,
    ObjectUpdateResponse,
    ObjectListResponse,
    ObjectDeleteResponse,
    ObjectCreatePresignedURLResponse,
    ObjectDownloadResponse,
    ObjectGetOcrWordsResponse,
    ObjectGetSummarizeJobResponse,
    ObjectGetTextResponse,
)
```

Methods:

- <code title="get /vault/{id}/objects/{objectId}">client.vault.objects.<a href="./src/casedev/resources/vault/objects.py">retrieve</a>(object_id, \*, id) -> <a href="./src/casedev/types/vault/object_retrieve_response.py">ObjectRetrieveResponse</a></code>
- <code title="patch /vault/{id}/objects/{objectId}">client.vault.objects.<a href="./src/casedev/resources/vault/objects.py">update</a>(object_id, \*, id, \*\*<a href="src/casedev/types/vault/object_update_params.py">params</a>) -> <a href="./src/casedev/types/vault/object_update_response.py">ObjectUpdateResponse</a></code>
- <code title="get /vault/{id}/objects">client.vault.objects.<a href="./src/casedev/resources/vault/objects.py">list</a>(id) -> <a href="./src/casedev/types/vault/object_list_response.py">ObjectListResponse</a></code>
- <code title="delete /vault/{id}/objects/{objectId}">client.vault.objects.<a href="./src/casedev/resources/vault/objects.py">delete</a>(object_id, \*, id, \*\*<a href="src/casedev/types/vault/object_delete_params.py">params</a>) -> <a href="./src/casedev/types/vault/object_delete_response.py">ObjectDeleteResponse</a></code>
- <code title="post /vault/{id}/objects/{objectId}/presigned-url">client.vault.objects.<a href="./src/casedev/resources/vault/objects.py">create_presigned_url</a>(object_id, \*, id, \*\*<a href="src/casedev/types/vault/object_create_presigned_url_params.py">params</a>) -> <a href="./src/casedev/types/vault/object_create_presigned_url_response.py">ObjectCreatePresignedURLResponse</a></code>
- <code title="get /vault/{id}/objects/{objectId}/download">client.vault.objects.<a href="./src/casedev/resources/vault/objects.py">download</a>(object_id, \*, id) -> str</code>
- <code title="get /vault/{id}/objects/{objectId}/ocr-words">client.vault.objects.<a href="./src/casedev/resources/vault/objects.py">get_ocr_words</a>(object_id, \*, id, \*\*<a href="src/casedev/types/vault/object_get_ocr_words_params.py">params</a>) -> <a href="./src/casedev/types/vault/object_get_ocr_words_response.py">ObjectGetOcrWordsResponse</a></code>
- <code title="get /vault/{id}/objects/{objectId}/summarize/{jobId}">client.vault.objects.<a href="./src/casedev/resources/vault/objects.py">get_summarize_job</a>(job_id, \*, id, object_id) -> <a href="./src/casedev/types/vault/object_get_summarize_job_response.py">ObjectGetSummarizeJobResponse</a></code>
- <code title="get /vault/{id}/objects/{objectId}/text">client.vault.objects.<a href="./src/casedev/resources/vault/objects.py">get_text</a>(object_id, \*, id) -> <a href="./src/casedev/types/vault/object_get_text_response.py">ObjectGetTextResponse</a></code>

# Voice

## Streaming

Types:

```python
from casedev.types.voice import StreamingGetURLResponse
```

Methods:

- <code title="get /voice/streaming/url">client.voice.streaming.<a href="./src/casedev/resources/voice/streaming.py">get_url</a>() -> <a href="./src/casedev/types/voice/streaming_get_url_response.py">StreamingGetURLResponse</a></code>

## Transcription

Types:

```python
from casedev.types.voice import TranscriptionCreateResponse, TranscriptionRetrieveResponse
```

Methods:

- <code title="post /voice/transcription">client.voice.transcription.<a href="./src/casedev/resources/voice/transcription.py">create</a>(\*\*<a href="src/casedev/types/voice/transcription_create_params.py">params</a>) -> <a href="./src/casedev/types/voice/transcription_create_response.py">TranscriptionCreateResponse</a></code>
- <code title="get /voice/transcription/{id}">client.voice.transcription.<a href="./src/casedev/resources/voice/transcription.py">retrieve</a>(id) -> <a href="./src/casedev/types/voice/transcription_retrieve_response.py">TranscriptionRetrieveResponse</a></code>
- <code title="delete /voice/transcription/{id}">client.voice.transcription.<a href="./src/casedev/resources/voice/transcription.py">delete</a>(id) -> None</code>

## V1

Types:

```python
from casedev.types.voice import V1ListVoicesResponse
```

Methods:

- <code title="get /voice/v1/voices">client.voice.v1.<a href="./src/casedev/resources/voice/v1/v1.py">list_voices</a>(\*\*<a href="src/casedev/types/voice/v1_list_voices_params.py">params</a>) -> <a href="./src/casedev/types/voice/v1_list_voices_response.py">V1ListVoicesResponse</a></code>

### Speak

Methods:

- <code title="post /voice/v1/speak">client.voice.v1.speak.<a href="./src/casedev/resources/voice/v1/speak.py">create</a>(\*\*<a href="src/casedev/types/voice/v1/speak_create_params.py">params</a>) -> BinaryAPIResponse</code>
