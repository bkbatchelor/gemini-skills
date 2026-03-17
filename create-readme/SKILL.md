---
name: create-readme
description: Generates or updates a high-quality README.md for a project, including support for multi-module Gradle builds. Use when the user asks to create or update project documentation, generate a README, or document the codebase.
---

# Create README Skill

## Overview

This skill helps you autonomously analyze a project's codebase and generate a comprehensive `README.md` file that accurately reflects its architecture, dependencies, and structure.

## Workflow Decision Tree

### 1. Project Analysis

Start by analyzing the root directory to determine the tech stack and project structure:
- Check for build files: `build.gradle`, `pom.xml`, `package.json`, `go.mod`, `requirements.txt`, etc.
- Identify the primary language and frameworks.

### 2. Multi-Module Project Check

Check if this is a Gradle multi-module project by looking for a `settings.gradle` or `settings.gradle.kts` file.
- If it is a multi-module Gradle project, consult the [Gradle Multi-Module Guide](references/gradle-multi-module.md) for instructions on how to parse subprojects and their dependencies.

### 3. README Generation

Generate the documentation using the provided template at [README Template](assets/readme-template.md).
- Ensure all sections are properly populated based on your analysis.
- If the project has sub-modules, clearly list them in the "Modules" section.
- Extract any setup or usage scripts defined in package descriptors or build files for the "Installation" and "Usage" sections.

### 4. Write to File

Save the generated markdown to `README.md` in the root of the project.