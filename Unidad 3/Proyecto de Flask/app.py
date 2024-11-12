from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        numbers = [float(request.form[f'number{i}']) for i in range(1, 6)]
        mayor = max(numbers)
        menor = min(numbers)
        promedio = sum(numbers) / len(numbers)
        return jsonify({
            'mayor': mayor,
            'menor': menor,
            'promedio': promedio
        })
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)