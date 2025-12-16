$(".btn").on("click", function () {
  const pagina = $(this).data("url");
  const mensaje = $(this).data("mensaje");

  Swal.fire({
    title: "Redirigiendo...",
    text: mensaje,
    icon: "info",
    timer: 3000,
    showConfirmButton: false,
    allowOutsideClick: false,
    allowEscapeKey: false,
    willClose: () => {
      window.location.href = pagina;
    },
  });
});
