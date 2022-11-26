
export interface IPersonas {
    id?: number;
    pers_nombre: string;
    pers_segundonombre: string;
    pers_apellido: string;
    pers_segundoapellido: string;
    pers_telefono: string;
    pers_correo: string;
    tiposexo: any;
    tipodocumento: any; 
  }
  
  export interface IEmpleado {
    id?: number;
    empl_nacionalidad: string;
    persona: any;
    tipoempleado: any;
  }
  
  export interface ICliente {
    id?: number;
    persona: any;
    clie_nacionalidad: string;
    tipocliente: any;
  }

