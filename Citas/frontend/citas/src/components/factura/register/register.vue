<template>
    <center>
        <div class="col-6">
            <div class="d-flex flex-row flex-wrap justify-content-around my-5">
                <div class="card" style="width: 80rem;">
                    <form>
                        <fieldset>
                            <legend>Formulario nueva factura.</legend>
                            <div class="form-group">
                                <label for="" class="form-label">Nombre</label>
                                <input type="text" v-model="factura.fact_nombre" class="form-control" required>
                            </div>
                            <div class="form-group">
                                <label for="" class="form-label">Precio</label>
                                <input type="text" v-model="factura.fact_precio" class="form-control" required>
                            </div>
                            <div class="form-group">
                                <label for="tiposervicio" class="form-label">Tipo de Servicio</label>
                                <select type="text" v-model="factura.tiposervicio" id="tiposervicio" class="form-control"
                                    required>
                                    <option>Seleccionar</option>
                                    <option>Planchado</option>
                                    <option>Corte de cabello</option>
                                
                                </select>
                            </div>
                            <button class="boton" @click="createFactura()">Crear</button> &nbsp;
                            <a class="boton" onclick="history.back()">Volver</a>
                        </fieldset>
                    </form>
                </div>
            </div>

        </div>
        <div class="col-2"></div>
    </center>
</template>

<script lang="ts">
import axios from 'axios'

export default {
    data() {
        return {
            factura: { fact_nombre: '', fact_precio: '', tiposervicio: 15 }
        }
    },
    methods: {
        createFactura() {
            axios
                .post('http://127.0.0.1:8000/facturas/fcreate/', this.factura)
                .then((response) => console.log(response))
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