FROM registry.suse.com/bci/python:3.13

WORKDIR /app

RUN pip install uv

COPY . .

RUN uv pip install --system -r pyproject.toml

CMD ["uv", "run", "main.py"]