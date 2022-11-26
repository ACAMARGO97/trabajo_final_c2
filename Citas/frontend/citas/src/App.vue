<script setup lang="ts">
import SideBar from './components/UI/sideBar.vue';
components: {
  SideBar
}
</script>

<template>
  <div class="container-main">
    <div class="sidebar">
      <SideBar />
    </div>
    <div class="main">
      <router-view></router-view>
    </div>
  </div>
</template>

<style scoped lang="scss">
</style>