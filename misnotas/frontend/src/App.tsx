import { useEffect, useState } from "react";
import "./App.css";

export default function App() {
  const empty = { id: null, title: "", body: "", priority: "medium" };
  const [notes, setNotes] = useState([]);
  const [form, setForm]   = useState(empty);

  // Cargar notas
  useEffect(() => {
    fetch("/api/notes").then(r => r.json()).then(setNotes);
  }, []);

  const save = e => {
    e.preventDefault();
    const method = form.id ? "PUT" : "POST";
    const url    = form.id ? `/api/notes/${form.id}` : "/api/notes";

    fetch(url, {
      method,
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(form),
    })
      .then(r => (method === "POST" ? r.json() : r.json()))
      .then(nota => {
        setNotes(form.id
          ? notes.map(n => (n.id === nota.id ? nota : n))
          : [...notes, nota]);
        setForm(empty);
      });
  };

  const edit   = nota => setForm(nota);
  const remove = id =>
    fetch(`/api/notes/${id}`, { method: "DELETE" }).then(() =>
      setNotes(notes.filter(n => n.id !== id))
    );

  return (
    <div className="container">
      <h1>Mis Notas</h1>

      <form onSubmit={save} className="form">
        <input
          placeholder="Título"
          value={form.title}
          onChange={e => setForm({ ...form, title: e.target.value })}
          required
        />
        <textarea
          placeholder="Cuerpo"
          value={form.body}
          onChange={e => setForm({ ...form, body: e.target.value })}
          required
        />
        <select
          value={form.priority}
          onChange={e => setForm({ ...form, priority: e.target.value })}
        >
          <option value="...">...</option>
		  <option value="Alta">Alta</option>
          <option value="Media">Media</option>
          <option value="Baja">Baja</option>
        </select>
        <button type="submit">{form.id ? "Actualizar" : "Crear"}</button>
        {form.id && (
          <button type="button" onClick={() => setForm(empty)}>
            Cancelar
          </button>
        )}
      </form>

      <table>
        <thead>
          <tr>
            <th>ID</th><th>Título</th><th>body</th><th>Prioridad</th><th>Acciones</th>
          </tr>
        </thead>
        <tbody>
          {notes.map(n => (
            <tr key={n.id}>
              <td>{n.id}</td>
              <td>{n.title}</td>
			  <td>{n.body}</td>
              <td>{n.priority}</td>
              <td  data-label="Acciones" className="actions">
                <button onClick={() => edit(n)}>Editar</button>
                <button onClick={() => remove(n.id)}>Eliminar</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
