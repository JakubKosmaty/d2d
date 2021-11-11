const state = {
  all: []
}

const getters = {}

const actions = {
  getAllCategories({commit}) {
    fetch(process.env.VUE_APP_API_URL + '/categories')
      .then(res => res.json())
      .then(data => commit('setCategories', data))
  }
}

const mutations = {
  setCategories(state, categories) {
    state.all = categories
  }
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}