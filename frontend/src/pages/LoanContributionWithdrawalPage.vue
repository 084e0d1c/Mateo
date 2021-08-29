<template>
  <q-page class="" style="background:#F2F5F7"> 
    <div class="bg-white q-pb-md q-pt-sm">
      <div class="q-pa-md q-pb-lg q-pt-sm q-mx-md text-white" style="background:#f2c037;  border-radius:5px;">
        
        <div class="flex justify-between items-center">
          <div class="">
              <div class="" style="font-size:4vw">Current Value</div>

              <div class="flex justify-between items-center">
                <div class="flex items-center">
                    <div class="" style="font-size:4.5vw">SGD</div>
                    <div class="q-ml-xs" style="font-size:6.5vw;font-weight:500">{{currentValue}}</div>
                </div>
            
              </div>
          </div>

          <div class="">
             <div class="flex">
                  <div class="" style="font-size:3.2vw">Stop All Future Loans</div>
                  <q-btn flat round icon="las la-info-circle" size="1.9vw">
                    <q-tooltip class="" max-width="50vw">
                      <div class="q-ml-xs text-justify" style="font-size: 3vw">
                        Remove existing funds from available pool and any loans that are repaid will no longer be available for future loans
                      </div>
                    </q-tooltip>
                  </q-btn>
                </div>
                <div class="" style="font-size:4.5vw;font-weight:500;text-align:end;margin-right:1vw"><q-toggle
                  v-model="stopLoansToggle"
                  color="green"
                /></div>
          </div>
         


        </div>
        
        <div class="flex justify-between items-center no-wrap">
          <q-knob
                    readonly
                    v-model="loanAmountPie"
                    show-value
                    size="20vw"
                    :thickness="0.22"
                    :color="'blue'"
                    track-color="grey-3"
                    class="q-my-sm q-mr-md"
                    
                  >
                  <div class="" style="font-size:3.8vw">
                    30%  
                  </div>
                  
              </q-knob>
          <div class="text-end">
            <div class="" style="font-size:3.5vw;">Pool Interest Rate: <span style="font-weight:500;">{{allData.interest_rate*100}}%</span></div>
            <div class="" style="font-size:3.5vw;">Amount currently loaned: <span style="font-weight:500;">SGD {{amountLoaned}}</span></div>
            <div class="" style="font-size:3.5vw;">Withdrawable amount: <span style="font-weight:500;">SGD {{withdrawableAmount}}</span></div>

          </div>

        </div>

      </div>

      <div class="">
        <div class="q-mt-md q-mx-md" style="font-size:4.5vw;font-weight:500">Make a Withdrawal</div>
      <q-separator class="q-mx-md" />

      <div class="q-mt-md q-mb-xs q-mx-md" style="text-align:end; color:#5B7282; font-size:3.5vw">Maximum amount: SGD{{currentValue}}</div>

      <q-input outlined v-model="withdrawalAmount"  type="number" placeholder="Amount" min="0" class="q-mb-xs q-mx-md">
          <template v-slot:prepend>
            <q-icon name="o_paid" />
          </template>
        </q-input>
      </div>
    </div>
    
    


    <div class="" style="">
      <div class="q-mx-md q-mt-sm" style="font-size:4.5vw;font-weight:500">Summary</div>

      <div class="q-mx-lg q-mt-sm">
        <div class="flex justify-between items-center" style="font-size:3.5vw">
          <div class="">Current value</div>
          <div class="" style="font-weight:400">SGD {{currentValue}}</div>
        </div>
        
        <div class="flex justify-between items-center q-mt-md q-mb-md" style="font-size:3.5vw">
          <div class="">Amount currently loaned</div>
          <div class="">SGD {{amountLoaned}}</div>
        </div>

        <div class="flex justify-between items-center q-mt-md q-mb-md" style="font-size:3.5vw">
          <div class="">Withdrawable amount</div>
          <div class="">SGD {{withdrawableAmount}}</div>
        </div>

        <div class="flex justify-between items-center q-mt-md q-mb-sm" style="font-size:3.5vw">
          <div class="">Withdrawal</div>
          <div class="">- SGD {{withdrawalAmount}}</div>
        </div>

        <div class="flex justify-between items-center q-mt-md q-mb-sm" style="font-size:3.5vw">
          <div class="">Administrative Fees</div>
          <div class="">0.01%</div>
        </div>

        

        <q-btn unelevated label="Confirm Withdrawal" class="full-width q-mt-md text-white q-py-xs q-mb-md" no-caps  style="border-radius:5px; background-color:#607d8b"/>

      </div>
    </div>
    




    
    
  </q-page>
