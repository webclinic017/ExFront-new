<template style="width:100%">
        <div class="navbar-collapse-header">
          <b-row>
            <b-col cols="6" class="collapse-close">
            </b-col>
          </b-row>
        </div>
        <b-navbar-brand to="/">
          <img class="d-none d-md-block " style="width:40px; height:50px" src="/img/brand/ars.png">
        </b-navbar-brand>
      <b-navbar-nav style="text-align:center"  class="align-items-lg-center ml-lg-auto" >

           <b-nav-item to="/news">
               <span class="nav-link-inner--text" style="color:#cecece"> اخبار </span>
           </b-nav-item>
           <b-nav-item to="/margin-trade/BTCUSDT">
               <span class="nav-link-inner--text" style="color:#cecece"> بازار مارجین </span>
           </b-nav-item>
           <b-nav-item to="/perpetual-trade/BTCUSDT">
               <span class="nav-link-inner--text" style="color:#cecece">بازار پرپشوال</span>
           </b-nav-item>
           <b-nav-item to="/wallets">
               <span class="nav-link-inner--text" style="color:#cecece">کیف های من </span>
           </b-nav-item>
           <b-nav-item to="/aboutus">
               <span class="nav-link-inner--text" style="color:#cecece">  درباره ما </span>
           </b-nav-item>
       </b-navbar-nav>
        <b-navbar-nav style="margin-right"  class="align-items-lg-center mr-lg-auto">
          <b-nav-item v-if="this.$store.state.isAuthenticated" to="/dashboard">
               <span class="nav-link-inner--text btn btn-light" style="background: none; padding: 7px 15px; color: #fff"> داشبورد </span>
           </b-nav-item>
           <b-nav-item v-if="this.$store.state.isAuthenticated" to="/logout">
               <span class="nav-link-inner--text btn btn-light" style="background: none; padding: 7px 15px; color: #fff"> خروج </span>
           </b-nav-item>
           <b-nav-item v-if="!this.$store.state.isAuthenticated" to="/register">
               <span class="nav-link-inner--text btn btn-light" style="background: none; padding: 7px 15px; color: #777"> ثبت نام </span>
           </b-nav-item>
           <b-nav-item v-if="!this.$store.state.isAuthenticated" to="/login" style="float:left">
               <span class="nav-link-inner--text btn btn-light" style="background: none; padding: 7px 15px; color: #777; margin-left:30px"> ورود </span>
           </b-nav-item>
       </b-navbar-nav>
       
     </template>