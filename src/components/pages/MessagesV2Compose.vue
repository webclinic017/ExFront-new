<template>
  <div>

    <!-- Add `.messages-card` to `.card` -->
    <b-card no-body class="messages-card" :class="{'messages-sidebox-open': sideboxOpen}">
      <div class="row no-gutters">

        <!-- Messages list -->
        <div class="col">
          <b-card-body>

            <!-- Header -->
            <h4 class="m-0">
              <a @click.prevent="sideboxOpen = !sideboxOpen" href="#" class="messages-sidebox-toggler d-lg-none text-muted align-middle pr-3 mr-1"><i class="ion ion-md-more"></i></a>
              New message
            </h4>
            <hr class="my-4">
            <!-- / Header -->

            <b-form-group label="To:">
              <b-input v-model="messageData.to" />
            </b-form-group>

            <b-form-group label="Subject:">
              <b-input v-model="messageData.subject" />
            </b-form-group>

            <b-form-group class="mt-4">
              <quill-editor v-model="messageData.content" :options="editorOptions" v-if="!isIE10Mode" />
              <!-- Fallback -->
              <b-textarea v-model="messageData.content" style="height: 400px" v-if="isIE10Mode" />
            </b-form-group>

            <!-- Footer -->
            <div class="text-right mt-4">
              <b-btn variant="dark ml-2"><i class="ion ion-ios-paper-plane"></i>&nbsp; Send</b-btn>
              <b-btn variant="default ml-2"><i class="ion ion-md-save"></i>&nbsp; Save</b-btn>
              <b-btn variant="default ml-2">Cancel</b-btn>
            </div>
            <!-- / Footer -->

          </b-card-body>
        </div>
        <!-- / Messages list -->

      </div><!-- / .row -->
    </b-card>

  </div>
</template>


<style lang="scss">
  .ql-container.ql-snow {
    height: 400px;
  }
</style>

<script>

export default {
  name: 'pages-messages-v2-compose',
  metaInfo: {
    title: 'Compose message v2 - Pages'
  },
  data: () => ({
    sideboxOpen: false,

    // Mail boxes
    currentMailBox: null,
    mailBoxes: {
      inbox: { title: 'Inbox', icon: 'ion ion-ios-filing', count: 15 },
      sent: { title: 'Sent', icon: 'ion ion ion-ios-mail' },
      drafts: { title: 'Drafts', icon: 'ion ion ion-md-create' },
      spam: { title: 'Spam', icon: 'ion ion ion-md-folder-open' },
      trash: { title: 'Trash', icon: 'ion ion ion-md-trash' }
    },

    // Labels
    labels: {
      clients: { title: 'Clients', color: 'success' },
      important: { title: 'Important', color: 'danger' },
      social: { title: 'Social', color: 'info' },
      other: { title: 'Other', color: 'warning' }
    },

    // Message
    messageData: {
      to: '',
      subject: '',
      content: ''
    },

    // Editor
    editorOptions: {
      modules: {
        toolbar: [
          [{ header: [1, 2, 3, 4, 5, 6, false] }, { font: [] }, { size: [] }],
          ['bold', 'italic', 'underline', 'strike'],
          [{ color: [] }, { background: [] }],
          [{ script: 'sub' }, { script: 'super' }],
          ['blockquote', 'code-block'],
          [{ list: 'ordered' }, { list: 'bullet' }, { indent: '-1' }, { indent: '+1' }],
          [{ direction: 'rtl' }, { align: [] }],
          ['link', 'image', 'video'],
          ['clean']
        ]
      }
    }
  }),
  mounted () {
    this.layoutHelpers.setCollapsed(true, false)
  }
}
</script>
