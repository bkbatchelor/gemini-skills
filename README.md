# Gemini Skills

> A collection of specialized Agent Skills designed to extend the capabilities of the Gemini CLI with focused workflows, rules, and procedures.

## 🚀 Features

- Enhances Gemini CLI with specialized knowledge and procedural tasks.
- Automates documentation generation and architectural blueprints.
- Organizes Google Drive assets into a "Second Brain" structure.
- Provides strict programming rules and best practices.

## 🛠 Tech Stack

- **Primary Languages**: Markdown, Python
- **Core Frameworks**: Agent Skills Open Standard
- **Environment**: Gemini CLI

## 📦 Skills (Modules)

- **[architecture-blueprint-generator]**: Creates comprehensive architectural documentation by analyzing codebases. Use when you need to generate architectural documentation, analyze the codebase for architectural patterns, or create diagrams of the system architecture.
  - Dependencies: Python
- **[create-readme]**: Generates or updates a high-quality `README.md` for a project, including support for multi-module Gradle builds. Use when you need to create or update project documentation.
- **[java-21-rules]**: Rules and best practices for developing in Java 21. Use when writing, refactoring, or reviewing Java 21 code, specifically around concurrency, threading, virtual threads, pinning, try-catch statements, and records.
- **[tech-brain]**: Process files from My Drive for insertion into the `TECH-SECOND-BRAIN` folder. Use when organizing, tagging, or standardizing raw Google Drive files into the Second Brain structure. Triggers: `show-toc`, `process-inbox`, `validate-note`.
  - Dependencies: Python, Google Workspace CLI (`gws`)

## 💻 Installation

1. Clone the repository:
   ```bash
   git clone git@github.com:bkbatchelor/gemini-skills.git
   ```
2. Install the skills directly to your Gemini CLI or symlink them to your local `~/.gemini/skills/` directory:
   ```bash
   # Using the Gemini CLI
   gemini extensions install $(pwd)/skills/architecture-blueprint-generator
   gemini extensions install $(pwd)/skills/create-readme
   gemini extensions install $(pwd)/skills/java-21-rules
   gemini extensions install $(pwd)/skills/tech-brain
   ```
   *Alternatively, symlink all skills at once:*
   ```bash
   ln -s $(pwd)/skills/* ~/.gemini/skills/
   ```

## 🏃 Usage

Once installed, the skills are automatically discovered by the Gemini CLI. You can view all available skills by running:

```bash
gemini skills list
```

To invoke a skill, simply ask Gemini CLI a question or give it a task that aligns with the skill's description. The CLI will automatically activate the relevant skill based on your request.

## 🤝 Contributing

Contributions are welcome! Please open an issue or submit a pull request if you have ideas for new skills or improvements to existing ones.

## 📜 License

This project is licensed under the [MIT License](LICENSE).
