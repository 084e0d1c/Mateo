<template>
  <q-page class="" style="overflow:hidden; background-color:#F2F5F7;"> 
    <div class="bg-white q-pb-xs" >
      <div class="q-pa-md q-pb-lg q-pt-sm q-mx-md" style="background:#DEE9F0;  border-radius:5px;">
      <div class="" style="font-size:4vw">Outstanding Loan</div>

      <div class="flex justify-between items-center">
        <div class="flex items-center">
            <div class="" style="font-size:4.5vw">SGD</div>
            <div class="q-ml-xs" style="font-size:6.5vw;font-weight:500">300.00</div>
        </div>

        <div class="flex items-center">
          <div class="" style="font-size:3.5vw">Interest Rate: </div>
          <div class="q-ml-xs" style="font-size:4.5vw;font-weight:500">10% </div>
        </div>
        
      </div>

      <q-linear-progress rounded size="20px" :value="progress" stripe style="color:#9FB1BD" class="q-mt-sm " />

      <div class="flex justify-between items-center no-wrap q-mt-md">
        <div class="">
            <div class="" style="font-size:3.5vw">Next Payment Due:</div>
            <div class="" style="font-size:4.5vw;font-weight:500">13 Days</div>
        </div>

        <div class="">
          <div class="" style="font-size:3.5vw">Payment Period:</div>
          <div class="" style="font-size:4.5vw;font-weight:500">2 Months </div>
        </div>
        
      </div>

    </div>

    <div class="q-mt-md q-mx-md" style="font-size:4.5vw;font-weight:500">Make a Payment</div>
    <q-separator class="q-mx-md" />

    <div class="q-mt-md q-mb-xs q-mx-md" style="text-align:end; color:#5B7282; font-size:3.5vw">Suggested amount: SGD15.00</div>

     <q-input outlined v-model="paymentAmount"  type="number" placeholder="Amount" min="0" class="q-mb-md q-mx-md">
        <template v-slot:prepend>
          <q-icon name="o_paid" />
        </template>
      </q-input>
    </div>
    


    <div class="" style="">
      <div class="q-mx-md q-mt-sm" style="font-size:4.5vw;font-weight:500">Summary</div>

      <div class="q-mx-lg q-mt-md">
        <div class="flex justify-between items-center" style="font-size:3.5vw">
          <div class="">Current Outstanding Loan</div>
          <div class="">SGD 300.00</div>
        </div>
        
        <div class="flex justify-between items-center q-mt-md q-mb-md" style="font-size:3.5vw">
          <div class="">Loan Payment</div>
          <div class="">SGD {{paymentAmount}}</div>
        </div>

        <q-separator />

        <div class="flex justify-between items-center q-mt-md" style="font-size:3.5vw">
          <div class="">Final Outstanding Loan</div>
          <div class="">SGD {{newOutstanding}}</div>
        </div>

        <q-btn unelevated label="Make Payment" class="full-width q-mt-md text-white q-py-xs" no-caps  style="border-radius:5px; background-color:#607d8b"/>

      </div>
    </div>
    
  </q-page>
</template>

<script>

export default {
  data() {
    return {
      progress:0,
      paymentAmount:'',
      currentOutstanding:300.00,
     

    };
  },
  computed:{
    newOutstanding: function(){
      return this.currentOutstanding - this.paymentAmount
    }
  },
  mounted(){
    this.progress = 0.8
  }
};
</script>

<style scoped>
</style>
