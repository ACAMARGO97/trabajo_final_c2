<template>
    <div>
        <div class="card">
            <div class="card-body text-center">
                <h2 class="fs-2">Mis Agendas</h2>
                <br />
            
            </div>
        </div>
    </div>
    <div class="d-flex flex-row flex-wrap justify-content-around my-5">
        <template v-for="fac in factura" :key="fac">
            <div class="card" style="width: 18rem;">
                <div class="card-body">
                    <h5 class="card-title">Numero de Agenda: {{ fac.agen_numero }}</h5>
                </div>
                <ul class="list-group list-group-flush">
                    <th class="list-group-item">Fecha: {{ fac.agen_fecha }}</th>
                    <th class="list-group-item">Cliente: {{ fac.cliente.persona.pers_nombre }}</th>
                    <th class="list-group-item">Empleado: {{ fac.empleado.persona.pers_nombre }}</th>
                    <th class="list-group-item">Factura: {{ fac.factura.fact_nombre }}</th>
                </ul>
            </div>
        </template>
    </div>
</template>

<script lang="ts" >
import axios from 'axios'

export default {
    data() {
        return {
            factura: []
        }
    },
    mounted() {
        axios.get("http://127.0.0.1:8000/agendas/a").then(response => this.factura = response.data)
    }
}
</script>

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