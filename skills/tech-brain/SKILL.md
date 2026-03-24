---
name: tech-brain
description: Process files from My Drive for insertion into the tech-brain folder. Use when organizing, tagging, or standardizing raw Google Drive files into the Second Brain structure. Triggers: show-toc, process-inbox, validate-note.
---

# Process Files for Tech Second Brain

Follow this strict procedure to review and process files from Google Drive into the `TECH-BRAIN` directory.

## 1. Exclude Private Folders
When querying Google Drive for files, you MUST filter out any folder that is prefixed with an underscore (`_`) or matches `.Trash*`.
- Example exclusions: `_PERSONAL`, `_SANDBOXDEV`, `_LEARNING`, and `.Trash*`.
- Use the Google Drive API query `q` parameter to exclude these parent folder IDs (`not "FOLDER_ID" in parents`).

## 2. Review Files in '00_inbox'
Scan ONLY the `00_inbox` folder (located inside `TECH-BRAIN`) for files that need processing. Ignore files that are already inside organized project structures unless explicitly told otherwise.

## 3. Apply Templates (MANDATORY)
Review the content of each file.
- Apply an appropriate document template to format the file's content cleanly.
- If no suitable template exists for the content type, **create a new one**.
- Save any newly created templates in the template folder located at: `'My Drive > TECH-BRAIN > .resources'`.

## 4. Folder Maintenance & File Placement
Determine the appropriate `TECH-BRAIN` sub-directory (e.g., `01_projects`, `02_areas`, `03_resources`) for the file based on its content and topics.
- **Archive Updates:** If you are updating an existing document (i.e., a file with the same name already exists in the destination or another organized folder), you MUST copy the original version to the `04_archives` directory before overwriting or modifying it.
- **Create missing folders:** If a required subfolder (such as a specific project folder under `01_projects` or a specific topic area under `02_areas`) does not exist, you MUST create it before saving the file.
- Save the formatted file into the appropriate sub-directory.

## 5. Front-matter and Tagging (MANDATORY)
After the file has been formatted and saved, you MUST populate its front-matter block using the template found at `assets/front_matter_template.md`.
- The `title`, `description`, and `tags` fields are MANDATORY in the front-matter block.
- **Title:** A concise, descriptive title for the document.
- **Description:** A brief summary of the file's content (1-2 sentences).
- **Tags:** Retrieve the current `tags.json` file located at `'My Drive > TECH-BRAIN > .resources'` and assign the appropriate tag(s).
- **If no suitable tag exists:** Create a new tag that accurately describes the content. You MUST add this new tag to `tags.json` and ensure it complies with the schema defined in `assets/tags_schema.json`. Update both the tags and the schema if a new category is introduced.

## 6. Clean Up Files and Empty Folders
Once a file has been successfully formatted, tagged, and saved:
- **Move original files to Trash:** You MUST move the original raw file from the `00_inbox` to Trash to prevent clutter. Ensure the new file is fully saved before moving the original.
- **Remove empty topics:** Scan the `TECH-BRAIN` directory and its sub-directories. Remove any topic area folder that are empty to maintain a clean workspace.

## 7. Custom Commands
You support the following custom commands:
- `show-toc`: ./references/show-toc.md
- `process-inbox`:  ./references/process-inbox.md
- `validate-note`: ./references/validate-note.md