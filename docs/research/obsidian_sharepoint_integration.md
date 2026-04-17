# Integrating Obsidian with AMS Microsoft 365 (SharePoint & OneDrive)

Given that AMS operates within the Microsoft 365 ecosystem, integrating a local, file-based tool like Obsidian requires a strategic approach to bridge the gap between cloud-based project document stores (SharePoint) and the researcher's local knowledge graph (Obsidian).

## 1. The Core Infrastructure: OneDrive Desktop Sync
The most robust and immediate method for AMS staff on Windows/macOS is to leverage the native OneDrive sync client.

*   **The Setup:** A user navigates to the relevant AMS Project in SharePoint online and clicks **"Sync"**. This creates a local folder on their PC (e.g., `C:\Users\[Username]\AMS Archaeological Management Solutions\[Project Name] - Documents`).
*   **The Vault:** The user then opens Obsidian and selects a sub-folder within that synced SharePoint directory as their "Vault".
*   **The Critical Rule ("Always Keep on This Device"):** Because Obsidian expects files to be instantly available on the hard drive, staff *must* right-click the Vault folder in Windows Explorer/Finder and select **"Always keep on this device"**. If OneDrive tries to use "Files On-Demand" (offloading files to the cloud to save space), Obsidian will throw errors or lose access to notes and plugins.

**Advantages:** Full version history via SharePoint, automatic cloud backup, and the ability for multiple team members to access the same Vault.

## 2. Mobile Access: The "Remotely Save" Plugin
If AMS staff need to access their SharePoint-hosted Obsidian Vaults on mobile devices (iOS/Android) while in the field, the native OneDrive app cannot expose the folder structure to the mobile Obsidian app.

*   **The Solution:** The community plugin **"Remotely Save"**.
*   **How it Works:** This plugin authenticates directly with OneDrive/SharePoint via the Microsoft Graph API. It performs a manual or scheduled two-way sync between the mobile device's local storage and the cloud.
*   **Advantage:** Allows field archaeologists to add site notes or transcriptions directly into the project Vault from their phones, which then syncs back to the main SharePoint repository for the desktop team.

## 3. Linking Evidence: M365 Web URIs & Embedding
Obsidian excels at linking, but we must avoid duplicating massive PDFs or Excel sheets (like a Trench Register) inside the Obsidian Vault if they already live in SharePoint.

*   **The Solution:** Staff can use "Copy Link" in SharePoint to get the web URL of a Word doc or Excel sheet. In Obsidian, they create a standard Markdown link: `[Trench 4 Register](https://ams-my.sharepoint.com/...)`.
*   **Advanced Embedding:** For dashboards or key reference documents, staff can use the `<iframe>` embed code provided by Word/Excel Online to view the live document *inside* an Obsidian note, ensuring they are always looking at the single source of truth.

## 4. Collaborative Best Practices
To make this work in a multi-user AMS environment, we must establish strict Standard Operating Procedures (SOPs):
*   **No Simultaneous Editing:** Obsidian does not have Google Docs-style real-time collaboration for the same text file over OneDrive. Staff must avoid editing the exact same note simultaneously to prevent OneDrive from creating "conflict copies."
*   **Granular Note Structure:** Encourage staff to create many small notes (e.g., one note per Context or Find) rather than monolithic "Site Report" notes. This drastically reduces the chance of sync conflicts across the team.
