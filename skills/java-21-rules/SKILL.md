---
name: java-21-rules
description: Rules and best practices for developing in Java 21. Use when writing, refactoring, or reviewing Java 21 code, specifically around concurrency, threading, virtual threads, pinning, try-catch statements, and records.
---

# Java 21 Rules

## Overview

This skill provides the essential rules and best practices for writing modern Java 21 applications. It focuses heavily on the new concurrency model, threading improvements (especially Virtual Threads), thread pinning, modern error handling via try-catch statements, and the use of records.

## Usage

When working on a Java codebase, consult the reference files to ensure your code complies with Java 21 standards:

1. **Concurrency, Threading, Virtual Threads, and Pinning:** See [references/concurrency-and-threads.md](references/concurrency-and-threads.md) for detailed rules on when to use Virtual Threads, how to avoid pinning, and general concurrency best practices.
2. **Try-Catch Statements and Error Handling:** See [references/try-catch-patterns.md](references/try-catch-patterns.md) for patterns using try-with-resources, multi-catch, and exception handling within Structured Concurrency.
3. **Records and Data Classes:** See [references/records-and-data-classes.md](references/records-and-data-classes.md) for rules on using records instead of traditional POJOs.

Always prioritize readability, modern language features (like switch expressions and pattern matching where applicable alongside these concurrency rules), and correct resource management.
