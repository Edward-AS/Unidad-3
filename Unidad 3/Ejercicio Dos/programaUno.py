from flask import Flask, render_template, request, jsonify

programaUno = Flask(__name__)

@programaUno.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nombre = request.form['nombre']
        calificaciones = [float(request.form[f'c{i}']) for i in range(1, 4)]
        promedio = round(sum(calificaciones) / len(calificaciones), 2)
        estado = "APROBADO" if promedio >= 70 and all(c >= 70 for c in calificaciones) else "REPROBADO"
        return jsonify({
            'nombre': nombre,
            'calificaciones': calificaciones,
            'promedio': promedio,
            'estado': estado
        })
    return render_template('indexUno.html')

if __name__ == '__main__':
    programaUno.run(debug=True)