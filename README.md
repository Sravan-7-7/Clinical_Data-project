Clinical Data Retrieval System

A lightweight Python-based tool designed to quickly search and retrieve patient medical records from a CSV database. This project is part of a larger initiative to manage and search clinical data efficiently.

🚀 FEATURES:

1.Instant Search: Retrieve full patient details by entering their name.

2.Error Handling: Case-insensitive search with clear feedback if a patient record is missing.

3.Data Integrity: Uses pandas for high-performance data manipulation and indexing.

🛠️ PREREQUISITES:

Before running the script, ensure you have Python and the pandas library installed:  pip install pandas

📂 PROJECT STRUCTURE:

  1.main.py: The core script for searching records.
  
  2.Clinical_Data.csv: The database file (ensure the first column is Name).

  📖 HOW TO USE:
       
  1.Ensure your Clinical_Data.csv file is in the same directory as the script.
  
  2.Run the program:  python main.py

  📈CODE SNIPPET:
  
  The retrieval logic utilizes the .loc indexer for $O(1)$ average time complexity.
