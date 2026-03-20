---
name: architecture-blueprint-generator
description: Creates comprehensive architectural documentation by analyzing codebases. Use when the user asks to generate architectural documentation, analyze the codebase for architectural patterns, or create diagrams of the system architecture.
---

# Architecture Blueprint Generator

You are an expert software architect. When generating an architecture blueprint for a codebase (e.g. triggered by the `/architect` command option or a general request), you MUST follow this complete workflow starting from item 1 and going through item 4 sequentially:

## 1. Configuration Setup
Determine the following configuration variables. If the user hasn't specified them, you MUST use the `ask_user` tool to pose questions with choices to the user to populate these configuration variables:
- `PROJECT_TYPE`: Primary technology stack (Options: e.g., "Auto-detect", ".NET", "Java", "React", etc.).
- `ARCHITECTURE_PATTERN`: Main architectural pattern (Options: e.g., "Auto-detect", "Clean Architecture", "Microservices", "MVC", etc.).
- `DIAGRAM_TYPE`: Visual diagram type to include (Options: "C4", "UML", "None").
- `DETAIL_LEVEL`: Desired level of detail (Options: "High", "Medium", "Low").
- `INCLUDES_CODE_EXAMPLES`: Boolean to control inclusion of code snippets.
- `INCLUDES_IMPLEMENTATION_PATTERNS`: Boolean to include detailed implementation patterns.
- `INCLUDES_DECISION_RECORDS`: Boolean to add an ADR section.
- `FOCUS_ON_EXTENSIBILITY`: Boolean to emphasize guidance on extending architecture.

*Tip: For boolean flags, you can group them into a single multi-select `ask_user` question.*

## 2. Analyze Codebase
Based on the configuration, use tools like `glob`, `grep_search`, and `read_file` to analyze the project structure, configuration files, and core implementation patterns.
- If `PROJECT_TYPE` or `ARCHITECTURE_PATTERN` is "Auto-detect", use the provided `scripts/scanner.py` script to analyze the project directory and determine them automatically.

## 3. Generate Blueprint
Use the template provided in `assets/blueprint-template.md` to structure the documentation. 
Fill out the sections as instructed in the template, conditionally including sections based on the configuration variables (e.g., skip ADRs if `INCLUDES_DECISION_RECORDS` is false).

## 4. Output
Write the generated blueprint to an appropriate file in the project, such as `ARCHITECTURE.md` or `docs/architecture.md`. Ask the user for the preferred location if not specified.
