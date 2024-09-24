# JSONPlaceholder Data Fetcher

This project is a Python script that fetches data from the [JSONPlaceholder API](https://jsonplaceholder.typicode.com/) and saves it into a SQLite database. The script is designed to insert new records and update existing records in the database, ensuring that you always have the most up-to-date information.

## Features

- Fetches posts data from the JSONPlaceholder API.
- Creates a SQLite database and a table for storing the posts.
- Inserts new posts and updates existing ones based on their IDs.
- Scheduled execution using Windows Task Scheduler.

## Requirements

- Python 3.x
- `requests` library
- SQLite3 (comes pre-installed with Python)

## Installation

1. Clone this repository or download the script files.

   ```bash
   git clone https://github.com/yourusername/jsonplaceholder-data-fetcher.git
   cd jsonplaceholder-data-fetcher
   ```

2. Install the required Python packages:

   ```bash
   pip install requests
   ```

## Usage

1. **Run the Script Manually:**

   You can run the script manually to fetch data and save it to the database.

   ```bash
   python script.py
   ```

   Replace `script.py` with the name of your Python script.

2. **Schedule the Script to Run Automatically:**

   To schedule the script to run at specific intervals using Windows Task Scheduler, follow these steps:

   ### Create a Batch File

   Create a batch file (`run_script.bat`) to execute your Python script:

   1. Open Notepad and enter the following content:

      ```bat
      @echo off
      python C:\path\to\your\script.py
      ```

      Replace `C:\path\to\your\script.py` with the actual path to your Python script.

   2. Save the file as `run_script.bat`.

   ### Set Up Windows Task Scheduler

   1. Open **Task Scheduler**:
      - Press `Windows Key + S` and type "Task Scheduler", then open it.

   2. Click on **Create Basic Task** in the right-hand Actions pane.

   3. **Name and Describe** the task:
      - Give your task a name, such as "Run Python Script".
      - Add a description if desired.

   4. **Trigger** the task:
      - Choose how often you want the task to run: daily, weekly, etc.
      - Set the start date, time, and recurrence.

   5. **Action** (start the batch file):
      - Select **Start a Program**.
      - In the **Program/script** field, click **Browse** and select your batch file (`run_script.bat`).

   6. **Finish** the setup:
      - Click **Next** and then **Finish**.

   Now your Python script will run based on the schedule you defined in Windows Task Scheduler.

## Database

The SQLite database file will be named `jsonplaceholder_data.db` and will be created in the same directory as the script. The database will have a table named `posts` with the following schema:

- `id`: INTEGER PRIMARY KEY
- `userId`: INTEGER
- `title`: TEXT
- `body`: TEXT



