<template>
  <div>
    <h4 class="font-weight-bold py-3 mb-4">
      <span class="text-muted font-weight-light">UI elements /</span> Vue Plyr
    </h4>

    <hr class="container-m-nx border-light mt-0">

    <div class="alert alert-danger" v-if="isIE10Mode">
      Plyr doesn't support IE10.
    </div>

    <div v-if="!isIE10Mode">
      <h5 class="font-weight-bold pt-1 pb-1 mt-4 mb-4">Video</h5>

      <vue-plyr>
        <div data-plyr-provider="youtube" data-plyr-embed-id="bTqVqk7FSmY"></div>
      </vue-plyr>

      <hr class="container-m-nx border-light my-4">

      <h5 class="font-weight-bold pt-1 pb-1 mb-4">Audio</h5>

      <vue-plyr>
        <audio controls>
          <source :src="`${publicUrl}audio/Water_Lily.mp3`" type="audio/mp3">
        </audio>
      </vue-plyr>
    </div>

  </div>
</template>

<style src="@/vendor/libs/vue-plyr/vue-plyr.scss" lang="scss"></style>

<script>
import VuePlyr from 'vue-plyr'

export default {
  name: 'ui-vue-plyr',
  metaInfo: {
    title: 'Vue Plyr - UI elements'
  },
  components: {
    VuePlyr
  }
}
</script>
