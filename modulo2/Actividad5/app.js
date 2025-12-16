$(document).ready(function () {
  $("#btnCalcular").on("click", function () {
    let monto = $("#montoPrestamo").val();
    let interes = $("#interesAnual").val();
    let meses = $("#cantidadMeses").val();

    let total = monto * (1 + interes / 12) ** meses;

    mostrarResultado(total);
  });

  function mostrarResultado(resultado) {
    $("#resultadoPrestamo").text("Total: " + resultado);
  }
});
