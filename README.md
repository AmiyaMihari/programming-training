# Preparación de entrevistas: Python backend

Inicio: 21 de octubre de 2026.

## Objetivo

Resolver y explicar problemas de programación sin asistencia de IA durante una entrevista, y defender decisiones de desarrollo backend en Python. Fullstack será una ampliación posterior.

Disponibilidad base: cuatro sesiones de 25–30 minutos por semana. El tiempo extra de fin de semana es opcional y se dedica a repasar, terminar un ejercicio o practicar un simulacro. No genera tareas pendientes adicionales.

Este documento es una ruta adaptable, no una fecha prometida de preparación. Con dos horas semanales, avanzar puede tomar varios meses. Las vacantes y el diagnóstico determinan la profundidad necesaria.

## Reglas de tutoría

- El tutor no entrega respuestas, código resuelto ni pseudocódigo que revele la solución de los ejercicios.
- Primero se pide un intento o una explicación de lo que impide empezar. No es obligatorio tener código para recibir ayuda.
- La ayuda consiste en preguntas y pistas pequeñas, progresivas y solicitadas. No se revela automáticamente un algoritmo por agotar el tiempo.
- Si falta un concepto, se explica con un ejemplo distinto y se vuelve al ejercicio original.
- Durante la práctica independiente se desactiva el autocompletado generativo y no se consultan soluciones, editoriales ni respuestas de otras personas.
- Fuera de los simulacros se permite consultar documentación de sintaxis. Se registra esa consulta para distinguir problemas de memoria y de razonamiento.
- Durante un simulacro se acuerdan antes las herramientas permitidas.
- El tutor revisa comprensión, razonamiento, código, pruebas y explicación. Un resultado aceptado por la plataforma no basta por sí solo.
- Se trabaja con datos ficticios y ejemplos públicos. No se publica código, información ni ejercicios confidenciales de empresas.

## Organización semanal

| Sesión | Trabajo principal |
| --- | --- |
| A | Recuperar lo anterior de memoria y abordar un problema nuevo |
| B | Continuar el problema, depurarlo y probar casos límite |
| C | Resolver una variante o practicar SQL/backend según la etapa |
| D | Repetición sin ayuda, explicación oral y registro de dificultades |

Distribución orientativa de una sesión: 3 minutos para recuperar lo aprendido, 20 para trabajar y 5 para explicar y registrar. Un problema puede ocupar varias sesiones. Al principio no se exige velocidad.

Si solo hay 10 minutos: recuperar la idea de un ejercicio previo, proponer casos de prueba o rastrear manualmente una ejecución. No abrir un tema nuevo por obligación.

## Etapa 0. Diagnóstico y preparación

Duración inicial orientativa: una semana. Sin cronómetro de entrevista.

- [ ] Resolver un ejercicio corto de condiciones y ciclos.
- [ ] Abordar un ejercicio de listas o cadenas.
- [ ] Explicar en lenguaje cotidiano qué pide cada problema antes de programar.
- [ ] Registrar si la dificultad fue entender, plantear, escribir, depurar o explicar.
- [ ] Preparar Python, un editor sencillo y una forma de ejecutar archivos.
- [ ] Crear el repositorio cuando se decida dónde alojarlo.

La referencia recordada como “buzz” podría ser FizzBuzz, pero no se conoce el enunciado de aquella prueba. No se considera evidencia del nivel actual ni se intenta reconstruir una evaluación confidencial.

Criterio de salida: contar con intentos que permitan elegir el nivel de práctica. No hay calificación de aprobado o reprobado.

## Etapa 1. Recuperar soltura en Python

Ventana inicial orientativa: semanas 2–4; ampliar o acortar según el diagnóstico.

Temas, en este orden aproximado:

1. Variables, tipos, operadores, condiciones y ciclos.
2. Funciones, parámetros, retorno y alcance básico.
3. Listas y cadenas: recorrer, acceder y modificar cuando corresponda.
4. Diccionarios y conjuntos: representar asociaciones y elementos únicos.
5. Mutabilidad, referencias, valores ausentes y excepciones básicas.

Práctica: ejercicios pequeños de transformación, validación y procesamiento de colecciones. El tutor selecciona uno por vez, sin anunciar la técnica que lo resuelve.

- [ ] Escribir funciones pequeñas sin código generado.
- [ ] Rastrear a mano lo que hace un ciclo.
- [ ] Diferenciar imprimir un valor y devolverlo.
- [ ] Construir pruebas normales y casos límite.
- [ ] Corregir un error explicando su causa.

Criterio de salida: resolver dos ejercicios nuevos del nivel trabajado en sesiones distintas sin pistas sobre la estrategia. Una consulta puntual de sintaxis se registra y se repasa después.

