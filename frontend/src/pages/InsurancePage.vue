<template>
  <q-page class="flex column justify-around items-center " style=""> 

    
      <!-- health insurance -->
     <q-expansion-item expand-icon-class="hidden" class="">
        <template v-slot:header >
          <div class="flex justify-center full-width">
            <img src="~assets/healthInsurance.svg" style="width:85vw" alt="">
            </div>

          <div class="absolute-center text-start text-white" style="font-size:7vw; width:80% ">Health Insurance</div>
          
          
        </template>

        <div class="flex justify-center items-center">
            <q-card class="q-px-lg q-py-md " style="width:85vw;">
          <div class="q-gutter-y-sm">
            <div class="flex items-center no-wrap">
            <q-icon name="las la-file-invoice-dollar" size="8vw" style="color:#3E5463" />
            <div class="q-ml-md" style="font-size:4vw">Cover overseas medical expenses</div>
          </div>

          <div class="flex  items-center no-wrap">
            <q-icon name="accessible" size="8vw" style="color:#3E5463" />
            <div class="q-ml-md" style="font-size:4vw">Protect yourself with disability benefits</div>
          </div>

          <div class="flex items-center no-wrap">
            <q-icon name="las la-hospital" size="8vw" style="color:#3E5463" />
            <div class="q-ml-md" style="font-size:4vw">Cash supplements during hospitalization</div>
          </div>
          </div>
          
          <div class="flex justify-end items-center">
            <q-btn label="Apply Now" unelevated style="background-color:rgb(62, 84, 99);color:white" class="q-mt-md" />
          </div>
          
        </q-card>
        </div>
        
      </q-expansion-item>


      <q-expansion-item expand-icon-class="hidden" class="">
        <template v-slot:header >
          <div class="flex justify-center full-width">
            <img src="~assets/homeInsurancePic.svg" style="width:88vw" alt="">
            </div>

          <div class="absolute-center text-start text-white" style="font-size:7vw; width:80% ">Home Insurance</div>
          
          
        </template>

        <div class="flex justify-center items-center">
            <q-card class="q-px-lg q-py-md " style="width:85vw;">
          <div class="q-gutter-y-sm">
            <div class="flex items-center no-wrap">
            <q-icon name="las la-fire-extinguisher" size="8vw" style="color:#3E5463" />
            <div class="q-ml-md" style="font-size:4vw">Cover damage from fires to your home</div>
          </div>

          <div class="flex  items-center no-wrap">
            <q-icon name="las la-shield-alt" size="8vw" style="color:#3E5463" />
            <div class="q-ml-md" style="font-size:4vw">Insure yourself against plumbing failure</div>
          </div>

          <div class="flex items-center no-wrap">
            <q-icon name="las la-user-secret" size="8vw" style="color:#3E5463" />
            <div class="q-ml-md" style="font-size:4vw">Protect yourself from loss due to theft</div>
          </div>
          </div>
          
          <div class="flex justify-end items-center">
            <q-btn label="Apply Now" unelevated style="background-color:rgb(62, 84, 99);color:white" class="q-mt-md" />
          </div>
          
        </q-card>
        </div>
        
      </q-expansion-item>
    
      <!-- vehicle insurance -->
       <q-expansion-item expand-icon-class="hidden" class="">
        <template v-slot:header >
          <div class="flex justify-center full-width">
            <img src="~assets/vehicleInsurancePic.svg" style="width:89vw" alt="">
            </div>

          <div class="absolute-center text-start text-white" style="font-size:7vw; width:80% ">Vehicle Insurance</div>
          
          
        </template>

        <div class="flex justify-center items-center">
            <q-card class="q-px-lg q-py-md " style="width:85vw;">
          <div class="q-gutter-y-sm">
            <div class="flex items-center no-wrap">
            <q-icon name="las la-hammer" size="8vw" style="color:#3E5463" />
            <div class="q-ml-md" style="font-size:4vw">Cover repair expenses from accidents</div>
          </div>

          <div class="flex  items-center no-wrap">
            <q-icon name="las la-shield-alt" size="8vw" style="color:#3E5463" />
            <div class="q-ml-md" style="font-size:4vw">Cover towing services after accidents</div>
          </div>

          <div class="flex items-center no-wrap">
            <q-icon name="las la-car-crash" size="8vw" style="color:#3E5463" />
            <div class="q-ml-md" style="font-size:4vw">Cover damage to 3rd party property</div>
          </div>
          </div>
          
          <div class="flex justify-end items-center">
            <q-btn label="Apply Now" unelevated style="background-color:rgb(62, 84, 99);color:white" class="q-mt-md" />
          </div>
          
        </q-card>
        </div>
        
      </q-expansion-item>

       <!-- travek insurance -->
       <q-expansion-item expand-icon-class="hidden" class="">
        <template v-slot:header >
          <div class="flex justify-center full-width">
            <img src="~assets/travelInsurancePic.svg" style="width:89vw" alt="">
            </div>

          <div class="absolute-center text-start text-white" style="font-size:7vw; width:80% ">Travel Insurance</div>
          
          
        </template>

        <div class="flex justify-center items-center q-mb-md">
            <q-card class="q-px-lg q-py-md " style="width:85vw;">
          <div class="q-gutter-y-sm">
            <div class="flex items-center no-wrap">
            <q-icon name="las la-file-medical" size="8vw" style="color:#3E5463" />
            <div class="q-ml-md" style="font-size:4vw">Cover overseas medical expenses</div>
          </div>

          <div class="flex  items-center no-wrap">
            <q-icon name="las la-suitcase" size="8vw" style="color:#3E5463" />
            <div class="q-ml-md" style="font-size:4vw">Protect against baggage loss or damage</div>
          </div>

          <div class="flex items-center no-wrap">
            <q-icon name="las la-money-check" size="8vw" style="color:#3E5463" />
            <div class="q-ml-md" style="font-size:4vw">Insure against exciting sports activities</div>
          </div>
          </div>
          
          <div class="flex justify-end items-center">
            <q-btn label="Apply Now" unelevated style="background-color:rgb(62, 84, 99);color:white" class="q-mt-md" />
          </div>
          
        </q-card>
        </div>
        
      </q-expansion-item>
    
    
  </q-page>
</template>

<script>

export default {
  data() {
    return {};
  },
  methods: {},
};
</script>

<style scoped>
</style>
