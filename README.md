# 🚀 Azure Table Storage Project

**Author:** Atul Kamble
**Role:** Cloud Solutions Architect | DevOps Trainer

---

# 📌 Project Overview

Azure Table Storage is a **NoSQL key-value store** designed for **massive scalability, low latency, and cost efficiency**.

### 🔥 Use Cases

* User profile storage
* IoT data ingestion
* Logging & monitoring
* Metadata storage

---

# 🏗️ Architecture Diagram

![Image](https://learn.microsoft.com/en-us/azure/storage/tables/media/storage-table-design-guide/storage-table-design-image12.png)

![Image](https://learn.microsoft.com/en-us/azure/includes/media/storage-table-concepts-include/table1.png)

![Image](https://docs.losant.com/assets/images/azure-table-storage-credentials-f5de0f22f3df1eb183d91b8180e18d81.png)

---

# 🧱 Components

| Component       | Description                     |
| --------------- | ------------------------------- |
| Storage Account | Base resource for Table Storage |
| Table           | Collection of entities          |
| Entity          | Individual record (like row)    |
| Partition Key   | Used for scalability            |
| Row Key         | Unique identifier               |

---

# ⚙️ Step 1: Create Storage Account

### Azure CLI

```bash
az login

az group create \
  --name table-rg \
  --location eastus

az storage account create \
  --name mystoragetable12345 \
  --resource-group table-rg \
  --location eastus \
  --sku Standard_LRS \
  --kind StorageV2
```

---

# 📦 Step 2: Create Table

```bash
az storage table create \
  --name mytable \
  --account-name mystoragetable12345
```

---

# 🧾 Step 3: Insert Data (Entity)

```bash
az storage entity insert \
  --table-name mytable \
  --entity PartitionKey=Users RowKey=1 Name=Atul Age=30 \
  --account-name mystoragetable12345
```

---

# 🔍 Step 4: Query Data

```bash
az storage entity query \
  --table-name mytable \
  --account-name mystoragetable12345
```

---

# 💻 Step 5: Python SDK Example

```python
from azure.data.tables import TableServiceClient

connection_string = "your_connection_string"

service = TableServiceClient.from_connection_string(conn_str=connection_string)

table_name = "mytable"
table_client = service.get_table_client(table_name)

entity = {
    "PartitionKey": "Users",
    "RowKey": "2",
    "Name": "Cloud Architect",
    "Age": 32
}

table_client.create_entity(entity=entity)

print("Entity inserted successfully!")
```

---

# 🔐 Step 6: Security Best Practices

* Use **Azure AD authentication** instead of keys
* Enable **Private Endpoint**
* Rotate access keys regularly
* Use **RBAC roles (Storage Table Data Contributor)**

---

# 📊 Data Model Design

![Image](https://learn.microsoft.com/en-us/rest/api/storageservices/media/azu_ch03_figure1.png)

![Image](https://miro.medium.com/1%2AsVr2MliIU2fCMwD2hZNhhA.jpeg)

![Image](https://learn.microsoft.com/en-us/azure/storage/tables/media/storage-table-design-guide/storage-table-design-image12.png)

![Image](https://learn.microsoft.com/en-us/azure/includes/media/storage-table-concepts-include/table1.png)

### 💡 Key Concepts

| Concept      | Explanation         |
| ------------ | ------------------- |
| PartitionKey | Groups related data |
| RowKey       | Unique identifier   |
| No Schema    | Flexible structure  |
| Indexed Keys | Fast lookups        |

---

# ⚡ Performance Tips

* Choose **good PartitionKey** (avoid hotspots)
* Use **batch operations**
* Avoid frequent updates on same partition
* Use **filter queries**

---

# 🚀 Advanced Features

* TTL (Time-to-Live via logic)
* Integration with Azure Functions
* Event-driven architecture
* Scalable to billions of records

---

# 🔄 CI/CD Integration (Azure DevOps)

### Example Pipeline Snippet

```yaml
trigger:
- main

pool:
  vmImage: ubuntu-latest

steps:
- script: |
    az login --service-principal \
      -u $(clientId) \
      -p $(clientSecret) \
      --tenant $(tenantId)

    az storage table create \
      --name mytable \
      --account-name mystoragetable12345
  displayName: "Create Table"
```

---

# 🧪 Testing Commands

```bash
# Insert multiple records
for i in {1..5}
do
  az storage entity insert \
    --table-name mytable \
    --entity PartitionKey=Test RowKey=$i Name=User$i \
    --account-name mystoragetable12345
done
```

---

# 📈 Monitoring

* Enable **Azure Monitor**
* Use **Metrics & Logs**
* Integrate with **Log Analytics**

---

# 📌 Points to Remember (Exam-Oriented)

* Azure Table Storage = **NoSQL Key-Value Store**
* Uses **PartitionKey + RowKey**
* Schema-less design
* Highly scalable
* Cost-effective

---

# 📂 Recommended GitHub Structure

```
azure-table-storage-project/
│
├── README.md
├── scripts/
│   ├── create-storage.sh
│   ├── insert-data.sh
│
├── python-app/
│   ├── app.py
│   └── requirements.txt
│
├── azure-pipelines.yml
└── architecture.png
```

---

# 🎯 Real-Time Use Case

👉 Build a **User Management System**

* Store user profiles
* Track login activity
* Scale to millions of users

---

# 🔚 Conclusion

Azure Table Storage is:

* Simple
* Scalable
* Cost-efficient

Perfect for **DevOps, cloud-native, and high-scale applications**.

---
