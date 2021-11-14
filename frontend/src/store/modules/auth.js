import AuthService from '../../services/auth-service';

const userLocal = JSON.parse(localStorage.getItem('user'));
const state = userLocal
  ? {status: {loggedIn: true}, user: userLocal}
  : {status: {loggedIn: false}, user: null};

const getters = {};

const actions = {
  login({commit}, user) {
    return AuthService.login(user).then(
      user => {
        commit('loginSuccess', user);
        return Promise.resolve(user);
      },
      error => {
        commit('loginFailure');
        return Promise.reject(error);
      }
    );
  },
  logout({commit}) {
    AuthService.logout();
    commit('logout');
  },
  register({commit}, user) {
    return AuthService.register(user).then(
      response => {
        commit('registerSuccess');
        return Promise.resolve(response.data);
      },
      error => {
        commit('registerFailure');
        return Promise.reject(error);
      }
    );
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