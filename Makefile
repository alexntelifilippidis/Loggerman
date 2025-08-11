# Makefile for Loggerman (Python logger project with Hatch + Ruff)

.PHONY: help install dev activate activate-dev remove-envs build publish test lint format clean bump-patch bump-minor bump-major

# 🛟 Show help menu
help:
	@echo "Available commands:"
	@echo "  make install       - Install dependencies"
	@echo "  make dev           - Install dev dependencies"
	@echo "  make activate      - Activate the default environment"
	@echo "  make activate-dev  - Activate the dev environment"
	@echo "  remove-envs        - Remove all enviroments"
	@echo "  make build         - Build the package"
	@echo "  make publish       - Publish to PyPI"
	@echo "  make test          - Run tests"
	@echo "  make lint          - Run Ruff linting"
	@echo "  make format        - Auto-fix with Ruff"
	@echo "  make clean         - Remove build artifacts"
	@echo "  make bump-patch    - Bump patch version"
	@echo "  make bump-minor    - Bump minor version"
	@echo "  make bump-major    - Bump major version"

# 📦 Install production dependencies
install:
	hatch env create

# 🧪 Install dev dependencies
dev:
	hatch env create dev

# 🐍 Activate the default environment
activate:
	hatch shell

# 🐍 Activate the dev environment
activate-dev:
	hatch shell dev

# 🧽 Remove all hatch envs
remove-envs:
	hatch env prune

# 🔨 Build the package
build:
	hatch build

# 🚀 Publish to PyPI
publish:
	hatch publish

# ✅ Run tests
test:
	hatch test --cover

# 🔍 Lint with Ruff
lint:
	hatch run ruff check .
	hatch run check

# ✨ Format with Ruff
format:
	hatch run ruff check . --fix

# 🧽 Remove build artifacts
clean:
	rm -rf build/ dist/ *.egg-info .pytest_cache .mypy_cache

# ⚙️ Version bumping commands
bump-patch:
	hatch version -b patch

bump-minor:
	hatch version -b minor

bump-major:
	hatch version -b major