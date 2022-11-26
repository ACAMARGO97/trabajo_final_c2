import { createRouter, createWebHistory } from "vue-router";
import Home from "../components/home/home.vue";
import verPersona from "../components/factura/ver/verPersonas.vue";
import verAgenda from "../components/factura/ver/verAgenda.vue";

import consulta from "../components/consultas/consulta.vue";
import consulta1 from "../components/consultas/consulta1.vue";
import consulta2 from "../components/consultas/consulta2.vue";
import consulta3 from "../components/consultas/consulta3.vue";

import NuevaPersona from "../components/factura/register/registerPersona.vue";
import NuevaFactura from "../components/factura/register/register.vue";

const verFactura = () =>
  import("../components/factura/ver/verfactura.vue");

const updateFactura = () => 
  import('../components/factura/edit/editfactura.vue');

const routes = [
  { path: "/facturas/all/", component: Home },

  { path: "/facturas", component: verFactura },
  { path: "/personas", component: verPersona },
  { path: "/agenda", component: verAgenda },

  { path: "/consulta", component: consulta },
  { path: "/consulta1", component: consulta1 },
  { path: "/consulta2", component: consulta2 },
  { path: "/consulta3", component: consulta3 },

  { path: "/nuevapersona", component: NuevaPersona },
  { path: "/nuevafactura", component: NuevaFactura },
  { path: "/facturas/update/:id", component: updateFactura, name: "updateFac",},
];

const history = createWebHistory();
const router = createRouter({
  history,
  routes,
});

export default router;