# process-inbox

You are executing the `tb-process-inbox` workflow. This is a child skill of the `tech-brain` skill.

## Objective
Automatically scan the `00_inbox` folder inside the `TECH-SECOND-BRAIN` directory on Google Drive and process any files found within it.

## Procedures

You MUST follow all the rules and procedures defined in the `tech-brain` skill when processing these files. Specifically, you must execute the following steps for each file found in the `00_inbox`:

1.  **Scan `00_inbox`**: Find the `00_inbox` folder inside the `TECH-SECOND-BRAIN` root directory. List all non-trashed files inside it.
2.  **Apply Templates**: Review the file content and format it cleanly using templates found in `.resources/templates`, or create a new template if none fit.
3.  **Folder Maintenance**: Determine the appropriate destination folder (`01_projects`, `02_areas`, `03_resources`) for the file based on its content. Move/save the formatted file there. If updating an existing document, copy the original to `04_archives` first. Create any missing subfolders as required.
4.  **Front-matter**: Add a mandatory front-matter block with `title`, `description` (1-2 sentences), and `tags` (using the tags from `.resources/tags.json`).
5.  **Clean Up**: Move the original raw file from `00_inbox` to Trash after the new file is fully formatted and saved. Ensure no empty topic folders remain.

For full details on these steps and constraints, refer to the parent `tech-brain` skill instructions.