</template>

<script>
const axios = require('axios')
export default {
  data() {
    return {
      currentValue:'',
      amountLoaned:'',
      withdrawableAmount:'',
      withdrawalAmount:'',
      
      totalValue:'100.00',
      stopLoansToggle:false,
      loanAmountPie:30,
      allData:''
    };
  },
  computed:{
    totalAmount: function(){
      this.borrowAmount = parseInt(this.borrowAmount)
      let newAmount = (this.borrowAmount*(this.bankFees/100)) 
      
      newAmount += this.borrowAmount
      return newAmount
    },

    valueLeft: function(){
      this.valueLeft = this.currentValue - this.withdrawalAmount
    }
  },
  methods: {},
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

      this.allData = response.data.body

      let currentPool = this.$route.fullPath.substr(this.$route.fullPath.length - 1)
      // console.log(currentPool)

      if (currentPool == 'B'){
        this.allData = response.data.body[2]
      } else if (currentPool == 'C'){
        this.allData = response.data.body[1]
      } else{
        this.allData = response.data.body[0]
      }


      // console.log(JSON.stringify(this.allData))

    }catch (err){
      console.log(err);
    }


    // GET THE LOANS TAB THINGS
     var config = {
      method: 'get',
      url: 'https://ks0iqp6qe8.execute-api.ap-southeast-1.amazonaws.com/dev/loanpool/user_profile',
      headers: { 
        'Authorization': `Bearer ${this.$store.state.AccessToken}`
      },
      data : data
    };

    try{
      let response = await axios(config)
      console.log(JSON.stringify(response.data.body))
      // console.log(response.data.body)

      this.loansTab = response.data.body

      let currentPool = this.$route.fullPath.substr(this.$route.fullPath.length - 1)
      
      
      
      if (currentPool == 'B'){
        if (typeof this.loansTab.deposits_to_pools.Gold != 'undefined' ){
          this.amountLoaned =  Math.round(this.loansTab.deposits_to_pools.Gold.in_loan * 100) / 100
          this.withdrawableAmount = Math.round(this.loansTab.deposits_to_pools.Gold.available* 100) / 100
          this.currentValue = this.loansTab.deposits_to_pools.Gold.initial_deposit + this.loansTab.deposits_to_pools.Gold.interest_reward
          // this.valueLeft = this.currentValue - this.withdrawalAmount
        }

      } else if (currentPool == 'C'){
        if (typeof this.loansTab.deposits_to_pools.Silver != 'undefined' ){
          this.amountLoaned = this.loansTab.deposits_to_pools.Silver.in_loan
          this.withdrawableAmount = this.loansTab.deposits_to_pools.Silver.available
          this.currentValue = this.loansTab.deposits_to_pools.Silver.initial_deposit + this.loansTab.deposits_to_pools.Gold.interest_reward
          // this.valueLeft = this.currentValue - this.withdrawalAmount
        }
      } else{
        if (typeof this.loansTab.deposits_to_pools.Bronze != 'undefined' ){
          this.amountLoaned = this.loansTab.deposits_to_pools.Bronze.in_loan
          this.withdrawableAmount = this.loansTab.deposits_to_pools.Bronze.available
          this.currentValue = this.loansTab.deposits_to_pools.Bronze.initial_deposit + this.loansTab.deposits_to_pools.Gold.interest_reward
          // this.valueLeft = this.currentValue - this.withdrawalAmount
        }
      }

    


    }catch (err){
      console.log(err);
    }


  }
};
</script>

<style scoped>
</style>
