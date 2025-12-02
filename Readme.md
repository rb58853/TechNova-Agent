# Technova Agent

## RUN API With Uvicorn
```shell
uvicorn src.api.server:app --host 0.0.0.0 --port 8000 --ws-ping-interval 0 --ws-ping-timeout 1200 --workers 1
```
