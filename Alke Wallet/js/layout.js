$(document).ready(function () {
  // Cargar navbar en el header
  $("#header").load("layout/navbar.html");

  // Cargar footer en el footer
  $("#footer").load("layout/footer.html");
});

$(document).on(
  "click",
  ".redireccion .nav-link, .redireccion .btn",
  function () {
    const pagina = $(this).data("url");

    if (!pagina) return;
    //evalua si está en la misma pagina antes de hacer algo
    if (window.location.pathname.endsWith(pagina)) return;

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
  }
);
