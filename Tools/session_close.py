import os
import sys
import datetime
import json

def find_root(start_dir):
    """
    Traverse up to find the root directory of the AMS monorepo.
    The root's GEMINI.md always starts with "# GEMINI Project: AMS Digital Ecosystem".
    """
    current = start_dir
    while current != os.path.dirname(current): # Stop at drive root
        gemini_path = os.path.join(current, 'GEMINI.md')
        if os.path.exists(gemini_path):
            with open(gemini_path, 'r', encoding='utf-8') as f:
                first_line = f.readline()
                if "AMS Digital Ecosystem" in first_line:
                    return current
        current = os.path.dirname(current)
    return start_dir

def close_session(summary, pending_tasks=None):
    """
    AMS Session Closer
    Automates the update of root and local logs with structured JSON handovers.
    Usage: python Tools/session_close.py "Summary of work done" '["Task 1", "Task 2"]'
    """
    today = datetime.date.today().strftime('%Y-%m-%d')
    cwd = os.getcwd()
    root_dir = find_root(cwd)
    dir_name = os.path.basename(cwd)
    
    tasks = pending_tasks if pending_tasks else []
    
    # Structured Handover Data
    handover_data = {
        "date": today,
        "module": dir_name,
        "summary": summary,
        "pending_tasks": tasks,
        "status": "Handover Complete"
    }

    # Format for Markdown
    json_stub = json.dumps(handover_data, indent=4)
    log_entry = f"""
## {today} - Session Close
*   **Summary:** {summary}
*   **Pending Tasks:** {", ".join(tasks) if tasks else "None"}
*   **Handover Status:** Complete

```json
{json_stub}
```
"""

    # 1. Update Local Log (CWD)
    local_log = None
    for file in os.listdir('.'):
        if file.endswith('log.md') and file != 'project_log.md':
            local_log = file
            break
    
    if local_log:
        with open(local_log, 'a', encoding='utf-8') as f:
            f.write(log_entry)
        print(f"Updated local log: {local_log}")
    else:
        print("No local log found in current directory to update.")

    # 2. Update Root Log
    root_log_path = os.path.join(root_dir, 'project_log.md')
    if os.path.exists(root_log_path):
        with open(root_log_path, 'a', encoding='utf-8') as f:
            f.write(f"\n## {today} - [{dir_name}] Update\n* {summary}\n")
            if tasks:
                f.write(f"* **Pending:** {', '.join(tasks)}\n")
        print(f"Updated root log: {root_log_path}")
    else:
        print(f"Root log not found at: {root_log_path}")

    # 3. Save Standalone Handover Stub (CWD)
    with open('handover.json', 'w', encoding='utf-8') as f:
        json.dump(handover_data, f, indent=4)
    print("Generated standalone handover.json")

    print("\n--- SESSION CLOSED: Neural Bridge Updated ---")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        summary_arg = sys.argv[1]
        tasks_arg = []
        if len(sys.argv) > 2:
            try:
                tasks_arg = json.loads(sys.argv[2])
            except json.JSONDecodeError:
                tasks_arg = [sys.argv[2]]
        close_session(summary_arg, tasks_arg)
    else:
        print("Error: Please provide a summary of the session.")
        print("Usage: python Tools/session_close.py \"Your summary here\" '[\"Pending Task 1\"]'")
