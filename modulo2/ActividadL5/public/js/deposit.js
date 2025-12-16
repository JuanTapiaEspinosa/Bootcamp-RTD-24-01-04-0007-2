// Esperar el click del botón
document.getElementById("btnDeposito").addEventListener("click", (e) => {
    e.preventDefault();
  const monto = parseFloat(document.getElementById("depositAmount").value);

  depositar(monto);

  document.getElementById("depositAmount").value = "";
});