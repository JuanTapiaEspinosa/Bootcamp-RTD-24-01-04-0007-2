//Lista de usuarios y contraseñas

const users = [
  { user: "admin@admin.cl", password: "admin" },
  { user: "test@test.cl", password: "test" },
];

//función que valida si el usuario y contraseña coincide con alguno de la lista

function validarUsuario(user, pass) {
  const encontrado = users.find((u) => u.user === user && u.password === pass);


  //las alertas están hechas importando sweetAlert2
  if (encontrado) {
    Swal.fire({
      title: "Usuario verificado",
      text: "Serás redirigido en 3 segundos",
      icon: "success",
      timer: 3000, 
      showConfirmButton: false,
      willClose: () => {
        window.location.href = "menu.html"; 
      },
    });
  } else {
    Swal.fire({
      title: "Error",
      text: "Usuario o contraseña incorrectos",
      icon: "error",
    });
  }
}

//captura de datos al apretar el botón del formulario

document.getElementById("loginForm").addEventListener("submit", function (e) {
  e.preventDefault();

  const user = document.getElementById("email").value;
  const pass = document.getElementById("password").value;
  validarUsuario(user, pass);
});
