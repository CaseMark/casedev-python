# Actions

## V1

Types:

```python
from casedotdev_sdk_py.types.actions import V1CreateResponse, V1ExecuteResponse
```

Methods:

- <code title="post /actions/v1">client.actions.v1.<a href="./src/casedotdev_sdk_py/resources/actions/v1.py">create</a>(\*\*<a href="src/casedotdev_sdk_py/types/actions/v1_create_params.py">params</a>) -> <a href="./src/casedotdev_sdk_py/types/actions/v1_create_response.py">V1CreateResponse</a></code>
- <code title="get /actions/v1/{id}">client.actions.v1.<a href="./src/casedotdev_sdk_py/resources/actions/v1.py">retrieve</a>(id) -> None</code>
- <code title="get /actions/v1">client.actions.v1.<a href="./src/casedotdev_sdk_py/resources/actions/v1.py">list</a>() -> None</code>
- <code title="delete /actions/v1/{id}">client.actions.v1.<a href="./src/casedotdev_sdk_py/resources/actions/v1.py">delete</a>(id) -> None</code>
- <code title="post /actions/v1/{id}/execute">client.actions.v1.<a href="./src/casedotdev_sdk_py/resources/actions/v1.py">execute</a>(id, \*\*<a href="src/casedotdev_sdk_py/types/actions/v1_execute_params.py">params</a>) -> <a href="./src/casedotdev_sdk_py/types/actions/v1_execute_response.py">V1ExecuteResponse</a></code>
- <code title="get /actions/v1/executions/{id}">client.actions.v1.<a href="./src/casedotdev_sdk_py/resources/actions/v1.py">retrieve_execution</a>(id) -> None</code>

# Convert

## V1

Types:

```python
from casedotdev_sdk_py.types.convert import V1CreateProcessResponse, V1CreateWebhookResponse
```

Methods:

- <code title="post /convert/v1/process">client.convert.v1.<a href="./src/casedotdev_sdk_py/resources/convert/v1/v1.py">create_process</a>(\*\*<a href="src/casedotdev_sdk_py/types/convert/v1_create_process_params.py">params</a>) -> <a href="./src/casedotdev_sdk_py/types/convert/v1_create_process_response.py">V1CreateProcessResponse</a></code>
- <code title="post /convert/v1/webhook">client.convert.v1.<a href="./src/casedotdev_sdk_py/resources/convert/v1/v1.py">create_webhook</a>(\*\*<a href="src/casedotdev_sdk_py/types/convert/v1_create_webhook_params.py">params</a>) -> <a href="./src/casedotdev_sdk_py/types/convert/v1_create_webhook_response.py">V1CreateWebhookResponse</a></code>
- <code title="get /convert/v1/download/{id}">client.convert.v1.<a href="./src/casedotdev_sdk_py/resources/convert/v1/v1.py">download</a>(id) -> BinaryAPIResponse</code>

### Jobs

Methods:

- <code title="get /convert/v1/jobs/{id}">client.convert.v1.jobs.<a href="./src/casedotdev_sdk_py/resources/convert/v1/jobs.py">retrieve</a>(id) -> None</code>
- <code title="delete /convert/v1/jobs/{id}">client.convert.v1.jobs.<a href="./src/casedotdev_sdk_py/resources/convert/v1/jobs.py">delete</a>(id) -> None</code>

# Format

## V1

Methods:

- <code title="post /format/v1/document">client.format.v1.<a href="./src/casedotdev_sdk_py/resources/format/v1/v1.py">create_document</a>(\*\*<a href="src/casedotdev_sdk_py/types/format/v1_create_document_params.py">params</a>) -> BinaryAPIResponse</code>

### Templates

Types:

```python
from casedotdev_sdk_py.types.format.v1 import TemplateCreateResponse
```

Methods:

- <code title="post /format/v1/templates">client.format.v1.templates.<a href="./src/casedotdev_sdk_py/resources/format/v1/templates.py">create</a>(\*\*<a href="src/casedotdev_sdk_py/types/format/v1/template_create_params.py">params</a>) -> <a href="./src/casedotdev_sdk_py/types/format/v1/template_create_response.py">TemplateCreateResponse</a></code>
- <code title="get /format/v1/templates/{id}">client.format.v1.templates.<a href="./src/casedotdev_sdk_py/resources/format/v1/templates.py">retrieve</a>(id) -> None</code>
- <code title="get /format/v1/templates">client.format.v1.templates.<a href="./src/casedotdev_sdk_py/resources/format/v1/templates.py">list</a>(\*\*<a href="src/casedotdev_sdk_py/types/format/v1/template_list_params.py">params</a>) -> None</code>

# Index

Methods:

- <code title="get /index">client.index.<a href="./src/casedotdev_sdk_py/resources/index.py">retrieve</a>() -> None</code>

# Llm

Methods:

- <code title="get /llm/config">client.llm.<a href="./src/casedotdev_sdk_py/resources/llm/llm.py">retrieve_config</a>() -> None</code>

## V1

Methods:

