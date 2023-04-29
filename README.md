# Django Storage API Comparison

This Django project is an API implementation for comparing the performance analytics of public cloud storage and IPFS using various parameters. The project is created for a blockchain class to explore the differences in performance between centralized cloud storage providers and decentralized IPFS storage.

## Features

- Upload files to Azure Blob Storage or IPFS using Pinata
- Download files from Azure Blob Storage or IPFS
- Delete files from Azure Blob Storage or IPFS
- Compare performance analytics for public cloud storage and IPFS

## Getting Started

Follow the steps below to set up the project on your local machine.

### Prerequisites

- Python 3.6 or higher
- pip
- virtualenv

### Installation

1. Clone the repository:

```bash
git clone https://github.com/srikar58/Blockchain_storage_analytics.git
cd django-storage-api-comparison
```

2. Create a virtual environment and activate it:
```bash
python -m venv .venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

3.Install the required packages:
```bash
pip install -r requirements.txt
```

4.Create a .env file in the root directory of your Django project and add your Azure Blob Storage and Pinata API keys:
```bash
AZURE_STORAGE_CONNECTION_STRING=your-azure-storage-connection-string
PINATA_API_KEY=your-pinata-api-key
PINATA_SECRET_API_KEY=your-pinata-secret-api-key
```

Replace the placeholders with your actual Azure and Pinata credentials.

5.Start the development server:
```bash
python manage.py runserver
```

Now, you can access the API endpoints at http://localhost:8000/api/.

## API Endpoints

### Upload

- **URL:** `/api/upload/`
- **Method:** `POST`
- **Form Data:**
  - `file`: The file to be uploaded.
  - `storage_type`: The storage type where the file will be uploaded, either `azure` or `ipfs`.

### Download

- **URL:** `/api/download/`
- **Method:** `POST`
- **Form Data:**
  - `file_identifier`: The name of the file(hash key or name) to be downloaded.
  - `storage_type`: The storage type from where the file will be downloaded, either `azure` or `ipfs`.

### Delete

- **URL:** `/api/delete/`
- **Method:** `POST`
- **Form Data:**
  - `file_identifier`: The identifier of the file(hash key or name) to be deleted.
  - `storage_type`: The storage type where the file will be deleted or unpinned, either `azure` or `ipfs`.

