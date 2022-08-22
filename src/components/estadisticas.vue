<template>
  <section>
    <div class="contenedor">
      <h1 style="text-align: center">Formulario</h1>
      <div v-if="data">
        <h3>Total Encuestados: {{ data.totalencuesta }}</h3>
        <div>
          <h3>Red Social Favorita:</h3>
          <h3 v-for="(f, index) in favorita" :key="index">- {{ f }}</h3>
        </div>
        <h3>
          Tiempo Promedio en Whatsapp:
          {{
            data.whatsapp.total > 0
              ? data.whatsapp.suma / data.whatsapp.total
              : 0
          }}
          hs
        </h3>
        <h3>
          Tiempo Promedio en Facebook:
          {{
            data.facebook.total > 0
              ? data.facebook.suma / data.facebook.total
              : 0
          }}
          hs
        </h3>
        <h3>
          Tiempo Promedio en Twitter:
          {{
            data.twitter.total > 0 ? data.twitter.suma / data.twitter.total : 0
          }}
          hs
        </h3>
        <h3>
          Tiempo Promedio en Instagram:
          {{
            data.instagram.total > 0
              ? data.instagram.suma / data.instagram.total
              : 0
          }}
          hs
        </h3>
        <h3>
          Tiempo Promedio en Tiktok:
          {{ data.tiktok.total > 0 ? data.tiktok.suma / data.tiktok.total : 0 }}
          hs
        </h3>
        <div>
          <h3>Red Social Menos Querida:</h3>
          <h3 v-for="(f, index2) in menosFavorita" :key="index2">- {{ f }}</h3>
        </div>
        <div>
          <h3>Rango de edad que más usa Whatsapp:</h3>
          <h3 v-for="(r, indexw) in rangoWhatsapp" :key="indexw">- {{ r }}</h3>
        </div>
        <div>
          <h3>Rango de edad que más usa Facebook:</h3>
          <h3 v-for="(r, indexf) in rangoFacebook" :key="indexf">- {{ r }}</h3>
        </div>
        <div>
          <h3>Rango de edad que más usa Twitter:</h3>
          <h3 v-for="(r, indext) in rangoTwitter" :key="indext">- {{ r }}</h3>
        </div>
        <div>
          <h3>Rango de edad que más usa Instagram:</h3>
          <h3 v-for="(r, indexi) in rangoInstagram" :key="indexi">- {{ r }}</h3>
        </div>
        <div>
          <h3>Rango de edad que más usa TikTok:</h3>
          <h3 v-for="(r, indexk) in rangoTiktok" :key="indexk">- {{ r }}</h3>
        </div>
      </div>
    </div>
  </section>
</template>
<script>
import extraer from "@/components/extraer";
export default {
  name: "Estadisticas_Encuesta",
  data() {
    return {
      data: null,
      error: null,
      rangoWhatsapp: [],
      rangoFacebook: [],
      rangoTwitter: [],
      rangoInstagram: [],
      rangoTiktok: [],
      favorita: [],
      menosFavorita: [],
    };
  },
  created() {
    this.extraerDatos();
  },
  methods: {
    async extraerDatos() {
      try {
        let datos = await extraer();
        this.data = datos;
        console.log(datos);
        if (datos) {
          this.rangoWhatsapp = this.mayor(
            this.data.whatsapp.edadA,
            this.data.whatsapp.edadB,
            this.data.whatsapp.edadC,
            this.data.whatsapp.edadD
          );
          this.rangoFacebook = this.mayor(
            this.data.facebook.edadA,
            this.data.facebook.edadB,
            this.data.facebook.edadC,
            this.data.facebook.edadD
          );
          this.rangoTwitter = this.mayor(
            this.data.twitter.edadA,
            this.data.twitter.edadB,
            this.data.twitter.edadC,
            this.data.twitter.edadD
          );
          this.rangoInstagram = this.mayor(
            this.data.instagram.edadA,
            this.data.instagram.edadB,
            this.data.instagram.edadC,
            this.data.instagram.edadD
          );
          this.rangoTiktok = this.mayor(
            this.data.tiktok.edadA,
            this.data.tiktok.edadB,
            this.data.tiktok.edadC,
            this.data.tiktok.edadD
          );
          this.favorita = this.buscarFavorita(
            this.data.whatsapp.favorite,
            this.data.facebook.favorite,
            this.data.twitter.favorite,
            this.data.instagram.favorite,
            this.data.tiktok.favorite,
            "mayor"
          );
          this.menosFavorita = this.buscarFavorita(
            this.data.whatsapp.favorite,
            this.data.facebook.favorite,
            this.data.twitter.favorite,
            this.data.instagram.favorite,
            this.data.tiktok.favorite,
            "menor"
          );
        }
      } catch (error) {
        this.error = error;
        console.log("Error Envio:", this.error);
      }
    },
    mayor(dato1, dato2, dato3, dato4) {
      let mayor = Math.max(dato1, dato2, dato3, dato4);
      let rango = [];
      if (mayor > 0) {
        if (dato1 == mayor) {
          rango.push("18-25");
        }
        if (dato2 == mayor) {
          rango.push("26-33");
        }
        if (dato3 == mayor) {
          rango.push("34-40");
        }
        if (dato4 == mayor) {
          rango.push("+40");
        }
      }
      return rango;
    },
    buscarFavorita(dato1, dato2, dato3, dato4, dato5, comparacion) {
      let comparar = 0;
      let fav = [];
      if (comparacion == "mayor") {
        comparar = Math.max(dato1, dato2, dato3, dato4, dato5);
      } else {
        comparar = Math.min(dato1, dato2, dato3, dato4, dato5);
      }
      console.log("Comparar:" + comparar);
      if ((comparacion == "mayor" && comparar > 0) || comparacion == "menor") {
        if (dato1 == comparar) {
          fav.push("Whatsapp");
        }
        if (dato2 == comparar) {
          fav.push("Facebook");
        }
        if (dato3 == comparar) {
          fav.push("Twitter");
        }
        if (dato4 == comparar) {
          fav.push("Instagram");
        }
        if (dato5 == comparar) {
          fav.push("TikTok");
        }
      }
      return fav;
    },
  },
};
</script>
<style scoped>
section {
  background-color: rgba(0, 0, 0, 0.2);
  min-height: 70vh;
  padding: 3em;
  display: flex;
  align-items: center;
  justify-content: center;
}
h3 {
  font-size: 0.9em;
  text-align: left;
}
.contenedor {
  max-width: 400px;
  min-width: 300px;
  margin: auto;
  border: 1px solid rgb(214, 214, 214);
  border-radius: 10px;
  padding: 10px;
  box-shadow: 5px 5px 5px rgba(0, 0, 0, 0.2);
  background-color: rgb(247, 243, 243);
}
</style>