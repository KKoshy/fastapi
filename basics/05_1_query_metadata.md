# 🚀 FastAPI Query: `title`, `description`, `alias`

Used inside `Query()` to provide **metadata and configuration** for a query parameter.

```python
from typing import Annotated
from fastapi import Query

q: Annotated[
    str | None,
    Query(
        title="Query string",
        description="Search for items",
        alias="item-query"
    )
] = None
```

## 🧠 Remember

| Option        | Meaning                                | Changes URL? |
| ------------- | -------------------------------------- | ------------ |
| `title`       | Human-readable **name** in API docs    | ❌            |
| `description` | Explains **what the parameter does**   | ❌            |
| `alias`       | **External/API name** of the parameter | ✅            |

### `title`

```python
Query(title="Query string")
```

📖 Documentation only.

---

### `description`

```python
Query(description="Search for items")
```

📖 Documentation only.

---

### `alias`

```python
Query(alias="item-query")
```

🌐 Changes the parameter name used in the API request.

```http
GET /items/?item-query=hello
```

Python still uses:

```python
q
```

## ⭐ Easy memory trick

```text
title       → What is it called?       📖
description → What does it do?         📖
alias       → What is its API name?    🌐
```

> **`title` + `description` = documentation**
> **`alias` = API/URL name**
