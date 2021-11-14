<template>
  <q-layout view="hHh lpR fFf">
    <q-header bordered class="bg-primary text-white">
      <q-toolbar>
        <q-btn dense flat icon="menu" round @click="toggleLeftDrawer" />

        <q-toolbar-title class="text-weight-medium">
          Dinner to Door
        </q-toolbar-title>

        <q-space></q-space>

        <q-toggle
            v-model="third"
            checked-icon="dark_mode"
            color="dark"
            icon-color="white"
            size="lg"
            unchecked-icon="light_mode"
            @click="toggleMode"
        />
      </q-toolbar>
    </q-header>

    <q-drawer v-model="leftDrawerOpen" bordered show-if-above side="left">
      <NavMenuItems />
    </q-drawer>

    <div v-if="currentRoute !== 'checkout' && cart.length > 0">
      <q-drawer v-model="rightDrawerOpen" bordered show-if-above side="right">
        <CartList :cart="cart" />
      </q-drawer>
    </div>

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script>
import { computed, ref } from "vue";
import { useQuasar } from "quasar";
import { useStore } from "vuex";
import { useRouter } from "vue-router";
import NavMenuItems from "../components/NavMenuItems.vue";
import CartList from "@/components/CartList";

export default {
  name: "MainLayout",
  components: {
    CartList,
    NavMenuItems,
  },
  setup() {
    const store = useStore();
    const router = useRouter();
    const leftDrawerOpen = ref(true);
    const third = ref(false);

    const cart = computed(() => store.state.cart.cartItems);
    const currentRoute = computed(() => router.currentRoute.value.name);

    const $q = useQuasar();

    return {
      cart,
      currentRoute,
      third,
      leftDrawerOpen,
      toggleLeftDrawer() {
        leftDrawerOpen.value = !leftDrawerOpen.value;
      },
      toggleMode() {
        $q.dark.set(third.value);
      }
    };
  },
};
</script>
