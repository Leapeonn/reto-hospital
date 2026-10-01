from flask import Flask, jsonify

app = Flask(__name__)

# Numero de documentos del checklist por perfil (segun plantillas de RRHH)
REQUERIDOS_ADMINISTRATIVO = 5
REQUERIDOS_MEDICO = 7


@app.route("/expediente/<nombreEmpleado>/<perfil>/<int:documentosSubidos>")
def evaluarExpediente(nombreEmpleado, perfil, documentosSubidos):
    perfil = perfil.lower()

    # 1. El checklist de documentos requeridos depende del perfil/puesto
    if perfil == "administrativo":
        documentosRequeridos = REQUERIDOS_ADMINISTRATIVO
    elif perfil == "medico":
        documentosRequeridos = REQUERIDOS_MEDICO
    else:
        # Caso por defecto: el perfil no existe en las plantillas de RRHH
        return jsonify({
            "empleado": nombreEmpleado,
            "perfil": perfil,
            "estado": "error: perfil no reconocido",
            "perfilesValidos": "administrativo, medico"
        }), 400

    # 2. Evaluar el estado del expediente segun el checklist del perfil
    if documentosSubidos == 0:
        estado = "sin iniciar"
    elif documentosSubidos < documentosRequeridos:
        estado = "incompleto"
    elif documentosSubidos == documentosRequeridos:
        estado = "completo"
    else:
        # Caso por defecto: mas documentos de los que pide el checklist
        estado = "error: documentos exceden el checklist"

    pendientes = max(documentosRequeridos - documentosSubidos, 0)

    return jsonify({
        "empleado": nombreEmpleado,
        "perfil": perfil,
        "documentosRequeridos": documentosRequeridos,
        "documentosSubidos": documentosSubidos,
        "documentosPendientes": pendientes,
        "estado": estado
    })


if __name__ == "__main__":
    app.run(debug=True)
