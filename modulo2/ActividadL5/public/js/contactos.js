//contactos iniciales
const contactosBase = [
  {
    nombre: "John Doe",
    cbu: "123456789",
    alias: "john.doe",
    banco: "ABC Bank",
  },
  {
    nombre: "Jane Smith",
    cbu: "987654321",
    alias: "jane.smith",
    banco: "XYZ Bank",
  },
  {
    nombre: "Juan Peréz",
    cbu: "123498765",
    alias: "juan.perez",
    banco: "MNO Bank",
  },
];

if (!localStorage.getItem("contactos")) {
  localStorage.setItem("contactos", JSON.stringify(contactosBase));
}

//carga los contactos del localStorage
const contactos = JSON.parse(localStorage.getItem("contactos")) || [];

//dibujo de los inputs

function crearContacto(contacto, index) {
  return (
    '<input type="radio" class="btn-check" name="btnradio" id="btnradio' +
    index +
    '" autocomplete="off">' +
    '<label class="btn btn-outline-dark w-100 text-start" for="btnradio' +
    index +
    '">' +
    '<span class="contact-name">' +
    contacto.nombre +
    "</span> <br>" +
    '<span class= "contact-details">' +
    "CBU:" +
    contacto.cbu +
    ", Alias:" +
    contacto.alias +
    ", Banco " +
    contacto.banco +
    "</span></label>"
  );
}

//mostrar nuevos contactos

function mostrarContactos() {
  const contenedor = document.getElementById("contactList");
  contenedor.innerHTML = "";

  contactos.forEach((contacto, index) => {
    contenedor.innerHTML += crearContacto(contacto, index);
  });
}

//agregar nuevo contacto

function agregarContacto() {
  const nuevo = {
    nombre: document.getElementById("floatingInput-name").value,
    cbu: document.getElementById("floatingInput-cbu").value,
    alias: document.getElementById("floatingInput-alias").value,
    banco: document.getElementById("banco").value,
  };

  if (!nuevo.nombre || !nuevo.cbu || !nuevo.alias || !nuevo.banco) {
    Swal.fire("Error", "Completa todos los campos", "error");
    return;
  }

  contactos.push(nuevo);
  localStorage.setItem("contactos", JSON.stringify(contactos));

  Swal.fire({
    icon: "success",
    title: "Éxito",
    text: "Contacto agregado correctamente",
    timer: 2000,
    showConfirmButton: false,
  }).then(() => {
    const modal = bootstrap.Modal.getInstance(
      document.getElementById("staticBackdrop")
    );
    if (modal) modal.hide();

    //limpia el modal
    document.getElementById("floatingInput-name").value = "";
    document.getElementById("floatingInput-cbu").value = "";
    document.getElementById("floatingInput-alias").value = "";
    document.getElementById("banco").value = "";
  });
}

//Event listeners

document.getElementById("btn-agregarContacto").addEventListener("click", () => {
  agregarContacto();
});


// Al cargar la página carga los contactos
document.addEventListener('DOMContentLoaded', () => {
  mostrarContactos();
});