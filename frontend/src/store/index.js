import { createStore, createLogger } from 'vuex'
import categories from './modules/categories'
import auth from "./modules/auth"
import cart from "./modules/cart"

const debug = process.env.NODE_ENV !== 'production'

export default createStore({
  modules: {
    categories,
    auth,
    cart
  },
  strict: debug,
  plugins: debug ? [createLogger()] : []
})
