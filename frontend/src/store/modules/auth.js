import AuthService from '../../services/auth-service';

const userLocal = JSON.parse(localStorage.getItem('user'));
const state = userLocal
  ? {status: {loggedIn: true}, user: userLocal}
  : {status: {loggedIn: false}, user: null};

const getters = {};

const actions = {
  login({commit}, user) {

    const user_test = {
      id: 1,
      name: "Jan Kowalski",
      email: "jan.kowalski@example.com",
      access_token: "TEST",
    };

    commit('loginSuccess', user_test);
    return user;
  },
  logout({commit}) {
    AuthService.logout();
    commit('logout');
  },
  register({commit}, user) {
    commit('registerSuccess');
    return user;
  }
};

const mutations = {
  loginSuccess(state, user) {
    state.status.loggedIn = true;
    state.user = user;
  },
  loginFailure(state) {
    state.status.loggedIn = false;
    state.user = null;
  },
  logout(state) {
    state.status.loggedIn = false;
    state.user = null;
  },
  registerSuccess(state) {
    state.status.loggedIn = false;
  },
  registerFailure(state) {
    state.status.loggedIn = false;
  }
};

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
};