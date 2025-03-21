# Silk Data Pipeline Exercise

**Description:**  
Pipeline to retrieve, normalize and deduplicate host data from Qualys and Crowdstrike with asynchronous queries, logging and visualization.

**Requirements:**  
- Python 3.10  
- MongoDB (or docker-compose for deployment)

**Install and run (locally):**  
1. Create a virtual environment: `python -m venv venv`.  
2. activate the environment and install dependencies: `pip install -r requirements.txt`.  
3. Set up environment variables, Copy the example file: `cp .env.example .env`.
4. Run the application: `python main.py`.  

**Run/Down with Docker:**  
1. Build and run the containers: `docker-compose up --build`  
2. To shut down and remove containers: `docker-compose down -v`

**Testing:**  
Run the tests with the command: `pytest`.

**Visualization:**  
The charts are saved in the `charts/` folder.

# Project Structure

```plaintext
silk_pipeline/
├── config.py              # Loads environment variables from .env
├── logging_config.py      # Configures structured logging for the project
├── main.py                # Entry point of the application
├── README.md              # This file
├── requirements.txt       # Python dependencies
├── Dockerfile             # Docker build instructions
├── docker-compose.yml     # Docker Compose configuration
├── .env.example           # Example environment variables file
├── db/
│   └── mongodb_client.py  # MongoDB connection helper
├── deduplication/
│   └── deduper.py         # Deduplication logic
├── fetcher/
│   ├── async_qualys_client.py      # Asynchronous API client for Qualys
│   └── async_crowdstrike_client.py # Asynchronous API client for Crowdstrike
├── normalization/
│   └── normalizer.py      # Data normalization logic
├── visualization/
│   └── charts.py          # Chart generation with matplotlib
└── tests/
    ├── test_normalizer.py # Unit tests for normalization functions
    └── test_deduper.py    # Unit tests for deduplication logic

