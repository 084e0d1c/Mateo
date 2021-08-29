// import state from './state'
// import * as getters from './getters'
// import * as mutations from './mutations'
// import * as actions from './actions'

const state = {
  user: {
    uid: "",
    name: "",
    accountType: "",
  },
};

const mutations = {
  setName(state, val) {
    state.user.name = val;
  },
  setUID(state, val) {
    state.user.uid = val;
  },
  setAccountType(state, val) {
    state.user.accountType = val;
  },
};

const actions = {
  setName({commit}, val) {
    commit("setName", val)
  }
};

const getters = {
  user: (state) => {
    return state.user;
  },
};

export default {
  namespaced: true,
  state,
  mutations,
  actions,
  getters,
};
