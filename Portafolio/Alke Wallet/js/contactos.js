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
let contactos = JSON.parse(localStorage.getItem("contactos")) || [];

//dibujo de los inputs

function crearContacto(contacto, index) {
  return `<input type="radio" class="btn-check" name="btnradio" id="btnradio${index}" autocomplete="off"
         data-nombre="${contacto.nombre}"
       data-cbu="${contacto.cbu}"
       data-alias="${contacto.alias}"
       data-banco="${contacto.banco}">
<label class="btn btn-outline-info w-100 text-start mb-2 p-3 d-flex flex-column align-items-start" for="btnradio${index}">
  <span class="contact-name fw-bold fs-5">${contacto.nombre}</span>
  <span class="contact-details text-light small">
    CBU: ${contacto.cbu} | Alias: ${contacto.alias} | Banco: ${contacto.banco}
  </span>
</label>`;
}

//mostrar nuevos contactos

function mostrarContactos() {
  const $contenedor = $("#contactList");
  $contenedor.empty();

  $.each(contactos, function (index, contacto) {
    $contenedor.append(crearContacto(contacto, index));
  });
}

//agregar nuevo contacto

function agregarContacto() {
  const nuevo = {
    nombre: $("#floatingInput-name").val(),
    cbu: $("#floatingInput-cbu").val(),
    alias: $("#floatingInput-alias").val(),
    banco: $("#banco").val(),
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
    const modal = bootstrap.Modal.getInstance($("#staticBackdrop")[0]);
    if (modal) modal.hide();

    //limpia los inputs del modal
    $("#floatingInput-name").val("");
    $("#floatingInput-cbu").val("");
    $("#floatingInput-alias").val("");
    $("#banco").val("");
  });

  mostrarContactos();
}

//Event listeners

$("#btn-agregarContacto").on("click", function () {
  agregarContacto();
});

// Al cargar la página carga los contactos
$(document).ready(function () {
  mostrarContactos();
});

//buscador en tiempo real
$("#searchContact").on("input", function () {
  const texto = $(this).val().trim().toLowerCase();

  const filtrados = contactos.filter((contacto) => {
    const nombre = contacto.nombre ? contacto.nombre.toLowerCase() : "";
    const alias = contacto.alias ? contacto.alias.toLowerCase() : "";

    return nombre.includes(texto) || alias.includes(texto);
  });

  mostrarContactosFiltrados(filtrados);
});

function mostrarContactosFiltrados(lista) {
  const $contenedor = $("#contactList");
  $contenedor.empty();

  $.each(lista, function (index, contacto) {
    $contenedor.append(crearContacto(contacto, index));
  });
}

// Evita que la lista de contactos se scrollee sola automaticamente
$(document).on("click", "#contactList .btn-check + label", function () {
  const $container = $("#contactList");
  const scrollTop = $container.scrollTop();

  const input = document.getElementById($(this).attr("for"));
  input.focus({ preventScroll: true });

  $container.scrollTop(scrollTop);
});
