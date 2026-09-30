Reto Hospital — Expedientes Digitales

Tarea 2: lógica de decisión con `if/elif/else` en una ruta Flask, aplicada al reto **Expedientes Digitales del Hospital de Diagnóstico** (RRHH).

Integrantes: Diego Díaz y María Guirola

 Levantamiento de requerimientos

1. Estados posibles. La ficha y el diagrama de flujo confirman dos estados: *incompleto* (visible para RRHH como pendiente) y *completo* (verde). Separamos *sin iniciar* (0 documentos) como un caso aparte de incompleto, porque corresponde a un empleado recién registrado que aún no tiene ningún documento subido.

2. Qué define cada estado.** El número de documentos subidos comparado con el checklist del perfil del empleado:

| Condición | Estado |
|---|---|
| 0 documentos | sin iniciar |
| Menos documentos que los requeridos por el perfil | incompleto |
| Exactamente los documentos requeridos | completo |

3. Reglas de la ficha que no estaban en el ejemplo genérico.
- El checklist no es fijo: la ficha indica que es configurable por perfil/puesto (administrativo, médico). Por eso la ruta recibe el perfil, y cada perfil tiene su propio número de documentos requeridos (administrativo: 5, médico: 7).
- Según el diagrama, cuando un documento se renueva (ej. carnet de junta de vigilancia) se guarda como nueva versión y no cuenta como documento adicional. Por eso el dato de entrada es el número de documentos distintos del checklist.

4. Caso por defecto.
- Si el perfil no existe en las plantillas de RRHH, el sistema responde `error: perfil no reconocido`.
- Si se reportan más documentos de los que pide el checklist, el sistema responde `error: documentos exceden el checklist`.

Cómo ejecutarlo

```
pip install flask
python app.py
```

Ruta: `/expediente/<nombreEmpleado>/<perfil>/<documentosSubidos>`

Pruebas

| URL | Estado obtenido |
|---|---|
| `http://127.0.0.1:5000/expediente/Ana/administrativo/0` | sin iniciar |
| `http://127.0.0.1:5000/expediente/Luis/medico/4` | incompleto (3 pendientes) |
| `http://127.0.0.1:5000/expediente/Sofia/administrativo/5` | completo |
| `http://127.0.0.1:5000/expediente/Pedro/medico/9` | error: documentos exceden el checklist |
| `http://127.0.0.1:5000/expediente/Eva/enfermero/3` | error: perfil no reconocido |

Respuestas completas:

```json
{"documentosPendientes": 5, "documentosRequeridos": 5, "documentosSubidos": 0, "empleado": "Ana", "estado": "sin iniciar", "perfil": "administrativo"}
{"documentosPendientes": 3, "documentosRequeridos": 7, "documentosSubidos": 4, "empleado": "Luis", "estado": "incompleto", "perfil": "medico"}
{"documentosPendientes": 0, "documentosRequeridos": 5, "documentosSubidos": 5, "empleado": "Sofia", "estado": "completo", "perfil": "administrativo"}
{"documentosPendientes": 0, "documentosRequeridos": 7, "documentosSubidos": 9, "empleado": "Pedro", "estado": "error: documentos exceden el checklist", "perfil": "medico"}
{"empleado": "Eva", "estado": "error: perfil no reconocido", "perfil": "enfermero", "perfilesValidos": "administrativo, medico"}
```

Las capturas de pantalla de cada prueba están en la entrega.
