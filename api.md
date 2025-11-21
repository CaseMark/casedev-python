# Actions

## V1

Methods:

- <code title="post /actions/v1">client.actions.v1.<a href="./src/casedotdev_sdk_py/resources/actions/v1.py">create</a>(\*\*<a href="src/casedotdev_sdk_py/types/actions/v1_create_params.py">params</a>) -> object</code>
- <code title="get /actions/v1/{id}">client.actions.v1.<a href="./src/casedotdev_sdk_py/resources/actions/v1.py">retrieve</a>(id) -> object</code>
- <code title="get /actions/v1">client.actions.v1.<a href="./src/casedotdev_sdk_py/resources/actions/v1.py">list</a>() -> object</code>
- <code title="delete /actions/v1/{id}">client.actions.v1.<a href="./src/casedotdev_sdk_py/resources/actions/v1.py">delete</a>(id) -> object</code>
- <code title="post /actions/v1/{id}/execute">client.actions.v1.<a href="./src/casedotdev_sdk_py/resources/actions/v1.py">execute</a>(id, \*\*<a href="src/casedotdev_sdk_py/types/actions/v1_execute_params.py">params</a>) -> object</code>
- <code title="get /actions/v1/executions/{id}">client.actions.v1.<a href="./src/casedotdev_sdk_py/resources/actions/v1.py">retrieve_execution</a>(id) -> object</code>

# Billing

## Stripe

Methods:

- <code title="post /billing/stripe/webhook">client.billing.stripe.<a href="./src/casedotdev_sdk_py/resources/billing/stripe.py">handle_webhook</a>(\*\*<a href="src/casedotdev_sdk_py/types/billing/stripe_handle_webhook_params.py">params</a>) -> object</code>

## V1

Methods:

- <code title="post /billing/v1/attach-payment-method">client.billing.v1.<a href="./src/casedotdev_sdk_py/resources/billing/v1.py">attach_payment_method</a>(\*\*<a href="src/casedotdev_sdk_py/types/billing/v1_attach_payment_method_params.py">params</a>) -> object</code>
- <code title="post /billing/v1/charge">client.billing.v1.<a href="./src/casedotdev_sdk_py/resources/billing/v1.py">create_charge</a>(\*\*<a href="src/casedotdev_sdk_py/types/billing/v1_create_charge_params.py">params</a>) -> object</code>
- <code title="post /billing/v1/setup-intent">client.billing.v1.<a href="./src/casedotdev_sdk_py/resources/billing/v1.py">create_setup_intent</a>(\*\*<a href="src/casedotdev_sdk_py/types/billing/v1_create_setup_intent_params.py">params</a>) -> object</code>
- <code title="get /billing/v1/usage">client.billing.v1.<a href="./src/casedotdev_sdk_py/resources/billing/v1.py">get_usage</a>() -> object</code>
- <code title="get /billing/v1/history">client.billing.v1.<a href="./src/casedotdev_sdk_py/resources/billing/v1.py">list_history</a>() -> object</code>

# Convert

## V1

Methods:

- <code title="post /convert/v1/process">client.convert.v1.<a href="./src/casedotdev_sdk_py/resources/convert/v1/v1.py">create_process</a>(\*\*<a href="src/casedotdev_sdk_py/types/convert/v1_create_process_params.py">params</a>) -> object</code>
- <code title="post /convert/v1/webhook">client.convert.v1.<a href="./src/casedotdev_sdk_py/resources/convert/v1/v1.py">create_webhook</a>(\*\*<a href="src/casedotdev_sdk_py/types/convert/v1_create_webhook_params.py">params</a>) -> object</code>
- <code title="get /convert/v1/download/{id}">client.convert.v1.<a href="./src/casedotdev_sdk_py/resources/convert/v1/v1.py">download</a>(id) -> object</code>

### Jobs

Methods:

- <code title="get /convert/v1/jobs/{id}">client.convert.v1.jobs.<a href="./src/casedotdev_sdk_py/resources/convert/v1/jobs.py">retrieve</a>(id) -> object</code>
- <code title="delete /convert/v1/jobs/{id}">client.convert.v1.jobs.<a href="./src/casedotdev_sdk_py/resources/convert/v1/jobs.py">delete</a>(id) -> object</code>

# Format

## V1

Methods:

- <code title="post /format/v1/document">client.format.v1.<a href="./src/casedotdev_sdk_py/resources/format/v1/v1.py">create_document</a>(\*\*<a href="src/casedotdev_sdk_py/types/format/v1_create_document_params.py">params</a>) -> object</code>

### Templates

Methods:

