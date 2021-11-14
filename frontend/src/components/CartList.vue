<template>
  <q-list>
    <q-item-label class="text-h5" header>Shopping Cart</q-item-label>

    <q-separator />

    <q-item v-for="item in cart" :key="item.id" class="q-pa-md">
      <q-item-section>
        <q-item-label class="text-weight-medium">{{ item.name }}</q-item-label>
        <q-item-label caption>x{{ item.quantity }}</q-item-label>
      </q-item-section>

      <q-item-section side top>
        <q-badge :label="(item.price * item.quantity).toFixed(2) + '$'" />
      </q-item-section>
    </q-item>

    <q-separator />

    <q-item v-ripple class="q-pa-md" clickable @click="router.push({name: 'checkout'})">
      <q-item-section avatar>
        <q-avatar color="teal" icon="shopping_cart" text-color="white" />
      </q-item-section>

      <q-item-section>Checkout</q-item-section>
    </q-item>

  </q-list>
</template>

<script>
import { useRouter } from "vue-router";

export default {
  name: "CartList",
  props: ['cart'],
  setup() {
    const router = useRouter();

    return {
      router
    };
  }
};
</script>
