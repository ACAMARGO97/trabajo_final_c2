<template>
    <div class="row">
        <div class="card">
            <div class="card-body text-center">
                <h2 class="fs-2">Consulta N# 2</h2>
                <br />
                <p class="card-text">Consultar los nombre y precios registrados.</p>
            </div>
        </div>
    </div>
    <div class="d-flex flex-row flex-wrap justify-content-around my-5">

        <div class="col-4">
            <div class="jumbotron jumbotron-fluid">
                <div class="container">
                    <h1 class="display-4">Facturas</h1>
                    <div>
                        <table class="table">
                            <thead>
                                <tr>
                                    <th scope="col">Nombres</th>
                                    <th scope="col">Precios</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr v-for="fac in factura" :key="fac">
                                    <td>{{ fac.fact_nombre }}</td>
                                    <td>{{ fac.fact_precio }}</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                    <br />
                     <button class="boton" onclick="history.back()">Volver</button>
                </div>
            </div>
        </div>

    </div>
</template>
<script>
import axios from 'axios'

export default {
    data() {
        return {
            factura: [
            ]
        }
    },
    mounted() {
        axios.get("http://127.0.0.1:8000/facturas/consulta2/").then(response => this.factura = response.data)
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