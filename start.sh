#!/bin/bash

# Start the FastApi backend in the background
cd backend
uvicorn main:app --host 0.0.0.0 --port 8000 &
cd ..

# Start the Streamlit frontend
cd frontend
streamlit run app.py --server.port="${PORT:-8501}" --server.address="0.0.0.0"
