// Mostrar secciones
function showSection(sectionId) {
    document.querySelectorAll('main section').forEach(section => {
        section.classList.remove('active');
    });
    document.getElementById(sectionId).classList.add('active');
    
    // Cargar datos al mostrar la sección
    if (sectionId === 'materiales') {
        loadMaterials();
    } else if (sectionId === 'usuarios') {
        loadUsers();
    } else if (sectionId === 'prestamos') {
        loadLoans();
    }
}

// Materiales
function showMaterialForm() {
    document.getElementById('material-form').style.display = 'block';
}


function hideMaterialForm() {
    document.getElementById('material-form').style.display = 'none';
    document.getElementById('add-material-form').reset();
}

function changeMaterialForm() {
    const type = document.getElementById('material-type').value;
    
    document.getElementById('libro-fields').style.display = 'none';
    document.getElementById('revista-fields').style.display = 'none';
    document.getElementById('dvd-fields').style.display = 'none';
    
    if (type === 'libro') {
        document.getElementById('libro-fields').style.display = 'block';
    } else if (type === 'revista') {
        document.getElementById('revista-fields').style.display = 'block';
    } else if (type === 'dvd') {
        document.getElementById('dvd-fields').style.display = 'block';
    }
}

async function addMaterial() {
    const type = document.getElementById('material-type').value;
    const titulo = document.getElementById('titulo').value;
    const autor = document.getElementById('autor').value;
    
    let material = { tipo: type, titulo, autor };
    
    if (type === 'libro') {
        material.paginas = document.getElementById('paginas').value;
    } else if (type === 'revista') {
        material.edicion = document.getElementById('edicion').value;
        material.fecha = document.getElementById('fecha').value;
    } else if (type === 'dvd') {
        material.duracion = document.getElementById('duracion').value;
        material.formato = document.getElementById('formato').value;
    }
    
    try {
        const result = await addMaterial(material);
        alert(result.message);
        hideMaterialForm();
        loadMaterials();
    } catch (error) {
        alert('Error al añadir material: ' + error.message);
    }
}

async function loadMaterials() {
    try {
        const data = await getMaterials();
        const listContainer = document.getElementById('material-list');
        
        if (data.materiales && data.materiales.length > 0) {
            let html = '<table><tr><th>ID</th><th>Tipo</th><th>Título</th><th>Autor</th><th>Detalles</th></tr>';
            
            data.materiales.forEach(material => {
                let detalles = '';
                if (material.tipo === 'libro') {
                    detalles = `Páginas: ${material.paginas}`;
                } else if (material.tipo === 'revista') {
                    detalles = `Edición: ${material.edicion}, Fecha: ${material.fecha_publicacion}`;
                } else if (material.tipo === 'dvd') {
                    detalles = `Duración: ${material.duracion} min, Formato: ${material.formato}`;
                }
                
                html += `
                    <tr>
                        <td>${material.id}</td>
                        <td>${material.tipo}</td>
                        <td>${material.titulo}</td>
                        <td>${material.autor}</td>
                        <td>${detalles}</td>
                    </tr>
                `;
            });
            
            html += '</table>';
            listContainer.innerHTML = html;
        } else {
            listContainer.innerHTML = '<p>No hay materiales registrados.</p>';
        }
    } catch (error) {
        document.getElementById('material-list').innerHTML = '<p>Error al cargar materiales.</p>';
    }
}

// Usuarios
function showUserForm() {
    document.getElementById('user-form').style.display = 'block';
}

function hideUserForm() {
    document.getElementById('user-form').style.display = 'none';
    document.getElementById('add-user-form').reset();
}

async function addUser() {
    const nombre = document.getElementById('nombre').value;
    
    try {
        const result = await addUser({ nombre });
        alert(result.message);
        hideUserForm();
        loadUsers();
    } catch (error) {
        alert('Error al añadir usuario: ' + error.message);
    }
}

async function loadUsers() {
    try {
        const data = await getUsers();
        const listContainer = document.getElementById('user-list');
        
        if (data.usuarios && data.usuarios.length > 0) {
            let html = '<table><tr><th>ID</th><th>Nombre</th></tr>';
            
            data.usuarios.forEach(user => {
                html += `
                    <tr>
                        <td>${user.id}</td>
                        <td>${user.nombre}</td>
                    </tr>
                `;
            });
            
            html += '</table>';
            listContainer.innerHTML = html;
        } else {
            listContainer.innerHTML = '<p>No hay usuarios registrados.</p>';
        }
    } catch (error) {
        document.getElementById('user-list').innerHTML = '<p>Error al cargar usuarios.</p>';
    }
}

// Préstamos
function showLoanForm() {
    document.getElementById('loan-form').style.display = 'block';
}

function hideLoanForm() {
    document.getElementById('loan-form').style.display = 'none';
    document.getElementById('add-loan-form').reset();
}

async function addLoan() {
    const idItem = document.getElementById('id-item').value;
    const idUsuario = document.getElementById('id-usuario').value;
    
    try {
        const result = await addLoan({ id_item: idItem, id_usuario: idUsuario });
        alert(result.message);
        hideLoanForm();
        loadLoans();
    } catch (error) {
        alert('Error al registrar préstamo: ' + error.message);
    }
}

async function loadLoans() {
    try {
        const data = await getLoans();
        const listContainer = document.getElementById('loan-list');
        
        if (data.prestamos && data.prestamos.length > 0) {
            let html = '<table><tr><th>ID</th><th>Material</th><th>Usuario</th><th>Fecha Préstamo</th><th>Fecha Límite</th><th>Estado</th><th>Acciones</th></tr>';
            
            data.prestamos.forEach(loan => {
                const statusClass = loan.devuelto ? 'status-returned' : 'status-pending';
                const statusText = loan.devuelto ? 'Devuelto' : 'Pendiente';
                
                html += `
                    <tr>
                        <td>${loan.id}</td>
                        <td>${loan.id_item} (${loan.titulo_material})</td>
                        <td>${loan.id_usuario} (${loan.nombre_usuario})</td>
                        <td>${new Date(loan.fecha_prestamo).toLocaleDateString()}</td>
                        <td>${loan.fecha_limite ? new Date(loan.fecha_limite).toLocaleDateString() : 'N/A'}</td>
                        <td class="${statusClass}">${statusText}</td>
                        <td>
                            ${!loan.devuelto ? `<button onclick="returnLoan(${loan.id})">Marcar como devuelto</button>` : ''}
                        </td>
                    </tr>
                `;
            });
            
            html += '</table>';
            listContainer.innerHTML = html;
        } else {
            listContainer.innerHTML = '<p>No hay préstamos registrados.</p>';
        }
    } catch (error) {
        document.getElementById('loan-list').innerHTML = '<p>Error al cargar préstamos.</p>';
    }
}

async function returnLoan(loanId) {
    if (confirm('¿Marcar este préstamo como devuelto?')) {
        try {
            const result = await updateLoan(loanId, { devuelto: true });
            alert(result.message);
            loadLoans();
        } catch (error) {
            alert('Error al actualizar préstamo: ' + error.message);
        }
    }
}

// Inicialización
document.addEventListener('DOMContentLoaded', () => {
    // Mostrar la sección de materiales por defecto
    showSection('materiales');
});