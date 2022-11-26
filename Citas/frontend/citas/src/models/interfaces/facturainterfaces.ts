export interface IFactura {
    id?: number;
    fact_nombre: string;
    fact_precio: string;
    tiposervicio: any;
  }

  export interface Iagenda {
    id?: number;
    agen_numero: string;
    agen_fecha: string;
    cliente: any;
    empleado: any;
    factura: any;
  }