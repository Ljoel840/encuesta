<template>
  <div class="home">
    <encuesta/>
  </div>
</template>

<script>
// @ is an alias to /src
import encuesta from '@/components/encuesta.vue'

export default {
  name: 'HomeView',
  components: {
    encuesta
  }
}
</script>
