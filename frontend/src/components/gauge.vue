<template>
  <div class="">
    <div class="" style="color: #7e96b8; font-size: 1.1vw">
        <metricToolTip 
              :metricName="gaugeHeader" 
              :metricDescription="metricDescription" />
      
    </div>
    <div class="flex justify-center no-wrap q-mt-md">
      <VueSvgGauge
        :start-angle="-90"
        :end-angle="90"
        :value="gaugeValue"
        :separator-step="20"
        :min="0"
        :max="100"
        base-color="#C1C1C1"
        :gauge-color="computedGaugeColor"
        :scale-interval="20"
        :inner-radius="65"
        style="width: 75%"
      >
        <div
          class="
            inner-text
            flex
            justify-center
            items-center
            text-center 
          "
          :class="{'text-red':isRed,  'text-yellow':isYellow,'text-green':isGreen}"
          style="margin-top: 35px"
        >
          {{status}}
        </div>
      </VueSvgGauge>
    </div>
  </div>
</template>

<script>
import { VueSvgGauge } from "vue-svg-gauge";
import metricToolTip from "../components/metricToolTip.vue"
export default {
  props: {
      gaugeHeader:
      {
          type:String
          },
      gaugeValue:{
          type: [Number, String],
          required: true
      },
      metricDescription:{
          type: String
      }
  },
  components: {
    VueSvgGauge,
    metricToolTip
  },
  data() {
    return {
        status:'',
        computedGaugeColor:[],
        isRed:false,
        isYellow:false,
        isGreen:false
    };
  },
//   to change the values based on the change in gauge value
  watch:{
      gaugeValue : function() {
          console.log('gauge value has changed', this.gaugeValue)
          if (this.gaugeValue < 20){
                this.status = 'Very Low'
                this.computedGaugeColor = 
        [
                { offset: 0, color: 'red' },
                { offset: 100, color: '#8CDFAD' },
              ]
                this.isRed = true
                this.isYellow = false
                this.isGreen = false
            } else if (this.gaugeValue <40){
                this.status = "Low"
                this.computedGaugeColor = 
        [
                { offset: 0, color: 'red' },
                { offset: 100, color: '#8CDFAD' },
              ]
                this.isRed = true
                this.isYellow = false
                this.isGreen = false
            }else if (this.gaugeValue <60){
                this.status = "Medium"
                this.computedGaugeColor = [
                { offset: 0, color: '#b39306' },
                { offset: 100, color: '#e6bc04' },
                ]
                this.isYellow = true
                this.isRed = false
                this.isGreen = false
            }else if (this.gaugeValue <80){
                this.status = "High"
                this.computedGaugeColor = [
                { offset: 0, color: '#209E1E' },
                { offset: 100, color: '#8CDFAD' },
                ]
                this.isGreen = true
                this.isYellow = false
                this.isRed = false
            }else{
                this.status = 'Very High'
                this.computedGaugeColor = [
                { offset: 0, color: '#209E1E' },
                { offset: 100, color: '#8CDFAD' },
                ]
                this.isGreen = true
                 this.isYellow = false
                this.isRed = false
            }
      }
  },
  mounted(){
      
      this.computedGaugeColor = 
        [
                { offset: 0, color: 'red' },
                { offset: 100, color: '#8CDFAD' },
              ]
      
      console.log(this.gaugeValue)
      
      if (this.gaugeValue < 20){
          this.status = 'Very Low'
          this.isRed = true
      } else if (this.gaugeValue <40){
          this.status = "Low"
          this.isRed = true
      }else if (this.gaugeValue <60){
          this.status = "Medium"
          this.computedGaugeColor = [
          { offset: 0, color: '#b39306' },
          { offset: 100, color: '#e6bc04' },
        ]
        this.isYellow = true
      }else if (this.gaugeValue <80){
          this.status = "High"
          this.computedGaugeColor = [
          { offset: 0, color: '#209E1E' },
          { offset: 100, color: '#8CDFAD' },
        ]
        this.isGreen = true
      }else{
          this.status = 'Very High'
          this.computedGaugeColor = [
          { offset: 0, color: '#209E1E' },
          { offset: 100, color: '#8CDFAD' },
        ]
        this.isGreen = true
      }


       console.log(this.status, this.gaugeValue)
  }
};
</script>

<style lang="scss">
.inner-text {
  // allow the text to take all the available space in the svg on top of the gauge
  height: 100%;
  width: 100%;

  span {
    max-width: 100px;
    
    // ...
  }
}
</style> 