- <code title="post /format/v1/templates">client.format.v1.templates.<a href="./src/casedotdev_sdk_py/resources/format/v1/templates.py">create</a>(\*\*<a href="src/casedotdev_sdk_py/types/format/v1/template_create_params.py">params</a>) -> object</code>
- <code title="get /format/v1/templates/{id}">client.format.v1.templates.<a href="./src/casedotdev_sdk_py/resources/format/v1/templates.py">retrieve</a>(id) -> object</code>
- <code title="get /format/v1/templates">client.format.v1.templates.<a href="./src/casedotdev_sdk_py/resources/format/v1/templates.py">list</a>() -> object</code>

# Index

Methods:

- <code title="get /index">client.index.<a href="./src/casedotdev_sdk_py/resources/index.py">retrieve</a>() -> object</code>

# Llm

Methods:

- <code title="get /llm/config">client.llm.<a href="./src/casedotdev_sdk_py/resources/llm/llm.py">retrieve_config</a>() -> object</code>

## V1

Methods:

- <code title="post /llm/v1/embeddings">client.llm.v1.<a href="./src/casedotdev_sdk_py/resources/llm/v1/v1.py">create_embedding</a>(\*\*<a href="src/casedotdev_sdk_py/types/llm/v1_create_embedding_params.py">params</a>) -> object</code>
- <code title="get /llm/v1/models">client.llm.v1.<a href="./src/casedotdev_sdk_py/resources/llm/v1/v1.py">list_models</a>() -> object</code>

### Chat

Methods:

- <code title="post /llm/v1/chat/completions">client.llm.v1.chat.<a href="./src/casedotdev_sdk_py/resources/llm/v1/chat.py">create_completion</a>(\*\*<a href="src/casedotdev_sdk_py/types/llm/v1/chat_create_completion_params.py">params</a>) -> object</code>

# Ocr

## V1

Methods:

- <code title="get /ocr/v1/{id}">client.ocr.v1.<a href="./src/casedotdev_sdk_py/resources/ocr/v1.py">retrieve</a>(id) -> object</code>
- <code title="get /ocr/v1/{id}/download/{type}">client.ocr.v1.<a href="./src/casedotdev_sdk_py/resources/ocr/v1.py">download</a>(type, \*, id) -> object</code>
- <code title="post /ocr/v1/process">client.ocr.v1.<a href="./src/casedotdev_sdk_py/resources/ocr/v1.py">process</a>(\*\*<a href="src/casedotdev_sdk_py/types/ocr/v1_process_params.py">params</a>) -> object</code>

# Vault

Methods:

- <code title="post /vault">client.vault.<a href="./src/casedotdev_sdk_py/resources/vault/vault.py">create</a>(\*\*<a href="src/casedotdev_sdk_py/types/vault_create_params.py">params</a>) -> object</code>
- <code title="get /vault/{id}">client.vault.<a href="./src/casedotdev_sdk_py/resources/vault/vault.py">retrieve</a>(id) -> object</code>
- <code title="post /vault/{id}/ingest/{objectId}">client.vault.<a href="./src/casedotdev_sdk_py/resources/vault/vault.py">ingest_object</a>(object_id, \*, id, \*\*<a href="src/casedotdev_sdk_py/types/vault_ingest_object_params.py">params</a>) -> object</code>
- <code title="post /vault/{id}/search">client.vault.<a href="./src/casedotdev_sdk_py/resources/vault/vault.py">search</a>(id, \*\*<a href="src/casedotdev_sdk_py/types/vault_search_params.py">params</a>) -> object</code>
- <code title="post /vault/{id}/upload">client.vault.<a href="./src/casedotdev_sdk_py/resources/vault/vault.py">upload</a>(id, \*\*<a href="src/casedotdev_sdk_py/types/vault_upload_params.py">params</a>) -> object</code>

## Graphrag

Methods:

- <code title="post /vault/{id}/graphrag/init">client.vault.graphrag.<a href="./src/casedotdev_sdk_py/resources/vault/graphrag.py">initialize</a>(id, \*\*<a href="src/casedotdev_sdk_py/types/vault/graphrag_initialize_params.py">params</a>) -> object</code>
- <code title="get /vault/{id}/graphrag/stats">client.vault.graphrag.<a href="./src/casedotdev_sdk_py/resources/vault/graphrag.py">retrieve_stats</a>(id) -> object</code>

## Objects

Methods:

