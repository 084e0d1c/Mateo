<template>
  <q-layout view="hHh lpR fFf">

    <q-header class="bg-white text-black" height-hint="98" v-show="this.$route.fullPath.includes('/loanDetails') == true || this.$route.fullPath.includes('/learn') == true || this.$route.fullPath.includes('/bankLoan') || this.$route.fullPath.includes('/loanPool') || this.$route.fullPath.includes('/loanContributionWithdrawal') ||this.$route.fullPath.includes('/bnpl') ">
      <q-toolbar>
         <q-btn v-if="!this.$route.fullPath.includes('/profile')"
        flat 
        dense 
        icon="eva-arrow-ios-back"
        @click="$router.go(-1)"
        />

        <q-toolbar-title class="absolute-center " style="font-weight:500">
          {{ title }}
        </q-toolbar-title>
      </q-toolbar>

     
    </q-header>


    <q-page-container>
      <router-view />
    </q-page-container>


    <q-footer  v-show="this.$route.fullPath != '/login' && this.$route.fullPath != '/signup' && this.$route.fullPath.includes('/loanDetails') != true && this.$route.fullPath.includes('/bankLoan') != true && this.$route.fullPath.includes('/bnpl') != true   " 
    style="border-top:1px solid lightgrey" >
      <q-tabs v-model="tab" class="text-grey-10 bg-white" active-color="primary" >
        <q-route-tab
          name="home"
          label="Home"
          icon="las la-home"
          class="q-py-sm"
          to="/home"
          
        />
        <q-route-tab
          name="Loans"
          label="loans"
          icon="las la-file-invoice-dollar"
          class="q-py-sm"
          to="/loans"
        />
        <q-route-tab
          name="Insurance"
          label="Insurance"
          icon="las la-shield-alt"
          class="q-py-sm"
          to="/insurance"
        />
       
        <q-route-tab
          name="Profile"
          label="Profile"
          icon="las la-user-circle"
          class="q-py-sm"
          to="/profile"
        />
      </q-tabs>
    </q-footer>



   
  </q-layout>
</template>

<script>
import EssentialLink from "components/EssentialLink.vue";
import router from 'src/router';

export default {
  name: "MainLayout",

  components: {
    EssentialLink,
  },
  data(){
    return{
      left: false,
      tab:'home'

    }
  },
  methods:{ 
  },
  computed: {
    
    title() {
      console.log(this.$route)
      let currentPath = this.$route.fullPath
      if (currentPath == '/home'){
        return 'Home'
      }else if (currentPath.includes('/loans')){
        return 'Loans'
      }else if (currentPath == '/resources'){
        return 'Resources'
      }else if (currentPath == '/profile'){
        return 'Profile'
      }else if (currentPath == '/signup'){
        return 'Sign Up'
      }else if (currentPath.includes('/loanDetails') || currentPath.includes('/loanPoolDetails') || currentPath.includes('/loanContributionWithdrawal')){
        return this.$route.params.loanName
      }else if (currentPath.includes('/bankLoan') || currentPath.includes('/loanPool') || currentPath.includes('/learn') || currentPath.includes('/QR') ){
        return this.$route.meta.header
      }
    }
  },
  mounted(){
    // change to login later
    this.$router.push('/login')

  }

  
  


};
</script>

<style lang="scss">
.tabsClass{
  font-size:5px
}


.searchPopup::-webkit-scrollbar {
  width: 5px;
}

.searchPopup::-webkit-scrollbar-track {
  border-radius:5px;
}

.searchPopup::-webkit-scrollbar-thumb {
  border-radius:5px;
  background-color:#7E96B8;
}

body::-webkit-scrollbar {
  width: 5px;
}

body::-webkit-scrollbar-track {
  // background: rgb(83, 109, 255);
  background-color: transparent;
  border-radius:5px;
}

body::-webkit-scrollbar-thumb {
  border-radius:5px;
  background-color:#445061;
}
  
</style>