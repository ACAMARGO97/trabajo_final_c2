<template>
    <center>
        <div class="col-6">
            <div class="d-flex flex-row flex-wrap justify-content-around my-5">
                <div class="card" style="width: 80rem;">
                    <form>
                        <fieldset>
                            <legend>Formulario nueva persona.</legend>
                            <div class="form-group">
                                <label for="pers_nombre" class="form-label mt-4">Nombre</label>
                                <input type="text" class="form-control" v-model="personaData.pers_nombre"
                                    placeholder="Nombre">
                            </div>
                            <div class="form-group">
                                <label for="pers_segundonombre" class="form-label mt-4">Segundo Nombre</label>
                                <input type="text" class="form-control" v-model="personaData.pers_segundonombre"
                                    placeholder="Nombre">
                            </div>
                            <div class="form-group">
                                <label for="pers_apellido" class="form-label mt-4">Apellido</label>
                                <input type="text" class="form-control" v-model="personaData.pers_apellido"
                                    placeholder="Apellido">
                            </div>
                            <div class="form-group">
                                <label for="pers_segundoapellido" class="form-label mt-4">Segundo Apellido</label>
                                <input type="text" class="form-control" v-model="personaData.pers_segundoapellido"
                                    placeholder="Apellido">
                            </div>
                            <div class="form-group">
                                <label for="pers_telefono" class="form-label mt-4">Telefono</label>
                                <input type="text" class="form-control" v-model="personaData.pers_telefono"
                                    placeholder="Telefono">
                            </div>
                            <div class="form-group">
                                <label for="pers_correo" class="form-label mt-4">Correo</label>
                                <input type="text" class="form-control" v-model="personaData.pers_correo"
                                    placeholder="Correo">

                            </div>
                            <button class="boton" @click="createNuevo()">Crear</button> &nbsp;
                            <a class="boton" onclick="history.back()">Volver</a>
                        </fieldset>
                    </form>
                </div>
            </div>

        </div>
        <div class="col-2"></div>
    </center>
</template>

<script>
import axios from 'axios'
export default {
    data() {
        return {
            personaData: { pers_nombre: '', pers_segundonombre: '', pers_apellido: '', pers_segundoapellido: '', pers_telefono: '', pers_correo: '' }
        }
    },
    methods: {
        createNuevo() {
            axios
                .post('http://127.0.0.1:8000/personas/create/', this.personaData)
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