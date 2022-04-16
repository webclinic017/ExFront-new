<template>
  <div>
    <h4 class="font-weight-bold py-3 mb-4">
      اطلاعات سایت  <span class="text-muted"></span>
    </h4>
    <b-card>
       <b-form-group label="">
            <label for="">مقدار درصدی افزایش قیمت دلار</label>
            <b-input v-model="USDTp" step="any" placeholder="درصد افزایش قیمت دلار"  class="mb-1 input-field" />
            <label for="">مقدار درصدی تفاوت تتر با باقی ارز ها</label>
            <b-input v-model="USDTp2" step="any" placeholder="مقدار درصدی تفاوت تتر با باقی ارز ها"  class="mb-1 input-field" />
            <div class="clear"></div>
        </b-form-group>
        <b-btn variant="dark" style="float:left" @click="submitusdtp">ثبت</b-btn>
    </b-card><br><br>

    <b-tabs class="nav-tabs-top nav-responsive-sm">
      <b-tab title=" تنظیمات کارمزد سطوح کاربری" active>
        <b-card-body>

        </b-card-body>
        <hr class="border-light m-0">
        <b-card-body class="pb-2">
          <div class="input-icons">
          <b-form-group >
            <label style="width:15%">سطح</label>
           <select v-model="id" @change="choose(id)" class="mb-1 input-field form-control" name="" id="">
             <option v-for="(item,idx) in levelfee" v-bind:key="idx" >{{item.id}}</option>
           </select>
            <div class="clear"></div>
          </b-form-group>
          <b-form-group >
            <label> خرید</label>
            <b-input v-model="buy" class="mb-1 input-field" />
            <div class="clear"></div>
          </b-form-group>

          <b-form-group >
            <label for="">فروش </label>
            <b-input v-model="sell" class="input-field"/>
            <div class="clear"></div>
          </b-form-group>

          <b-form-group label="">
            <label for="">پرپشوال  </label>
            <b-input v-model="perpetual"  class="input-field"/>
            <div class="clear"></div>
          </b-form-group>

          <b-form-group label="">
            <label for="">مرجین  </label>
            <b-input v-model="margin" maxlength="10" @input="ptoe()" class="mb-1 input-field" />
            <div class="clear"></div>
          </b-form-group>

          <b-form-group label="">
            <label for="">اکسچینج </label>
            <b-input v-model="exchange" maxlength="10"  @input="ptoe()" class="mb-1 input-field" />
            <div class="clear"></div>
          </b-form-group>
          </div>
           <b-btn variant="dark" style="float:left" @click="submit()">ثبت اطلاعات</b-btn>
           <div class="clear"></div>
        </b-card-body><br><br>
        <b-card-body class="pb-2">

        </b-card-body>
        <div class="table-responsive">
        </div>
      </b-tab>
    </b-tabs>

    <div class="text-right mt-3">
    </div>

    <h4 class="d-flex flex-wrap justify-content-between align-items-center pt-3 mb-4">
      <div class="col-12 col-md-3 p-0 ">
      </div>
    </h4>
      </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'pages-user-edit',
  metaInfo: {
    title: 'User edit - Pages'
  },
  data: () => ({
    id: '',
    buy : '',
    sell : '',
    USDTp: 0,
    USDTp2: 0,
    perpetual:'',
    margin:'',
    exchange:'',
    levelfee: []
  }),
  mounted () {
    this.get_general()
    this.getusdtp()
  },
  beforeCreate () {
    this.$store.commit('initializeStore')
    const token = this.$store.state.token
    if (token) {
      axios.defaults.headers.common.Authorization = 'Token ' + token
      this.$store.state.isAuthenticated = true
    } else {
      axios.defaults.headers.common.Authorization = ''
    }
  },
  methods: {
    async submitusdtp() {
      await axios
        .post('adminpanel/USDTP', {USDTp : this.USDTp , USDTp2 : this.USDTp2})
        .then(response => {
          this.USDTp = response.data
          this.$swal('<div class="swal2-header"><ul class="swal2-progress-steps" style="display: none;"></ul><div class="swal2-icon swal2-success swal2-icon-show" style="display: flex;"><div class="swal2-success-circular-line-left" style="background-color: rgb(255, 255, 255);"></div><span class="swal2-success-line-tip"></span> <span class="swal2-success-line-long"></span><div class="swal2-success-ring"></div> <div class="swal2-success-fix" style="background-color: rgb(255, 255, 255);"></div><div class="swal2-success-circular-line-right" style="background-color: rgb(255, 255, 255);"></div></div><img class="swal2-image" style="display: none;"><button type="button" class="swal2-close" aria-label="Close this dialog" style="display: none;">×</button></div>' + '<h5>ثبت اطاعات شما با موفقیت انجام شد . </h5>')
        })
        .catch(error => {
        })
    },
    async getusdtp() {
      await axios
        .get('adminpanel/USDTP')
        .then(response => {
          this.USDTp = response.data.USDTp
          this.USDTp2 = response.data.USDTp2
        })
        .catch(error => {
        })
    },
    checkadmin (){
      if (!this.$store.state.isAdmin){
            this.$swal.fire({
              title: 'توجه',
              text: 'شما به این بخش دسترسی ندارید',
              icon: 'warning',
              showCancelButton: true,
              confirmButtonColor: '#3085d6',
              cancelButtonColor: '#d33',
              confirmButtonText: 'ورود ادمین',
              cancelButtonText: 'بازگشت به صفحه اصلی'
            }).then(result => {
              if (result.isConfirmed) {
                const toPath = this.$route.go || '/adminpanel/login'
                this.$router.push(toPath)
              }else {
                const toPath = this.$route.query.to || '/'
                this.$router.push(toPath)
              }
            })
      }
    },
    async get_general () {
      await axios
        .get('adminpanel/levelfee')
        .then(response => {
          this.levelfee = response.data
        })
        .catch(error => {
        })
    },
    choose (id) {
          id = id-1
          this.buy = this.levelfee[id]['buy']
          this.sell = this.levelfee[id]['sell']
          this.perpetual = this.levelfee[id]['perpetual']
          this.margin = this.levelfee[id]['margin']
          this.exchange = this.levelfee[id]['exchange']
    },
    async submit () {
      this.errors = []
      const formData = {
        buy: this.buy,
        sell: this.sell,
        perpetual: this.perpetual,
        margin: this.margin,
        exchange: this.exchange,
        id: this.id,
      }
      await axios
        .post('adminpanel/levelfee', formData)
        .then(response => {
          this.$swal('<div class="swal2-header"><ul class="swal2-progress-steps" style="display: none;"></ul><div class="swal2-icon swal2-success swal2-icon-show" style="display: flex;"><div class="swal2-success-circular-line-left" style="background-color: rgb(255, 255, 255);"></div><span class="swal2-success-line-tip"></span> <span class="swal2-success-line-long"></span><div class="swal2-success-ring"></div> <div class="swal2-success-fix" style="background-color: rgb(255, 255, 255);"></div><div class="swal2-success-circular-line-right" style="background-color: rgb(255, 255, 255);"></div></div><img class="swal2-image" style="display: none;"><button type="button" class="swal2-close" aria-label="Close this dialog" style="display: none;">×</button></div>' + '<h5>ثبت اطاعات شما با موفقیت انجام شد . </h5>')
          this.get_general()
        })
        .catch(error => {
          if (error.response) {
            for (const property in error.response.data) {
              this.errors.push(`${property}: ${error.response.data[property]}`)
            }
          } else if (error.message) {
            this.errors.push(error.message)
          }
        })
    },
  }
}
</script>
<style>
.invalid-tooltip{
  position: relative;
  top:0;
  background-color: rgba(0, 0, 0, 0);
  color: red;
  text-align: left;
}
.input-icons i {
left:7%;
position: absolute;
}
.input-icons {
width: 100%;
margin-bottom: 10px;
}
.icon {
padding: 10px;
min-width: 40px;
}
.input-field {
width: 100%;
padding: 10px;
text-align: center;
}
label{
  width:15%;
}
.input-field{
  width: 85%;
  float: left;
}
.clear{
  clear: both;
}
</style>
