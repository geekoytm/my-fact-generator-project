from flask import Flask, jsonify, render_template

app = Flask(__name__)

# Define some personal fun facts
fun_facts = [
    "I love playing sports and going to the gym.",
    "Traveling is one of my passions.",
    "I enjoy both team activities and working independently."
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/facts')
def get_facts():
    return jsonify(fun_facts)

if __name__ == '__main__':
    app.run(debug=True)
