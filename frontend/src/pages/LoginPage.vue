<template>
  <q-page class="flex justify-center items-center q-pb-lg" style="height: 100%">
    <div class="flex justify-center items-center">
      <img src="~assets/logo.svg" alt="" />
    </div>

    <div class="" style="width: ">
      <img
        src="~assets/loginPic.svg"
        alt=""
        style="
          width: 100vw;
          clip-path: polygon(100% 0, 100% 81%, 0 100%, 0 17%);
        "
      />
    </div>

    <div class="flex column justify-center items-center">
      <q-btn
        dense
        unelevated
        label="Log In"
        class="q-mt-md text-white q-py-xs"
        no-caps
        style="border-radius: 5px; background-color: #607d8b; width: 80vw"
        @click="loginPopup = true"
      />

      <q-btn
        dense
        unelevated
        outline
        label="Sign Up"
        class="q-mt-md q-py-xs"
        no-caps
        style="border-radius: 5px; width: 80vw"
        @click="signupPopup = true"
      />
    </div>

    <!-- login dialog -->
    <q-dialog v-model="loginPopup" position="bottom" style="">
      <q-card
        style="height: 48vh; padding-bottom: 4vh"
        class="flex justify-center items-center"
      >
        <div class="" style="width: 85vw">
          <div class="" style="font-size: 4.5vw; font-weight: 600">
            Log into your account
          </div>

          <div class="flex column justify-between no-wrap" style=""></div>

          <div class="q-mt-sm q-gutter-y-md">
            <q-input v-model="username" label="Username" outlined autofocus>
              
            </q-input>

            <q-input
              v-model="password"
              :type="isPwd ? 'password' : 'text'"
              label="Enter your password"
              outlined
              input-style=""
              style="width: 100%"
            >
              <template v-slot:prepend>
                <q-icon name="eva-lock-outline" size="20px" />
              </template>
              <template v-slot:append>
                <q-icon
                  size="20px"
                  :name="isPwd ? 'visibility_off' : 'visibility'"
                  class="cursor-pointer"
                  @click="isPwd = !isPwd"
                />
              </template>
            </q-input>
          </div>
        </div>

        <div class="flex justify-center items-center column">
          <q-btn
            dense
            unelevated
            label="Log In"
            class="text-white q-py-xs"
            no-caps
            style="
              border-radius: 5px;
              background-color: #607d8b;
              width: 85vw;
              margin-top: 5vw;
            "
            @click="login()"
          />

          <q-btn
            dense
            unelevated
            label="Forget your password?"
            class="q-mt-md q-py-xs"
            no-caps
            style="border-radius: 5px; width: 100%"
          />
        </div>
      </q-card>
    </q-dialog>

    <!-- signup dialog -->
    <q-dialog v-model="signupPopup" position="bottom" style="">
      <q-card
        style="padding-top: 4vh; padding-bottom: 4vh"
        class="flex justify-center items-center"
      >
        <div class="" style="width: 85vw">
          <div class="" style="font-size: 4.5vw; font-weight: 600">
            Sign up for Mateo!
          </div>

          <div class="q-mt-sm q-gutter-y-md">
            <q-input
              v-model="signupUsername"
              label="Username"
              outlined
              autofocus
              bottom-slots
            >
             
            </q-input>

            <q-input
              v-model="signupEmail"
              label="Email"
              outlined
              autofocus
              :rules="[(val) => !!val || 'Email is missing', isValidEmail]"
            >
              <template v-slot:prepend>
                <q-icon name="eva-email-outline" size="20px" />
              </template>
            </q-input>

            <q-input
              v-model="signupPassword"
              :rules="[
                (val) => val.length >= 8 || 'Please use minimum 8 characters',
              ]"
              :type="isPwd ? 'password' : 'text'"
              label="Enter your password"
              outlined
              input-style=""
              style="width: 100%"
              bottom-slots
            >
              <template v-slot:prepend>
                <q-icon name="eva-lock-outline" size="20px" />
              </template>
              <template v-slot:append>
                <q-icon
                  size="20px"
                  :name="isPwd ? 'visibility_off' : 'visibility'"
                  class="cursor-pointer"
                  @click="isPwd = !isPwd"
                />
              </template>
              <template v-slot:hint>
                We recommend adding at least one number, special character,
                lowercase letter and uppercase letter.
              </template>
            </q-input>
          </div>
        </div>

        <div class="flex justify-center items-center column">
          <q-btn
          :disable="!signupUsername || !isValidEmail(signupEmail) || !signupPassword"
            dense
            unelevated
            label="Sign Up"
            class="text-white q-py-xs"
            no-caps
            style="
              border-radius: 5px;
              background-color: #607d8b;
              width: 85vw;
              margin-top: 10vw;
            "
            @click="signupPopup2 = true"
          />
          <!-- <div class="q-mt-sm" style="width: 85vw; font-size: 3vw">
            By creating a new account, you accept our
            <span style="color: #0caf88; text-decoration: underline">
              terms and conditions</span
            >
            as well as
            <span style="color: #0caf88; text-decoration: underline">
              privacy policy</span
            >.
          </div> -->
        </div>
      </q-card>
    </q-dialog>

    <!-- signup2 dialog -->
    <q-dialog v-model="signupPopup2">
      <q-card style="height: 50vh; width:90vw"
        class="flex justify-center items-center ">
        <div class="absolute" style="right:2vw;top:2vw">
          <q-btn round flat outline icon="close" @click="handleSignUp2Close()" />
        </div>

        <div class="q-gutter-y-md">
            <div class="text-center " style="color:#5B7282; font-size:4vw">
                <div class="" style="margin-bottom:2vw">You're almost done!</div>
                <div class="" style="margin-bottom:5vw">Help us set up your profile.</div>
            </div>
             <q-input v-model="signupName" label="Full Name" outlined autofocus style="width:70vw">
              <template v-slot:prepend>
                <q-icon name="las la-user" size="20px" />
              </template>
            </q-input>


            <q-input v-model="signupPhone" type="number" label="Phone Number" outlined autofocus style="width:70vw">
              <template v-slot:prepend>
                <q-icon name="las la-phone" size="20px" />
              </template>
            </q-input>

            <div class="flex justify-center items-center">
                 <q-btn
                        
                        dense
                        unelevated
                        label="Create a New Account"
                        class="text-white q-py-xs"
                        no-caps
                        style="
                        border-radius: 5px;
                        background-color: #607d8b;
                        width:100%;
                        margin-top: 3vw;
                        "
                        @click="signUp()"
                    />

                    
                    
            </div>

            <div class="q-mt-sm" style="width: 70vw; font-size: 3vw">
            By creating a new account, you accept our
            <span style="color: #0caf88; text-decoration: underline">
              terms and conditions</span
            >
            as well as
            <span style="color: #0caf88; text-decoration: underline">
              privacy policy</span
            >.
          </div>


           
        </div>
        

       
        


        
      </q-card>
    </q-dialog>


  </q-page>
