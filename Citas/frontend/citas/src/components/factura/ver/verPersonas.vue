<template>
    <div>
        <div class="card">
            <div class="card-body text-center">
                <h2 class="fs-2">Tabla De Personas</h2>
                <br />
                <a href="/nuevapersona" class="boton">Agregar</a>
                <br/>
                <br/>
                <a  class="boton" @click="excel()">Descargar</a>
            </div>
        </div>
    </div>
    <div class="d-flex flex-row flex-wrap justify-content-around my-5">
        <template v-for="fac in factura" :key="fac">
            <div class="card" style="width: 18rem;">
                <div class="card-body">
                    <h5 class="card-title">Nombre: {{ fac.pers_nombre }}</h5>
                    <h4 class="card-title">Segundo Nombre: {{ fac.pers_segundonombre }}</h4>
                    <h4 class="card-title">Apellido: {{ fac.pers_apellido }}</h4>
                    <h4 class="card-title">Segundo Apellido: {{ fac.pers_segundoapellido }}</h4>
                </div>
                <ul class="list-group list-group-flush">
                    <th class="list-group-item">Telefono: {{ fac.pers_telefono }}</th>
                    <th class="list-group-item">Correo: {{ fac.pers_correo }}</th>
                </ul>
            </div>
        </template>
    </div>
</template>

<script lang="ts" >
import axios from 'axios'
import exportXlsFile from 'export-from-json'

export default {
    data() {
        return {
            factura: []
        }
    },
    mounted() {
        axios.get("http://127.0.0.1:8000/personas/").then(response => this.factura = response.data)
    },
    methods:{
        excel() {
        const data = this.factura;
        const fileName = 'excel';
        const exportType = exportXlsFile.types.xls
        exportXlsFile({data, fileName, exportType})
    }
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