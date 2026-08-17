# Laboratorio 02 — Configuración del entorno de trabajo

1. Se creó el entorno virtual con:
```bash
 python -m venv venv
```
2. En Windows con Git Bash se activó usando:
```bash
 source venv/Scripts/activate
```
3. Se instaló `matplotlib` dentro del entorno virtual.
4. Las dependencias se registraron con:
```bash
 pip freeze > requirements.txt
```
5. Para reproducir el entorno se crea nuevamente el venv y se activa.
6. Luego se deben instalar las dependencias con:
```bash
 pip install -r requirements.txt
```
7. El entorno se verifica con `pip list`.
8. La carpeta `venv/` está incluida en `.gitignore` y no se versiona.
