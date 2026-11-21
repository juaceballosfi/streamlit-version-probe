# Prueba de compatibilidad de Streamlit en Fi Apps

Aplicación mínima con Streamlit **1.66.1** y datos sintéticos. Comprueba el menú superior nativo, una página de detalle oculta del menú y la conexión del navegador tras el inicio de sesión OIDC. La pantalla muestra la versión efectiva de Streamlit y Python y si existe la cabecera `X-User-Id`. Solo indica su presencia.

## Ejecutar en local

Desde esta carpeta, usa Python 3.13 en un entorno virtual propio.

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m streamlit run app.py --server.address 127.0.0.1 --server.port 8521
```

Abre [la prueba local](http://127.0.0.1:8521). Fuera del gateway de Fi Apps, `X-User-Id: absent` es el resultado esperado.

## Probar en Fi Apps

1. Publica esta carpeta en un repositorio Git de prueba accesible para Fi Apps. Configura **una aplicación nueva** con la plantilla **Streamlit app**, el repositorio de prueba y `app.py` como entrada. La plantilla instala `requirements.txt` desde la raíz. Deja **Environment** vacío, como indica [`.env.example`](.env.example).
2. Configura el puerto compartido como **Collaborators only + OIDC**. Ejecuta **Deploy** y abre la URL compartida desde una ventana privada autenticándote con una cuenta colaboradora.
3. Comprueba que el login vuelve a la URL compartida y que la app muestra `Streamlit 1.66.1` y `X-User-Id: present`. Si hay un fallo, registra la etapa, el estado HTTP y si el destino era el host público o el interno. Evita copiar la URL completa de la autenticación, cabeceras o cookies.
4. En el menú deben aparecer **Documents** y **Export**. Abre **Warnings (1)** en Documents. Pulsa **Sample contract**, marca **Reviewed** y vuelve con **Back to Documents**. En una sesión nueva, añadir `/review` a la URL base de la app debe hacer que muestre Documents al faltar una selección.

En Fi Apps, el responsable confirmó que OIDC funciona con **1.55.0** y que el fallo persiste con **1.67.0**. La siguiente prueba usa **1.66.1**, la versión publicada inmediatamente anterior a 1.67.0. Si completa el inicio de sesión y la navegación, el siguiente paso es validar ContractFlow completo con 1.66.1 en un entorno de prueba. [Historial de versiones en PyPI](https://pypi.org/project/streamlit/#history)
