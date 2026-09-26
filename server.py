from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
import threading
import webbrowser

ROOT = Path(__file__).parent

class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

def open_browser():
    webbrowser.open("http://127.0.0.1:8080")

if __name__ == "__main__":
    print("\n  ❤️  Lyrics site is running")
    print("  🌌  Open: http://127.0.0.1:8080")
    print("  🎵  Put your song file at: song.mp3")
    print("  Press Ctrl+C to stop.\n")

    threading.Timer(0.8, open_browser).start()
    server = ThreadingHTTPServer(("0.0.0.0", 8080), Handler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped.")
        server.server_close()
