<template>
  <q-page class="q-px-md" style=""> 
     <div class="q-pt-md">
       <VueApexCharts type="bar" height="180" :options="chartOptions" :series="series"></VueApexCharts>
     </div>
        
    <div class="q-pa-md q-pb-lg" style="background:#3E5463; color:#F2F5F7; border-radius:5px; ">
        <div class="">
          
        </div>
        <div class="" style="font-size:3.5vw">Total Outstanding Loans</div>
        <div class="flex items-center q-mt-xs">
          <div class="" style="font-size:4.5vw">SGD</div>
          <div class="q-ml-xs" style="font-size:6.5vw"><animated-number :value="outstandingLoans" :formatValue="formatToPrice" :duration="duration"/></div>
        </div>

        <q-linear-progress rounded size="20px" :value="progress" stripe color="warning" class="q-mt-sm" />
        

    </div>


    <div class="shadow-2 q-pt-sm" style="border-radius:5px; height:27.5vh; overflow-y:scroll;">
      
        <q-item
          v-for="event in events"
          :key="event.id"
          clickable
          v-ripple
          class=""
          style="border-bottom: 0.3px solid lightgrey"
          :to="`/loanDetails/${event.title}`"
        >
        <div class="flex justify-around items-center no-wrap full-width">
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

    </div>


    <div class="flex items-center justify-center no-wrap q-mt-sm q-mb-md">
      <q-item clickable v-ripple class="flex column justify-center " style="background:#B9E8FF;border-radius:10px;width:45vw; height:20vh" to="/bankLoan" >
        <div class="">
          <img src="~assets/bankLoan.svg" alt="" style="width:100%; height:9vh">
        </div>
        <div class="">
          <div class="" style="font-size:4vw">Apply for a </div>
        <div class="" style="font-size:6vw;color:#186ADE">Bank Loan</div>
        </div>
        
      </q-item>

      <q-item clickable v-ripple class="flex column justify-center q-ml-sm" style="background:#FFD1BC;border-radius:10px;width:45vw;height:20vh " to="/loanPool">
        <div class="">
          <img src="~assets/loanPool.svg" alt="" style="width:100%;height:9vh">
        </div>
        <div class="">
          <div class="" style="font-size:4vw">Check out the </div>
        <div class="" style="font-size:6vw;color:#E86427">Loan Pools</div>
        </div>
        
      </q-item>
      


    </div>


    
  </q-page>
</template>

<script>
import AnimatedNumber from "animated-number-vue";
import VueApexCharts from 'vue-apexcharts'
export default {
   components: {
    AnimatedNumber, VueApexCharts
  },
  data() {
    return {
      outstandingLoans:'',
      duration:300,
      progress: 0,
      series: [{
            name: 'Loan Repayments',
            data: [400, 400, 600, 800, 800, 1000, 400, 400, 600, 700, 900, 450]
          }],
      chartOptions: {
            chart: {
              type: 'bar',
              height:200,
              
            },
            plotOptions: {
              bar: {
                borderRadius: 5,
                dataLabels: {
                  position: 'top', // top, center, bottom
                },
              }
            },
            dataLabels: {
              enabled: true,
              formatter: function (val) {
                return "$" + val;
              },
              offsetY: -20,
              style: {
                fontSize: '2.5vw',
                colors: ["#304758"]
              }
            },
            
            xaxis: {
              categories: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
              position: 'top',
              axisBorder: {
                show: false
              },
              axisTicks: {
                show: false
              },
              crosshairs: {
                fill: {
                  type: 'gradient',
                  gradient: {
                    colorFrom: '#D8E3F0',
                    colorTo: '#BED1E6',
                    stops: [0, 100],
                    opacityFrom: 0.4,
                    opacityTo: 0.5,
                  }
                }
              },
              tooltip: {
                enabled: false,
                
              }
            },
            yaxis: {
              axisBorder: {
                show: false
              },
              axisTicks: {
                show: false,
              },
              labels: {
                show: false,
                formatter: function (val) {
                  return "$"+val ;
                }
              }
            
            },
            title: {
              text: 'Repayment chart',
              floating: true,
              offsetY: 160,
              align: 'center',
              style: {
                color: '#444',
                fontSize:'13px',
                
              }
            }
          },
          
        events: [
        {
          id: "01",
          title: "Personal Loan",
          interestRate:'4.7',
          days:'13',
          period:'2 months',
          color: "light-blue",
          progress: 67,
          loanAmount:'300.00'
        },
        {
          id: "02",
          title: "Home Loan",
          interestRate:'3.9',
          days:'17',
          period:'12 months',
          color: "teal",
          progress: 82,
          loanAmount:'150.00'
        },
        {
          id: "03",
          title: "Credit Card Loan",
          interestRate:'6.4',
          days:'21',
          period:'24 months',
          color: "amber",
          progress: 60,
          loanAmount:'270.00'
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
    // for the animation of progress bar
    this.progress = 0.7

    const axios = require('axios')
    var data = '';

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
      console.log(JSON.stringify(response.data.body))
      console.log(response.data.body)

      this.outstandingLoans = response.outsanding_loan_amount
    }catch (err){
      console.log(err);
    }
    
    

  }

  


};
</script>

<style scoped>
</style>
