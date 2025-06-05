const API_BASE_URL = 'https://127.0.0.1:8000';

document.addEventListener("DOMContentLoaded",function(){
    document.getElementById("btnMateriales").addEventListener('click',function(){
        getMaterials();
    });
});
// Funciones para Materiales
// export async function getMaterials() {
//     console.log("Press TEST")
//     const response = await fetch(`${API_BASE_URL}/material`);
//     return await response.json();
// }

async function getMaterials() {
    console.log("Press TEST")
    const response = await fetch(`http://127.0.0.1:8000/material`);
    return await response.json();
}

export async function addMaterial(material) {
    const response = await fetch(`${API_BASE_URL}/material`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(material)
    });
    return await response.json();
}

// Funciones para Usuarios
export async function getUsers() {
    const response = await fetch(`${API_BASE_URL}/usuarios`);
    return await response.json();
}

export async function addUser(user) {
    const response = await fetch(`${API_BASE_URL}/usuarios`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(user)
    });
    return await response.json();
}

// Funciones para Préstamos
export async function getLoans() {
    const response = await fetch(`${API_BASE_URL}/prestamos`);
    return await response.json();
}

export async function addLoan(loan) {
    const response = await fetch(`${API_BASE_URL}/prestamos`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(loan)
    });
    return await response.json();
}

export async function updateLoan(loanId, updateData) {
    const response = await fetch(`${API_BASE_URL}/prestamos`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            id_prestamo: loanId,
            ...updateData
        })
    });
    return await response.json();
}