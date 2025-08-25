# Step 0 — Bare-Metal Project Setup (Poetry · FastAPI · PostgreSQL)

## 📌 Summary
This step establishes the foundation for the **Agents + MCP Bootcamp project**.  
We set up a clean Python project managed by **Poetry**, build a minimal **FastAPI** app, and connect it to a bare-metal **PostgreSQL** database with **async SQLAlchemy** and **Alembic** migrations.  
Every file and configuration is explained in detail: what it does, why it exists, and how each important line works.  
This ensures you not only have working code, but also understand the reasoning behind each decision.

---

# 📁 Project Map

```
agents-mcp-bootcamp/
├─ src/
│  └─ amcp/
│     ├─ __init__.py
│     ├─ config.py
│     ├─ db.py
│     └─ main.py
├─ alembic/            # created by `alembic init`
│  ├─ env.py
│  ├─ script.py.mako
│  └─ versions/
├─ .env.example
├─ .env                # (created locally from .env.example; not committed)
├─ alembic.ini
├─ Makefile
└─ pyproject.toml
```

---

## 1) `pyproject.toml`
**What it is:** Poetry’s “single source of truth” for your project: dependencies, Python version, formatting/linting tool config.

**How it fits:**  
- When you run `poetry install`, Poetry reads this file to create a virtualenv and lock dependencies.
- Tools like Black/Ruff/Isort read their sections here for consistent style.

**Important lines/blocks:**
- `[tool.poetry]` → Project metadata and packaging.
  - `packages = [{ include = "amcp", from = "src" }]`  
    Tells Poetry that your importable package **amcp** lives in the **src** folder. Prevents “import from current working directory” pitfalls.
- Dependencies sections:
  - Runtime: `fastapi`, `uvicorn[standard]`, `sqlalchemy[asyncio]`, `asyncpg`, `alembic`, `pydantic-settings`, `httpx`, etc.
  - Dev: `ruff`, `black`, `isort`, `pytest`, `pytest-asyncio`.
- Tool configs:
  - `[tool.black]`, `[tool.isort]`, `[tool.ruff]`  
    Define line length, Python targets, and linting rules so your codebase stays consistent.

---

## 2) `.env.example` and `.env`
**What it is:** Environment variable templates and your local copy.

**How it fits:**  
- Your app reads config (ports, DB creds) from environment variables.  
- `.env.example` is a **safe-to-commit** template; `.env` is your **local, uncommitted** file with real values.

**Important keys:**
- `APP_HOST`, `APP_PORT` → where FastAPI listens.
- `DB_HOST`, `DB_PORT`, `DB_USER`, `DB_PASSWORD`, `DB_NAME` → Postgres connection settings.

---

## 3) `Makefile`
**What it is:** Shortcuts for common commands.

**How it fits:**  
- Saves you from typing long commands.  
- Encourages consistent workflows (`make run`, `make rev m="..."`, `make migrate`).

**Important targets:**
- `run` → Starts FastAPI in hot-reload mode, pointing to `app` inside `src/amcp/main.py`.
- `rev` → Creates a migration script by **diffing** your SQLAlchemy models vs DB.
- `migrate` → Applies migrations to the database.

---

## 4) `src/amcp/__init__.py`
**What it is:** Marks `src/amcp` as a Python package.

**How it fits:**  
- Allows `from amcp import ...` to work (because we told Poetry the package root is `src`).

**Important lines:**  
- Usually empty, or you might expose package-level symbols later.

---

## 5) `src/amcp/config.py`
**What it is:** Centralized typed configuration via `pydantic-settings`.

**How it fits:**  
- Any part of your app can import `from .config import settings` to read env-config safely and consistently.

**Important lines:**
```python
class Settings(BaseSettings):
    ...
    model_config = SettingsConfigDict(env_file=".env", case_sensitive=False)
```
- `BaseSettings` binds fields from environment variables.
- `env_file=".env"` → loads from a local `.env` during dev.

