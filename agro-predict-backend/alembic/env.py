"""Alembic migration environment."""

from alembic import context


target_metadata = None


def run_migrations_online() -> None:
    raise NotImplementedError("Configure the async SQLAlchemy engine before running migrations.")


if context.is_offline_mode():
    raise NotImplementedError("Offline migrations are not configured yet.")
else:
    run_migrations_online()
