<template>
    <nav class="navbar navbar-expand-lg bg-light">
        <div class="container-fluid">
          <a class="navbar-brand" href="#">Citas</a>
          <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav me-auto mb-2 mb-lg-0">
              <li class="nav-item">
                <router-link to="/facturas/all/" class="nav-link">
                    &nbsp;&nbsp;
                    <p style="cursor: pointer;"> Inicio </p>
                </router-link>
              </li>
              <li class="nav-item">
                <router-link to="/facturas" href="#" class="nav-link">
                    &nbsp;&nbsp;
                    <p> Facturas <i class="right fas fa-angle-left"></i></p>
                </router-link>
              </li>
              <li class="nav-item">
                <router-link to="/personas" href="#" class="nav-link">
                    &nbsp;&nbsp;
                    <p> Personas <i class="right fas fa-angle-left"></i></p>
                </router-link>
              </li>
              <li class="nav-item">
                <router-link to="/agenda" href="#" class="nav-link">
                    &nbsp;&nbsp;
                    <p> Agenda <i class="right fas fa-angle-left"></i></p>
                </router-link>
              </li>
              <li class="nav-item">
                <router-link to="/consulta" href="#" class="nav-link">
                    &nbsp;&nbsp;
                    <p> Consultas <i class="right fas fa-angle-left"></i></p>
                </router-link>
              </li>
            </ul>
          </div>
        </div>
      </nav>
</template>

<script lang="ts" scope>
export default {
    data() {
        return {
            display: false
        }
    },
    methods: {
        changeDisplay() {
            this.display = !this.display;
        }
    }
}
</script>

<style scoped lang="scss">
</style>