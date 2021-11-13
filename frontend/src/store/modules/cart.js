const state = {
  cartItems: []
}

const getters = {}

const actions = {}

const getItemIndex = (cart, inputItem) => {
  return cart.findIndex(function (item, index) {
    if (item.id === inputItem.id) {
      return true;
    }
  })
}

const mutations = {
  addItemToCart(state, item) {
    const itemIndex = getItemIndex(state.cartItems, item)

    if (itemIndex === -1) {
      item.quantity = 1
      state.cartItems.push(item)
    } else {
      state.cartItems[itemIndex].quantity++
    }
  },
  removeItemFromCart(state, item) {
    const itemIndex = getItemIndex(state.cartItems, item)

    if (itemIndex !== -1) {
      if (state.cartItems[itemIndex].quantity === 1) {
        state.cartItems = state.cartItems.filter(el => el.id !== item.id)
      } else {
        state.cartItems[itemIndex].quantity--
      }
    }
  }
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}