<template>
    <div class="cursor-pointer">{{metricName}}
                <q-tooltip
                  anchor="center left" 
                  self="center right"
                  :offset="[10, 10]"
                  class="bg-blue-grey-7"
                  max-width="15rem"
                  content-style="overflow:hidden;"
                >
                  <div class="text-justify" style="font-size: 13px">
                  {{metricDescription}} 
                  </div>
                </q-tooltip>
    </div>
    
</template>
<script>
export default {
    props: {
      metricName:
      {
          type:String
          },
      metricDescription:
      {
          type:String
          },
  },
}
</script>