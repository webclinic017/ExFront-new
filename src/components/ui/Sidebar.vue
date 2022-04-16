<template>
  <div>
    <h4 class="font-weight-bold py-3 mb-4">
      <span class="text-muted font-weight-light">UI elements /</span> Sidebar
    </h4>

    <hr class="container-m-nx border-light mt-0 mb-5">

    <b-button v-b-toggle.sidebar-left>Toggle Left Sidebar</b-button>
    <b-button v-b-toggle.sidebar-right>Toggle Right Sidebar</b-button>

    <b-sidebar id="sidebar-left" title="Sidebar" text-variant="body" class="theme-bg-white" shadow>
      <div class="py-2 px-3">
        <p>
          Cras mattis consectetur purus sit amet fermentum. Cras justo odio, dapibus ac facilisis
          in, egestas eget quam. Morbi leo risus, porta ac consectetur ac, vestibulum at eros.
        </p>
        <b-img :src="`${publicUrl}img/bg/4.jpg`" fluid thumbnail></b-img>
      </div>

      <template v-slot:footer="{ hide }">
       <div class="d-flex align-items-center bg-light py-2 px-3">
        <strong class="mr-auto">Footer</strong>
        <b-button size="sm" @click="hide">Close</b-button>
       </div>
      </template>
    </b-sidebar>

    <b-sidebar id="sidebar-right" right title="Sidebar" text-variant="body" class="theme-bg-white" shadow>
      <div class="py-2 px-3">
        <p>
          Cras mattis consectetur purus sit amet fermentum. Cras justo odio, dapibus ac facilisis
          in, egestas eget quam. Morbi leo risus, porta ac consectetur ac, vestibulum at eros.
        </p>
        <b-img :src="`${publicUrl}img/bg/4.jpg`" fluid thumbnail></b-img>
      </div>

      <template v-slot:footer="{ hide }">
       <div class="d-flex align-items-center bg-light py-2 px-3">
        <strong class="mr-auto">Footer</strong>
        <b-button size="sm" @click="hide">Close</b-button>
       </div>
      </template>
    </b-sidebar>

    <hr class="container-m-nx border-light my-4">
    <h6 class="text-muted small font-weight-bold py-3 mt-4 mb-2">
      Variants
    </h6>

    <b-form-select class="d-inline-block w-auto" v-model="sidebarVariant" :options="sidebarVariants"></b-form-select>
    <b-button v-b-toggle.sidebar-variant>Toggle Sidebar</b-button>

    <b-sidebar id="sidebar-variant" title="Sidebar" :bg-variant="sidebarVariant[0]" :text-variant="sidebarVariant[1]" shadow>
      <div class="py-2 px-3">
        <p>
          Cras mattis consectetur purus sit amet fermentum. Cras justo odio, dapibus ac facilisis
          in, egestas eget quam. Morbi leo risus, porta ac consectetur ac, vestibulum at eros.
        </p>
        <b-img :src="`${publicUrl}img/bg/4.jpg`" fluid thumbnail></b-img>
      </div>

      <template v-slot:footer="{ hide }">
       <div class="d-flex align-items-center bg-light py-2 px-3">
        <strong class="mr-auto">Footer</strong>
        <b-button size="sm" @click="hide">Close</b-button>
       </div>
      </template>
    </b-sidebar>
  </div>
</template>

<script>
const sidebarVariants = [
  { value: ['white', 'dark'], text: 'White bg / Dark text' },
  { value: ['dark', 'white'], text: 'Dark bg / White text' },
  { value: ['primary', 'white'], text: 'Primary bg / White text' },
  { value: ['secondary', 'white'], text: 'Secondary bg / White text' },
  { value: ['info', 'white'], text: 'Info bg / White text' },
  { value: ['warning', 'dark'], text: 'Warning bg / Dark text' },
  { value: ['danger', 'white'], text: 'Danger bg / White text' }
]

export default {
  name: 'ui-sidebar',
  metaInfo: {
    title: 'Sidebar - UI elements'
  },
  data: () => ({
    sidebarVariants,
    sidebarVariant: sidebarVariants[0].value
  })
}
</script>
