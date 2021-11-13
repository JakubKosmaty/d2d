<template>
  <q-list>

    <q-item-label header class="text-h5">Shopping Cart</q-item-label>

    <q-separator />

    <q-item v-for="item in cart" class="q-pa-md" :key="item.id">
      <q-item-section>
        <q-item-label class="text-weight-medium" >{{ item.name }}</q-item-label>
        <q-item-label caption>x{{ item.quantity }}</q-item-label>
      </q-item-section>

      <q-item-section side top>
        <q-badge :label="(item.price * item.quantity).toFixed(2) + ' $'" />
      </q-item-section>
    </q-item>

    <q-separator />

    <q-item clickable v-ripple class="q-pa-md" @click="router.push({name: 'checkout'})">
      <q-item-section avatar>
        <q-avatar color="teal" text-color="white" icon="shopping_cart" />
      </q-item-section>

      <q-item-section>Checkout</q-item-section>


    </q-item>

  </q-list>
</template>

<script>
import {useRouter} from "vue-router";

export default {
  name: "CartList",
  props: ['cart'],
  setup() {
    const router = useRouter()

    return {
      router
    }
  }
}
</script>

<style scoped>

</style>