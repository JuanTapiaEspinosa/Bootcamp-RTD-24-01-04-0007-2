
const transaccionesIniciales = [
  "Compra en línea - $50.00",
  "Depósito - $100.00",
  "Transferencia recibida - $75.00",
  "Compra en línea - $5550.00",
  "Depósito misma cuenta - $10500.00",
  "Transferencia recibida - $7575.00",
];

if (!localStorage.getItem("transacciones")) {
  localStorage.setItem("transacciones", JSON.stringify(transaccionesIniciales));
}

function mostrarTransacciones() {
  const lista = document.getElementById("listaTransacciones");
  lista.innerHTML = "";

  let transacciones = JSON.parse(localStorage.getItem("transacciones")) || [];

  transacciones.forEach((t) => {
    const li = document.createElement("li");
    li.className = "list-group-item list-group-item-action";
    li.textContent = t;
    lista.appendChild(li);
  });
}

mostrarTransacciones();