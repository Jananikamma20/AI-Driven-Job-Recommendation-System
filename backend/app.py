from flask import Flask
from flask_cors import CORS

from backend.routes.resume_routes import resume_bp
from backend.routes.recommendation_routes import recommendation_bp

app = Flask(__name__)

# Enable CORS
CORS(app)

app.register_blueprint(resume_bp)
app.register_blueprint(recommendation_bp)

print("\nRegistered Routes:")
for rule in app.url_map.iter_rules():
    print(rule)

@app.route("/")
def home():
    return "THIS IS THE CORRECT FLASK SERVER"

if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=False
    )