## Etapa 2. Resolver problemas de entrevista

Ventana inicial orientativa: semanas 5–9. No exige completar todos los temas en ese plazo.

Orden propuesto:

1. Recorridos de listas y cadenas, conteos y búsquedas.
2. Diccionarios y conjuntos aplicados a problemas.
3. Complejidad temporal y espacial: O(1), O(n), O(n log n) y O(n²).
4. Ordenamiento, dos punteros y ventana deslizante.
5. Pilas, colas y búsqueda binaria.

Se introduce una técnica después de observar la necesidad que resuelve. No se convierte cada ejercicio en una prueba de adivinar un patrón.

Para cada problema:

- [ ] Reformular el enunciado y aclarar entradas, salidas y restricciones.
- [ ] Proponer ejemplos propios.
- [ ] Explicar una primera estrategia antes de codificar.
- [ ] Implementar y probar.
- [ ] Estimar tiempo y memoria, con una justificación sencilla.
- [ ] Volver a intentarlo entre 3 y 7 días después.
- [ ] Resolver posteriormente una variante que no se haya visto.

Criterio de salida: resolver y explicar problemas nuevos de los temas practicados con autonomía. La dificultad que asigna una plataforma es una referencia, no una medida exacta de capacidad.

Árboles, recorridos de grafos, heaps, recursión y programación dinámica quedan para una ampliación según las vacantes. Si se priorizan procesos de algoritmos exigentes, como determinadas posiciones de Amazon, habrá que ampliar esta parte. No se presupone que una ruta básica cubra todo su proceso.

## Etapa 3. SQL y backend para entrevistas

Ventana inicial orientativa: semanas 10–14. Se puede intercalar una sesión semanal antes si las vacantes lo requieren.

### SQL

- [ ] SELECT, WHERE, ORDER BY y manejo de NULL.
- [ ] Agregaciones, GROUP BY y HAVING.
- [ ] INNER JOIN y LEFT JOIN; detectar duplicación de filas.
- [ ] Subconsultas y expresiones de tabla comunes (CTE).
- [ ] Funciones de ventana cuando las consultas anteriores sean sólidas.
- [ ] Claves, restricciones, índices y transacciones mediante casos concretos.

Practicar con un esquema pequeño y datos ficticios. Antes de ejecutar, predecir las filas esperadas. Usar PostgreSQL como motor de referencia y registrar las diferencias de dialecto al practicar en plataformas.

### Python y backend

- [ ] Explicar mutabilidad, excepciones, generadores y organización de módulos con ejemplos propios.
- [ ] Entender peticiones HTTP, métodos, códigos de estado y JSON.
- [ ] Diseñar endpoints, validar entradas y manejar errores.
- [ ] Diferenciar autenticación y autorización.
- [ ] Explicar consultas parametrizadas y manejo de secretos.
- [ ] Diferenciar trabajo de entrada/salida y trabajo de CPU antes de usar async/await.
- [ ] Escribir pruebas útiles de reglas de negocio y endpoints.
- [ ] Leer y depurar código ajeno pequeño.

Práctica integradora: una API pequeña de tareas o solicitudes con FastAPI y persistencia. Construir un comportamiento por sesión y poder explicar cada parte. No se requiere un proyecto grande ni incorporar IA.

Criterio de salida: implementar y probar una funcionalidad pequeña sin generación de código, y explicar sus decisiones y limitaciones.

## Etapa 4. Simulacros y defensa de proyectos

Introducir simulacros breves cuando haya soltura básica. Reservar sesiones de 45–60 minutos para fines de semana solo cuando haya tiempo disponible.

- [ ] Practicar problemas nuevos con tiempo acordado.
- [ ] Hablar mientras se razona, sin narrar cada tecla.
- [ ] Pedir aclaraciones cuando el enunciado sea ambiguo.
- [ ] Practicar cómo retomar el trabajo después de quedarse en blanco.
- [ ] Explicar dos proyectos del CV, decisiones propias, errores y mejoras.
- [ ] Distinguir qué se implementó personalmente y cómo se verificó el trabajo asistido por IA.
- [ ] Hacer alguna práctica oral en inglés cuando la resolución ya sea manejable.

Protocolo ante un bloqueo: pausar, reformular el objetivo, construir un ejemplo pequeño, identificar qué se conoce y proponer un primer paso verificable. Si no alcanza, comunicar exactamente dónde está la duda.

Rúbrica de revisión, de 0 a 2 por dimensión:

| Dimensión | 0 | 1 | 2 |
| --- | --- | --- | --- |
| Comprensión | No logra precisar la tarea | Necesita aclaraciones guiadas | Define tarea y restricciones |
| Estrategia | No plantea un camino | Avanza con pistas | Propone y justifica un camino |
| Implementación | No traduce la idea | Código parcial o ayuda frecuente | Implementa de forma autónoma |
| Pruebas | No verifica | Prueba ejemplos normales | Incluye casos límite y corrige |
| Explicación | No puede explicar | Explicación incompleta | Explica decisiones y costo |

