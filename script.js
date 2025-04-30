function getStudents() {
  return JSON.parse(localStorage.getItem("students") || "[]");
}

function saveStudent(student) {
  const students = getStudents();
  students.push(student);
  localStorage.setItem("students", JSON.stringify(students));
}

function showStudents() {
  const students = getStudents();
  const list = document.getElementById("student-list");
  if (!list) return;
  if (students.length === 0) {
    list.innerHTML = "<li>Nessuno studente registrato.</li>";
    return;
  }
  list.innerHTML = students.map(s =>
    `<li><strong>${s.nome} ${s.cognome}</strong> – ${s.email} (${s.corso})</li>`
  ).join("");
}

function showError(inputId, message) {
  const input = document.getElementById(inputId);
  const errorEl = document.getElementById(`err-${inputId}`);
  input.classList.add("error-border");
  errorEl.textContent = message;
  errorEl.classList.add("active");
}

function clearError(inputId) {
  const input = document.getElementById(inputId);
  const errorEl = document.getElementById(`err-${inputId}`);
  input.classList.remove("error-border");
  errorEl.textContent = "";
  errorEl.classList.remove("active");
}

document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("registration-form");
  if (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();

      const nome = document.getElementById("nome").value.trim();
      const cognome = document.getElementById("cognome").value.trim();
      const dataNascita = document.getElementById("dataNascita").value;
      const email = document.getElementById("email").value.trim();
      const corso = document.getElementById("corso").value;

      let valid = true;

      if (!nome) {
        showError("nome", "Inserisci il nome.");
        valid = false;
      } else {
        clearError("nome");
      }

      if (!cognome) {
        showError("cognome", "Inserisci il cognome.");
        valid = false;
      } else {
        clearError("cognome");
      }

      if (!dataNascita) {
        showError("dataNascita", "Inserisci la data di nascita.");
        valid = false;
      } else {
        clearError("dataNascita");
      }

      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      if (!email || !emailRegex.test(email)) {
        showError("email", "Email non valida.");
        valid = false;
      } else {
        clearError("email");
      }

      if (!corso) {
        showError("corso", "Seleziona un corso.");
        valid = false;
      } else {
        clearError("corso");
      }

      if (valid) {
        saveStudent({ nome, cognome, dataNascita, email, corso });
        window.location.href = "index.html";
      }
    });
  } else {
    showStudents();
  }
});

function deleteStudent(index) {
  const students = getStudents();
  students.splice(index, 1);  // Rimuove lo studente dalla lista
  localStorage.setItem("students", JSON.stringify(students));
  showStudents();  // Ricarica la lista aggiornata
}

function showStudents() {
  const students = getStudents();
  const list = document.getElementById("student-list");
  if (!list) return;
  if (students.length === 0) {
    list.innerHTML = "<li>Nessuno studente registrato.</li>";
    return;
  }
  list.innerHTML = students.map((s, index) =>
    `<li><strong>${s.nome} ${s.cognome}</strong> – ${s.email} (${s.corso}) 
      <button class="delete-btn" onclick="handleDelete(${index})">❌ Elimina</button></li>`
  ).join("");
}

function handleDelete(index) {
  const button = document.querySelector(`#student-list li:nth-child(${index + 1}) .delete-btn`);
  button.classList.add("removing");
  setTimeout(() => deleteStudent(index), 500);  // Attendi la fine dell'animazione prima di rimuovere
}

