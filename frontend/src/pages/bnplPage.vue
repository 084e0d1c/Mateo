<template>
  <q-page class="flex column justify-center items-center" style=""> 
    
      <q-spinner-gears
          color="primary"
          size="30vw"
        />
        <div class="q-mt-sm" style="font-size:5vw;margin-bottom:20vh">Bringing you to Marcus</div>



        <q-dialog v-model="bnplPopup2">
      <q-card class="q-pa-md">
        <div class="absolute" style="right:2vw;top:2vw">
          <q-btn round flat outline icon="close" v-close-popup />
        </div>
        

        <img src="~assets/bnplPic2.svg" alt="" style="width:100%;" class="q-mt-lg">

        <div class="text-center q-mt-md" style="font-size:3.5vw">
          Pay <span style="font-weight:600">a third</span> of your bill now and make another 2 payments over the next 2 months with <br><span style="font-weight:600">0% interest</span>!

        </div>
        <div class="text-center q-my-md" style="font-size:3.5vw; font-weight:600">Become more financially flexible today.</div>
        
      
        
        <q-btn unelevated label="Count Me In!" class="full-width q-mt-xs text-white q-py-xs" no-caps  style="border-radius:5px; background-color:#D9A514" v-close-popup/>


      </q-card>
    </q-dialog>

  </q-page>
</template>

<script>

export default {
  data() {
    return {
      bnplPopup2:true,
    };
  },
  methods: {},
  

  
};
</script>

<style scoped>
</style>
