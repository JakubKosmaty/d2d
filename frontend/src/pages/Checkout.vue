<template>
  <q-page v-if="user">
    <div class="row justify-center q-pa-lg">
      <div class="col-md-4 col-xs-12 q-ma-sm">
        <q-card>
          <q-card-section>
            <div class="text-h4 text-weight-medium">Delivery details</div>
          </q-card-section>

          <q-separator inset/>


          <q-card-section>


            <q-input v-model="user.name" class="q-ma-md" disable prefix="Name:">
              <template v-slot:prepend>
                <q-icon name="account_circle"/>
              </template>
            </q-input>


            <q-input v-model="user.email" class="q-ma-md" disable prefix="Email:">
              <template v-slot:prepend>
                <q-icon name="mail"/>
              </template>
            </q-input>

            <q-input v-model="address" class="q-ma-md" prefix="Address:">
              <template v-slot:prepend>
                <q-icon name="apartment"/>
              </template>
            </q-input>

            <q-input v-model="phone" class="q-ma-md" prefix="Phone:">
              <template v-slot:prepend>
                <q-icon name="smartphone"/>
              </template>
            </q-input>


          </q-card-section>
        </q-card>
      </div>
      <div class="col-md-4 col-xs-12 q-ma-sm">
        <q-card>
          <q-card-section>
            <div class="text-h4 text-weight-medium">Order details</div>
          </q-card-section>

          <q-separator inset/>

          <q-list bordered padding>
            <q-item-label header>Products</q-item-label>

            <q-item v-for="item in cart" :key="item.id" v-ripple clickable>
              <q-item-section>
                <q-item-label>{{ item.name }} </q-item-label>
                <q-item-label caption>
                  x{{ item.quantity }}
                </q-item-label>
              </q-item-section>

              <q-item-section side top>
                Price {{ (item.price * item.quantity).toFixed(2)}}$
              </q-item-section>

            </q-item>

            <q-separator spaced />
            <q-item-label header class="text-weight-bold">Sum: {{totalPrice}}$</q-item-label>

          </q-list>

          <q-card-actions vertical align="center">
            <q-btn color="purple" class="full-width">Order</q-btn>
          </q-card-actions>
        </q-card>
      </div>
    </div>
  </q-page>
</template>

<script>
import {computed, ref} from 'vue'
import {useStore} from "vuex";
import {useRouter} from "vue-router";

export default {
  name: "Checkout",
  setup() {
    const store = useStore()
    const router = useRouter()

    const address = ref(null)
    const phone = ref(null)

    const user = computed(() => store.state.auth.user)
    const cart = computed(() => store.state.cart.cartItems)

    const totalPrice = computed(() => {
      let tempPrice = 0
      for (let item of cart.value) {
        console.log(item)
        tempPrice += item.quantity * item.price
      }
      return tempPrice
    })

    if (!user.value) {
      router.push({name: 'login'})
    }

    return {
      user,
      cart,
      totalPrice,
      address,
      phone
    }
  },
};
</script>
