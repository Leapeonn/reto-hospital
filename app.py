from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/expediente/<nombreEmpleado>/<perfil>/<int:documentosSubidos>")
def evaluarExpediente(nombreEmpleado, perfil, documentosSubidos):
    # El checklist de documentos requeridos depende del perfil/puesto del empleado
    if perfil == "administrativo":
        documentosRequeridos = 5
    else:
        documentosRequeridos = 7

    # Evaluar el estado del expediente segun el checklist del perfil
    if documentosSubidos < documentosRequeridos:
        estado = "incompleto"
    else:
        estado = "completo"

    return jsonify({
        "empleado": nombreEmpleado,
        "perfil": perfil,
        "estado": estado
    })


if __name__ == "__main__":
    app.run(debug=True)
