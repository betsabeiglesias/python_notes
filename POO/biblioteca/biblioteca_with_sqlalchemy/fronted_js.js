const API_URL = 'http://127.0.0.1:8000';

//********* MATERIALES *********\\

async function consultar_elemento_catalogo() {
    const item = document.getElementById("id_consultar").value;
    const res = await fetch(`${API_URL}/material/${item}`,{
        method: 'GET',
        headers: { 'Content-Type': 'application/json' },
 
    });
    const data = await res.json()
    document.getElementById("info_item").textContent = JSON.stringify(data, null, 2);
    
    
}

document.getElementById("tipo_material").addEventListener("change", function() {
    const tipo = this.value;
    
    document.getElementById("form_libro").style.display = "none";
    document.getElementById("form_revista").style.display = "none";
    document.getElementById("form_dvd").style.display = "none";

    if (tipo === "libro") {
        document.getElementById("form_libro").style.display = "block";
    } else if (tipo === "revista") {
        document.getElementById("form_revista").style.display = "block";
    } else if (tipo === "dvd") {
        document.getElementById("form_dvd").style.display = "block";
    }
});



async function registrar_material() {
  const tipo = document.getElementById("tipo_material").value;

  let body = {
    tipo: tipo,
    titulo: "",
    autor: ""
  };

  if (tipo === "libro") {
    body.titulo = document.getElementById("titulo_libro").value;
    body.autor = document.getElementById("autor_libro").value;
    body.paginas = parseInt(document.getElementById("paginas").value);
  }

  else if (tipo === "revista") {
    body.titulo = document.getElementById("titulo_revista").value;
    body.autor = document.getElementById("autor_revista").value;
    body.edicion = parseInt(document.getElementById("edicion").value);
    body.fecha = document.getElementById("fecha").value;
  }

  else if (tipo === "dvd") {
    body.titulo = document.getElementById("titulo_dvd").value;
    body.autor = document.getElementById("autor_dvd").value;
    body.duracion = parseInt(document.getElementById("duracion").value);
    body.formato = document.getElementById("formato").value;
  }

  try {
    const res = await fetch(`${API_URL}/material`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(body)
    });

    console.log("Datos enviados:", body);
    const data = await res.json();
    if (!res.ok) {
    // Si el servidor respondió con error (ej: 400 o 500)
    throw new Error(data.detail || "Error desconocido en el servidor");
    }
    alert(data.message || "✅ Material registrado");
    console.log(data);
  } catch (error) {
    alert("❌ Error al registrar material");
    console.error(error);
  }
}



//********* PRÉSTAMOS *********\\


async function registrar_prestamo(){
    const item = document.getElementById("id_a_prestar").value;
    const user = document.getElementById("id_usuario").value;

    try{
        const res = await fetch(`${API_URL}/prestamos`,{
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify("id_item"=item, "id_usuario"=user )
        })
        if (!res.ok) {
          throw new Error(data.detail || "Error desconocido en el servidor");
        }
        alert(data.message || "✅ Material registrado");
        console.log(data);
  }
    catch (error){
      alert("❌ Error al registrar material");
      console.error(error);
    }

};