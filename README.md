# fastapi

A hands-on collection of scripts for learning [FastAPI](https://fastapi.tiangolo.com/), following the official FastAPI tutorial. Each script in `basics/` builds on the last, introducing one concept at a time, with a matching `.http` file in `tests/` for trying out the endpoints.

## Repo structure

```
basics/   Step-by-step FastAPI example scripts
tests/    .http request files for exercising each example
```

| Script | Topic |
|---|---|
| `01_first_steps.py` | The simplest possible FastAPI app |
| `02_path_parameters.py` | Dynamic URLs and path parameters |
| `03_query_parameters.py` | Optional query parameters |
| `04_request_body.py` | Handling POST requests with a request body (Pydantic models) |
| `05_query_parameters_str_validation.py` | Validating and constraining query parameters |
| `06_path_parameters_numeric_validation.py` | Validating and constraining path parameters |

## Getting started

1. **Install dependencies**
   ```bash
   pip install fastapi "uvicorn[standard]"
   ```

2. **Run any example**
   ```bash
   python -m uvicorn basics.01_first_steps:app --reload
   ```
   (Swap in the filename of whichever example you want to run.)

3. **Try the endpoints**
   Open the interactive docs at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs), or use the matching `.http` file in `tests/` (works directly in VS Code with the REST Client extension, or JetBrains IDEs).

## Requirements

- Python 3.8+
- [FastAPI](https://pypi.org/project/fastapi/)
- [Uvicorn](https://www.uvicorn.org/) (ASGI server)

## Reference

Based on the official FastAPI tutorial: https://fastapi.tiangolo.com/tutorial/
