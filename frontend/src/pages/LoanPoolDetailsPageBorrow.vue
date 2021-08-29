<template>
  <q-page class="" style="background:#F2F5F7"> 
    <div class="bg-white q-pb-md q-pt-sm">
      <div class="q-pa-md q-pb-lg q-pt-sm q-mx-md text-white" style="background:#3E5463;  border-radius:5px;">
        <div class="" style="font-size:4vw">Total Available in Pool</div>

        <div class="flex justify-between items-center">
          <div class="flex items-center">
              <div class="" style="font-size:4.5vw">SGD</div>
              <div class="q-ml-xs" style="font-size:6.5vw;font-weight:500">{{allData.available_amount}}</div>
          </div>
      
        </div>
        <div class="flex justify-between items-center no-wrap q-mt-md">
          <div class="">
              <div class="" style="font-size:3.5vw">Prevailing Interest Rate:</div>
              <div class="text-center" style="font-size:4.5vw;font-weight:500">{{allData.interest_rate*100}}%</div>
          </div>

          <div class="">
            <div class="" style="font-size:3.5vw">Min. Credit Rating:</div>
            <div class="text-center" style="font-size:4.5vw;font-weight:500;">{{allData.credit_rating_requirement}}</div>
          </div>
          
        </div>

      </div>

      <div class="">
        <div class="q-mt-md q-mx-md" style="font-size:4.5vw;font-weight:500">Borrow from Pool</div>
      <q-separator class="q-mx-md" />

      <div class="q-mt-md q-mb-xs q-mx-md" style="text-align:end; color:#5B7282; font-size:3.5vw">Maximum amount: SGD{{allData.max_deposit}}</div>

      <q-input outlined v-model="borrowAmount"  type="number" placeholder="Amount" min="0" class="q-mb-md q-mx-md">
          <template v-slot:prepend>
            <q-icon name="o_paid" />
          </template>
        </q-input>
      </div>
    </div>
    
    


    <div class="" style="">
      <div class="q-mx-md q-mt-sm" style="font-size:4.5vw;font-weight:500">Summary</div>

      <div class="q-mx-lg q-mt-md">
        <div class="flex justify-between items-center" style="font-size:3.5vw">
          <div class="">Amount Borrowed from Pool</div>
          <div class="" style="font-weight:500" v-if="borrowAmount">SGD {{borrowAmount}}</div>
        </div>
        
        <div class="flex justify-between items-center q-mt-md q-mb-md" style="font-size:3.5vw">
          <div class="">Interest Rate</div>
          <div class="">{{allData.interest_rate*100}}%</div>
        </div>

        <div class="flex justify-between items-center q-mt-md q-mb-md" style="font-size:3.5vw">
          <div class="">Payment Period</div>
          <div class="">{{allData.repayment_schedule}}</div>
        </div>

        <div class="flex justify-between items-center q-mt-md" style="font-size:3.5vw">
          <div class="">Bank Fees</div>
          <div class="">{{allData.administrative_fees*100}}%</div>
        </div>

        <q-separator />

        <div class="flex justify-between items-center q-mt-md" style="font-size:3.5vw">
          <div class="">Total Upfront Fees</div>
          <div class="" v-if="totalAmount">SGD {{totalAmount}}</div>
        </div>

        <q-btn :disable="!borrowAmount " unelevated label="Confirm Loan" class="full-width q-mt-md text-white q-py-xs" no-caps  style="border-radius:5px; background-color:#607d8b" @click="postData()"/>

      </div>
    </div>
    




    
    
  </q-page>
</template>

<script>
const axios = require('axios')
export default {
  data() {
    return {
      borrowAmount:'',
      interestRate:12.5,
      bankFees:1,
      allData:''
    };
  },
  computed:{
    totalAmount: function(){
      this.borrowAmount = parseInt(this.borrowAmount)
      let newAmount = (this.borrowAmount*(this.allData.administrative_fees*100)) 
      
      newAmount += this.borrowAmount
      return newAmount
    }
  },
  methods: {
    async postData(){
      
    var dataToPost = JSON.stringify({
        loan_amount: this.borrowAmount,
        pool_id: this.allData.pool_id,
        fees:(this.borrowAmount*(this.allData.administrative_fees*100)) 
      });

      console.log('post data',dataToPost)
      var config = {
        method: "post",
        url: "https://ks0iqp6qe8.execute-api.ap-southeast-1.amazonaws.com/dev/loanpool/loan",
        headers: {
          "Content-Type": "application/json",
          'Authorization': `Bearer ${this.$store.state.AccessToken}`
        },
        data: dataToPost,
      };

      try {
        let response = await axios(config);
        console.log(response.data);

        this.success = true
       
      } catch (error) {
        console.log(error);
      
      }
    }


  },
  async mounted(){
    var data = '';

    // get call
    var config1 = {
      method: 'get',
      url: 'https://ks0iqp6qe8.execute-api.ap-southeast-1.amazonaws.com/dev/loanpool/pools',
      headers: { 
        'Authorization': `Bearer ${this.$store.state.AccessToken}`
      },
      data : data
    };

    try{
      let response = await axios(config1)
      // console.log(JSON.stringify(response.data.body))
      // console.log(response.data.body)

      // this.allData = response.data.body

      let currentPool = this.$route.fullPath.substr(this.$route.fullPath.length - 1)
      // console.log(currentPool)

      if (currentPool == 'B'){
        this.allData = response.data.body[2]
      } else if (currentPool == 'C'){
        this.allData = response.data.body[1]
      } else{
        this.allData = response.data.body[0]
      }


      console.log(this.allData)

    }catch (err){
      console.log(err);
    }
  }
};
</script>

<style scoped>
</style>
