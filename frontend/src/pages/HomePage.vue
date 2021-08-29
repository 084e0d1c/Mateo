<template>
  <q-page class="q-pa-md" style=""> 

    <!-- <div class="flex" @click="$router.push('/profile')">
      <div class="" style="width:15vw;">
         <img src="~assets/profilePic2.jpg" alt="" style="width:100%;border-radius:100%">
      </div>
     

      <div class="q-ml-md flex column justify-center">
        <div class="" style="font-size:5.5vw;font-weight:500">Greg G Tan</div>
        <div class="" style="color:#5B7282; font-size:3.5vw; font-weight:500">Member since Aug 2020</div>
      </div>

    </div> -->
    <div class="flex justify-center items-center q-mb-md">
      
    <img src="~assets/logo.svg" alt="">
    </div>


    <div class="flex justify-center items-center no-wrap">
      <div class="q-mt-md q-pa-md flex items-center justify-center no-wrap"  style="background:#3E5463; color:#F2F5F7;width:50vw; border-radius:5px; height:22vh ">
        <div class="">
          <div class="" style="font-size:3.5vw">Bank Balance</div>
        <div class="flex items-center q-mt-xs">
          <div class="" style="font-size:4.5vw">SGD</div>
          <div class="q-ml-xs" style="font-size:6.5vw"><animated-number :value="bankBalance" :formatValue="formatToPrice" :duration="duration"/></div>
        </div>

        <q-separator style="background:#9FB1BD;height:2px" class="q-my-xs" />

        <div class="flex items-center">
          <div class="" style="font-size:3.5vw">Credit Rating </div>
          <q-btn flat round icon="las la-info-circle" size="2.5vw">
                <q-tooltip
                  class=""
                  max-width="30vw"
                >
                  <div class="" style="font-size: 3vw">
                    Evaluation of your credit risk by Goldman Sachs
                  </div>
                </q-tooltip>
              </q-btn>
        </div>  
        
          <div class="" style="font-size:6vw">{{creditRating}}</div>
        </div>
        
        

      </div>


      <div class="q-mt-md  q-ml-md flex justify-center items-center" style="width:35vw; background-color:#9FB1BD;height:22vh;border-radius:5px; " @click="$router.push('/bnpl')">
        <div class="flex column justify-around items-center ">
          <q-icon name="qr_code_scanner" style="font-size:28vw" />
          <div class="" style="font-size:3vw; color:#">Buy Now Pay Later</div>
        </div>
        
       
        

      </div>

    </div>

    <!-- loans div -->
    <div class="q-mt-md">
      <q-item clickable v-ripple to="/loans">
        <div class="" style="width:100%">
            <div class="flex items-center justify-between">
              <div class="" style="border-left:3px solid #0D4EA6;padding-left:5px; font-size:4vw;font-weight:500">Loans</div>
              <div class="">
                <div class="" style="font-size:4vw; color:#9FB1BD">Total Loans</div>
              </div>
              
            </div>

            <div class="flex items-center justify-end">
              <div class="q-mr-xs" style="color:#9FB1BD;font-size:3vw">SGD </div>
              <div class="" style="font-size:5vw; font-weight:500"><animated-number :value="outstandingLoans" :formatValue="formatToPrice" :duration="duration"/></div>
            </div>



        </div>
      </q-item>
    </div>

    <q-separator class="q-my-xs"/>

    <!-- insurance div -->
    <div class="">
      <q-item clickable v-ripple to="/insurance">
        <div class="" style="width:100%">
            <div class="">
              <div class="" style="border-left:3px solid #E86427;padding-left:5px; font-size:4vw;font-weight:500">Insurance</div>
              
            </div>

           <div class="flex items-center no-wrap q-mt-md">
             <img src="~assets/insuranceHome.svg" alt="">
             <div class="q-ml-md">
               <div class="text-">
                 Do not have an existing insurance plan? Get the right protection for your needs today with microinsurance.
                 </div>

                <div class="q-mt-xs" style="color:#0D4EA6">BROWSE PRODUCTS</div>   
                 
              </div>
           </div>



        </div>
      </q-item>
    </div>

    <q-separator class="q-my-sm"/>

    <!-- financial literacy -->
    <div class="q-px-md" @click="$router.push('/learn')">
      <!-- <div class="q-mb-sm" style="font-size:4vw; font-weight:500">Learn Finance Tips</div> -->
      <div class="q-mb-md " style="border-left:3px solid #C127E8;padding-left:5px; font-size:4vw;font-weight:500">Learn Finance Tips</div>


    <carousel :autoplay="true" :nav="false" :margin="15" :loop="true" :center="true" :items="2" >

     <img src="~assets/moneySaving.png" alt="" style="border-radius:8px">
     <img src="~assets/insurance.png" alt="" style="border-radius:8px" >
     <img src="~assets/fiveWays.png" alt="" style="border-radius:8px" >

    </carousel>





    </div>

    <!-- bnpl dialog 1 -->
    <q-dialog v-model="bnplPopup1">
      <q-card class="q-pa-md">
        <div class="absolute" style="right:2vw;top:2vw">
          <q-btn round flat outline icon="close" v-close-popup />
        </div>
        

        <img src="~assets/bnplPic1.png" alt="" >

        <div class="text-center q-mt-md" style="font-size:3.3vw">
          Why spend all your cash at once when you can choose to split the bill at 0% interest? 
          

        </div>
        <div class="text-center q-my-md" style="font-size:4.3vw; font-weight:600">Link your bank account now!</div>

        
        <q-btn unelevated label="Link My Bank Account" class="full-width q-mt-md text-white q-py-xs" no-caps  style="border-radius:5px; background-color:#D9A514" to="/profile"/>


      </q-card>
    </q-dialog>


    <!-- bnpl dialog 2 -->
    




    
  </q-page>
</template>

<script>
var axios = require('axios');
import AnimatedNumber from "animated-number-vue";
import carousel from 'vue-owl-carousel'
export default {
  components: {  carousel, AnimatedNumber},
  data() {
    return {
      bankBalance:0,   //change to empty and dynamic
      duration:300,
      outstandingLoans:0,
      creditRating:'',
      bnplPopup1:false
      
      
    };
  },
  async mounted() {
   console.log(this.$store.state.AccessToken)
  this.bnplPopup1 = true
    var data = '';

    var config1 = {
      method: 'get',
      url: 'https://ks0iqp6qe8.execute-api.ap-southeast-1.amazonaws.com/dev/loanpool/user_profile',
      headers: { 
        'Authorization': `Bearer ${this.$store.state.AccessToken}`
      },
      data : data
    };

    try{
      let response = await axios(config1)
      console.log(JSON.stringify(response.data.body))
      console.log(response.data.body)

      this.creditRating = response.data.body.credit_rating
      this.outstandingLoans = response.data.body.total_loan_oustanding
      
    }catch (err){
      console.log(err);
    }

    // get bank balance
    var data = '';

    var config1 = {
      method: 'get',
      url: 'https://k9k7c7vvdb.execute-api.ap-southeast-1.amazonaws.com/dev/user/details',
      headers: { 
        'Authorization': `Bearer ${this.$store.state.AccessToken}`
      },
      data : data
    };

    try{
      let response = await axios(config1)
      console.log(JSON.stringify(response.data))
      
      this.bankBalance = response.data.data.plaid_account.balances.available

      
    }catch (err){
      console.log(err);
    }
    
  },
  methods: {
    formatToPrice(outstandingLoans) {
      return `<span>${Number(outstandingLoans).toFixed(2)}</span>`;
    },
    
  },
};
</script>

<style scoped>
</style>
