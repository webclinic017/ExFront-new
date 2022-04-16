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
      axios.defaults.headers.common.Authorization = ''
      localStorage.removeItem('token')
      localStorage.removeItem('admin')
      localStorage.removeItem('username')
      localStorage.removeItem('userid')
      localStorage.removeItem('admin')
      this.$store.isAdmin = false
      this.$store.commit('removeAdmin')
      this.$store.commit('removeToken')
      this.$router.push('/login')
    }
  }
}
</script>
