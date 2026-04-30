# Use a lightweight Python image as the base
FROM python:3.13-slim

# Copy the UV binary from the official image to use it for dependency management and running the app
COPY --from=ghcr.io/astral-sh/uv:0.9.26 /uv /uv /bin/

# Set the working directory in the container
WORKDIR /app

# Prevent Python from writing .pyc files and enable unbuffered output
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONBUFFERED=1

# Copy the dependency file to the working directory
COPY ./pyproject.toml ./uv.lock /app/

# Use UV to install dependencies without dev dependencies and without installing the project itself
RUN uv sync --no-dev --no-install-project

# Copy the application code to the working directory
COPY ./agent.py .

# Expose the port that the application will run on
EXPOSE 8000

# Use `uv run` to start the application
# This automatically uses the virtual environment created by `uv sync` and ensures that the application runs with the correct dependencies
# CMD ["uv", "run", "./src/main.py"]
CMD ["uv", "run", "uvicorn", "agent:a2a_app", "--host", "0.0.0.0", "--port", "8000"]
