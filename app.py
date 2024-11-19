from flask import Flask
import os

app = Flask(__name__)  # Create the Flask app instance

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Get the PORT from the environment, default to 5000
    app.run(host='0.0.0.0', port=port)        # Run the app on the specified port
