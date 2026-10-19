# Homework 5 — Deploying ML models: notes

The model artifact, lockfile, API and Dockerfile are the course's frozen 2026 release.
`pipeline.bin` checksum verified before use:

```
1646bbdcd38d4f044da6b630c5b332c93a314245a8c21929011c42de51f629f1  pipeline.bin
```

| Q | Answer | How |
|---|---|---|
| 1 | uv 0.11.32 | `uv --version` |
| 2 | scikit-learn 1.7.2 | `pyproject.toml` pin and `uv.lock` |
| 3 | 0.533 | `uv run python q3_predict.py` (pickle load + `predict_proba`) |
| 4 | 0.770 | `uv run uvicorn predict:app --port 9696`, then `POST /predict` |
| 5 | `python:3.11.15-slim-bookworm` | `Dockerfile` `FROM` line |
| 6 | 0.770 | Same artifact, lockfile and Python 3.11.15 as the container |

## Reproduce

```bash
uv sync --locked
uv run python smoke_test.py
uv run python q3_predict.py

uv run uvicorn predict:app --host 0.0.0.0 --port 9696
curl -s http://localhost:9696/health
python q6_test.py           # hits /predict with the Q4/Q6 lead

docker build -t zoomcamp-model:2026-hw5 .
docker run --rm -p 9696:9696 zoomcamp-model:2026-hw5
python q6_test.py           # same request, now against the container
```

API responses observed locally:

```json
GET  /health  → {"status":"ok","model_sha256":"1646bbdc…f629f1", ...}
POST /predict → {"conversion_probability":0.769799,"conversion":true}
```
