<template>
<div></div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'app-layout-navbar',
  props: {
    sidenavToggle: {
      type: Boolean,
      default: true
    }
  },
  mounted () {
    this.logout()
  },
  methods: {
    logout () {
      this.$router.push('/wallets')
    }
  }
}
</script>
