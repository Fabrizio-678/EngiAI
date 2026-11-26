from flask_cors import CORS
from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)
CORS(app)

def connect_with_db():
    conn = sqlite3.connect('links_data_base.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/backend/posts', methods=['GET'])
def get_posts():
    page = int(request.args.get('page', 1))
    limit = int(request.args.get('limit', 14))
    offset = (page - 1) * limit

    conn = connect_with_db()
    cursor = conn.cursor()

    read_db = 'SELECT title, link, description, image_url FROM links LIMIT ? OFFSET ?'
    selected_posts = cursor.execute(read_db, (limit, offset)).fetchall()

    total_posts = cursor.execute('SELECT COUNT(*) FROM links').fetchone()[0]
    conn.close()

    return jsonify({
        'data': [dict(post) for post in selected_posts],
        'page': page,
        'limit': limit,
        'has_more_pages': (offset + limit) < total_posts
    })

if __name__ == '__main__':
    app.run(port=5000, debug=True)
