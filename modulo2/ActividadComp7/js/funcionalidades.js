function calcularBeca() {
  const edad = Number(document.getElementById("edad").value);
  const puntaje = Number(document.getElementById("puntaje").value);
  const ocupacionActual = document.querySelector('input[name="ocupacionActual"]:checked').value;
  const mensajeDiv = document.getElementById("mensajeBecas");
  let becas = [];

  //Beca Talento Joven -> 50%
  if (edad < 25 && puntaje > 80) {
    becas.push("Beca Talento Joven (50% de descuento)");
  }

  if (ocupacionActual === "cesante" && puntaje > 60) {
    becas.push("Beca Reconversión (40% de descuento)");
  }

  if (puntaje >= 90) {
    becas.push("Beca Alto Puntaje (60% de descuento)");
  }

  if (becas.length === 0) {
    mensajeDiv.innerText = "No aplica a ninguna beca.";
  } else {
    mensajeDiv.innerText = "Cumples con los requisitos para las becas: :" + becas.join(", ");
  }
}
