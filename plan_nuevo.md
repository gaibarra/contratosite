## Plan: Prompt maestro de modernización contractual

Crear una aplicación nueva, desplegable en paralelo con el sistema legado, sobre la misma base PostgreSQL. El enfoque recomendado usa Django 5.2 LTS y Django REST Framework para una API versionada, React con Next.js estable para la interfaz, migraciones exclusivamente aditivas y snapshots/versiones inmutables para que editar una cláusula nunca altere contratos históricos.

**Objetivo del prompt**
Solicitar a un agente de desarrollo que primero audite el repositorio y el esquema real, luego proponga y ejecute una modernización incremental. La prioridad funcional es que una persona pueda crear, encontrar, comparar, versionar, ordenar y ubicar cláusulas dentro de plantillas y contratos, conocer dónde se usa cada versión y generar documentos reproducibles.

**Pasos**

### Fase 1: Descubrimiento y salvaguardas
1. Levantar inventario verificable del esquema PostgreSQL, datos, constraints, volúmenes, codificación, archivos multimedia e integraciones. Tomar como referencias principales `cto.models.Contratos`, `Tipocontrato`, `Secuencia`, `Requisitos`, `Doctos`, `Valida`, `Partes`, `Departamento`, `cto.views.contratos2`, `coverletter_export`, `contratosAvanza` y `contratosDevuelve`.
2. Crear respaldo probado y ensayar restauración antes de cualquier migración. Prohibir operaciones destructivas o renombres de tablas/campos legados en la primera etapa.
3. Documentar el mapeo entre los campos actuales y el nuevo dominio. En particular, resolver la doble fuente `Contratos.clausula`/`Secuencia.textoSecuencia`, los niveles `nivel1` a `nivel4`, los rangos hardcodeados de generación, los responsables enteros `rstep1` a `rstep6` y las secuencias administrativas `Departamento.f001` a `f050`.
4. Definir una línea base de pruebas de caracterización para generación DOCX, permisos, estados y consultas principales. Esta fase bloquea las migraciones y puede avanzar en paralelo con el prototipo UX de la fase 3.

### Fase 2: Arquitectura y modelo aditivo
5. Crear un backend separado con Python compatible, Django 5.2 LTS, DRF, OpenAPI, PostgreSQL y tareas asíncronas solo donde aporten valor. Mantener una API `/api/v2`; no modificar el contrato de `/api/v1`.
6. Mapear tablas legadas conservando exactamente nombres, tipos y claves. Toda evolución inicial debe agregar tablas, columnas, índices o vistas compatibles; nunca hacer que la aplicación actual deje de funcionar.
7. Diseñar `Clause` como identidad estable y `ClauseVersion` como contenido inmutable, con título, categoría, etiquetas, jurisdicción, idioma, propietario, nivel de riesgo, estado editorial, vigencia, motivo de cambio, autoría, hash y relación con la versión anterior.
8. Diseñar `ContractTemplate` y `TemplateVersion`, más una estructura ordenada `TemplateNode` que admita secciones y cláusulas mediante `parent`, `position`, identificador visible, obligatoriedad, condiciones y metadatos de ubicación. Aplicar constraints para impedir posiciones duplicadas y ciclos.
9. Diseñar `Contract`/adaptador del contrato legado y `ContractClauseSnapshot`: cada contrato debe guardar la versión exacta, contenido renderizado, variables y ubicación usadas al generarlo. Los cambios futuros en catálogo no pueden reescribir contratos históricos.
10. Añadir tablas de uso e impacto que respondan eficientemente qué contratos y plantillas usan una cláusula o versión, en qué sección y posición, y qué elementos quedarían afectados por una nueva versión.
11. Modelar workflows configurables con definiciones, pasos, asignaciones por rol/usuario, transiciones validadas, devoluciones, comentarios, plazos y eventos. Mantener un adaptador de lectura/escritura para los seis pasos legados durante la convivencia.
12. Modelar requisitos y documentos por contrato, estado de cumplimiento, vigencia, archivos, revisiones y alertas. Preservar y migrar referencias de `Requisitos` y `Doctos`.
13. Incorporar RBAC con mínimo privilegio para administrador, responsable jurídico, editor, revisor, aprobador, capturista y consulta. Registrar auditoría append-only de cambios, accesos sensibles, publicaciones, generación y descargas.

### Fase 3: Experiencia de usuario
14. Construir una interfaz de trabajo en español, accesible WCAG 2.2 AA, responsive y orientada a productividad: navegación estable, tablas densas, filtros persistentes, paginación servidor y estados de carga/error/vacío.
15. Crear biblioteca de cláusulas con búsqueda PostgreSQL de texto completo, filtros por metadatos/estado/vigencia, comparación entre versiones, historial, borradores, revisión y publicación. Resaltar coincidencias y mostrar usos e impacto.
16. Crear editor visual de plantillas con árbol/esquema, arrastrar y soltar con teclado accesible, numeración automática, inserción desde catálogo, secciones, condiciones, variables validadas, autoguardado, control de concurrencia y vista previa paginada.
17. En el contrato, mostrar índice navegable y permitir localizar una cláusula en un clic, ver su ruta, versión, origen y estado. Permitir excepciones contractuales como snapshots explícitos sujetos a permiso y auditoría.
18. Implementar constructor asistido por pasos: tipo y partes, datos variables, selección de cláusulas, requisitos, validación, vista previa, aprobación y generación. Evitar un formulario único masivo.
19. Generar DOCX y PDF deterministas mediante un servicio de plantillas probado. Mantener compatibilidad visual con documentos actuales, sanitizar rich text, validar variables faltantes y conservar hash/archivo/fecha/usuario de cada versión generada.
20. Añadir bandejas de trabajo, búsquedas avanzadas, alertas de vigencia/SLA, historial cronológico y notificaciones configurables sin bloquear el flujo principal.

