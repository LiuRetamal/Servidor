onload=principal;

let listaCamiones;
let ldc;

function principal(){
    listaCamiones.document.getElementById("listaCamiones");
    cargarServidorCamiones();
}

function cargarServidorCamiones(){
    //peticion al servidor de la lista de camiones
    let jsonhttp = new XMLHttpRequest();

    jsonhttp.onreadystatechange = function(){
        //evaluar la respuesta del servidor
        if (this.readyState == 4 && this.status == 200) {
            //this.responseText -> datos en formato JSON
            //datosCamiones = JSON.parse(this.responseText);
            let ldc = JSON.parse(this.responseText);
            for(const camion of ldc){
                listaCamiones.append(creaCamion(camion));
            }
        }
    }

    //construir la peticion al servidor
    jsonhttp.open("GET", "http://www.servidor.es/catalogoCamiones/listarCamiones.py", true);
    //ejecutar la peticion al servidor
    jsonhttp.send();
    
}

function creaCamion(camion){
    let img= camion[4];
    let textImg= camion[4];
    let modelo= camion[1];
    let marca= camion[0];
    let precio= camion[3];
    let desc= camion[2];

    let divTarjCam = document.createElement("div");
    divTarjCam.setAttribute("class", "card m-3");
    let divRow = document.createElement("div");
    divRow.setAttribute("class", "row g-0");
    let subDivImg = document.createElement("div");
    subDivImg.setAttribute("class", "col-md-5");
    subDivImg.innerHTML='<img src=img/'+img+' class="img-fluid rounded-start" alt='+textImg+'>'
 
    let subDivInfo  = document.createElement("div");
    subDivInfo.setAttribute("class","col-md-7");
    subDivInfo.innerHTML='<div class="card-body">\
                            <h5 class="card-title">Modelo: '+modelo+'</h5>\
                            <p class="card-text">Marca: '+marca+'</p>\
                            <p class="card-text">Precio: '+precio+' &euro;</p>\
                            <p class="card-text">Descripci&oacute;n: '+desc+'</p>\
                          </div>';
 
    divRow.appendChild(subDivImg)
    divRow.appendChild(subDivInfo)
    divTarjCam.appendChild(divRow)
 
    return divTarjCam;
 

}
function enviarCamion(){
    //objeto para comunicarnos con el servidor
    let jsonhttp = new XMLHttoRequest();

    //datos para enviar al servidor
    let marca = document.getElementById("marca").value;
    let modelo = document.getElementById("modelo").value;
    let precio = document.getElementById("precio").value;
    let desc = document.getElementById("desc").value;

    //codigo que espera respuesta del servidor 
    jsonhttp.onreadystatechange = function(){
        //evaluar la respuesta del servidor
        if (this.readyState == 4 && this.status == 200) {
            //this.responseText -> datos en formato JSON
            //datosCamiones = JSON.parse(this.responseText);
            let resultado = JSON.parse(this.responseText);
            if(resultado){
                camion=[marca,modelo,desc, precio, "img/camionBlanco.img"]
                listaCamiones.insertBefore(creaCamion(camion), listaCamiones.firstChild);
                
            }
            
        }
    }
    //enviar informacion al servidor
    jsonhttp.open("POST", "http://www.servidor.es/catalogoCamiones/guardarCamion.py", true)
    jsonhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");    
    jsonhttp.send("marca="+marca+"&modelo="+modelo+"&precio="+precio+"&desc="+desc);

}