<template>
  <div>


      <b-card no-body class="col-12 d-none d-md-block">

        <b-card-header class="row no-gutters align-items-center">
          <div class="col-2 cent">نام کاربری</div>
          <div class="col-2 cent">نوع ارز </div>
          <div class="col-2 cent">پرداختی ریالی</div>
          <div class="col-2 cent"> مقدار</div>
          <div class="col-2 cent">زمان ثبت</div>
          <div class="col-2 cent">عملیات</div>

        </b-card-header>

        <div v-for="section in requests" :key="section.title">
          <b-card-body v-if="section" class="py-3 wallets">

            <div class="row no-gutters align-items-center">
              <div class="col-2 cent">{{section.get_user}}</div>
              <div class="col-2 cent">{{section.currency}}</div>
              <div class="col-2 cent" style="font:12px 'arial'">{{section.ramount}}</div>
              <div class="col-2 cent" style="font:12px 'arial'">{{section.camount}}</div>
              <div class="col-2 cent">{{section.get_age}}</div>
              <div class="col-2 cent"><form @submit="accept(section.id)"><input required class="form-control" min="100000" :id="section.id" style="width:100%; float:left" type="number" placeholder=" قیمت تمام شده"><button type="submit" class="btn btn-success" style="width:100%; float:left">تایید</button></form></div>
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
              <b-card v-for="transaction in requests" v-bind:key="transaction" style="min-height:150px ; maring-bottom:10px ; padding:5px!important" class="row no-gutters align-items-center ">
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
              <h5  style=" height:50px ; text-align:left">{{transaction.get_age}}</h5><br>
              </div>
              <div class="col-12 cent"><form @submit.prevent="maccept(transaction.id)"><input required class="form-control" min="100000" :id="'m' +  transaction.id" style="width:100%; float:left" type="number" placeholder=" قیمت تمام شده"><button type="submit" class="btn btn-success" style="width:100%; float:left">تایید</button></form></div>
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
        .get('adminpanel/sell')
        .then(response => {
          this.requests = response.data
        })
    },
    async accept (id) {
      var amount = document.getElementById(id).value
      await axios
        .post('adminpanel/sell' , {id: id , act:'accept' , rramount: amount})
        .then(response => {
          this.getc()
        })
    },
    async maccept (id) {
      var amount = document.getElementById('m' + id).value
      await axios
        .post('adminpanel/sell' , {id: id , act:'accept' , rramount: amount})
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
