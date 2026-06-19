# AI Workspace

The AI Workspace page is the hub for local AI tooling on YasserOS. It provides
at-a-glance status for the most popular open-source AI tools and quick shortcuts
to launch them.

## Vision

YasserOS is designed to be a ready-to-use local AI development environment. The
goal is that a fresh install should let you go from zero to running a local LLM
in under five minutes — without cloud accounts, API keys, or internet access.

## Included Tool Integrations

| Tool         | Purpose                                 | Install command                   |
|--------------|-----------------------------------------|-----------------------------------|
| Python 3     | Interactive REPL / scripting            | Pre-installed                     |
| Jupyter Lab  | Notebook-based experimentation          | `pip install jupyterlab`          |
| Ollama       | Run LLMs locally (Llama, Mistral, etc.) | https://ollama.ai                 |
| Open WebUI   | Browser-based chat for local LLMs       | `pip install open-webui`          |

## Local Models Directory

By default, models are stored in `~/Models`. This can be overridden by setting
the `YASSEROS_MODELS_DIR` environment variable in your shell profile:

```bash
export YASSEROS_MODELS_DIR=/mnt/data/models
```

## Roadmap

- Auto-detect and list downloaded Ollama models
- One-click model pull from the UI
- Integrated Jupyter server management (start/stop/restart)
- GPU availability indicator
