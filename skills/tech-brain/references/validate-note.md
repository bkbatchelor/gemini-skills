# validate-note

This skill is a child of the `tech-brain` skill and inherits all of its procedures and rules.

## Overview
The `validate-note` skill accepts a file name as an argument. It verifies the contents of the specified note against authoritative resources to ensure accuracy and reliability.

## Workflow
1. **Identify Topics:** Run the provided Python script (`./scripts/validate.py <file_name>`) to scan the note and identify its main topics.
2. **Validate:** Use your reasoning and search capabilities to verify the contents of the note based on the identified topics against authoritative resources.
3. **Score and Report:** Output a final message containing:
   - A **correctness score** ranging from 0.0 to 1.0.
   - If the correctness score is less than 1.0, provide **recommendations** to resolve the discrepancies.
   - A list of the **resources** used in the validation.

## Resources
- **Script:** `./scripts/validate.py  - Scans the note to identify its main topics.