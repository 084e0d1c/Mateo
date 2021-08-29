import Vue from "vue";
import Vuex from "vuex";

import example from "./module-example";

Vue.use(Vuex);

/*
 * If not building with SSR mode, you can
 * directly export the Store instantiation;
 *
 * The function below can be async too; either use
 * async/await or return a Promise which resolves
 * with the Store instance.
 */

export default function (/* { ssrContext } */) {
  const Store = new Vuex.Store({
    // modules: {
    //   example
    // },

    // enable strict mode (adds overhead!)
    // for dev mode only
    // strict: process.env.DEV

    state: {
      outstandingLoans:45387.81,
      AccessToken:'eyJraWQiOiJEWGFkNW9lZkpkWlhVWm9aMUU1THJ3YXFFVFNzK0YyYkYzYmNSc3E3Y2k0PSIsImFsZyI6IlJTMjU2In0.eyJvcmlnaW5fanRpIjoiOTI4MjU5ZDctYmQ5NC00NGU5LTliYjMtOThhZTU1YWU5NDE0Iiwic3ViIjoiMGEzOGI2MjgtN2Y2Yy00YzI5LWFmOTMtMDk1Y2RhZTA3ZTQxIiwiZXZlbnRfaWQiOiJkMWIxNDM0MS05YzQ0LTQ5MGItYWE1MS1mMzk0OGIyZDllM2EiLCJ0b2tlbl91c2UiOiJhY2Nlc3MiLCJzY29wZSI6ImF3cy5jb2duaXRvLnNpZ25pbi51c2VyLmFkbWluIiwiYXV0aF90aW1lIjoxNjMwMjE3MTI4LCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAuYXAtc291dGhlYXN0LTEuYW1hem9uYXdzLmNvbVwvYXAtc291dGhlYXN0LTFfWEJqQ1l5d3FDIiwiZXhwIjoxNjMwMzAzNTI4LCJpYXQiOjE2MzAyMTcxMjgsImp0aSI6IjhjYjQ5MDNmLTJhZjYtNDAzZC05N2VkLWFiMGIyOTUxMjcyOSIsImNsaWVudF9pZCI6IjZsNGwwcHZ1Z251NXJvbWxiZjNpN3MyYWo1IiwidXNlcm5hbWUiOiJVc2VyMyJ9.kF4cYS3WJr7sJmQb-_zfaJrOVdVpTTzXRTlZlBR-MvEz32wVE5zt0OoRDd4DcAscbyDzOGE_XGS6RV6q9N_JFlCQqYpKdJRJaJc34tQgi4vykbmrFuOxRnAxohekAUmTYs7QgLbFXBYS4NOHf4WLi7DLljXT0PvIy9WRf17oBNUONUfqcG-f6iZ8Bo--nZOQtZlva_jRC29RxBXrtBg-TOE0bhKzSWfGEFXst8oXPNUCxJTG-UplVmm86Q5_KnmXXi6BorIoImMF8istrlsVMxs4amGs0jnW8gqI-h4OUtJMVRFeaIv7x4t-LAAtvZogTcg52Pe9F9n1xBQYcDk5EA'

    },
    getters:{
      
    },
    mutations: {
      storeAccessToken(state, AccessToken){
        state.AccessToken = AccessToken
      }
    },
    actions: {
      
    },
    
  });

  return Store;
}
