# 🏡 Databricks Delta Lake Pipeline with Azure DevOps CI/CD

This project demonstrates a **real-world Delta Lake pipeline** with full **CI/CD automation using Azure DevOps** and **Databricks CLI deployment**.

---

## 🚀 What This Project Does

✔️ Ingests and cleans real property management data  
✔️ Writes the result as a Delta Lake table  
✔️ Automates deployment via Azure DevOps Pipelines  
✔️ Deploys the notebook to a Databricks workspace  
✔️ (Optional) Schedules refresh using Databricks Jobs

---

## 💼 Tech Stack

| Component         | Usage                                           |
|------------------|-------------------------------------------------|
| **Databricks**   | Delta Lake storage + PySpark notebook           |
| **Azure DevOps** | CI/CD automation for notebook deployment        |
| **Databricks CLI** | Workspace upload (manual for SCIM/AAD setups) |
| **Python**       | Data wrangling and ETL scripting                |
| **Delta Lake**   | ACID-compliant table storage for large datasets|

---

## 🛠 Project Structure

RentalPipeline/ │ ├── RentalPipeline.py # PySpark notebook logic ├── azure-pipelines.yml # DevOps pipeline config └── README.md

## 🔐 Authentication Notes

> ⚠️ Due to AAD/SCIM enforcement on the Databricks workspace, CLI-based auth was not supported in DevOps.

Deployment was completed using **manual CLI login** via:
```bash
databricks workspace import RentalPipeline.py /Users/<workspace-path> --language PYTHON --overwrite

📦 What You’ll Learn from This Project
✅ How to clean and structure real estate data
✅ How to write to Delta format
✅ How to build a real Azure DevOps YAML pipeline
✅ How to integrate Databricks notebooks into CI/CD
✅ How to troubleshoot the CLI like a boss  

## 📸 Project Screenshots

### 🛡️ Azure DevOps Variable Group
Securely stored and injected Databricks host/token values.

![Variable Group](./screenshots/Variable%20Group.png)

---

### 📓 Databricks Notebook in Workspace
Notebook was successfully deployed to workspace using CLI.

![Databricks Notebook](./screenshots/Databricks%20Notebook.png)

---

### 💥 Job Execution Failure due to Quota Limits
Notebook execution failed due to Azure vCPU quota being exhausted in South India.

![Quota Error](./screenshots/Quota%20Exceeded%20-%20Job%20Failed.png)

---

### 📬 Requested Quota Increase from Azure Portal
Request submitted to unblock execution. Shows real-world issue handling.

![Quota Request](./screenshots/Requesting%20Quota.png)

---

## ⚙️ Deployment Path

1. Data loaded from CSV
2. Cleaned using PySpark
3. Written to Delta Lake
4. YAML pipeline written and deployed
5. Notebook uploaded to workspace via CLI


🧠 Author
Banu V

Azure Data Engineer + Streaming Architect




## 📝 Notes

- This is a real hands-on implementation.
- Built from scratch, encountered real infrastructure blockers.
- Proved full pipeline + DevOps CI/CD capability even without cluster execution.
