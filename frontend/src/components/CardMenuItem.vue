<template>
  <q-card>
    <q-img :src="itemInfo.imageUrl" height="250px" width="100%" />

    <q-card-section>
      <div class="row no-wrap items-center">
        <div class="col text-h6 ellipsis">{{ itemInfo.name }}</div>
      </div>
    </q-card-section>

    <q-card-section class="q-pt-none">
      <div class="text-subtitle1">Price: {{ itemInfo.price }}$</div>
      <div class="text-caption text-grey">
        Small plates, salads & sandwiches in an intimate setting.
      </div>
    </q-card-section>

    <q-separator />

    <q-card-actions align="right">
      <q-btn color="red" flat icon="remove" round @click="removeItemFromCart(itemInfo)" />
      <q-btn color="teal" flat icon="add" round @click="addItemToCart(itemInfo)" />
    </q-card-actions>
  </q-card>
</template>

<script>
import { useStore } from "vuex";

export default {
  name: 'CardMenuItem',
  props: ['itemInfo'],
  setup() {
    const store = useStore();

    const addItemToCart = (item) => store.commit('cart/addItemToCart', item);
    const removeItemFromCart = (item) => store.commit('cart/removeItemFromCart', item);

    return {
      addItemToCart,
      removeItemFromCart
    };
  },
};
</script>
