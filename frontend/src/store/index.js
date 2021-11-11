import { createStore, createLogger } from 'vuex'
import categories from './modules/categories'

const debug = process.env.NODE_ENV !== 'production'

export default createStore({
  modules: {
    categories
  },
  strict: debug,
  plugins: debug ? [createLogger()] : []
})