- <code title="post /llm/v1/embeddings">client.llm.v1.<a href="./src/casedotdev_sdk_py/resources/llm/v1/v1.py">create_embedding</a>(\*\*<a href="src/casedotdev_sdk_py/types/llm/v1_create_embedding_params.py">params</a>) -> None</code>
- <code title="get /llm/v1/models">client.llm.v1.<a href="./src/casedotdev_sdk_py/resources/llm/v1/v1.py">list_models</a>() -> None</code>

### Chat

Types:

```python
from casedotdev_sdk_py.types.llm.v1 import ChatCreateCompletionResponse
```

Methods:

- <code title="post /llm/v1/chat/completions">client.llm.v1.chat.<a href="./src/casedotdev_sdk_py/resources/llm/v1/chat.py">create_completion</a>(\*\*<a href="src/casedotdev_sdk_py/types/llm/v1/chat_create_completion_params.py">params</a>) -> <a href="./src/casedotdev_sdk_py/types/llm/v1/chat_create_completion_response.py">ChatCreateCompletionResponse</a></code>

# Ocr

## V1

Types:

```python
from casedotdev_sdk_py.types.ocr import V1ProcessResponse
```

Methods:

- <code title="get /ocr/v1/{id}">client.ocr.v1.<a href="./src/casedotdev_sdk_py/resources/ocr/v1.py">retrieve</a>(id) -> None</code>
- <code title="get /ocr/v1/{id}/download/{type}">client.ocr.v1.<a href="./src/casedotdev_sdk_py/resources/ocr/v1.py">download</a>(type, \*, id) -> None</code>
- <code title="post /ocr/v1/process">client.ocr.v1.<a href="./src/casedotdev_sdk_py/resources/ocr/v1.py">process</a>(\*\*<a href="src/casedotdev_sdk_py/types/ocr/v1_process_params.py">params</a>) -> <a href="./src/casedotdev_sdk_py/types/ocr/v1_process_response.py">V1ProcessResponse</a></code>

# Vault

Types:

```python
from casedotdev_sdk_py.types import (
    VaultCreateResponse,
    VaultIngestObjectResponse,
    VaultSearchResponse,
    VaultUploadResponse,
)
```

Methods:

- <code title="post /vault">client.vault.<a href="./src/casedotdev_sdk_py/resources/vault/vault.py">create</a>(\*\*<a href="src/casedotdev_sdk_py/types/vault_create_params.py">params</a>) -> <a href="./src/casedotdev_sdk_py/types/vault_create_response.py">VaultCreateResponse</a></code>
- <code title="get /vault/{id}">client.vault.<a href="./src/casedotdev_sdk_py/resources/vault/vault.py">retrieve</a>(id) -> None</code>
- <code title="post /vault/{id}/ingest/{objectId}">client.vault.<a href="./src/casedotdev_sdk_py/resources/vault/vault.py">ingest_object</a>(object_id, \*, id) -> <a href="./src/casedotdev_sdk_py/types/vault_ingest_object_response.py">VaultIngestObjectResponse</a></code>
- <code title="post /vault/{id}/search">client.vault.<a href="./src/casedotdev_sdk_py/resources/vault/vault.py">search</a>(id, \*\*<a href="src/casedotdev_sdk_py/types/vault_search_params.py">params</a>) -> <a href="./src/casedotdev_sdk_py/types/vault_search_response.py">VaultSearchResponse</a></code>
- <code title="post /vault/{id}/upload">client.vault.<a href="./src/casedotdev_sdk_py/resources/vault/vault.py">upload</a>(id, \*\*<a href="src/casedotdev_sdk_py/types/vault_upload_params.py">params</a>) -> <a href="./src/casedotdev_sdk_py/types/vault_upload_response.py">VaultUploadResponse</a></code>

## Graphrag

Methods:

- <code title="post /vault/{id}/graphrag/init">client.vault.graphrag.<a href="./src/casedotdev_sdk_py/resources/vault/graphrag.py">initialize</a>(id) -> None</code>
- <code title="get /vault/{id}/graphrag/stats">client.vault.graphrag.<a href="./src/casedotdev_sdk_py/resources/vault/graphrag.py">retrieve_stats</a>(id) -> None</code>

## Objects

Types:

```python
from casedotdev_sdk_py.types.vault import ObjectCreatePresignedURLResponse
```

Methods:

- <code title="get /vault/{id}/objects/{objectId}">client.vault.objects.<a href="./src/casedotdev_sdk_py/resources/vault/objects.py">retrieve</a>(object_id, \*, id) -> None</code>
- <code title="get /vault/{id}/objects">client.vault.objects.<a href="./src/casedotdev_sdk_py/resources/vault/objects.py">list</a>(id) -> None</code>
- <code title="post /vault/{id}/objects/{objectId}/presigned-url">client.vault.objects.<a href="./src/casedotdev_sdk_py/resources/vault/objects.py">create_presigned_url</a>(object_id, \*, id, \*\*<a href="src/casedotdev_sdk_py/types/vault/object_create_presigned_url_params.py">params</a>) -> <a href="./src/casedotdev_sdk_py/types/vault/object_create_presigned_url_response.py">ObjectCreatePresignedURLResponse</a></code>
- <code title="get /vault/{id}/objects/{objectId}/download">client.vault.objects.<a href="./src/casedotdev_sdk_py/resources/vault/objects.py">download</a>(object_id, \*, id) -> None</code>
- <code title="get /vault/{id}/objects/{objectId}/text">client.vault.objects.<a href="./src/casedotdev_sdk_py/resources/vault/objects.py">retrieve_text</a>(object_id, \*, id) -> None</code>