```python
@property
def database_url_async(self) -> str:
    return (
        f"postgresql+asyncpg://{self.db_user}:{self.db_password}"
        f"@{self.db_host}:{self.db_port}/{self.db_name}"
    )
```
- Builds the SQLAlchemy **async** DSN string used by your engine.

```python
settings = Settings()
```
- A singleton-like instance you import elsewhere.

---

## 6) `src/amcp/db.py`
**What it is:** Database engine and session factory.

**How it fits:**  
- You import `get_session()` in your API routes/services to run DB work with an `AsyncSession`.

**Important lines:**
```python
engine = create_async_engine(settings.database_url_async, future=True, echo=False, pool_pre_ping=True)
```
- `create_async_engine` → async engine for Postgres via `asyncpg`.
- `pool_pre_ping=True` → validates connections before using.

```python
SessionLocal = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
```
- Factory that gives you `AsyncSession` objects.

```python
@asynccontextmanager
async def get_session():
    async with SessionLocal() as session:
        yield session
```
- Context manager ensures sessions are closed properly.

---

## 7) `src/amcp/main.py`
**What it is:** The FastAPI application entry point.

**How it fits:**  
- `uvicorn` loads `app` from here.
- You’ll add routers, middleware, startup/shutdown events later.

**Important lines:**
```python
app = FastAPI(title="Agents + MCP Bootcamp API", version="0.1.0")
```
- Creates the ASGI app. Title/version show up in `/docs`.

```python
@app.get("/health", tags=["system"])
async def health():
    return {"status": "ok"}
```
- A simple probe endpoint to confirm the app is running.

---

## 8) `alembic.ini`
**What it is:** Alembic’s global config file.

**How it fits:**  
- Alembic uses this to know how to connect to your DB and where migration scripts live.

**Important lines:**
```
sqlalchemy.url = postgresql+asyncpg://amcp:amcp@127.0.0.1:5432/amcp
```
- Connection string Alembic uses **for migrations**.

---

## 9) `alembic/env.py`
**What it is:** The runtime “driver” that tells Alembic *how* to run migrations.

**How it fits:**  
- Executes whenever you run `alembic revision` / `alembic upgrade`.
- Configures migration context, database connection, and `Base.metadata`.

**Key sections:**
```python
config = context.config
fileConfig(config.config_file_name)
```
- Loads Alembic config + logging.

```python
target_metadata = None
```
- Will later be replaced with `Base.metadata` from your models.

```python
def run_migrations_offline(): ...
```
- Generates SQL strings without connecting to DB.

```python
def do_run_migrations(connection: Connection): ...
```
- Executes migrations against a live DB connection.

```python
async def run_migrations_online(): ...
```
- Uses async engine, connects, and applies migrations.

```python
if context.is_offline_mode(): ...
else: asyncio.run(run_migrations_online())
```
- Switch depending on mode.

**Mental model:** `env.py` = Alembic’s adapter. You wire in your models here, it handles running migrations.

---

## 10) `alembic/script.py.mako` & `alembic/versions/`
**What it is:**  
- Template + folder for generated migration scripts.

**How it fits:**  
- `make rev m="..."` → creates a new file in `versions/` with `upgrade()` and `downgrade()`.

---

# ✅ Sanity Checks
- Run `poetry install`
- Start API: `make run` → visit `http://127.0.0.1:8000/health` and expect `{"status": "ok"}`
- DB check: `psql -h 127.0.0.1 -U amcp -d amcp -c "SELECT version();"`

---

# 🎯 Recap
- Poetry → reproducible environment & dependency mgmt.  
- FastAPI skeleton → API base for later MCP/agents.  
- Pydantic settings → clean configuration via `.env`.  
- Async SQLAlchemy + asyncpg → real-world DB layer.  
- Alembic (async env.py) → schema migrations.  
- Local Postgres (bare metal) → practice with production-style DB, no Docker magic.

