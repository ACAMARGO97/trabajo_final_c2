<template>
    <div>
        <Form :factura="factura" :submit-data="submitData" />
    </div>
</template>

<script lang="ts">
import { } from "vue-router";
import { IFactura } from "../../../models/interfaces/facturainterfaces";
import Form from "../../UI/form.vue";

import { store } from "../../../context/store";

const factura: IFactura = {
    fact_nombre: '',
    fact_precio: '',
    tiposervicio: '',
};

export default {

    data() {
        return {
            factura: factura
        }
    },
    methods: {
        submitData(factura: IFactura) {
            store.commit('putFactura', { url: "http://localhost:8000/facturas/fupdate/" + this.$route.params.id + '/', data: factura });
            this.$router.push('/facturas/mine/');
        }
    },
    mounted() {
        this.$data.factura = store.state.verFactura.find((fac) => fac.id === Number(this.$route.params.id))!;
    },
    components: {
        Form
    }
}
</script>

<style>
</style>