</template>

<script>
var axios = require("axios");
export default {
  data() {
    return {
      loginPopup: false,
      signupPopup: false,
      signupPopup2:false,
      isPwd: true,
      username: "",
      password: "",

      signupUsername: "",
      signupEmail: "",
      signupPassword: "",
      signupName:'',
      signupPhone:''
    };
  },
  methods: {
    isValidEmail(val) {
      const emailPattern =
        /^(?=[a-zA-Z0-9@._%+-]{6,254}$)[a-zA-Z0-9._%+-]{1,64}@(?:[a-zA-Z0-9-]{1,63}\.){1,8}[a-zA-Z]{2,63}$/;


      return emailPattern.test(val) || "Invalid email";
    },
    handleSignUp2Close(){
        this.signupPopup2 = false
        this.signupPopup = true
    },
    async signUp() {

      var data = JSON.stringify({
        email: this.signupEmail,
        password: this.signupPassword,
        username: this.signupUsername,
        phone: this.signupName,
        fullname: this.signupPhone,
      });
      console.log(data);

      var config = {
        method: "post",
        url: "https://k9k7c7vvdb.execute-api.ap-southeast-1.amazonaws.com/dev/user/signup",
        headers: {
          "Content-Type": "application/json",
        },
        data: data,
      };

      try {
        let response = await axios(config);
        console.log(response.data);

        // trigger success popup

      } catch (error) {
        console.log(error);

        // trigger error for sign up popup
      }
    },

    async login() {
      var data = JSON.stringify({
        password: this.password,
        username: this.username,
      });
      var config = {
        method: "post",
        url: "https://k9k7c7vvdb.execute-api.ap-southeast-1.amazonaws.com/dev/user/login",
        headers: {
          "Content-Type": "application/json",
        },
        data: data,
      };

      try {
        let response = await axios(config);
        console.log(response.data.body.AccessToken);

        // mutate state
        // this.$store.state.AccessToken = response.data.body.AccessToken

        this.$store.commit("storeAccessToken", response.data.body.AccessToken);

        console.log(this.$store.state.AccessToken);

        var config = {
          method: 'get',
          url: 'https://k9k7c7vvdb.execute-api.ap-southeast-1.amazonaws.com/dev/user/plaid-link-token',
          headers: { 
            'Authorization': `Bearer ${this.$store.state.AccessToken}`
          },
          data : data
        }


        try{
          let response = await axios(config);
          console.log(response.data.data.link_token)

          this.$store.commit("storeLinkToken", response.data.data.link_token);
          this.$router.push('/home')
        }catch (err){
          console.log(err)
        }
        
      } catch (error) {
        console.log(error);
        // trigger the invalid username / password popup here
      }
    },
  },
  async mounted() {
    console.log(this.$store.state.outstandingLoans);
  },
};
</script>

<style scoped>
</style>
