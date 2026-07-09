---
title: Contributing Guide
scope: Development setup, commit conventions, pull request process, and code style
last_updated: 2026-03-27
---

# Contributing

Thank you for your interest in contributing! This guide will help you get started.

## Development Setup

1. **Fork and clone** the repository:

   ```bash
   git clone https://github.com/jeff-is-working/<repo-name>.git
   cd <repo-name>
   ```

2. **Install dependencies**:

   ```bash
   # Node.js projects
   npm install

   # Python projects
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Copy environment variables**:

   ```bash
   cp .env.example .env
   ```

4. **Run the development server** (if applicable):

   ```bash
   npm run dev
   ```

## Commit Messages

This project follows [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>(<scope>): <description>

[optional body]

[optional footer(s)]
```

**Types**: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`, `ci`

**Examples**:
- `feat(auth): add OAuth2 login support`
- `fix(api): handle null response from external service`
- `docs: update deployment instructions`

## Pull Request Process

1. Create a feature branch from `main`:

   ```bash
   git checkout -b feat/my-feature
   ```

2. Make your changes and commit using conventional commits.

3. Push your branch and open a pull request against `main`.

4. Fill out the PR template completely.

5. Ensure all CI checks pass.

6. Request a review from a maintainer.

## Code Style

- Follow existing patterns in the codebase
- Write meaningful variable and function names
- Add comments only where the logic isn't self-evident
- Write tests for new functionality

## Reporting Issues

- Use the provided issue templates
- Include steps to reproduce for bugs
- Check existing issues before creating a new one

## Questions?

Open a [discussion](https://github.com/jeff-is-working/<repo-name>/discussions) for questions or ideas.
