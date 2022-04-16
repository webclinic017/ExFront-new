<template>
  <div>


      <b-card no-body class="col-12 d-none d-md-block">

        <b-card-header class="row no-gutters align-items-center">
          <div class="col-2 cent">نام کاربری</div>
          <div class="col-2 cent">نوع ارز </div>
          <div class="col-2 cent">پرداختی ریالی</div>
          <div class="col-2 cent"> مقدار</div>
          <div class="col-2 cent">زمان ثبت</div>

        </b-card-header>

        <div v-for="section in requests" :key="section.title">
          <b-card-body v-if="section" class="py-3 wallets">

            <div class="row no-gutters align-items-center">
              <div class="col-2 cent">{{section.get_user}}</div>
              <div class="col-2 cent">{{section.currency}}</div>
              <div class="col-2 cent" style="font:12px 'arial'">{{section.ramount}}</div>
              <div class="col-2 cent" style="font:12px 'arial'">{{section.camount}}</div>
              <div class="col-2 cent">{{section.get_age}}</div>
            </div>

          </b-card-body>
        </div>
        <div v-if="!requests">
          <b-card-body class="py-3 wallets">

            <div class="row no-gutters align-items-center">
              <div class="col-12 cent">موردی یافت نشد</div>
            </div>

          </b-card-body>
        </div>

      </b-card>
      <div  class="d-md-none transm">
            <div v-if="requests">
              <b-card v-for="transaction in requests" v-bind:key="transaction" style="min-height:150px ; maring-bottom:10px ; padding:5px!important" class="row no-gutters align-items-center">
                <div style="width:45% ;float:right">
              <h6  style=" height:50px ">نام</h6>
              <h6  style=" height:50px ">نوع ارز</h6>
              <h6  style=" height:50px ">پرداختی ریالی</h6>
              <h6  style=" height:50px ">مقدار </h6>
              <h6  style=" height:50px ">زمان ثبت </h6>
              </div>
              <div style="width:45% ;float:left">
              <h4  style=" height:50px ; text-align:left">{{transaction.get_user}}</h4>
              <h4  style=" height:50px ; text-align:left">{{transaction.currency}}</h4>
              <h4  style=" height:50px ; text-align:left">{{transaction.ramount}}</h4>
              <h4  style=" height:50px ; text-align:left">{{transaction.camount}}</h4>
              <h5  style=" height:50px ; text-align:left">{{transaction.get_age}}</h5>
              </div>
                  </b-card><br>
            <div v-if="!requests" class="cent">
              <h3>تراکنشی پیدا نشد</h3>
            </div>
            </div>
      </div>

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
        .get('adminpanel/exchangereject')
        .then(response => {
          this.requests = response.data
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
