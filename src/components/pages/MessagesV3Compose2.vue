<template>
  <div>
    <div class="row">
      <h3 style="width:100%">تیکت ها</h3><br><br><br><br>
      <div style="clear:both"></div>
      <h4> موضوع : {{title}}</h4>
      <div v-for="item in tickets" v-bind:key="item" class="col-12">
        <b-card>
        <h5>{{item.get_user}}</h5>
        <h6>{{item.get_age}}</h6>
        <p>{{item.text}}</p>
        </b-card><br>
      </div>
      <div class="col-12">
        <b-card header-tag="h4" header-class="py-4">

          <b-form-group label="موضوع:">
            <b-input v-model="messageData.subject" />
          </b-form-group>

          <b-form-group class="mt-4" label="متن:">
            <!-- Fallback -->
            <b-textarea v-model="messageData.content" style="height: 150px"/>
          </b-form-group>

          <!-- Footer -->
          <div class="text-right mt-4">
            <b-btn variant="dark ml-2"><i class="ion ion-ios-paper-plane"></i>&nbsp; ارسال</b-btn>
          </div>
          <!-- / Footer -->

        </b-card>
      </div>
    </div><!-- / .row -->
  </div>
</template>

<style lang="scss">
  .ql-container.ql-snow {
    height: 400px;
  }
</style>

<script>
import axios from 'axios'
export default {
  name: 'pages-messages-v3-compose',
  metaInfo: {
    title: 'Compose message v3 - Pages'
  },
  components: {
  },
  data: () => ({
    tickets: [],
    title: '',
    // Message
    messageData: {
      subject: '',
      content: '',
      id: ''
    }
  }),
  mounted () {
    this.get()
  },
  methods: {
    async get () {
      const id = this.$route.params.id
      await axios
        .get(`/ticket/${id}`)
        .then(response => {
          this.tickets = response.data
          this.title = response.data[0].get_title
        })
        .catch(() => {
        })
    },
    async send () {
      const id = this.$route.params.id
      const formData = {
        text: this.messageData.text,
        subid: id
      }
      await axios
        .post('/ticket', formData)
        .then(response => {
          location.reload()
        })
        .catch(() => {
        })
    }
  }
}
</script>
