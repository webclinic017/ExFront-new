<template>
  <div>


      <b-card no-body class="col-12"><br>
        <h2>خرید</h2>
        <b-card-header class="row no-gutters align-items-center">
          <div class="col-2 cent">سمت </div>
          <div class="col-2 cent">نام کاربری</div>
          <div class="col-1 cent">نوع ارز </div>
          <div class="col-2 cent">پرداختی ریالی</div>
          <div class="col-3 cent"> مقدار</div>
          <div class="col-2 cent">زمان ثبت</div>

        </b-card-header>

        <div v-for="section in requestsbuy" :key="section.title">
          <b-card-body class="py-3 wallets">

            <div class="row no-gutters align-items-center">
              <div v-if="String(section.act) === '0'" style="color:yellow" class="col-2 cent alert alert-secondary">{{String(section.act).replace('0','در حال پیگیری').replace('2','انجام شده').replace('1','رد شده')}}</div>
              <div v-if="String(section.act) === '2'" style="color:green" class="col-2 cent alert alert-secondary">{{String(section.act).replace('0','در حال پیگیری').replace('2','انجام شده').replace('1','رد شده')}}</div>
              <div v-if="String(section.act) === '1'" style="color:red" class="col-2 cent alert alert-secondary">{{String(section.act).replace('0','در حال پیگیری').replace('2','انجام شده').replace('1','رد شده')}}</div>
              <div class="col-2 cent">{{section.get_user}}</div>
              <div class="col-1 cent">{{section.currency}}</div>
              <div class="col-2 cent" style="font:12px 'arial'">{{section.ramount}}</div>
              <div class="col-3 cent" style="font:12px 'arial'">{{section.camount}}</div>
              <div class="col-2 cent">{{section.get_age}}</div>
            </div>
            <div class="row no-gutters align-items-center" style="margin:0;margin-top:15px">
              <div class="col-2 cent">آدرس:</div>
              <div class="col-10 cent"> <input class="form-control" type="text" readonly :value="section.address" ></div>
            </div>
                   
              <hr style="margin:0;margin-top:15px">
          </b-card-body>
        </div>
        <div class="row no-gutters align-items-center" style="margin:0;margin-top:15px">
            <div v-if="!requestsbuy.length" class="col-12 cent"> <h2>موردی یافت نشد</h2></div>
            </div>   

      </b-card>


<br><br>
      <b-card no-body class="col-12"><br>
        <h2>فروش</h2>

        <b-card-header class="row no-gutters align-items-center">
          <div class="col-2 cent">سمت </div>
          <div class="col-2 cent">نام کاربری</div>
          <div class="col-1 cent">نوع ارز </div>
          <div class="col-2 cent">پرداختی ریالی</div>
          <div class="col-3 cent"> مقدار</div>
          <div class="col-2 cent">زمان ثبت</div>

        </b-card-header>

        <div v-for="section in requestssell" :key="section.title">
          <b-card-body class="py-3 wallets">

            <div class="row no-gutters align-items-center">
              <div v-if="String(section.act) === '0'" style="color:yellow" class="col-2 cent alert alert-secondary">{{String(section.act).replace('0','در حال پیگیری').replace('2','انجام شده').replace('1','رد شده')}}</div>
              <div v-if="String(section.act) === '2'" style="color:green" class="col-2 cent alert alert-secondary">{{String(section.act).replace('0','در حال پیگیری').replace('2','انجام شده').replace('1','رد شده')}}</div>
              <div v-if="String(section.act) === '1'" style="color:red" class="col-2 cent alert alert-secondary">{{String(section.act).replace('0','در حال پیگیری').replace('2','انجام شده').replace('1','رد شده')}}</div>
              <div class="col-2 cent">{{section.get_user}}</div>
              <div class="col-1 cent">{{section.currency}}</div>
              <div class="col-2 cent" style="font:12px 'arial'">{{section.ramount}}</div>
              <div class="col-3 cent" style="font:12px 'arial'">{{section.camount}}</div>
              <div class="col-2 cent">{{section.get_age}}</div>
            </div>
            <div class="row no-gutters align-items-center" style="margin:0;margin-top:15px">
              <div class="col-2 cent">هش:</div>
              <div class="col-10 cent"> <input class="form-control" type="text" readonly :value="section.hash" ></div>
            </div>
            

            <hr style="margin:0;margin-top:15px">
          </b-card-body>
        </div>
        <div class="row no-gutters align-items-center" style="margin:0;margin-top:15px">
            <div v-if="!requestssell.length" class="col-12 cent"> <h2>موردی یافت نشد</h2></div>
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
    this.getd()
  },
  data: () => ({
    requests: [],
    requestsbuy: [],
    requestssell: []
  }),
  forumPath: [
    { text: 'کیف ها', active: true }
  ],
  methods: {
    async getc () {
      await axios
        .get('adminpanel/buyouthistory')
        .then(response => {
          this.requestsbuy = response.data
        })
    },
    async getd () {
      await axios
        .get('adminpanel/sellouthistory')
        .then(response => {
          this.requestssell = response.data
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
