<template>
  <div>

    <h4 class="d-flex flex-wrap justify-content-between align-items-center pt-3 mb-4">
      <div class="col-12 col-md-3 p-0">
      </div>
    </h4>

    <div>
      <b-card no-body class="col-12 d-none d-md-block">
        <b-card-header class="row no-gutters align-items-center">
          <div class="col-1 ">ردیف</div>
          <div class="d-none d-md-block col-10 text-muted">
            <div class="row no-gutters align-items-center">
              <div class="col-3 cent">زمان</div>
              <div class="col-1 cent">نوع</div>
              <div class="col-2 cent">ارز </div>
              <div class="col-2 cent">مقدار </div>
              <div class="col-2 cent">قیمت </div>
            </div>
          </div>
        </b-card-header>

        <div>
          <b-card-body class="py-3">

            <div v-for="(item,idx) in sellmaintrades" v-bind:key="idx" class="row no-gutters align-items-center">
              <div class="col-1 ">{{idx+1}}</div>
              <div class="d-none d-md-block col-10">

                <div  class="row no-gutters align-items-center">
                  <div v-if="item.get_age !== ''" class="col-3 cent">{{item.get_age}}پیش</div>
                  <div v-if="item.get_age === ''" class="col-3 cent">لحظاتی پیش</div>
                  <div class="col-1 cent">فروش</div>
                  <div class="col-2 cent">{{item.currency}}</div>
                  <div class="col-2 cent">{{item.camount}} </div>
                  <div class="col-2 cent">{{item.ramount}} </div>
                </div>
              </div>
              <hr style="width:100%">
            </div>
            <div v-for="(item,idx) in buymaintrades" v-bind:key="idx" class="row no-gutters align-items-center">
              <div class="col-1 ">{{idx+1}}</div>
              <div class="d-none d-md-block col-10">

                <div  class="row no-gutters align-items-center">
                  <div v-if="item.get_age !== ''" class="col-3 cent">{{item.get_age}}پیش</div>
                  <div v-if="item.get_age === ''" class="col-3 cent">لحظاتی پیش</div>
                  <div class="col-1 cent">خرید</div>
                  <div class="col-2 cent">{{item.currency}}</div>
                  <div class="col-2 cent">{{item.camount}} </div>
                  <div class="col-2 cent">{{item.ramount}} </div>
                </div>
              </div>
              <hr style="width:100%">
            </div>
          </b-card-body>
        </div>

      </b-card>


      <b-card  class="d-md-none mob">
            <div>
              <b-card v-for="(item,idx) in sellmaintrades" v-bind:key="idx" style="min-height:150px; padding:0" class="row no-gutters align-items-center">
                <div style="width:45% ;float:right">
                  <h4 style=" height:50px " >زمان</h4>
                  <h4 style=" height:50px " >نوع</h4>
                  <h4 style=" height:50px " >ارز </h4>
                  <h4 style=" height:50px " >مقدار </h4>
                  <h4 style=" height:50px " >قیمت </h4>
                </div>
                <div style="width:45% ;float:left">
                  <h4 style=" height:50px ; text-align:left" v-if="item.get_age !== ''" >{{item.get_age}}پیش</h4>
                  <h4 style=" height:50px ; text-align:left" v-if="item.get_age === ''" >لحظاتی پیش</h4>
                  <h4 style=" height:50px ; text-align:left" >فروش</h4>
                  <h4 style=" height:50px ; text-align:left" >{{item.currency}}</h4>
                  <h4 style=" height:50px ; text-align:left" >{{item.camount}} </h4>
                  <h4 style=" height:50px ; text-align:left" >{{item.ramount}} </h4>
                </div>
              </b-card><br>
              <b-card v-for="(item,idx) in buymaintrades" v-bind:key="idx" style="min-height:150px; padding:0" class="row no-gutters align-items-center">
                <div style="width:45% ;float:right">
                  <h4 style=" height:50px " >زمان</h4>
                  <h4 style=" height:50px " >نوع</h4>
                  <h4 style=" height:50px " >ارز </h4>
                  <h4 style=" height:50px " >مقدار </h4>
                  <h4 style=" height:50px " >قیمت </h4>
                </div>
                <div style="width:45% ;float:left">
                  <h4 style=" height:50px ; text-align:left " v-if="item.get_age !== ''">{{item.get_age}}پیش</h4>
                  <h4 style=" height:50px ; text-align:left " v-if="item.get_age === ''">لحظاتی پیش</h4>
                  <h4 style=" height:50px ; text-align:left " >فروش</h4>
                  <h4 style=" height:50px ; text-align:left " >{{item.currency}}</h4>
                  <h4 style=" height:50px ; text-align:left " >{{item.camount}} </h4>
                  <h4 style=" height:50px ; text-align:left " >{{item.ramount}} </h4>
              
                </div>
              </b-card><br>
            </div>
            <div v-if="!buymaintrades.length && !sellmaintrades.length" class="cent">
              <h3>تراکنشی پیدا نشد</h3>
            </div>
      </b-card>
    </div>

  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'pages-forums-list',
  metaInfo: {
    title: 'Forum list - Pages'
  },
  data: () => ({
    sellmaintrades: [],
    buymaintrades: []
  }),
  mounted () {
    this.checklevel()
    this.getselltrades()
    this.getbuytrades()
  },
  methods: {
    async checklevel (id) {
      await axios
        .get('/userinfo')
        .then(response => {
          if (response.data[0].level === 0) {
            this.$swal.fire({
              title: 'توجه',
              text: 'برای استفاده از این بخش ابتدا احراز هویت را کامل کنید',
              icon: 'warning',
              showCancelButton: true,
              confirmButtonColor: '#3085d6',
              cancelButtonColor: '#d33',
              confirmButtonText: 'شروع تایید هویت',
              cancelButtonText: 'بعدا انجام میدهم'
            }).then(result => {
              if (result.isConfirmed) {
                const toPath = this.$route.query.to || '/user-level'
                this.$router.push(toPath)
              }else {
                const toPath = this.$route.query.to || '/dashboard'
                this.$router.push(toPath)
              }
            })
          }

        })
    },
    async getselltrades () {
      await axios
        .get('/sellhis')
        .then(data => {
          this.sellmaintrades = data.data
        })
    },
    async getbuytrades () {
      await axios
        .get('/buyhis')
        .then(data => {
          this.buymaintrades = data.data
        })
    }
  }
}
</script>
<style>
.cent{
  text-align: center;
}
.mob .card-body{
  padding:0;
  width:95%;
  margin:2.5%;
}
</style>
