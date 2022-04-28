import Layout2 from '@/layout/Layout2'
import adminLayout2 from '@/layout/adminLayout2'
import LayoutWithoutSidenav from '@/layout/LayoutWithoutSidenav'
import LayoutBlank from '@/layout/LayoutBlank'
import sampleLayout from '@/views/Pages/sampleLayout.vue';
import NotFound from '@/views/NotFoundPage.vue';
import AuthLayout from '@/views/Pages/AuthLayout.vue';

export default [{
  // Layout 2
    path: '/',
    redirect: '/',
    component: sampleLayout,
    children: [
      {
        path: '/',
        component: () => import(/* webpackChunkName: "demo" */ '../views/Index.vue')
      },
      {
        path: 'a',
        component: () => import(/* webpackChunkName: "demo" */ '../views/Index1.vue')
      },
      {
        path: 'b',
        component: () => import(/* webpackChunkName: "demo" */ '../views/Index2.vue')
      },
      {
        path: 'c',
        component: () => import(/* webpackChunkName: "demo" */ '../views/Index3.vue')
      },
      {
        path: 'd',
        component: () => import(/* webpackChunkName: "demo" */ '../views/Index4.vue')
      },
      {
        path: 'news',
        component: () => import(/* webpackChunkName: "demo" */ '../views/news.vue')
      },
      {
        path: 'pages/:page',
        component: () => import('../views/pages')
      }
    ]
  },
  {
    path: '/',
    redirect: '/',
    component: Layout2,
    children: [
      {
        path: '/dashboard',
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () => import(/* webpackChunkName: "demo" */ '../components/dashboards/Dashboard1.vue')
      },
    ]
  },
  {
    path: '/adminpanel',
    redirect: 'adminpanel/dashboard',
    component: adminLayout2,
    children: [
      {
        path: 'dashboard',
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () => import(/* webpackChunkName: "demo" */ '../components/dashboards/Dashboard2.vue')
      },
    ]
  },
  {
    path: '/',
    redirect: '/',
    component: Layout2,
    children: [
      {
        path: '/withdraw',
        component: () => import('@/components/pages/withdraw.vue')
      }, {
        path: 'ticketadd',
        component: () => import('@/components/pages/ticketadd')
      }, {
        path: 'buy/:symbol',
        component: () => import('@/components/pages/buy')
      }, {
        path: 'buy',
        component: () => import('@/components/pages/buy')
      }, {
        path: 'buyapp',
        component: () => import('@/components/pages/buyapp')
      }, {
        path: 'sell/:symbol',
        component: () => import('@/components/pages/sell')
      }, {
        path: 'sell',
        component: () => import('@/components/pages/sell')
      }, {
        path: 'buy-out',
        component: () => import('@/components/pages/buyout')
      }, {
        path: 'sell-out',
        component: () => import('@/components/pages/sellout')
      }, {
        path: 'exchange',
        component: () => import('@/components/pages/exchange')
      }, {
        path: 'ticket/:id',
        component: () => import('@/components/adminpages/ticket')
      }, {
        path: 'trades/:id',
        component: () => import('@/components/pages/Trades')
      }, {
        path: 'protrades/:id',
        component: () => import('@/components/pages/ProTrades')
      }, {
        path: 'fastorder',
        component: () => import('@/components/pages/fastorder')
      }, {
        path: 'deposit',
        component: () => import('@/components/pages/deposit')
      }, {
        path: 'margindeposit',
        component: () => import('@/components/pages/margindeposit')
      }, {
        path: 'perpetualdeposit',
        component: () => import('@/components/pages/perpetualdeposit')
      }, {
        path: 'addcard',
        component: () => import('@/components/pages/addcard')
      }, {
        path: '/wallets',
        component: () => import('@/components/pages/wallets')
      }, {
        path: '/cpwallets',
        component: () => import('@/components/pages/cpwallets')
      }, {
        path: '/wallets/1',
        component: () => import('@/components/pages/rial')
      }, {
        path: '/wallets/1/:place',
        component: () => import('@/components/pages/rial')
      }, {
        path: '/wallets/:id',
        component: () => import('@/components/pages/wallet')
      }, {
        path: '/wallets/:id/:place',
        component: () => import('@/components/pages/wallet')
      }, {
        path: '/cpwallets/:id',
        component: () => import('@/components/pages/cpwallet')
      }, {
        path: '/cpwallets/:id/:place',
        component: () => import('@/components/pages/cpwallet')
      }, {
        path: '/transactions',
        component: () => import('@/components/pages/transactions')
      }, {
        path: '/open-orders',
        component: () => import('@/components/pages/openorders')
      }, {
        path: '/open-orders-out',
        component: () => import('@/components/pages/openordersout')
      }, {
        path: '/history-out',
        component: () => import('@/components/pages/historyout')
      }, {
        path: '/history',
        component: () => import('@/components/pages/history')
      }, {
        path: 'user',
        component: () => import('@/components/pages/User')
      }, {
        path: 'user-level',
        component: () => import('@/components/pages/UserLevel')
      }, {
        path: 'user-security',
        component: () => import('@/components/pages/Usersecurity')
      }, {
        path: 'Messages',
        component: () => import('@/components/pages/MessagesV2Compose')
      }, {
        path: 'perpetualrequest',
        component: () => import('@/components/pages/perpetualrequest')
      }, 
    ]
  },
  {
    path: '/adminpanel',
    redirect: 'adminpanel/dashboard',
    component: adminLayout2,
    children: [{
      path: 'verifybank',
      component: () => import('@/components/adminpages/verifybank')
    }, {
      path: 'userlevel-settings',
      component: () => import('@/components/adminpages/userlevelsettings')
    }, {
      path: 'buy',
      component: () => import('@/components/adminpages/buy')
    }, {
      path: 'buydone',
      component: () => import('@/components/adminpages/buydone')
    }, {
      path: 'buyreject',
      component: () => import('@/components/adminpages/buyreject')
    }, {
      path: 'exchange',
      component: () => import('@/components/adminpages/exchange')
    }, {
      path: 'exchangedone',
      component: () => import('@/components/adminpages/exchangedone')
    }, {
      path: 'exchangereject',
      component: () => import('@/components/adminpages/exchangereject')
    }, {
      path: 'deposit',
      component: () => import('@/components/adminpages/deposit')
    }, {
      path: 'depositdone',
      component: () => import('@/components/adminpages/depositdone')
    }, {
      path: 'depositreject',
      component: () => import('@/components/adminpages/depositreject')
    }, {
      path: 'selldone',
      component: () => import('@/components/adminpages/selldone')
    }, {
      path: 'sellset',
      component: () => import('@/components/adminpages/sellset')
    }, {
      path: 'buy-out',
      component: () => import('@/components/adminpages/buyout')
    }, {
      path: 'sell-out',
      component: () => import('@/components/adminpages/sellout')
    }, {
      path: 'history-out',
      component: () => import('@/components/adminpages/outhistory')
    }, {
      path: 'open-orders-out',
      component: () => import('@/components/adminpages/outopen')
    }, {
      path: 'users/:id/ticketadd',
      component: () => import('@/components/adminpages/ticketadd')
    }, {
      path: 'main-page-top-stickers',
      component: () => import('@/components/adminpages/main-page-top-stickers')
    }, {
      path: 'main-page-bottom-stickers',
      component: () => import('@/components/adminpages/main-page-bottom-stickers')
    }, {
      path: 'main-page-posts',
      component: () => import('@/components/adminpages/main-page-posts')
    }, {
      path: 'main-page-bottom-sticker',
      component: () => import('@/components/adminpages/main-page-bottom-stickers')
    }, {
      path: 'main-page-top-sticker',
      component: () => import('@/components/adminpages/main-page-top-stickers')
    }, {
      path: 'other-pages',
      component: () => import('@/components/adminpages/other-pages')
    }, {
      path: 'details',
      component: () => import('@/components/adminpages/details')
    }, {
      path: 'transactions',
      component: () => import('@/components/adminpages/transactions')
    }, {
      path: 'profit',
      component: () => import('@/components/adminpages/profit')
    }, {
      path: 'cptransactions',
      component: () => import('@/components/adminpages/cptransactions')
    }, {
      path: 'profit',
      component: () => import('@/components/adminpages/transactions')
    }, {
      path: 'cwithdraw',
      component: () => import('@/components/adminpages/cwithdraw')
    }, {
      path: 'withdraw',
      component: () => import('@/components/adminpages/withdraw')
    }, {
      path: 'rcwithdraw',
      component: () => import('@/components/adminpages/rcwithdraw')
    }, {
      path: 'ccwithdraw',
      component: () => import('@/components/adminpages/ccwithdraw')
    }, {
      path: 'general-settings',
      component: () => import('@/components/adminpages/general')
    }, {
      path: 'verifymelli',
      component: () => import('@/components/adminpages/verifymelli')
    }, {
      path: 'verifyaccept',
      component: () => import('@/components/adminpages/verifyaccept')
    }, {
      path: 'verifybankaccount',
      component: () => import('@/components/adminpages/verifybankaccount')
    }, {
      path: 'verifyperpetual',
      component: () => import('@/components/adminpages/verifyperpetual')
    }, {
      path: 'verifyperpetual/:id',
      component: () => import('@/components/adminpages/verifyperpetualaccept')
    }, {
      path: 'users',
      component: () => import('@/components/adminpages/Users')
    }, {
      path: 'users/:id',
      component: () => import('@/components/adminpages/User')
    }, {
      path: 'tickets',
      component: () => import('@/components/adminpages/tickets')
    }, {
      path: 'tickets/:id',
      component: () => import('@/components/adminpages/ticket')
    }, {
      path: 'chats/:uri',
      component: () => import('@/components/pages/adminchats')
    }, {
      path: 'chats',
      component: () => import('@/components/adminpages/chats')
    }]
  },
  {
    path: '/',
    redirect: '',
    component: LayoutWithoutSidenav,
    children: [
      {
        path: '/adminpanel/login',
        component: () => import('@/components/adminpages/LogIn')
      },
      {
        path: 'contacts',
        component: () => import('@/components/pages/Contacts')
      }, 
      {
        path: 'aboutus',
        component: () => import('@/components/pages/aboutus')
      },
      {
        path: '/login',
        component: () => import('../views/Pages/Login.vue')
      },
      {
        path: '/forgetpassword',
        component: () => import('@/components/pages/ForgetPassword.vue')
      },
      {
        path: '/resetpass/:key',
        component: () => import('@/components/pages/ResetPass')
      },
      {
        path: '/success',
        component: () => import(/* webpackChunkName: "demo" */ '../views/success.vue')
      },
      {
        path: '/register',
        component: () => import(/* webpackChunkName: "demo" */ '../views/Pages/Register.vue')
      },
      {
        path: '/register/:id',
        component: () => import(/* webpackChunkName: "demo" */ '../views/Pages/RegisterInvited.vue')
      },
      {
        path: '/margin-trade/:sym',
        component: () => import(/* webpackChunkName: "demo" */ '@/components/pages/oltrade.vue')
      },
      {
        path: '/oltrade',
        component: () => import(/* webpackChunkName: "demo" */ '@/components/pages/oltrade.vue')
      },
      {
        path: '/perpetual-trade/:sym',
        component: () => import(/* webpackChunkName: "demo" */ '@/components/pages/olptrade.vue')
      },
      {
        path: 'logout',
        component: () => import(/* webpackChunkName: "demo" */ '@/components/pages/logout.vue')
      },
      { path: '*', component: NotFound }
    ]
  }
]