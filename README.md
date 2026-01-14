# Chatbot Project

Overview
--------

This repository contains a small Python-based chatbot project with a modular layout: agents, API glue, configuration, data sources, and a simple static chat widget. The README below lists the full project structure and explains the purpose of each file and folder.

Project structure
-----------------

```
app.py
main.py
requirements.txt
vercel.json
agents/
    __init__.py
    product_agent.py
    __pycache__/
api/
    __init__.py
config/
    __init__.py
    settings.py
    __pycache__/
data/
    __init__.py
    faqs.py
    products.py
    __pycache__/
static/
    chat-widget.html
utils/
    __init__.py
    helpers.py

```

File and folder explanations
--------------------------

- `app.py` : Application entrypoint or WSGI/ASGI mount. Likely sets up the web server (Flask, FastAPI, etc.), initializes routing, and registers endpoints or middleware. This is where the app object is created and run.

- `main.py` : Secondary runner script. Often used to start the application for local development or to provide an alternate CLI entrypoint. May import `app` and call `run()`.

- `requirements.txt` : Python dependency list used to install required packages with `pip install -r requirements.txt`.

- `vercel.json` : Vercel deployment configuration. Controls how the project is deployed to Vercel (build settings, routes, serverless functions mapping, etc.).

- `agents/` : Contains agent implementations which encapsulate conversational/business logic.
  - `__init__.py` : Marks the directory as a Python package and may expose package-level imports.
  - `product_agent.py` : Agent focused on product-related interactions (searching products, answering product questions, recommending items). Contains the logic that interprets user intents and queries `data/products.py` or other services.

- `api/` : API layer for the app.
  - `__init__.py` : Package initializer; may register API routes or expose helper functions used by the web server.

- `config/` : Configuration values and settings loader.
  - `__init__.py` : Package initializer.
  - `settings.py` : Centralized configuration (environment variables, toggles, API keys, host/port, and other runtime settings).

- `data/` : Static or example data used by the agents.
  - `__init__.py` : Package initializer.
  - `faqs.py` : Frequently asked questions dataset (likely a dict/list of Q&A pairs used for retrieval or matching).
  - `products.py` : Product dataset (list/dict of product entries used by `product_agent.py` for lookup or recommendations).

- `static/` : Static assets for a frontend widget or demo.
  - `chat-widget.html` : A simple frontend chat widget (HTML + inline JS/CSS) that can connect to the backend API to send/receive messages.

- `utils/` : Utility helpers used across the project.
  - `__init__.py` : Package initializer.
  - `helpers.py` : Reusable functions (text normalization, matching helpers, small utilities to keep core logic clean).

Notes and recommendations
-------------------------

- The `__pycache__` folders contain Python bytecode caches and can be ignored/removed from version control (add them to `.gitignore` if needed).
- To run locally, install dependencies from `requirements.txt`, then run `python main.py` or `python app.py` depending on which script is intended to start the server.
- If deploying to Vercel, ensure `vercel.json` is configured to point the serverless entrypoint to the correct Python file or function.

Contact / Next steps
--------------------

If you want, I can:

- Add a short `README` usage section with exact run commands based on the detected framework (Flask/FastAPI) if you want me to inspect `app.py` or `main.py`.
- Generate a `requirements.txt` pin file (if missing packages are discovered).

This README was created without modifying any existing code.
