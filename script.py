import requests
import sqlite3


# 1. Fetch data from the JSONPlaceholder API
def fetch_api_data(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()  # API returns data in JSON format
    else:
        print(f"Error fetching data from API: {response.status_code}")
        return None


# 2. Create a SQLite database and table for posts
def create_database():
    conn = sqlite3.connect('jsonplaceholder_data.db')  # Connect to SQLite database (or create it)
    cursor = conn.cursor()

    # Create a table for posts (customize the schema based on API data)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY,
            userId INTEGER,
            title TEXT,
            body TEXT
        )
    ''')

    conn.commit()
    return conn


# 3. Insert or update posts data into the SQLite database
def insert_or_update_data(conn, data):
    cursor = conn.cursor()

    # Check if post exists; if it does, update it; otherwise, insert a new record
    for post in data:
        cursor.execute('''
            SELECT * FROM posts WHERE id = ?
        ''', (post['id'],))
        existing_post = cursor.fetchone()

        if existing_post:
            # Update the existing post
            cursor.execute('''
                UPDATE posts
                SET userId = ?, title = ?, body = ?
                WHERE id = ?
            ''', (post['userId'], post['title'], post['body'], post['id']))
        else:
            # Insert a new post
            cursor.execute('''
                INSERT INTO posts (id, userId, title, body)
                VALUES (?, ?, ?, ?)
            ''', (post['id'], post['userId'], post['title'], post['body']))

    conn.commit()


# 4. Main function to run the steps
def main():
    api_url = 'https://jsonplaceholder.typicode.com/posts'  # JSONPlaceholder posts API
    data = fetch_api_data(api_url)

    if data:
        conn = create_database()
        insert_or_update_data(conn, data)
        conn.close()
        print("Data saved to database successfully.")
    else:
        print("No data to save.")


if __name__ == '__main__':
    main()
