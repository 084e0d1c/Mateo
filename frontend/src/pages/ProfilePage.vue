<template>
  <q-page class="" style=""> 
    <div class="flex justify-center items-center q-py-sm" style="background:">
      <img src="~assets/profilePic2.jpg" alt="" style="width:30vw; border-radius:100%;margin-top:10px; ">
    </div>
    <q-separator spaced />
    <div class="q-px-md">
      <div class="flex justify-between items-center q-mt-md q-mx-lg">
      <div class="" style="font-weight:500; font-size:3.5vw">Full Name</div>
      <div class="" style=" font-size:3.5vw">Greg G Tan</div>
    </div>

    <div class="flex justify-between items-center q-mt-md q-mx-lg">
      <div class="" style="font-weight:500; font-size:3.5vw">Phone Number</div>
      <div class="" style=" font-size:3.5vw">+65 9022 3288</div>
    </div>

    <div class="flex justify-between items-center q-mt-md q-mx-lg">
      <div class="" style="font-weight:500; font-size:3.5vw">Email</div>
      <div class="" style=" font-size:3.5vw">greggtan99@gmail.com</div>
    </div>
     


     <!-- settings body div -->
    <div class="q-mt-md">
      <div class="bg-white">
        <q-list >
          <q-item clickable v-ripple>
            <q-item-section avatar>
              <q-icon color="primary" name="las la-university" />
            </q-item-section>
            <q-item-section>Link Bank Account</q-item-section>
            <q-item-section avatar>
              <q-icon color="grey-6" size="17px" name="las la-angle-right" />
            </q-item-section>
          </q-item>

          <q-item clickable v-ripple>
            <q-item-section avatar>
              <q-icon color="primary" name="las la-file-invoice-dollar" />
            </q-item-section>
            <q-item-section>My Transaction History</q-item-section>
            <q-item-section avatar>
              <q-icon color="grey-6" size="17px" name="las la-angle-right" />
            </q-item-section>
          </q-item>
          <q-item clickable v-ripple>
            <q-item-section avatar>
              <q-icon color="primary" name="las la-user" />
            </q-item-section>
            <q-item-section>Edit Personal Information</q-item-section>
            <q-item-section avatar>
              <q-icon color="grey-6" size="17px" name="las la-angle-right" />
            </q-item-section>
          </q-item>

          

          
          

           <q-item clickable v-ripple>
            <q-item-section avatar>
              <q-icon color="primary" name="las la-question-circle" />
            </q-item-section>
            <q-item-section>Help & Support</q-item-section>
            <q-item-section avatar>
              <q-icon color="grey-6" size="17px" name="las la-angle-right" />
            </q-item-section>
          </q-item>



          <q-separator spaced />
          <q-item-label header>General</q-item-label>

          <q-item tag="label" v-ripple>
            <q-item-section side top>
              <q-checkbox v-model="check1" color="green" />
            </q-item-section>

            <q-item-section>
              <q-item-label>Notifications</q-item-label>
              <q-item-label caption>
                Notify me about any financial news (loans, insurance etc)
              </q-item-label>
            </q-item-section>
          </q-item>

          <q-item tag="label" v-ripple>
            <q-item-section side top>
              <q-checkbox v-model="check2" color="green"/>
            </q-item-section>

            <q-item-section>
              <q-item-label>Enable Face ID Login</q-item-label>
              <q-item-label caption>
                For a personalized experience
              </q-item-label>
            </q-item-section>
          </q-item>

          
          <q-separator spaced />
          <q-item-label header>Settings</q-item-label>

          

          

          <q-item tag="label" v-ripple>
            <q-item-section>
              <q-item-label>Join Mateo's Mailing List</q-item-label>
              <q-item-label caption
                >To keep up to date with all the latest news</q-item-label
              >
            </q-item-section>
            <q-item-section side top>
              <q-toggle color="red" v-model="notif3" val="picture" />
            </q-item-section>
          </q-item>

          <q-item tag="label" v-ripple>
            <q-item-section>
              <q-item-label>Low battery mode</q-item-label>
            </q-item-section>
            <q-item-section side>
              <q-toggle color="blue" v-model="notif1" val="battery" />
            </q-item-section>
          </q-item>

<!-- 
          <q-item clickable v-ripple class="q-mt-md">
            <q-item-section avatar>
              <q-icon color="red" name="o_logout" />
            </q-item-section>
            <q-item-section class="text-red">Log Out</q-item-section>
           
          </q-item> -->

          <div class="flex justify-center items-center q-my-lg">
            <q-btn outline color="red" icon="o_logout" label="Log Out" style=" padding: 0px 30px" />
            </div>
          
          


          
          

          
        </q-list>
      </div>
    </div>


    </div>

    
    
  </q-page>
</template>

<script>

export default {
  data() {
    return {
       check1: true,
      check2: false,
      check3: false,

      notif1: true,
      notif2: true,
      notif3: false,

      volume: 6,
      brightness: 3,
      mic: 8,
    };
  },
  methods: {},
};
</script>

<style scoped>
</style>
