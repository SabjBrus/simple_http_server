import http.server
import socketserver
import json
import pickle


class Record:
    """Класс записи."""
    def __init__(self, id, data):
        self.id = id
        self.data = data


def save_records():
    """Сохранение записи."""
    with open('records.pickle', 'wb') as file:
        pickle.dump(records, file)


def load_records():
    """Загрузка записи."""
    try:
        with open('records.pickle', 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        return {}


records = load_records()


class RequestHandler(http.server.BaseHTTPRequestHandler):
    def do_POST(self):
        """HTTP метод POST."""
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = json.loads(post_data)
        id = data['id']
        record_data = data['data']
        records[id] = Record(id, record_data)
        save_records()
        self.send_response(200)
        self.end_headers()

    def do_GET(self):
        """HTTP метод GET."""
        path_parts = self.path.split('/')
        if path_parts[1].isdigit():
            id = int(path_parts[1])
            if id in records:
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps(records[id].__dict__).encode())
            else:
                self.send_response(404)
                self.end_headers()
        else:
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps([record.__dict__ for record in records.values()]).encode())


PORT = 8080
Handler = RequestHandler
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
