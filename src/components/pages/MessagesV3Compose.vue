<template>
  <div>
    <div class="row">
      <h4 style="width:100%">تیکت ها</h4><br><br><br><br>
      <h4>ایجاد تیکت جدید</h4><br><br><br><br>
      <div class="col-12">
        <b-card header-tag="h4" header-class="py-4">

          <b-form-group label="موضوع:">
            <b-input v-model="messageData.subject" />
          </b-form-group>

          <b-form-group class="mt-4" label="متن:">
            <!-- Fallback -->
            <b-textarea v-model="messageData.content" style="height: 400px"/>
          </b-form-group>

          <!-- Footer -->
          <div class="text-right mt-4">
            <b-btn @click="send()" variant="dark ml-2"><i class="ion ion-ios-paper-plane"></i>&nbsp; ارسال</b-btn>
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
    // Message
    messageData: {
      subject: '',
      content: '',
      id: ''
    }
  }),
  mounted () {
  },
  methods: {
    async send () {
      const formData = {
        title: this.messageData.subject,
        text: this.messageData.content
      }
      await axios
        .post('/subject', formData)
        .then(response => {
          this.$router.push(`/ticket/${response.data.subid}`)
        })
        .catch(errors => {
        })
    }
  }
}
</script>
