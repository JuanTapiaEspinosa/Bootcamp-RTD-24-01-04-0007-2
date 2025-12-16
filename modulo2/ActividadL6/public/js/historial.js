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

function mostrarTransacciones(filtroTipo = "Todas") {
  const $lista = $("#listaTransacciones");
  $lista.empty(); //limpia el contenido

  const transacciones = JSON.parse(localStorage.getItem("transacciones")) || [];

  $.each(transacciones, function (index, t) {
    const tMinus = t.toLowerCase(); //convierte el texto a minuscula
    const tipo = filtroTipo.toLowerCase(); //convierte el filtro a minusculas

    const coincideTipo = tipo === "todas" || tMinus.includes(tipo);

    if (coincideTipo) {
      const $li = $("<li>")
        .addClass("list-group-item list-group-item-action")
        .text(t);
      $lista.append($li);
    }
  });
}

$(document).ready(function () {
  mostrarTransacciones();

  $("#tipoTransaccion").on("change", function () {
    const tipo = $(this).val(); // obtiene el valor del select
    mostrarTransacciones(tipo); // aplica el filtro
  });
});
