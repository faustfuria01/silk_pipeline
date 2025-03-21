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

Translated with DeepL.com (free version)
