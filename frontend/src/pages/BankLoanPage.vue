<template>
  <q-page class="" style="background:#F2F5F7"> 
    <div class="bg-white q-px-md q-pb-lg">
      <div class="q-mb-sm q-mt-sm " style="font-weight:500; font-size:4.5vw">Purpose of Loan</div>

        <q-tabs
        v-model="purpose"
        
        active-color="grey-2"
        active-bg-color="blue-grey-6"
        indicator-color="transparent"
        content-class="q-gutter-x-lg"
      >
        <q-tab
          name="Home"
          label="Home"
          style="border-radius: 10px; border: 2px solid #607d8b "
          no-caps
          exact
          class=""
          
        />
        <q-tab name="Eduaction" label="Eduaction" exact  style="border-radius: 10px; border: 2px solid #607d8b"
          class=""
          no-caps />
        <q-tab name="Other" label="Other" exact   style="border-radius: 10px; border: 2px solid #607d8b"
          class=""
          no-caps />
    
         
        
      </q-tabs>

      <div class="q-mb-sm q-mt-md" style="font-weight:500; font-size:4.5vw">Duration of Loan</div>

      <q-tabs
        v-model="duration"
        
        active-color="grey-2"
        active-bg-color="blue-grey-6"
        indicator-color="transparent"
        content-class="q-gutter-x-sm  "
        style="width:100%"
      >
        <q-tab
          name="1y"
          label="1y"
          style="border-radius: 10px; border: 2px solid #607d8b "
          no-caps
          exact
          class=""
          
        />
        <q-tab
          name="2y"
          label="2y"
          style="border-radius: 10px; border: 2px solid #607d8b "
          no-caps
          exact
          class=""
          
        />

        <q-tab
          name="3y"
          label="3y"
          style="border-radius: 10px; border: 2px solid #607d8b "
          no-caps
          exact
          class=""
          
        />

        <q-tab
          name="4y"
          label="Other"
          style="border-radius: 10px; border: 2px solid #607d8b "
          no-caps
          exact
          class=""
          
        />

      </q-tabs>


      <div class="q-mb-sm q-mt-lg" style="font-weight:500; font-size:4.5vw">Loan Amount</div>
      
      <div class="flex justify-between items-center no-wrap q-mb-sm">
        <div class="">Quick amounts:</div>
        <div class="q-gutter-x-sm">
          <q-btn unelevated label="1k"  style="background-color:#9FB1BD;color:white" @click="loanAmount = 1000" />
          <q-btn unelevated label="5k" style="background-color:#9FB1BD;color:white" @click="loanAmount = 5000" />
          <q-btn unelevated label="10k" style="background-color:#9FB1BD;color:white" @click="loanAmount = 10000" />
        </div>
      </div>

      <q-input outlined v-model="loanAmount"  type="number" placeholder="Amount" min="0" class="q-mb-md q-mt-md">
        <template v-slot:prepend>
          <q-icon name="o_paid" />
        </template>
      </q-input>


       <div class="q-mb-sm q-mt-lg" style="font-weight:500; font-size:4.5vw">Proof of Income</div>

      <div class="flex justify-between items-center no-wrap">
          <q-file outlined v-model="file" label="Upload Latest Payslip" label-color="white" style="background-color:#607d8b;width:100%" input-style="color:white">
          <template v-slot:prepend>
            <q-icon name="attach_file" color="white" />
          </template>
        </q-file>
      </div>
       
    </div>
    


       <div class="q-px-md q-pb-lg">
         <div class="q-mb-sm q-mt-lg" style="font-weight:500; font-size:4.5vw">Loan Details</div>
         <div class="q-mx-lg q-mt-md">

            <div class="q-mb-md flex items-center " v-if="file && loanAmount"> 
              <q-icon name="check_circle" color="green" style="font-size:6vw; margin-right:5px"/>
              <i>Eligibile for Loan!</i>
            </div>
            <div class="flex justify-between items-center" style="font-size:3.5vw">
              <div class="">Effective Interest Rate (% p.a.)</div>
              <div class="">5.6%</div>
            </div>
            
            <div class="flex justify-between items-center q-mt-md q-mb-md" style="font-size:3.5vw">
              <div class="">Monthly Repayment</div>
              <div class="">SGD 943.56</div>
            </div>

            <div class="flex justify-between items-center">
              <q-btn unelevated :disable="file == null || loanAmount== '' " label="Confirm Loan Application" class=" q-mt-md text-white q-py-xs full-width" no-caps  style="border-radius:5px; background-color:#607d8b"/>
              
            </div>
            

          </div>
       </div>
  </q-page>
</template>

<script>

export default {
  data() {
    return {
      purpose: "Home",
      duration: "2y",
      loanAmount:'',
      file:null
    };
  },
  methods: {},
};
</script>

<style scoped>
</style>
