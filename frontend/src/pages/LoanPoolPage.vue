<template>
  <q-page class="" style="">
    <!-- B pool div -->
    <q-expansion-item class="" style="border-bottom:2px solid lightgrey">
      <template v-slot:header>
        <q-item-section avatar>
          <div class="flex items-center">
            <img src="~assets/bPool.svg" alt="" style="width: 10vw" />
            <div class="q-ml-xs" style="font-size: 5vw">Pool B</div>
          </div>
        </q-item-section>

        <q-item-section>
          <div class="" style="width: 25vw">
            <div class="flex items-center justify-end" style="">
              <div class="q-mr-xs" style="font-size: 3.5vw; color: #9fb1bd">
                SGD
              </div>
              <div class="" style="font-size: 4.5vw; font-weight: 500">
                <animated-number :value="allData[2].available_amount" :formatValue="formatToPrice" :duration="duration"/>
              </div>
            </div>
            <div
              class=""
              style="text-align: end; font-size: 3vw; color: #9fb1bd"
            >
              Available
            </div>
          </div>
        </q-item-section>

        <q-item-section side>
          <div class="flex column justify-end items-end q-mr-md">
            <div
              class=""
              style="font-size: 4.5vw; font-weight: 500; color: #077d55"
            >
              {{allData[2].interest_rate * 100}}%
            </div>
            <div class="font-size:3vw;color:#9FB1BD">Yield</div>
          </div>
        </q-item-section>
      </template>

      <q-card class>
        <q-card-section>
          <div class="" >
            <div class="flex justify-around items-center q-mx-l ">
              <div
                class="flex items-center no-wrap"
                style="max-width: 60vw; font-size: 3vw"
              >
                <div class="" style="">
                  Minimum required credit rating to borrow from pool
                </div>

                <q-btn flat round icon="las la-info-circle" size="2.5vw">
                  <q-tooltip class="" max-width="40vw">
                    <div class="" style="font-size: 3vw">
                      Evaluation of your credit risk by Goldman Sachs
                    </div>
                  </q-tooltip>
                </q-btn>
              </div>

              <div
                class=""
                style="font-weight: 600; font-size: 4.5vw; margin-right: 10vw"
              >
                {{allData[2].credit_rating_requirement}}
              </div>
            </div>

            <div class="flex justify-around items-center q-mx-sm">
              <q-btn
                :disable=" allData[2].loan"
                unelevated
                label="Borrow From Pool"
                class="q-mt-md text-white q-py-xs"
                no-caps
                style="
                  border-radius: 5px;
                  background-color: #607d8b;
                  width: 40vw;
                "
                to="loanPoolDetailsBorrow/Pool B"
              />
              <q-btn
                :disable="typeof allData[2].deposit == 'undefined' "
                unelevated
                label="Contribute To Pool"
                class="q-mt-md text-white q-py-xs"
                no-caps
                style="
                  border-radius: 5px;
                  background-color: #f2c037;
                  width: 40vw;
                "

                to="loanPoolDetailsContribute/Pool B"
              />
            </div>
          </div>
        </q-card-section>

        
      </q-card>
    </q-expansion-item>

    <!-- C pool div -->
    <q-expansion-item class="" style="border-bottom:2px solid lightgrey">
      <template v-slot:header>
        <q-item-section avatar>
          <div class="flex items-center">
            <img src="~assets/cPool.svg" alt="" style="width: 10vw" />
            <div class="q-ml-xs" style="font-size: 5vw">Pool C</div>
          </div>
        </q-item-section>

        <q-item-section>
          <div class="" style="width: 25vw">
            <div class="flex items-center justify-end" style="">
              <div class="q-mr-xs" style="font-size: 3.5vw; color: #9fb1bd">
                SGD
              </div>
              <div class="" style="font-size: 4.5vw; font-weight: 500">
                <animated-number :value="allData[1].available_amount" :formatValue="formatToPrice" :duration="duration"/>
              </div>
            </div>
            <div
              class=""
              style="text-align: end; font-size: 3vw; color: #9fb1bd"
            >
              Available
            </div>
          </div>
        </q-item-section>

        <q-item-section side>
          <div class="flex column justify-end items-end q-mr-md">
            <div
              class=""
              style="font-size: 4.5vw; font-weight: 500; color: #077d55"
            >
              {{allData[1].interest_rate * 100}}%
            </div>
            <div class="font-size:3vw;color:#9FB1BD">Yield</div>
          </div>
        </q-item-section>
      </template>

      <q-card>
        <q-card-section>
          <div class="" >
            <div class="flex justify-around items-center q-mx-l">
              <div
                class="flex items-center no-wrap"
                style="max-width: 60vw; font-size: 3vw"
              >
                <div class="" style="">
                  Minimum required credit rating to borrow from pool
                </div>

                <q-btn flat round icon="las la-info-circle" size="2.5vw">
                  <q-tooltip class="" max-width="40vw">
                    <div class="" style="font-size: 3vw">
                      Evaluation of your credit risk by Goldman Sachs
                    </div>
                  </q-tooltip>
                </q-btn>
              </div>

              <div
                class=""
                style="font-weight: 600; font-size: 4.5vw; margin-right: 10vw"
              >
                {{allData[1].credit_rating_requirement}}
              </div>
            </div>

            <div class="flex justify-around items-center q-mx-sm">
              <q-btn
              :disable="!allData[1].loan"
                unelevated
                label="Borrow From Pool"
                class="q-mt-md text-white q-py-xs"
                no-caps
                style="
                  border-radius: 5px;
                  background-color: #607d8b;
                  width: 40vw;
                "
                to="loanPoolDetailsBorrow/Pool C"
              />
              <q-btn
              :disable="!allData[1].deposit"
                unelevated
                label="Contribute To Pool"
                class="q-mt-md text-white q-py-xs"
                no-caps
                style="
                  border-radius: 5px;
                  background-color: #f2c037;
                  width: 40vw;
                "
                to="loanPoolDetailsContribute/Pool C"
              />
            </div>
          </div>
        </q-card-section>
      </q-card>
    </q-expansion-item>

    <!-- D pool div -->
      <q-expansion-item class="" style="border-bottom:2px solid lightgrey">
      <template v-slot:header>
        <q-item-section avatar>
          <div class="flex items-center">
            <img src="~assets/dPool.svg" alt="" style="width: 10vw" />
            <div class="q-ml-xs" style="font-size: 5vw">Pool D</div>
          </div>
        </q-item-section>

        <q-item-section>
          <div class="" style="width: 25vw">
            <div class="flex items-center justify-end" style="">
              <div class="q-mr-xs" style="font-size: 3.5vw; color: #9fb1bd">
                SGD
              </div>
              <div class="" style="font-size: 4.5vw; font-weight: 500">
                <animated-number :value="allData[0].available_amount" :formatValue="formatToPrice" :duration="duration"/>
              </div>
            </div>
            <div
              class=""
              style="text-align: end; font-size: 3vw; color: #9fb1bd"
            >
              Available
            </div>
          </div>
        </q-item-section>

        <q-item-section side>
          <div class="flex column justify-end items-end q-mr-md">
            <div
              class=""
              style="font-size: 4.5vw; font-weight: 500; color: #077d55"
            >
              {{allData[0].interest_rate * 100}}%
            </div>
            <div class="font-size:3vw;color:#9FB1BD">Yield</div>
          </div>
        </q-item-section>
      </template>

      <q-card >
        <q-card-section>
          <div class="" style="">
            <div class="flex justify-around items-center q-mx-l">
              <div
                class="flex items-center no-wrap"
                style="max-width: 60vw; font-size: 3vw"
              >
                <div class="" style="">
                  Minimum required credit rating to borrow from pool
                </div>

                <q-btn flat round icon="las la-info-circle" size="2.5vw">
                  <q-tooltip class="" max-width="40vw">
                    <div class="" style="font-size: 3vw">
                      Evaluation of your credit risk by Goldman Sachs
                    </div>
                  </q-tooltip>
                </q-btn>
              </div>

              <div
                class=""
                style="font-weight: 600; font-size: 4.5vw; margin-right: 10vw"
              >
                {{allData[0].credit_rating_requirement}}
              </div>
            </div>

            <div class="flex justify-around items-center q-mx-sm">
              <q-btn
              :disable="!allData[0].loan"
                unelevated
                label="Borrow From Pool"
                class="q-mt-md text-white q-py-xs"
                no-caps
                style="
                  border-radius: 5px;
                  background-color: #607d8b;
                  width: 40vw;
                "
                to="loanPoolDetailsBorrow/Pool D"
              />
              <q-btn
              :disable="!allData[0].deposit"
                unelevated
                label="Contribute To Pool"
                class="q-mt-md text-white q-py-xs"
                no-caps
                style="
                  border-radius: 5px;
                  background-color: #f2c037;
                  width: 40vw;
                "
                to="loanPoolDetailsContribute/Pool D"
              />
            </div>
          </div>
        </q-card-section>
      </q-card>
    </q-expansion-item>


    <div class="q-pa-md">
      <q-card>
        <q-tabs
          no-caps
          v-model="tab"
          
          class=""
          active-color="white"
          indicator-color="white"
          align="justify"
          narrow-indicator
          style="background:#9FB1BD;"
          
        >
          <q-tab name="loans" label="Loans" :disable="loansTabDisable" />
          <q-tab name="contributions" label="Contributions" :disable="contributionsTabDisable" />
          <q-tab name="transaction history" label="Transactions" />
        </q-tabs>

        <q-separator />

        <q-tab-panels v-model="tab" animated>
          <!-- loans tab -->
          <q-tab-panel name="loans" class="q-px-md">
            <div class="flex justify-between items-start">

              <div>
                <div class=""  style="font-size:3.2vw">
                  Total Outstanding Pool Loans
                </div>
                <div class="flex items-center">
                  <div class="" style="font-size:3.5vw">SGD</div>
                  <div class="q-ml-xs" style="font-size:5.5vw;font-weight:500">900.00</div>
                </div >
              </div>

              <div class="">
                <div class="flex items-">
                  <div class="" style="font-size:3.2vw">Your Credit Rating</div>
                  <q-btn flat round icon="las la-info-circle" size="1.9vw">
                    <q-tooltip class="" max-width="40vw">
                      <div class="q-ml-xs" style="font-size: 3vw">
                        Evaluation of your credit risk by Goldman Sachs
                      </div>
                    </q-tooltip>
                  </q-btn>
                </div>

                <div class="" style="font-size:4.5vw;font-weight:500;text-align:end;margin-right:1vw">BB</div>
              </div>
            </div>


             <q-item
              v-for="event in events"
              :key="event.id"
              clickable
              v-ripple
              class=""
              style="border-bottom: 0.3px solid lightgrey"
              :to="`/loanDetails/${event.title}`"
            >
            <div class="flex justify-between items-center no-wrap full-width">
              <div class="flex items-center no-wrap">
                <q-knob
                    readonly
                    v-model="event.progress"
                    show-value
                    size="16vw"
                    :thickness="0.22"
                    :color="event.color"
                    track-color="grey-3"
                    class="q-my-sm q-mr-md"
                    :class="`text-${event.color}`"
                  >
                  <div class="" style="font-size:3.8vw">
                    {{event.progress}}%  
                  </div>
                  
              </q-knob>

              <div class="">
                <div class="" style="font-size:4vw">{{event.title}}</div>
                <div class="" style="color:#5B7282; font-size:3vw">Interest Rate: <span style="font-weight:600">{{event.interestRate}}%</span></div>
                <div class="" style="color:#5B7282; font-size:3vw">Days till next payment: <span style="font-weight:600">{{event.days}}</span></div>
                <div class="" style="color:#5B7282 ; font-size:3vw">Payment period: <span style="font-weight:600">{{event.period}}</span></div>
              </div>
              </div>

              <div class="">
                
                <div class="" style="color:#9FB1BD; font-size:2.5vw;text-align:end ">SGD</div>
                <div class="" style="font-weight:500; font-size:4vw ">{{event.loanAmount}}</div>
                <div class="text-center q-mt-sm" style="padding:5px; background: #5B7282; color:white; font-size:3vw; border-radius:30px ">Pay</div>
              </div>
              
            </div>
            </q-item>
          
          </q-tab-panel>


          <!-- contributions tab -->
          <q-tab-panel name="contributions">
            <div class="flex justify-between items-start">

              <div>
                <div class=""  style="font-size:3.2vw">
                  Total Contributions
                </div>
                <div class="flex items-center">
                  <div class="" style="font-size:3.5vw">SGD</div>
                  <div class="q-ml-xs" style="font-size:5.5vw;font-weight:500">{{totalContributions}}</div>
                </div >
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

            <q-item
              v-for="event in contributions"
              :key="event.id"
              clickable
              v-ripple
              class=""
              style="border-bottom: 0.3px solid lightgrey"
              :to="`/loanContributionWithdrawal/${event.title}`"
              
            >
            <div v-show="event.interestRate" class="flex justify-between items-start no-wrap full-width ">
              <div class="flex justify-between items-start  no-wrap ">
                <img :src="event.imgSrc" alt="" style="width: 10vw;margin-right:3vw" />

                <div class="">
                  <div class="" style="font-size:4vw">{{event.title}}</div>
                  <div class="" style="color:#5B7282; font-size:3vw">Interest Rate: <span style="font-weight:600">{{event.interestRate}}%</span></div>

                  <div class="flex justify-between items-center" style="width:60vw">
                    <div class="">
                      <div class="" style="color:#5B7282; font-size:3vw">Deposited Value:</div>
                      <div class="flex items-center">
                        <div class="" style="font-size:3vw">SGD</div>
                        <div class="q-ml-xs" style="font-size:4.5vw;font-weight:500">{{event.depositValue}}</div>
                      </div>
                      
                    </div>

                    <div class="">
                      <div class="" style="color:#5B7282; font-size:3vw">Current Value:</div>
                      <div class="flex items-center">
                        <div class="" style="font-size:3vw">SGD</div>
                        <div class="q-ml-xs" style="font-size:4.5vw;font-weight:500">{{event.currentValue}}</div>
                      </div>
                      
                    </div>




                  </div>

                  
                  

                  


                </div>
              </div>

              <q-icon name="eva-arrow-ios-forward" size="6vw" style="color:#9FB1BD"/>
              
              </div>
            </q-item>
          </q-tab-panel>

          <!-- transaction history tab -->
          <q-tab-panel name="transaction history" style="height:50vh">
            <q-item
              clickable
              v-ripple
              class=""
              style="border-bottom: 0.3px solid lightgrey"
              
              
            >
         

              <div class="flex justify-between items-center full-width">
                <!-- left side -->
                <div class="">
                  <div class="" style="font-size:3vw;color:#9FB1BD">Payment</div>
                  <div class="" style="font-size:4.5vw;">Loan from Pool B</div>
                  <div class="" style="font-size:3vw;color:#9FB1BD">28 Aug 2021 - Transaction ID: 987654</div>
                </div>

                <!-- right side -->
                <div class="">
                    <div class="text-end" style="font-size:2.7vw;">SGD</div>
                    <div class="text-end" style="font-size:4.5vw;">20.00</div>
                </div>


              </div>


     

            </q-item>

            

            <!-- item 4 -->
            <q-item
              clickable
              v-ripple
              class=""
              style="border-bottom: 0.3px solid lightgrey"
              
            >
         

              <div class="flex justify-between items-center full-width">
                <!-- left side -->
                <div class="">
                  <div class="" style="font-size:3vw;color:#9FB1BD">Payment</div>
                  <div class="" style="font-size:4.5vw;">Loan from Pool B</div>
                  <div class="" style="font-size:3vw;color:#9FB1BD">15 Aug 2021 - Transaction ID: 678901</div>
                </div>

                <!-- right side -->
                <div class="">
                    <div class="text-end" style="font-size:2.7vw;">SGD</div>
                    <div class="text-end" style="font-size:4.5vw;">20.00</div>
                </div>


              </div>


     

            </q-item>

            <q-item
              clickable
              v-ripple
              class=""
              style="border-bottom: 0.3px solid lightgrey"
              
            >
         

              <div class="flex justify-between items-center full-width">
                <!-- left side -->
                <div class="">
                  <div class="" style="font-size:3vw;color:#9FB1BD">Withdrawal</div>
                  <div class="" style="font-size:4.5vw;">Contributions in Pool C</div>
                  <div class="" style="font-size:3vw;color:#9FB1BD">28 Jul 2021 - Transaction ID: 184332</div>
                </div>

                <!-- right side -->
                <div class="">
                    <div class="text-end" style="font-size:2.7vw;">SGD</div>
                    <div class="text-end" style="font-size:4.5vw;">40.00</div>
                </div>


              </div>

            </q-item>

            <q-item
              clickable
              v-ripple
              class=""
              style="border-bottom: 0.3px solid lightgrey"
              
            >
         

              <div class="flex justify-between items-center full-width">
                <!-- left side -->
                <div class="">
                  <div class="" style="font-size:3vw;color:#9FB1BD">Withdrawal</div>
                  <div class="" style="font-size:4.5vw;">Contributions in Pool D</div>
                  <div class="" style="font-size:3vw;color:#9FB1BD">23 Jul 2021 - Transaction ID: 184332</div>
                </div>

                <!-- right side -->
                <div class="">
                    <div class="text-end" style="font-size:2.7vw;">SGD</div>
                    <div class="text-end" style="font-size:4.5vw;">285.00</div>
                </div>


              </div>

            </q-item>

            <q-item
              clickable
              v-ripple
              class=""
              style="border-bottom: 0.3px solid lightgrey"
              
            >
         

              <div class="flex justify-between items-center full-width">
                <!-- left side -->
                <div class="">
                  <div class="" style="font-size:3vw;color:#9FB1BD">Withdrawal</div>
                  <div class="" style="font-size:4.5vw;">Loan from Pool B</div>
                  <div class="" style="font-size:3vw;color:#9FB1BD">28 Jul 2021 - Transaction ID: 184332</div>
                </div>

                <!-- right side -->
                <div class="">
                    <div class="text-end" style="font-size:2.7vw;">SGD</div>
                    <div class="text-end" style="font-size:4.5vw;">50.00</div>
                </div>


              </div>


     

            </q-item>

          </q-tab-panel>
        </q-tab-panels>
      </q-card>
    </div>

    
  </q-page>
