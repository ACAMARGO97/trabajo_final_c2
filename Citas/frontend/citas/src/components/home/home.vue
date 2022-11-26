<template>
    <div>
        <Search />
    </div>
    <div class="alert alert-dismissible alert-warning">
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
        <h4 class="alert-heading">Citas !!</h4>
        <p class="mb-0">Aparta tu cita para cortrte el cabello, planchado y mucho mas...</p>
    </div>

</template>

<script lang="ts" >
import { store } from '../../context/store';
import verfactura from '../factura/ver/verfactura.vue';
import Search from '../UI/search.vue';

export default {
    data() {
        return {
            factura: [...store.state.factura]
        }
    },
    mounted() {
        store.commit('getAllFactura', "http://127.0.0.1:8000/facturas/fall/")
    },
    components: {
        Search,
        verfactura
    },
}
</script>

<style scoped lang="scss">

</style>