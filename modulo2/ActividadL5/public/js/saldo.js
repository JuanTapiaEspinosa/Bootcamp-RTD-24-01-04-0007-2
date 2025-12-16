let saldo = parseFloat(localStorage.getItem("saldo")) || 0;

function actualizarSaldo() {
  const elementoSaldo = document.querySelectorAll(".saldo");
  elementoSaldo.forEach((el) => (el.textContent = "$" + saldo.toFixed(2)));
}

function depositar(monto) {
  if (monto <= 0 || isNaN(monto)) {
    Swal.fire("Error", "Ingrese monto válido", "error");
    return;
  }
  saldo += monto;
  localStorage.setItem("saldo", saldo); //aquí se guarda el saldo para las otras vistas
  actualizarSaldo();
  Swal.fire("Éxito", "Has depositado $" + monto, "success");

  let transacciones = JSON.parse(localStorage.getItem("transacciones")) || [];
  const nuevaTransaccion = `Depósito - $${monto}`;
  transacciones.unshift(nuevaTransaccion); 
  localStorage.setItem("transacciones", JSON.stringify(transacciones));
}

actualizarSaldo();