### Fase 4: Asistencia con IA controlada
21. Implementar IA como capacidad opcional y desacoplada. Casos permitidos: búsqueda semántica sobre cláusulas aprobadas, sugerencia de cláusulas similares, resumen de diferencias, detección de variables ausentes, duplicados e inconsistencias.
22. Exigir confirmación humana para toda inserción o cambio; mostrar fuente, versión y explicación. La IA no publica cláusulas, no aprueba contratos y no sustituye revisión jurídica.
23. Proteger datos personales y contractuales: no enviarlos a proveedores externos por defecto, aplicar redacción/minimización, autorización explícita, registros de uso, retención configurable y proveedor intercambiable. Usar full-text search como base; `pgvector` solo si infraestructura y política lo permiten.

### Fase 5: Migración y convivencia
24. Crear importadores idempotentes y reanudables con dry-run para convertir `Tipocontrato`/`Secuencia` en plantillas versionadas y asociar `Contratos.clausula` como contenido legado claramente marcado. Conservar IDs de origen y tablas de correspondencia.
25. Emitir reportes de registros ambiguos, duplicados, niveles inválidos, referencias huérfanas y diferencias de conteo/hash. Nunca inventar orden cuando no pueda inferirse; enviarlo a una cola de resolución manual.
26. Desplegar en modo lectura, luego piloto de escritura controlada, después convivencia con feature flags. Definir rollback, métricas de paridad y criterio formal para retirar cada flujo legado.
27. Mantener Nginx/PostgreSQL y archivos existentes durante la transición; externalizar secretos, actualizar TLS/cabeceras, añadir health checks, logs estructurados, trazas, métricas, backups y monitoreo.

### Fase 6: Calidad y entrega
28. Añadir pruebas unitarias, de API, permisos, migración, concurrencia, auditoría, generación documental y end-to-end. Incluir casos de regresión con contratos históricos anonimizados y comparación de DOCX/PDF.
29. Configurar CI para formato, lint, tipos, análisis de seguridad, dependencias, migraciones, tests y build frontend. Bloquear cambios con migraciones destructivas o pérdida de cobertura crítica.
30. Entregar ADRs, diccionario de datos, OpenAPI, runbooks de respaldo/rollback, guía de despliegue, manual por rol y registro de decisiones. Cada fase debe terminar con demo y criterios de aceptación medibles antes de iniciar la siguiente.

**Relevant files**
- `/home/gaibarra/contrato/cto/models.py` — esquema legado y entidades `Contratos`, `Tipocontrato`, `Secuencia`, `Requisitos`, `Doctos` y `Valida`.
- `/home/gaibarra/contrato/cto/views.py` — creación, workflow y generación DOCX que deben caracterizarse antes de reemplazarse.
- `/home/gaibarra/contrato/cto/forms.py` — validaciones y campos actuales del contrato.
- `/home/gaibarra/contrato/cto/migrations/` — historia y constraints que la convivencia debe respetar.
- `/home/gaibarra/contrato/api/viewsets.py` y `/home/gaibarra/contrato/api/serializer.py` — API v1 que debe aislarse; incluye el queryset incorrecto de `TipocontratoViewSet`.
- `/home/gaibarra/contrato/contrato/settings/` y `/home/gaibarra/contrato/deploy/` — PostgreSQL, seguridad y despliegue actuales.
- `/home/gaibarra/contrato/requirements.txt` — baseline obsoleto Django 3.2.9 y dependencias a sustituir o aislar.

**Verification**
1. Restaurar un backup anonimizado y ejecutar migraciones aditivas sin cambios destructivos; comprobar que la aplicación antigua continúa sus flujos principales.
2. Comparar conteos, IDs, relaciones y hashes antes/después de cada importación; repetir dry-run y ejecución para demostrar idempotencia.
3. Verificar que editar/publicar una cláusula crea versión y no cambia ningún contrato o documento ya generado.
4. Probar búsqueda, localización, reordenamiento, navegación por teclado, control de concurrencia e impacto de versiones en desktop y móvil.
5. Probar matriz de permisos y transiciones, incluidos accesos negativos, devoluciones, comentarios y auditoría.
6. Generar DOCX/PDF con muestras representativas y comparar contenido, orden, variables, firmas y metadatos con salidas legadas aprobadas.
7. Probar que las funciones de IA funcionan desactivadas, no modifican datos sin confirmación y no exfiltran información sensible.
8. Ejecutar suite completa, análisis de seguridad, build reproducible, smoke test de despliegue, restauración y rollback ensayado.

**Decisions**
- Se reutiliza la misma instancia PostgreSQL y se permite ampliar el esquema con cambios compatibles.
- Backend objetivo: Django 5.2 LTS y API v2; frontend: React con la versión estable compatible de Next.js, sin fijar una versión futura no verificada.
- La primera versión incluye catálogo/editor, constructor, workflow/auditoría, documentos/requisitos, migración/convivencia e IA opcional.
- PostgreSQL full-text es obligatorio; búsqueda vectorial es opcional y condicionada a infraestructura y privacidad.
- Quedan fuera de la primera transición los renombres/eliminaciones del esquema legado y la aprobación jurídica autónoma por IA.