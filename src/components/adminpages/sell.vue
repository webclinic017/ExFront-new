<template>
  <div>


      <b-card no-body class="col-12">

        <b-card-header class="row no-gutters align-items-center">
          <div class="col-2 cent">نام کاربری</div>
          <div class="col-1 cent">نوع ارز </div>
          <div class="col-2 cent">پرداختی ریالی</div>
          <div class="col-2 cent"> مقدار</div>
          <div class="col-2 cent">زمان ثبت</div>
          <div class="col-2 cent">عملیات</div>

        </b-card-header>

        <div v-for="section in requests" :key="section.title">
          <b-card-body class="py-3 wallets">

            <div class="row no-gutters align-items-center">
              <div class="col-2 cent">{{section.get_user}}</div>
              <div class="col-1 cent">{{section.currency}}</div>
              <div class="col-2 cent" style="font:12px 'arial'">{{section.ramount}}</div>
              <div class="col-3 cent" style="font:12px 'arial'">{{section.camount}}</div>
              <div class="col-2 cent">{{section.get_age}}</div>
              <div class="col-2 cent"><button @click="accept(section.id)" class="btn btn-success" style="width:100%; float:left">تایید</button><button @click="reject(section.id)" class="btn btn-danger " style="width:100%; float:left">رد</button></div>
            </div>

          </b-card-body>
        </div>

      </b-card>

  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'pages-forums-list',
  metaInfo: {
    title: 'کیف ها'
  },
  mounted () {
    this.getc()
  },
  data: () => ({
    requests: []
  }),
  forumPath: [
    { text: 'کیف ها', active: true }
  ],
  methods: {
    async getc () {
      await axios
        .get('adminpanel/sell')
        .then(response => {
          this.requests = response.data
        })
    },
    async accept (id) {
      await axios
        .post('adminpanel/sell' , {id: id , act:'accept'})
        .then(response => {
          this.getc()
        })
    },
    async reject (id) {
      await axios
        .post('adminpanel/sell' , {id: id , act:'reject'})
        .then(response => {
          this.getc()
        })
    },
  }
}

</script>
<style>
.cent{
  text-align: center;
}
.btnfont{
  font-size: 12px;
  padding: 9px;
  margin: 2px;
}
.wallets:hover{
  background: #efefff;
}
.left{
  float: left;
}
</style>
