<template>
    <div class="row">
        <div class="card">
            <div class="card-body text-center">
                <h2 class="fs-2">Mis Consultas</h2>
                <br />
            </div>
        </div>
    </div>
    <div class="d-flex flex-row flex-wrap justify-content-around my-5">
        <div class="col-5">
            <div class="card">
                <div class="card-body">
                    <h4 class="card-title">Consulta N# 1</h4>
                    <p class="card-text"> Consultar el numero de registros que hay en facturas.</p>
                    <a href="/consulta1" class="boton">Ver</a>
                </div>
            </div>
        </div>
        <div class="col-5">
            <div class="card">
                <div class="card-body">
                    <h4 class="card-title">Consulta N# 2</h4>
                    <p class="card-text">Consultar los nombre y precios registrados</p>
                    <a href="/consulta2" class="boton">Ver</a>
                </div>
            </div>
        </div>
        <div class="col-5">
            <div class="card">
                <div class="card-body">
                    <h4 class="card-title">Consulta N# 3</h4>
                    <p class="card-text">Consulta con la utilizacion de SQL, Retorna los datos id, Nombre y fecha en los registros agendados.</p>
                    <a href="/consulta3" class="boton">Ver</a>
                </div>
            </div>
        </div>
    </div>
</template>
<style scoped >
.boton {
    background-color: #bddbfa;
    border-radius: 28px;
    border: 1px solid #84bbf3;
    display: inline-block;
    cursor: pointer;
    color: #ffffff;
    font-family: Arial;
    font-size: 19px;
    padding: 5px 38px;
    text-decoration: none;
    text-shadow: 0px 1px 0px #528ecc;
}

.boton:hover {
    background-color: #80b5ea;
}

.boton:active {
    position: relative;
    top: 1px;
}
</style>