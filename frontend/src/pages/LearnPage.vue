<template>
  <q-page class="" style=""> 
    <div class="full-width">
      <img src="~assets/podcast.svg" alt="" style="width:100%">
    </div>

    <div class="q-px-md q-mt-sm">
      <div class="q-pa-md q-pb-lg shadow-2" style="background:#3E5463; color:#F2F5F7; border-radius:10px; ">
          <div class="">
            
          </div>
          <div class="q-mb-md" style="font-size:4.5vw;font-weight:500">Learning Progress</div>
          <q-linear-progress rounded size="10px" :value="progress"  color="warning" class="q-mt-sm" />
          <div class="q-mt-xs" style="font-weight:500">50% Complete</div>
          
          <div class="q-mt-sm text-justify">You have made some progress on learning about the different types of financial services available to you and how they can help improve your life! Keep going!</div>
      </div>

      <div class="q-mt-sm q-mb-sm" style="font-size:5.5vw; font-weight:500">Tips on Finance</div>


      <carousel  :nav="false" :margin="15" :loop="true" :autoplay="true" :center="true" :items="1" class="">
        <div class="">
          <div class="absolute q-px-sm" style="top:5vw;left:20vw;z-index:1;background:#D4D4D4;border-radius:5px; color:white; font-size:3.5vw">READ</div>
        
            <div class="flex justify-center">
              <div class="shadow-3 q-mb-sm" style="border-radius:20px;width:65vw">
                <img src="~assets/moneyPic.png" alt="" style="width:100%; height:60%;border-top-left-radius:20px;border-top-right-radius:20px;">
                <div class="q-px-md q-pt-sm q-pb-md" style="">
                    <div class="" style="font-size:3.5vw; color:#E2BA4C; font-weight:500">GROW YOUR WEALTH</div>
                    <div class="" style="font-size:4.5vw;font-weight:600">Top 10 Tips to Save Money</div>
                    <!-- <div class="q-mt-xs" style="font-size:3.5vw; max-width:55vw">Learn more about how to grow your savings with several key habits!</div> -->
                </div>
                
              </div>

            
            </div>
        </div>

        <div class="">
          <div class="absolute q-px-sm" style="top:5vw;left:20vw;z-index:1;background:#D4D4D4;border-radius:5px; color:white; font-size:3.5vw">WATCH</div>
        
            <div class="flex justify-center">
              <div class="shadow-3 q-mb-sm" style="border-radius:20px;width:65vw">
                <img src="~assets/house.png" alt="" style="width:100%; height:60%;border-top-left-radius:20px;border-top-right-radius:20px;">
                <div class="q-px-md q-pt-sm q-pb-md" style="">
                    <div class="" style="font-size:3.5vw; color:#E2BA4C; font-weight:500">PROTECT YOURSELF</div>
                    <div class="" style="font-size:4.5vw;font-weight:600">What Types of Insurance Should I Apply For? </div>
                    <!-- <div class="q-mt-xs" style="font-size:3.5vw; max-width:55vw">Learn more about how to grow your savings with several key habits!</div> -->
                </div>
                
              </div>

            
            </div>
        </div>
        

    </carousel>






    </div>
   
    

    
  </q-page>
</template>

<script>
import carousel from 'vue-owl-carousel'
export default {
  components: {  carousel},
  data() {
    return {
      progress:0.5
    };
  },
  methods: {},
  mounted(){
    console.log(this.$route.meta.header)
  }
};
</script>

<style scoped>
</style>
