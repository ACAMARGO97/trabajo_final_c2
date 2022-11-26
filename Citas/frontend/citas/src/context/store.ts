import axios from "axios";
import { createStore } from "vuex";
import { IFactura } from "../models/interfaces/facturainterfaces";

const factura: IFactura[] = [];
const verFactura: IFactura[] = [];

export const store = createStore({
  state() {
    return {
        factura,
        verFactura,
    };
  },
  mutations: {
    async getAllFactura(state, url: string) {
      try {
        const resp = await axios.get(url);
        state.factura = [...resp.data];
      } catch (error) {
        console.log(error);
      }
    },
    async postfactura(state, data: IFactura) {
      try {
        await axios.post("http://127.0.0.1:8000/facturas/fcreate/", data);
        state.factura.push(data);
      } catch (error) {
        console.log(error);
      }
    },
    async getFactura(state, url: string) {
      try {
        const resp = await axios.get(url);
        state.verFactura = [...resp.data];
      } catch (error) {
        console.log(error);
      }
    },
    async putFactura(state, props: { url: string; data: IFactura }) {
      try {
        await axios.put(props.url, props.data);
      } catch (error) {
        console.log(error);
      }
    },
  },
});