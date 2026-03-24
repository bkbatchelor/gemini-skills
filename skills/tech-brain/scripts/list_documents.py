#!/usr/bin/env python3
import json
import subprocess
import sys

ROOT_FOLDER_NAME = "TECH-BRAIN"

def run_gws_query(query, fields="files(id,name,mimeType,parents)"):
    cmd = ["gws", "drive", "files", "list", "--params", json.dumps({"q": query, "fields": fields})]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        return []
    # Strip keyring warnings
    out = res.stdout.strip().split('\n')
    json_str = "\n".join([line for line in out if not line.startswith("Using keyring")])
    try:
        data = json.loads(json_str)
        return data.get("files", [])
    except Exception:
        return []

def main():
    # 1. Find root folder
    root_files = run_gws_query(f"name='{ROOT_FOLDER_NAME}' and mimeType='application/vnd.google-apps.folder' and trashed=false", "files(id,name)")
    if not root_files:
        print(f"Error: Could not find '{ROOT_FOLDER_NAME}' folder.", file=sys.stderr)
        return
    
    root_id = root_files[0]['id']
    
    # 2. Get all files and folders iteratively
    folders_to_process = [(root_id, "")]
    
    while folders_to_process:
        current_id, current_path = folders_to_process.pop(0)
        
        children = run_gws_query(f"'{current_id}' in parents and trashed=false")
        
        # Sort children for consistent output: folders first, then files
        children.sort(key=lambda x: (x.get("mimeType") != "application/vnd.google-apps.folder", x.get("name", "")))
        
        for child in children:
            name = child.get("name", "Unknown")
            is_folder = child.get("mimeType") == "application/vnd.google-apps.folder"
            
            if is_folder and (name.startswith("_") or name.startswith(".Trash")):
                continue
                
            path = f"{current_path}/{name}" if current_path else name
            
            if is_folder:
                folders_to_process.append((child['id'], path))
            else:
                print(path)

if __name__ == "__main__":
    main()