# Agro Predict Backend

Backend foundation for the Agro-Processing Supply Predictability System.

## Project structure

```text
agro-predict-backend/
├── .env.example                           # Example environment variables for local runs
├── .gitignore                             # Ignore local environment and generated files
├── Dockerfile                             # Container build definition for the backend
├── docker-compose.yml                     # Local service orchestration for app and dependencies
├── pyproject.toml                         # Python app configuration and dependency metadata
├── alembic.ini                            # Alembic migration configuration
├── alembic/                               # Database migration scripts
│   ├── env.py                             # Migration environment setup
│   ├── script.py.mako                     # Migration template
│   └── versions/                          # Future database migration versions
├── README.md                              # Backend setup and structure documentation
├── src/
│   ├── main.py                            # FastAPI application entry point
│   ├── common/                            # Shared utilities and reusable backend logic
│   ├── core/                              # Core app configuration and database setup
│   │   ├── __init__.py                    # Core package initializer
│   │   ├── config.py                      # Environment and app settings
│   │   └── database.py                    # Database connection and engine configuration
│   ├── integrations/                      # External integrations (telephony, APIs, gateways)
│   ├── modules/                           # Business-domain modules
│   │   ├── auth/                          # Authentication, users, roles, permissions
│   │   ├── commodities/                   # Commodity catalog and product definitions
│   │   ├── demand/                        # Processor demand records and requirements
│   │   ├── farms/                         # Farmer profiles, farms, crops, and field data
│   │   ├── forecasting/                   # Supply forecasting logic and prediction services
│   │   ├── matching/                      # Supply-to-demand matching and gap analysis
│   │   ├── supply/                        # Supply records, inventory, expected harvest, stock
│   │   ├── sync/                          # Synchronization tasks and import/export logic
│   │   └── telephony/                     # SMS/call communication and field notification flows
│   └── workers/                           # Background processing and async tasks
│       └── tasks/                         # Scheduled or deferred jobs such as notifications and sync
└── .venv/                                 # Local virtual environment for development
```

## Module responsibilities

### `src/core`

Handles the application foundation:

- configuration via `config.py`
- database setup via `database.py`
- shared startup behavior for the API

### `src/modules/auth`

Responsible for user authentication and authorization.

- login and session handling
- roles and permissions
- platform accounts for farmers, processors, warehouses, and administrators

### `src/modules/farms`

Handles farm and producer data.

- farmer profiles
- farm registration
- crop and acreage data
- planting and harvest tracking

### `src/modules/commodities`

Defines the agricultural commodities used across the system.

- crop names and categories
- quality classifications
- commodity metadata

### `src/modules/supply`

Tracks actual and expected supply.

- available quantities
- store and warehouse inventory
- expected and actual harvest
- supply reports for processors

### `src/modules/demand`

Captures processor needs.

- purchase requirements
- commodity demand schedules
- required delivery dates
- demand aggregation and review

### `src/modules/forecasting`

Supports prediction and planning.

- historical trend analysis
- future supply estimation
- forecasting endpoints or service logic
- AI or statistical model integration later

### `src/modules/matching`

Matches available supply with demand.

- compare expected supply vs. processor needs
- detect supply gaps or surpluses
- support procurement planning

### `src/modules/sync`

Handles synchronization and data maintenance.

- import/export flows
- upstream or downstream data alignment
- job-based updates and reconciliation

### `src/modules/telephony`

Supports communication functions.

- SMS alerts
- voice or call workflows
- field notifications and operational updates

### `src/integrations`

Contains external service logic.

- SMS gateways
- telephony providers
- market or weather APIs
- other third-party integrations

### `src/workers/tasks`

Contains background jobs.

- scheduled notifications
- async processing jobs
- forecast refresh tasks
- data cleaning or syncing operations

### `alembic/versions`

Stores database schema migration scripts for evolving the project data model.

## Run locally

```powershell
python -m uvicorn src.main:app --reload
```

Copy `.env.example` to `.env` before starting dependent services.
