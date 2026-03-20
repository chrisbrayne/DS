# Digital Scholar: Publishing & Deployment Strategy

This document outlines the protocol for publishing the **AMS Digital Scholar (DS)** resource site to Netlify via GitHub, ensuring consistency with the **AI Strategy** and **BIM** modules.

## 1. Core Architecture
*   **Static Site Generator:** MkDocs (Material Theme).
*   **Hosting:** Netlify (Primary).
*   **Source Control:** GitHub (AMS Digital Ecosystem Root).
*   **Automation:** Git-triggered builds (Netlify) and `safe_push_all.ps1` (Local Sync).

## 2. Netlify Configuration
The `DS/netlify.toml` file manages the build environment. It is configured to:
1.  Install dependencies from `DS/requirements.txt`.
2.  Build the site using `mkdocs build`.
3.  Publish the resulting `site/` directory.
4.  Enforce a `noindex` header to keep the training resource internal to AMS.

## 3. Automated Sync Workflow
The **DS** module is integrated into the root `safe_push_all.ps1` script. To publish updates:
1.  Complete your edits in the `DS/docs` directory.
2.  Run `powershell .\safe_push_all.ps1` from the project root.
3.  The script will:
    *   Detect changes in the `DS` directory.
    *   Commit changes with an automated timestamp.
    *   Push to the GitHub repository.
    *   Trigger the Netlify build.

## 4. Dependencies (`requirements.txt`)
All necessary plugins and themes must be listed in `DS/requirements.txt`:
*   `mkdocs`
*   `mkdocs-material`
*   `pymdown-extensions`

## 5. Deployment Checklist
- [ ] Verify `mkdocs build` runs locally without errors.
- [ ] Ensure all internal links (e.g., to AI Strategy) are relative and valid.
- [ ] Check `netlify.toml` for correct path resolution.
- [ ] Confirm `safe_push_all.ps1` includes the `DS` directory.

---
*Maintenance of this deployment pipeline is managed by the AI Strategy team.*