# Voice

## Streaming

Methods:

- <code title="get /voice/streaming/url">client.voice.streaming.<a href="./src/casedotdev_sdk_py/resources/voice/streaming.py">retrieve_url</a>() -> None</code>

## Transcription

Types:

```python
from casedotdev_sdk_py.types.voice import TranscriptionRetrieveResponse
```

Methods:

- <code title="post /voice/transcription">client.voice.transcription.<a href="./src/casedotdev_sdk_py/resources/voice/transcription.py">create</a>(\*\*<a href="src/casedotdev_sdk_py/types/voice/transcription_create_params.py">params</a>) -> None</code>
- <code title="get /voice/transcription/{id}">client.voice.transcription.<a href="./src/casedotdev_sdk_py/resources/voice/transcription.py">retrieve</a>(id) -> <a href="./src/casedotdev_sdk_py/types/voice/transcription_retrieve_response.py">TranscriptionRetrieveResponse</a></code>

## V1

Methods:

- <code title="get /voice/v1/voices">client.voice.v1.<a href="./src/casedotdev_sdk_py/resources/voice/v1/v1.py">list_voices</a>(\*\*<a href="src/casedotdev_sdk_py/types/voice/v1_list_voices_params.py">params</a>) -> None</code>

### Speak

Methods:

- <code title="post /voice/v1/speak">client.voice.v1.speak.<a href="./src/casedotdev_sdk_py/resources/voice/v1/speak.py">create</a>(\*\*<a href="src/casedotdev_sdk_py/types/voice/v1/speak_create_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="post /voice/v1/speak/stream">client.voice.v1.speak.<a href="./src/casedotdev_sdk_py/resources/voice/v1/speak.py">stream</a>(\*\*<a href="src/casedotdev_sdk_py/types/voice/v1/speak_stream_params.py">params</a>) -> BinaryAPIResponse</code>

# Webhooks

## V1

Types:

```python
from casedotdev_sdk_py.types.webhooks import V1CreateResponse
```

Methods:

- <code title="post /webhooks/v1">client.webhooks.v1.<a href="./src/casedotdev_sdk_py/resources/webhooks/v1.py">create</a>(\*\*<a href="src/casedotdev_sdk_py/types/webhooks/v1_create_params.py">params</a>) -> <a href="./src/casedotdev_sdk_py/types/webhooks/v1_create_response.py">V1CreateResponse</a></code>
- <code title="get /webhooks/v1/{id}">client.webhooks.v1.<a href="./src/casedotdev_sdk_py/resources/webhooks/v1.py">retrieve</a>(id) -> None</code>
- <code title="get /webhooks/v1">client.webhooks.v1.<a href="./src/casedotdev_sdk_py/resources/webhooks/v1.py">list</a>() -> None</code>
- <code title="delete /webhooks/v1/{id}">client.webhooks.v1.<a href="./src/casedotdev_sdk_py/resources/webhooks/v1.py">delete</a>(id) -> None</code>

# Workflows

## V1

Types:

```python
from casedotdev_sdk_py.types.workflows import V1ExecuteResponse
```

Methods:

- <code title="get /workflows/v1/{id}">client.workflows.v1.<a href="./src/casedotdev_sdk_py/resources/workflows/v1.py">retrieve</a>(id) -> None</code>
- <code title="get /workflows/v1">client.workflows.v1.<a href="./src/casedotdev_sdk_py/resources/workflows/v1.py">list</a>(\*\*<a href="src/casedotdev_sdk_py/types/workflows/v1_list_params.py">params</a>) -> None</code>
- <code title="post /workflows/v1/{id}/execute">client.workflows.v1.<a href="./src/casedotdev_sdk_py/resources/workflows/v1.py">execute</a>(id, \*\*<a href="src/casedotdev_sdk_py/types/workflows/v1_execute_params.py">params</a>) -> <a href="./src/casedotdev_sdk_py/types/workflows/v1_execute_response.py">V1ExecuteResponse</a></code>
- <code title="get /workflows/v1/executions/{id}">client.workflows.v1.<a href="./src/casedotdev_sdk_py/resources/workflows/v1.py">execution_retrieve</a>(id) -> None</code>
- <code title="post /workflows/v1/search">client.workflows.v1.<a href="./src/casedotdev_sdk_py/resources/workflows/v1.py">search</a>(\*\*<a href="src/casedotdev_sdk_py/types/workflows/v1_search_params.py">params</a>) -> None</code>
