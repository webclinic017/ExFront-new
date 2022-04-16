<template>
  <div>
    <h4 class="font-weight-bold py-3 mb-4">
      <span class="text-muted font-weight-light">UI elements /</span> Avatars
    </h4>

    <hr class="container-m-nx border-light mt-0 mb-5">

    <b-avatar></b-avatar>
    <b-avatar variant="primary" text="BV"></b-avatar>
    <b-avatar variant="info" :src="`${publicUrl}img/avatars/4.png`"></b-avatar>
    <b-avatar variant="default"><span class="ion ion-md-contacts text-big"></span></b-avatar>

    <hr class="container-m-nx border-light my-4">
    <h6 class="text-muted small font-weight-bold py-3 mt-4 mb-2">
      Styling
    </h6>

    <b-avatar variant="default"></b-avatar>
    <b-avatar variant="secondary"></b-avatar>
    <b-avatar variant="primary"></b-avatar>
    <b-avatar variant="dark"></b-avatar>
    <b-avatar variant="light"></b-avatar>
    <b-avatar variant="success"></b-avatar>
    <b-avatar variant="danger"></b-avatar>
    <b-avatar variant="warning"></b-avatar>
    <b-avatar variant="info"></b-avatar>

    <hr class="container-m-nx border-light my-4">
    <h6 class="text-muted small font-weight-bold py-3 mt-4 mb-2">
      Sizing
    </h6>

    <b-avatar></b-avatar>
    <b-avatar size="sm"></b-avatar>
    <b-avatar size="lg"></b-avatar>
    <b-avatar :size="24"></b-avatar>
    <b-avatar size="3em"></b-avatar>
    <b-avatar size="72px"></b-avatar>

    <hr class="container-m-nx border-light my-4">
    <h6 class="text-muted small font-weight-bold py-3 mt-4 mb-2">
      Square
    </h6>

    <b-avatar square></b-avatar>

    <hr class="container-m-nx border-light my-4">
    <h6 class="text-muted small font-weight-bold py-3 mt-4 mb-2">
      Rounded
    </h6>

    <b-avatar rounded="sm"></b-avatar>
    <b-avatar rounded></b-avatar>
    <b-avatar rounded="lg"></b-avatar>
    <b-avatar rounded="top"></b-avatar>
    <b-avatar rounded="left"></b-avatar>
    <b-avatar rounded="right"></b-avatar>
    <b-avatar rounded="bottom"></b-avatar>

    <hr class="container-m-nx border-light my-4">
    <h6 class="text-muted small font-weight-bold py-3 mt-4 mb-2">
      Button
    </h6>

    <div>
      <b-avatar button variant="primary" text="FF" class="align-baseline"></b-avatar>
      Button Avatar
    </div>

    <hr class="container-m-nx border-light my-4">
    <h6 class="text-muted small font-weight-bold py-3 mt-4 mb-2">
      Link
    </h6>

    <div>
      <b-avatar href="javascript:void(0)" variant="info" :src="`${publicUrl}img/avatars/4.png`"></b-avatar>
      Link Avatar
    </div>
  </div>
</template>

<script>
export default {
  name: 'ui-avatars',
  metaInfo: {
    title: 'Avatars - UI elements'
  }
}
</script>