- <code title="get /vault/{id}/objects/{objectId}">client.vault.objects.<a href="./src/casedotdev_sdk_py/resources/vault/objects.py">retrieve</a>(object_id, \*, id) -> object</code>
- <code title="get /vault/{id}/objects">client.vault.objects.<a href="./src/casedotdev_sdk_py/resources/vault/objects.py">list</a>(id) -> object</code>
- <code title="post /vault/{id}/objects/{objectId}/presigned-url">client.vault.objects.<a href="./src/casedotdev_sdk_py/resources/vault/objects.py">create_presigned_url</a>(object_id, \*, id, \*\*<a href="src/casedotdev_sdk_py/types/vault/object_create_presigned_url_params.py">params</a>) -> object</code>
- <code title="get /vault/{id}/objects/{objectId}/download">client.vault.objects.<a href="./src/casedotdev_sdk_py/resources/vault/objects.py">download</a>(object_id, \*, id) -> object</code>
- <code title="get /vault/{id}/objects/{objectId}/text">client.vault.objects.<a href="./src/casedotdev_sdk_py/resources/vault/objects.py">retrieve_text</a>(object_id, \*, id) -> object</code>

# Voice

## Streaming

Methods:

- <code title="get /voice/streaming/url">client.voice.streaming.<a href="./src/casedotdev_sdk_py/resources/voice/streaming.py">retrieve_url</a>() -> object</code>

## Transcription

Methods:

- <code title="post /voice/transcription">client.voice.transcription.<a href="./src/casedotdev_sdk_py/resources/voice/transcription.py">create</a>(\*\*<a href="src/casedotdev_sdk_py/types/voice/transcription_create_params.py">params</a>) -> object</code>
- <code title="get /voice/transcription/{id}">client.voice.transcription.<a href="./src/casedotdev_sdk_py/resources/voice/transcription.py">retrieve</a>(id) -> object</code>

## V1

Methods:

- <code title="get /voice/v1/voices">client.voice.v1.<a href="./src/casedotdev_sdk_py/resources/voice/v1/v1.py">list_voices</a>() -> object</code>

### Speak

Methods:

- <code title="post /voice/v1/speak">client.voice.v1.speak.<a href="./src/casedotdev_sdk_py/resources/voice/v1/speak.py">create</a>(\*\*<a href="src/casedotdev_sdk_py/types/voice/v1/speak_create_params.py">params</a>) -> object</code>
- <code title="post /voice/v1/speak/stream">client.voice.v1.speak.<a href="./src/casedotdev_sdk_py/resources/voice/v1/speak.py">stream</a>(\*\*<a href="src/casedotdev_sdk_py/types/voice/v1/speak_stream_params.py">params</a>) -> object</code>

# Webhooks

## V1

Methods:

- <code title="post /webhooks/v1">client.webhooks.v1.<a href="./src/casedotdev_sdk_py/resources/webhooks/v1.py">create</a>(\*\*<a href="src/casedotdev_sdk_py/types/webhooks/v1_create_params.py">params</a>) -> object</code>
- <code title="get /webhooks/v1/{id}">client.webhooks.v1.<a href="./src/casedotdev_sdk_py/resources/webhooks/v1.py">retrieve</a>(id) -> object</code>
- <code title="get /webhooks/v1">client.webhooks.v1.<a href="./src/casedotdev_sdk_py/resources/webhooks/v1.py">list</a>() -> object</code>
- <code title="delete /webhooks/v1/{id}">client.webhooks.v1.<a href="./src/casedotdev_sdk_py/resources/webhooks/v1.py">delete</a>(id) -> object</code>

# Workflows

## V1

Methods:

- <code title="get /workflows/v1/{id}">client.workflows.v1.<a href="./src/casedotdev_sdk_py/resources/workflows/v1.py">retrieve</a>(id) -> object</code>
- <code title="get /workflows/v1">client.workflows.v1.<a href="./src/casedotdev_sdk_py/resources/workflows/v1.py">list</a>() -> object</code>
- <code title="post /workflows/v1/{id}/execute">client.workflows.v1.<a href="./src/casedotdev_sdk_py/resources/workflows/v1.py">execute</a>(id, \*\*<a href="src/casedotdev_sdk_py/types/workflows/v1_execute_params.py">params</a>) -> object</code>
- <code title="get /workflows/v1/executions/{id}">client.workflows.v1.<a href="./src/casedotdev_sdk_py/resources/workflows/v1.py">execution_retrieve</a>(id) -> object</code>
- <code title="post /workflows/v1/search">client.workflows.v1.<a href="./src/casedotdev_sdk_py/resources/workflows/v1.py">search</a>(\*\*<a href="src/casedotdev_sdk_py/types/workflows/v1_search_params.py">params</a>) -> object</code>
