
from flask import Flask, jsonify
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
import time
import random

app = Flask(__name__)

# 1. Définition des métriques Prometheus

REQUEST_COUNT = Counter(
    'app_requests_total',
    'Nombre total de requêtes reçues par l’application'
)

REQUEST_LATENCY = Histogram(
    'app_request_latency_seconds',
    'Latence des requêtes en secondes'
)

# 2. Route principale de l'application
@app.route('/')
def index():
    start_time = time.time()

    # Incrémenter le compteur de requêtes
    REQUEST_COUNT.inc()

    # Simulation d'un traitement aléatoire
    time.sleep(random.uniform(0.1, 0.5))

    # Enregistrer la durée du traitement
    REQUEST_LATENCY.observe(time.time() - start_time)

    return jsonify(message="Hello DevOps!"), 200


# 3. Route d'exposition des métriques Prometheus
@app.route('/metrics')
def metrics():
    return generate_latest(), 200, {
        'Content-Type': CONTENT_TYPE_LATEST
    }


# 4. Démarrage du serveur Flask
if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000
    )
