<template>
  <div>
    <h4 class="font-weight-bold py-3 mb-4">
      <span class="text-muted font-weight-light">UI elements /</span> Rating
    </h4>

    <hr class="container-m-nx border-light mt-0 mb-5">

    <b-form-rating v-model="rating" />

    <hr class="container-m-nx border-light my-4">
    <h6 class="text-muted small font-weight-bold py-3 mt-4 mb-2">
      Read-only
    </h6>

    <b-form-rating v-model="rating" readonly />

    <hr class="container-m-nx border-light my-4">
    <h6 class="text-muted small font-weight-bold py-3 mt-4 mb-2">
      Variants
    </h6>

    <b-form-rating v-model="rating" variant="warning" class="mb-2" />
    <b-form-rating v-model="rating" variant="success" class="mb-2" />
    <b-form-rating v-model="rating" variant="danger" class="mb-2" />
    <b-form-rating v-model="rating" variant="primary" class="mb-2" />
    <b-form-rating v-model="rating" variant="info" />

    <hr class="container-m-nx border-light my-4">
    <h6 class="text-muted small font-weight-bold py-3 mt-4 mb-2">
      Show value
    </h6>

    <b-form-rating v-model="rating" show-value show-value-max />

    <hr class="container-m-nx border-light my-4">
    <h6 class="text-muted small font-weight-bold py-3 mt-4 mb-2">
      Sizes
    </h6>

    <b-form-rating v-model="rating" size="sm" class="mb-2" />
    <b-form-rating v-model="rating" size="lg" />

    <hr class="container-m-nx border-light my-4">
    <h6 class="text-muted small font-weight-bold py-3 mt-4 mb-2">
      Number of stars
    </h6>

    <b-form-rating v-model="rating10" stars="10" />

    <hr class="container-m-nx border-light my-4">
    <h6 class="text-muted small font-weight-bold py-3 mt-4 mb-2">
      Inline
    </h6>

    <b-form-rating inline v-model="rating" />

    <hr class="container-m-nx border-light my-4">
    <h6 class="text-muted small font-weight-bold py-3 mt-4 mb-2">
      Borderless
    </h6>

    <b-form-rating v-model="rating" no-border class="bg-transparent" />
  </div>
</template>

<script>
export default {
  name: 'ui-rating',
  metaInfo: {
    title: 'Rating - UI elements'
  },
  data: () => ({
    rating: 4,
    rating10: 6
  })
}
</script>
