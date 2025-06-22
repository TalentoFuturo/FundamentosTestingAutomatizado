# Instrucciones de instalación y ejecución aplicativo Mis Notas

Mis Notas en una aplicación demostrativa si persistencia de datos en BD para mostrar el uso de Test.

- **[Frontend](https://github.com/TalentoFuturo/FundamentosTestingAutomatizado/blob/main/misnotas/frontend/vite-project/README.md)**
- **[Backend](https://github.com/TalentoFuturo/FundamentosTestingAutomatizado/blob/main/misnotas/backend/readme.md)**

## Mini guía – Selenium IDE con nuestro CRUD de Notas

Este tutorial cubre **solo la parte de pruebas** una vez que ya tienes:

* Backend Flask corriendo → `http://localhost:5000`
* Frontend React corriendo → `http://localhost:5173`

La idea es grabar un flujo *Crear / Verificar / Editar / Eliminar* y comprobarlo automáticamente.

---

### 1 . Instalar Selenium IDE

| Navegador | Pasos |
|-----------|-------|
| **Chrome / Edge** | 1. Abre la [Chrome Web Store](https://chrome.google.com/webstore/detail/selenium-ide/mooikfkahbdckldjjndioackbalphokd).<br>2. Haz clic en **Añadir a Chrome** → **Añadir extensión**. |
| **Firefox** | 1. Abre [addons.mozilla.org](https://addons.mozilla.org/firefox/addon/selenium-ide/).<br>2. Pulsa **Añadir a Firefox** → **Agregar** → **Aceptar**. |

Tras instalar verás un icono rojo **Se** junto a la barra de direcciones. ¡Listo para grabar!

1. Abre Chrome o Firefox.  
2. Busca **“Selenium IDE”** en la tienda de extensiones y agrégala.  
3. Verás un icono rojo con “Se” en la barra.

---

### 2 . Iniciar un nuevo proyecto

1. Haz clic en el icono **Se** → **Create a new project**.  
2. Nómbralo por ejemplo `Notas CRUD`.

---

### 3 . Grabar la creación de una nota

1. **URL de inicio:** `http://localhost:5173`  
2. Selenium abre la página y empieza a grabar.  
3. Completa el formulario:

   * Título → “Nota Selenium”  
   * Cuerpo  → “Ejemplo desde Selenium IDE”  
   * Prioridad → “Alta”  
   * Pulsa **Crear**

4. Detén la grabación.

Ya tienes los comandos `type`, `select` y `click` grabados.

### Ejercicios
- Prueba: Crear una nota, elimina y editar.
- Ahora lo mismo e incorpora Assets

---
