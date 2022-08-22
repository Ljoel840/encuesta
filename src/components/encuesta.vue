<template>
  <section>
    <div class="formulario">
      <h1 style="text-align: center">Formulario</h1>
      <div class="formInput">
        <label for="email" class="div1">Email:</label>
        <input name="email" type="mail" v-model="email" class="div2" />
      </div>
      <div class="formInput">
        <label>Edad:</label>
        <select v-model="age">
          <option v-for="(a, index) in rangeAge" :value="a.value" :key="index">
            {{ a.text }}
          </option>
        </select>
      </div>
      <div class="formInput">
        <label>Sexo:</label>
        <select v-model="gender">
          <option
            v-for="(s, index2) in rangeGender"
            :value="s.value"
            :key="index2"
          >
            {{ s.text }}
          </option>
        </select>
      </div>
      <div class="formInput">
        <label>Red Social Favorita:</label>
        <select v-model="socialmedia">
          <option
            v-for="(m, index3) in rangeFavorite"
            :value="m.value"
            :key="index3"
          >
            {{ m.text }}
          </option>
        </select>
      </div>
      <div class="formInput">
        <label for="whatsapp">Tiempo diario en Whatsapp (En Horas):</label>
        <input
          name="whatsapp"
          type="number"
          v-model="whatsapptime"
          min="0"
          max="24"
        />
      </div>
      <div class="formInput">
        <label for="whatsapp">Tiempo diario en Facebook (En Horas):</label>
        <input
          name="whatsapp"
          type="number"
          v-model="facebooktime"
          min="0"
          max="24"
        />
      </div>
      <div class="formInput">
        <label for="whatsapp">Tiempo diario en Twitter (En Horas):</label>
        <input
          name="whatsapp"
          type="number"
          v-model="twittertime"
          min="0"
          max="24"
        />
      </div>
      <div class="formInput">
        <label for="whatsapp">Tiempo diario en Instagram (En Horas):</label>
        <input
          name="whatsapp"
          type="number"
          v-model="instagramtime"
          min="0"
          max="24"
        />
      </div>
      <div class="formInput">
        <label for="whatsapp">Tiempo diario en Tiktok (En Horas):</label>
        <input
          name="whatsapp"
          type="number"
          v-model="tiktoktime"
          min="0"
          max="24"
        />
      </div>
      <div class="buttons">
        <button class="btn btnSend" @click="sendForm()">Enviar</button>
        <button class="btn btnCancel" @click="cancelForm()">Cancelar</button>
      </div>
      <div v-if="error" class="error">
        <p>{{ error }}</p>
      </div>
      <div v-if="mensaje" class="mensaje">
        <p>{{ mensaje }}</p>
      </div>
    </div>
  </section>
</template>
<script>
import enviar from "@/components/enviar";
export default {
  name: "Formulario_Encuesta",
  data() {
    return {
      email: "",
      age: "",
      gender: "",
      socialmedia: "",
      whatsapptime: 0,
      facebooktime: 0,
      twittertime: 0,
      instagramtime: 0,
      tiktoktime: 0,
      rangeAge: [
        { text: "18-25", value: "A" },
        { text: "26-33", value: "B" },
        { text: "34-40", value: "C" },
        { text: "40+", value: "D" },
      ],
      rangeGender: [
        { text: "Femenino", value: "A" },
        { text: "Masculino", value: "B" },
        { text: "No Contestar", value: "C" },
      ],
      rangeFavorite: [
        { text: "Whatsapp", value: "A" },
        { text: "Facebook", value: "B" },
        { text: "Twitter", value: "C" },
        { text: "Instagram", value: "D" },
        { text: "Tiktok", value: "E" },
        { text: "Otro", value: "F" },
      ],
      error: null,
      mensaje: null,
    };
  },
  methods: {
    sendForm() {
      this.error = null;
      if (!this.email || !this.age || !this.gender || !this.socialmedia) {
        this.error = "Complete los datos";
      } else {
        this.enviarFormulario();
        // this.postData();
      }
    },
    async enviarFormulario() {
      try {
        let formSend = await enviar({
          //   form: {
          email: this.email,
          age: this.age,
          gender: this.gender,
          socialmedia: this.socialmedia,
          whatsapptime: this.whatsapptime,
          facebooktime: this.facebooktime,
          twittertime: this.twittertime,
          instagramtime: this.instagramtime,
          tiktoktime: this.tiktoktime,
          //   },
        });
        if (formSend) {
          this.cancelForm();
          this.mensaje = "Formulario Enviado con exito";
        }
      } catch (error) {
        this.error = error;
        console.log("Error Envio:", this.error);
      }
    },
    cancelForm() {
      (this.email = ""),
        (this.age = ""),
        (this.gender = ""),
        (this.socialmedia = ""),
        (this.whatsapptime = 0),
        (this.facebooktime = 0),
        (this.twittertime = 0),
        (this.instagramtime = 0),
        (this.tiktoktime = 0);
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
.formulario {
  max-width: 400px;
  margin: auto;
  border: 1px solid rgb(214, 214, 214);
  border-radius: 10px;
  padding: 10px;
  box-shadow: 5px 5px 5px rgba(0, 0, 0, 0.2);
  background-color: rgb(247, 243, 243);
}
.formInput {
  padding: 5px;
  text-align: left;
  display: grid;
  grid-template-columns: auto 1fr;
  grid-template-rows: 1fr;
  grid-column-gap: 0px;
  grid-row-gap: 0px;
  justify-items: auto;
  justify-content: space-between;
  align-items: center;
}

.div1 {
  grid-area: 1 / 1 / 2 / 2;
}
.div2 {
  grid-area: 1 / 2 / 2 / 3;
}

input,
select {
  border-radius: 3px;
  border: 1px solid rgb(214, 214, 214);
  margin: 5px;
  padding: 5px;
  width: auto;
}

.btn {
  width: 80px;
  padding: 5px;
  border: none;
  margin: 10px;
  color: #ffffff;
  cursor: pointer;
  border-radius: 3px;
}
.btnSend {
  background: rgb(56, 184, 135);
}
.btnCancel {
  background: rgb(184, 56, 94);
}

.btnSend:hover,
.btnCancel:hover {
  background: #000000;
}
.error {
  color: #ff0000;
  font-size: 0.9em;
}
.mensaje {
  color: #04ce47;
  font-size: 0.9em;
}
</style>