function enviarDinero() {
  const montoInput = document.getElementById("floatingInput-montoEnviar");
  const monto = parseFloat(montoInput.value);

  if (isNaN(monto) || monto <= 0) {
    Swal.fire("Error", "Ingresa un monto válido", "error");
    return;
  }

  const radioSeleccionado = document.querySelector(
    "input[name=btnradio]:checked"
  );
  if (!radioSeleccionado) {
    Swal.fire("Error", "selecciona un contacto", "error");
    return;
  }

  const indexContacto = parseInt(
    radioSeleccionado.id.replace("btnradio", ""),
    10
  );
  const contacto = contactos[indexContacto];

  if (!contacto) {
    Swal.fire("Error", "Contacto no válido", "error");
    return;
  }

  if (monto > saldo) {
    Swal.fire("Error", "Saldo insuficiente", "error");
  }

  Swal.fire({
    title: "Confirmar envío",
    text: `¿Deseas enviar $${monto} a ${contacto.nombre}?`,
    icon: "question",
    showCancelButton: true,
    confirmButtonText: "Sí, enviar",
    cancelButtonText: "Cancelar",
  }).then((result) => {
    if (result.isConfirmed) {
      //Aquí se reduce el monto
      saldo -= monto;
      localStorage.setItem("saldo", saldo);
      //aquí se guarda la transacción

      let transacciones =
        JSON.parse(localStorage.getItem("transacciones")) || [];
      const nuevaTransaccion = `Transferencia a ${contacto.nombre} - $${monto}`;
      //unshift hace que se guarde primero
      transacciones.unshift(nuevaTransaccion);
      localStorage.setItem("transacciones", JSON.stringify(transacciones));

      //Mensaje de éxito
      Swal.fire({
        icon: "success",
        title: "Envío realizado",
        text: `Has enviado $${monto} a ${contacto.nombre}`,
        timer: 2000,
        showConfirmButton: false,
      });

      //se limpia el monto
      montoInput.value = "";

      console.log("Lista actual de transacciones:", transacciones);
    }
  });

  montoInput.value = "";
}

document.getElementById("btnEnviar").addEventListener("click", enviarDinero);
