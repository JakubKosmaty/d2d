const state = {
  all: []
};

const getters = {};

const actions = {
  getAllCategories({commit}) {
    const categories = [
      {
        id: 1,
        name: 'Main Dish',
        items: [
          {
            id: 1,
            name: "Tortillas",
            image_url: 'https://foodhub.scene7.com/is/image/woolworthsltdprod/2006-mexican-chicken-tortillas:Desktop-1300x658',
            price: 5.0
          },
          {
            id: 2,
            name: "Tortillas",
            image_url: 'https://foodhub.scene7.com/is/image/woolworthsltdprod/2006-mexican-chicken-tortillas:Desktop-1300x658',
            price: 5.0
          },
          {
            id: 3,
            name: "Tortillas",
            image_url: 'https://foodhub.scene7.com/is/image/woolworthsltdprod/2006-mexican-chicken-tortillas:Desktop-1300x658',
            price: 5.0
          }
        ]
      },
      {
        id: 2,
        name: 'Sushi',
        items: [
          {
            id: 1,
            name: "Tortillas",
            image_url: 'https://foodhub.scene7.com/is/image/woolworthsltdprod/2006-mexican-chicken-tortillas:Desktop-1300x658',
            price: 5.0
          },
          {
            id: 2,
            name: "Tortillas",
            image_url: 'https://foodhub.scene7.com/is/image/woolworthsltdprod/2006-mexican-chicken-tortillas:Desktop-1300x658',
            price: 5.0
          },
          {
            id: 3,
            name: "Tortillas",
            image_url: 'https://foodhub.scene7.com/is/image/woolworthsltdprod/2006-mexican-chicken-tortillas:Desktop-1300x658',
            price: 5.0
          }
        ]
      },
      {
        id: 3,
        name: 'Desserts',
        items: [
          {
            id: 1,
            name: "Tortillas",
            image_url: 'https://foodhub.scene7.com/is/image/woolworthsltdprod/2006-mexican-chicken-tortillas:Desktop-1300x658',
            price: 5.0
          },
          {
            id: 2,
            name: "Tortillas",
            image_url: 'https://foodhub.scene7.com/is/image/woolworthsltdprod/2006-mexican-chicken-tortillas:Desktop-1300x658',
            price: 5.0
          },
          {
            id: 3,
            name: "Tortillas",
            image_url: 'https://foodhub.scene7.com/is/image/woolworthsltdprod/2006-mexican-chicken-tortillas:Desktop-1300x658',
            price: 5.0
          }
        ]
      }
    ]

    commit('setCategories', categories)
  }
};

const mutations = {
  setCategories(state, categories) {
    state.all = categories;
  }
};

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
};