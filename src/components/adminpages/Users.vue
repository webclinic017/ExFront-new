<template>
  <div>


    <div>
      <b-card no-body class="col-12 d-none d-md-block">
        <b-card-header class="row no-gutters align-items-center">
          <b-input placeholder="search..." v-model="searchtxt" @input="search()"></b-input>
          <div class="col-1 ">ردیف</div>
          <div class="d-none d-md-block col-11 text-muted">
            <div class="row no-gutters align-items-center">
              <div class="col-1 cent">نام کاربری</div>
              <div class="col-1 cent">سطح</div>
              <div class="col-2 cent">دارایی ریالی</div>
              <div class="col-8 cent">ورود به پروفایل  </div>
            </div>
          </div>
        </b-card-header>

        <div>
          <b-card-body class="py-3">

            <div v-for="(item,idx) in users" v-bind:key="idx" class="row no-gutters align-items-center">
              <div class="col-1 ">{{item.id}}</div>
              <div class=" col-11">

                <div  class="row no-gutters align-items-center">
                  <div class="col-1 cent">{{item.username}}</div>
                  <div class="col-1 cent">{{item.level}}</div>
                  <div class="col-2 cent calibri">{{balance(parseInt(item.balance))}}</div>
                  <div class="col-8 cent">
                    <b-button v-if="item.is_active && !item.is_admin" variant="warning" @click="block(item.id)">مسدود کردن حساب</b-button>
                    <b-button v-if="!item.is_active && !item.is_admin" variant="light" @click="block(item.id)">فعال کردن حساب</b-button>
                    <b-button v-if="item.is_admin" disabled variant="dark" @click="block(item.id)">مدیر</b-button>
                    <router-link :to="'users/' + item.username" class="btn btn-success">ورود به پروفایل</router-link>
                    <router-link :to="'users/' + item.username + '/ticketadd'" class="btn btn-info">ارسال پیام</router-link>
                  </div>
                </div>
              </div>
              <hr style="width:100%">
            </div>
          </b-card-body>
        </div>

      </b-card>

      <div  class="d-md-none transm">
            <div v-if="users">
              <b-input placeholder="search..." v-model="searchtxt" @input="search()" style="margin-bottom:15px"></b-input><br>
              <b-card v-for="transaction in users" v-bind:key="transaction" style="min-height:150px ; maring-bottom:10px ; padding:5px!important" class="row no-gutters align-items-center">
                <div style="width:25% ;float:right">
                <h6  style=" height:50px ">نام</h6>
                <h6  style=" height:50px "> سطح</h6>
                <h6  style=" height:50px ">دارایی ریالی</h6>
                </div>
                <div style="width:65% ;float:left">
                <h4  style=" height:50px ; text-align:left">{{transaction.username}}</h4>
                <h4  style=" height:50px ; text-align:left">{{transaction.level}}</h4>
                <h4  style=" height:50px ; text-align:left">{{balance(parseInt(transaction.balance))}}</h4>
                </div>
                <div class="col-12 cent">
                  <b-button style="width:100% ; margin:0 ; margin-bottom:5px" v-if="transaction.is_active && !transaction.is_admin" variant="warning" @click="block(transaction.id)">مسدود کردن حساب</b-button>
                  <b-button style="width:100% ; margin:0 ; margin-bottom:5px" v-if="!transaction.is_active && !transaction.is_admin" variant="light" @click="block(transaction.id)">فعال کردن حساب</b-button>
                  <b-button style="width:100% ; margin:0 ; margin-bottom:5px" v-if="transaction.is_admin" disabled variant="dark" @click="block(transaction.id)">مدیر</b-button><br>
                  <router-link style="width:100% ; margin:0 ; margin-bottom:5px" :to="'users/' + transaction.username" class="btn btn-success">ورود به پروفایل</router-link><br>
                  <router-link style="width:100% ; margin:0 ; margin-bottom:15px" :to="'users/' + transaction.username + '/ticketadd'" class="btn btn-info">ارسال پیام</router-link><br><br>
                </div>
              </b-card><br>
            <div v-if="!users" class="cent">
              <h3>تراکنشی پیدا نشد</h3>
            </div>
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
    title: 'Forum list - Pages'
  },
  data: () => ({
    users: [],
    usersback: [],
    searchtxt: '',
  }),
  mounted () {
    this.getusers()
  },
  methods: {
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
    search(){
      this.users = []
      for (var item of this.usersback){
        if(item.username.includes(this.searchtxt) | item.id === this.searchtxt){
          this.users.push(item)
        }
      }
    },
    async getusers () {
      await axios
        .get('/adminpanel/users')
        .then(data => {
          this.users = data.data
          this.usersback = data.data
        })
    },
    async block (id) {
      await axios
        .post('/adminpanel/user', { act: 1, id: id })
        .then(() => {
          this.$swal('<div class="swal2-header"><ul class="swal2-progress-steps" style="display: none;"></ul><div class="swal2-icon swal2-success swal2-icon-show" style="display: flex;"><div class="swal2-success-circular-line-left" style="background-color: rgb(255, 255, 255);"></div><span class="swal2-success-line-tip"></span> <span class="swal2-success-line-long"></span><div class="swal2-success-ring"></div> <div class="swal2-success-fix" style="background-color: rgb(255, 255, 255);"></div><div class="swal2-success-circular-line-right" style="background-color: rgb(255, 255, 255);"></div></div><img class="swal2-image" style="display: none;"><button type="button" class="swal2-close" aria-label="Close this dialog" style="display: none;">×</button></div>' + '<h5>     انجام شد .</h5>')
          location.reload()
        })
    },
    balance (input) {
      if (String(input).length > 3) {
        var item = String(input)
        var last = item.length % 3
        var out = item.slice(0, last) + ','
        for (var i = 0; i < parseInt(item.length / 3) - 1; i++) {
          out = out + item.slice(last + (i * 3), last + ((i + 1) * 3)) + ','
        }
        out = out + item.slice(last + ((parseInt(item.length / 3) - 1) * 3), last + (((parseInt(item.length / 3) - 1) + 1) * 3))
        return out
      } else {
        return input
      }
    }
  }
}
</script>
<style>
.cent{
  text-align: center;
}
.calibri{
    font-family: 'calibri';
}
</style>
