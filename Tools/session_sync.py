import os

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

def sync_session():
    """
    AMS Session Synchroniser
    Aggregates global standards and the latest project logs for AI onboarding.
    """
    print("--- AMS SESSION INITIALISATION ---")
    
    cwd = os.getcwd()
    root_dir = find_root(cwd)
    
    # 1. Global Standards (Always from Root)
    paths = [
        'GEMINI.md',
        'Templates/AMS_Style_Guide.md',
        'DOC_PRODUCTION_STANDARD.md'
    ]
    
    for path in paths:
        full_path = os.path.join(root_dir, path)
        if os.path.exists(full_path):
            print(f"\n[READING STANDARD: {path}]")
            with open(full_path, 'r', encoding='utf-8') as f:
                # Print first 20 lines for context
                lines = f.readlines()
                print("".join(lines[:20]))

    # 2. Latest Logs (Root + Local)
    # Root log (project_log.md)
    root_log = os.path.join(root_dir, 'project_log.md')
    if os.path.exists(root_log):
        print(f"\n[READING LOG: project_log.md]")
        with open(root_log, 'r', encoding='utf-8') as f:
            # Print last 30 lines of the main project log
            lines = f.readlines()
            print("".join(lines[-30:]))

    # 3. Local Context (Sub-directory log)
    # Search for files ending in log.md in the CWD
    for file in os.listdir('.'):
        if file.endswith('log.md') and file != 'project_log.md':
            print(f"\n[READING LOCAL LOG: {file}]")
            with open(file, 'r', encoding='utf-8') as f:
                # Print last 2000 chars
                content = f.read()
                print(content[-2000:])

    # 4. Structured Handover
    if os.path.exists('handover.json'):
        print("\n[DETECTED STRUCTURED HANDOVER: handover.json]")
        with open('handover.json', 'r', encoding='utf-8') as f:
            print(f.read())

    print("\n--- SYNCHRONISATION COMPLETE: READY FOR INSTRUCTIONS ---")

if __name__ == "__main__":
    sync_session()
