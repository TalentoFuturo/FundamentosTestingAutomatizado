## Frontend – Notas CRUD (React)

Instrucciones para levantar el front y conectarlo al backend Flask sin problemas

---

### 1. Requisitos

| Herramienta | Versión recomendada | Comando para chequear |
|-------------|--------------------|-----------------------|
| **Node.js** | ≥18LTS (20LTS OK) | `node -v` |
| **npm**     | viene con Node     | `npm -v` |

> Si usas **nvm‑windows** o **nvm** en mac/Linux, selecciona la versión 18o20 antes de empezar.

---

### 2. Crear el proyecto (si aún no existe)

El repo ya incluye el código, pero dejo los comandos por si toca empezar desde cero:

```bash
npm create vite@latest frontend -- --template react
cd frontend
npm install
```

(En este punto tenemos la carpeta `frontend/` con React+Vite).

---

### 3. Instalar dependencias extra

```bash
cd frontend
npm install
```

No hay libs externas aparte de las que trae la plantilla (`react`, `vite`, etc.).

---

### 4. Proxy a Backend

`vite.config.ts` ya está configurado así:

```ts
import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

export default defineConfig({
  plugins: [react()],
  server: {
    proxy: {
      "/api": "http://localhost:5000", // backend Flask por defecto
    },
  },
});
```

> ⚠️ Si cambias el puerto del backend, actualiza aquí.

---

### 5. Arrancar en modo desarrollador

```bash
npm run dev
```

Abre `http://localhost:5173` (Vite avisa la URL en consola).  
Los cambios en código y CSS recargan en caliente.

---

### 6. Estructura de carpetas

```
frontend/
├─ index.html
├─ vite.config.ts
└─ src/
   ├─ main.tsx
   ├─ App.tsx
   └─ App.css
```

* `main.tsx` monta la app en el DOM.  
* `App.tsx` contiene el CRUD y llamadas fetch al backend.  
* `App.css` maneja el estilo (fuente Poppins + layout centrado).

---

¡Eso es todo! Con `npm run dev` y el backend en `python app.py` ya tenemos la app completa funcionando