La rúbrica muestra qué entrenar. No predice una contratación. Antes de aumentar dificultad, revisar el desempeño en al menos dos sesiones distintas.

## Etapa 5. Ampliación a fullstack

Comenzar cuando el trabajo de Python backend sea estable, salvo que una vacante concreta cambie la prioridad.

1. JavaScript: funciones, arrays, objetos, alcance y asincronía.
2. HTML semántico, formularios y CSS práctico.
3. Consumo de APIs, estados de carga y errores.
4. React: componentes, props, estado, efectos y formularios.
5. Integrar una interfaz pequeña con la API anterior.
6. Practicar depuración entre navegador, API y base de datos.

No estudiar simultáneamente varios frameworks. Preparar entrevistas fullstack también exige práctica específica de JavaScript y navegador.

## Recursos y regla de selección

- [HackerRank: Python](https://www.hackerrank.com/domains/python): apoyo inicial si falta soltura de lenguaje.
- [HackerRank: preparación de entrevistas](https://www.hackerrank.com/interview/interview-preparation-kit): banco complementario de ejercicios.
- [LeetCode: Top Interview 150](https://leetcode.com/studyplan/top-interview-150/): banco para seleccionar problemas por tema cuando exista base suficiente.
- [LeetCode: SQL 50](https://leetcode.com/studyplan/top-sql-50/): práctica de consultas según el nivel.
- [Documentación de Python](https://docs.python.org/es/3/): consultas puntuales de lenguaje.
- [Documentación de PostgreSQL](https://www.postgresql.org/docs/current/): consultas puntuales de SQL.
- [Documentación de FastAPI](https://fastapi.tiangolo.com/): referencia durante la práctica backend.

Usar un banco principal a la vez. No es necesario completar listas enteras ni comprar una suscripción para comenzar. El tutor asigna el siguiente problema según las dificultades observadas.

## Estructura sugerida del repositorio

| Ruta | Contenido |
| --- | --- |
| README.md | Objetivo, reglas y enlace a este roadmap |
| ROADMAP.md | Ruta y avances por etapa |
| python/ | Intentos y soluciones propias de Python |
| sql/ | Consultas propias y datos de práctica |
| backend/ | Ejercicios de API y pruebas |
| fullstack/ | Ampliación posterior |
| notas/ | Conceptos breves y errores recurrentes |
| sesiones/ | Una bitácora por fecha |
| simulacros/ | Evaluaciones y puntos por reforzar |

Convención opcional: nombres como `001_nombre_del_ejercicio.py`. Guardar el primer intento y su evolución mediante commits. Publicar una solución propia después de resolverla no contradice la regla de que el tutor no entregue respuestas. Si el repositorio es público, respetar las condiciones de cada plataforma y preferir enlaces a los enunciados.

## Plantilla de bitácora

```markdown
# Sesión AAAA-MM-DD

- Ejercicio o enlace:
- Tema:
- Tiempo dedicado:
- Qué entendí del problema:
- Estrategia que intenté:
- Dónde me atoré:
- Ayuda recibida: ninguna / sintaxis / pregunta / pista conceptual
- Casos que probé:
- Error encontrado y su causa:
- Qué puedo explicar ahora:
- Próxima repetición:
- Estado: pendiente / en progreso / resuelto con ayuda / resuelto sin ayuda / consolidado
```

“Consolidado” significa haberlo vuelto a resolver en otra sesión y haber aplicado la idea en una variante. No significa recordar una solución escrita.

## Primera semana

- [ ] Sesión A: primer ejercicio diagnóstico de Python.
- [ ] Sesión B: revisar el intento y trabajar una variante o un segundo diagnóstico.
- [ ] Sesión C: ejercicio de listas o cadenas al nivel observado.
- [ ] Sesión D: repetir uno sin ayuda, explicar el razonamiento y ajustar la siguiente semana.

No preparar los diagnósticos mirando soluciones. Su función es elegir desde dónde empezar.

## Revisión cada cuatro semanas

- ¿Qué tareas puedo hacer ahora sin ayuda?
- ¿Qué errores siguen apareciendo?
- ¿Falta sintaxis, razonamiento, depuración o comunicación?
- ¿La carga cabe en el tiempo disponible?
- ¿Las vacantes que busco siguen siendo Python backend?
- ¿Conviene repetir, avanzar o cambiar la distribución de sesiones?

El avance se mide por autonomía y transferencia a problemas nuevos. No por rachas, horas acumuladas ni cantidad de ejercicios aceptados.
