document.querySelectorAll(".btn").forEach((boton) => {
  boton.addEventListener("click", () => {
    const pagina = boton.dataset.url;
    const mensaje = boton.dataset.mensaje;

    Swal.fire({
      title: "Redirigiendo...",
      text: mensaje,
      icon: "info",
      timer: 3000,
      showConfirmButton: false,
      allowOutsideClick: false,
      allowEscapeKey: false
    });

    setTimeout(() => {
      window.location.href = pagina;
    }, 3000);
  });
});