</template>

<script>
import AnimatedNumber from "animated-number-vue";
export default {
  components: {
    AnimatedNumber
  },
  data() {
    return {
      tab:'',
      stopLoansToggle:false,
      loansTabDisable:false,
      contributionsTabDisable:false,
      allData:'',
      loansTab:'',
      duration:300,
      totalContributions:0,
      events: [
        {
          id: "01",
          title: "Loan from Pool B",
          interestRate:'',
          days:'5',
          period:'1 month',
          color: "light-blue",
          progress: 91,
          loanAmount:'300.00'
        },
        {
          id: "02",
          title: "Loan from Pool C",
          interestRate:'12.5',
          days:'13',
          period:'6 months',
          color: "teal",
          progress: 77,
          loanAmount:'150.00'
        },
        {
          id: "03",
          title: "Loan from Pool D",
          interestRate:'13.5',
          days:'23',
          period:'24 months',
          color: "amber",
          progress: 36,
          loanAmount:'270.00'
        },
        
      ],

      contributions: [
        {
          id: "01",
          title: "Funds in Pool B",
          interestRate:'',
          days:'5',
          period:'1 month',
          color: "light-blue",
          progress: 91,
          loanAmount:'300.00',
          imgSrc:'../statics/bPool.svg',
          depositValue:'0',
          currentValue:'0'
        },
        {
          id: "02",
          title: "Funds in Pool C",
          interestRate:'',
          days:'13',
          period:'6 months',
          color: "teal",
          progress: 77,
          loanAmount:'150.00',
          imgSrc:'../statics/cPool.svg',
          depositValue:'0',
          currentValue:'0'
        },
        {
          id: "03",
          title: "Funds in Pool D",
          interestRate:'',
          days:'23',
          period:'24 months',
          color: "amber",
          progress: 36,
          loanAmount:'270.00',
          imgSrc:'../statics/dPool.svg',
          depositValue:'0',
          currentValue:'0'
        },
        
      ],
          
    };
  },
  methods: {
    formatToPrice(outstandingLoans) {
      return `<span>${Number(outstandingLoans).toFixed(2)}</span>`;
    },
  },

  async mounted(){
    const axios = require('axios')
    var data = '';

    var config = {
      method: 'get',
      url: 'https://ks0iqp6qe8.execute-api.ap-southeast-1.amazonaws.com/dev/loanpool/pools',
      headers: { 
        'Authorization': `Bearer ${this.$store.state.AccessToken}`
      },
      data : data
    };

    try{
      let response = await axios(config)
      // console.log('GET DATA ALL DATA:',JSON.stringify(response.data.body))
      // console.log(response.data.body)

      this.allData = response.data.body
      // console.log(this.allData)

      
      // store interest rate for pool B for loans and contributions
      this.events[0].interestRate = this.allData[2].interest_rate*100
      this.contributions[0].interestRate = this.allData[2].interest_rate*100

      this.events[1].interestRate = this.allData[1].interest_rate*100
      this.contributions[1].interestRate = this.allData[1].interest_rate*100

      this.events[2].interestRate = this.allData[0].interest_rate*100
      this.contributions[2].interestRate = this.allData[0].interest_rate*100

      

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
      console.log(response.data.body)

      this.loansTab = response.data.body


      // selecting the apt tab and siabling the other
      if (this.loansTab.outstanding_loan_amount == 0){
        this.loansTabDisable = true;
        this.contributionsTabDisable = false;
        this.tab = 'contributions'
      }else{
        this.contributionsTabDisable = true;
        this.lonsTabDisable = false;
        this.tab = 'loans'
      }

      
      let totalContributions = 0;
      // B pool
      console.log(this.loansTab.deposits_to_pools.Gold)

      if (typeof this.loansTab.deposits_to_pools.Gold != 'undefined' ){
        this.contributions[0].depositValue = this.loansTab.deposits_to_pools.Gold.initial_deposit
        this.contributions[0].currentValue = this.loansTab.deposits_to_pools.Gold.initial_deposit + this.loansTab.deposits_to_pools.Gold.interest_reward

        totalContributions += this.loansTab.deposits_to_pools.Gold.initial_deposit + this.loansTab.deposits_to_pools.Gold.interest_reward
      }
      
      if (typeof this.loansTab.deposits_to_pools.Silver != 'undefined' ){
        this.contributions[1].depositValue = this.loansTab.deposits_to_pools.Silver.initial_deposit
        this.contributions[1].currentValue = this.loansTab.deposits_to_pools.Silver.initial_deposit + this.loansTab.deposits_to_pools.Silver.interest_reward

        totalContributions += this.loansTab.deposits_to_pools.Gold.initial_deposit + this.loansTab.deposits_to_pools.Gold.interest_reward
      }
        
      

      if (typeof this.loansTab.deposits_to_pools.Bronze != 'undefined' ){
        this.contributions[2].depositValue = this.loansTab.deposits_to_pools.Bronze.initial_deposit
      this.contributions[2].currentValue = this.loansTab.deposits_to_pools.Bronze.initial_deposit + this.loansTab.deposits_to_pools.Gold.interest_reward

      totalContributions += this.loansTab.deposits_to_pools.Bronze.initial_deposit + this.loansTab.deposits_to_pools.Bronze.interest_reward
      }
      
      this.totalContributions = totalContributions
      console.log(totalContributions)


    }catch (err){
      console.log(err);
    }





  }
};
</script>

<style scoped>
</style>
