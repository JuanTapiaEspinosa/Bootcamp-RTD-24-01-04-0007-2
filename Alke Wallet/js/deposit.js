// Esperar el click del botón
$("#btnDeposito").on("click", function (e) {
  e.preventDefault();
  const monto = parseFloat($("#depositAmount").val());
  if (isNaN(monto) || monto <= 0) {
    Swal.fire("Error", "Monto inválido", "error");
    return;
  } else {
    depositar(monto);
    $("#depositAmount").val("");

    Swal.fire({
      icon: "success",
      title: "Éxito",
      text: "Depósito realizado con éxito",
      timer: 2000, // se cierra sola en 2 segundos
      showConfirmButton: false, // sin botón
      allowOutsideClick: false, // no se puede cerrar clickeando fuera
      allowEscapeKey: false, // no se puede cerrar con ESC
      willClose: () => {
        window.location.href = "menu.html"; // redirige al cerrarse
      },
    });

    return;
  }
});
