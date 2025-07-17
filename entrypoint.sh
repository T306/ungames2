#!/bin/bash
python uv run dbgen.py
bash uv run uvicorn main:app --host 0.0.0.0 --port 5000
