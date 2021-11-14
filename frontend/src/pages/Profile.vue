<template>
  <q-page v-if="user">
    <div class="row justify-center q-pa-lg">
      <div class="col-md-4 col-xs-12 q-ma-sm">
        <q-card>
          <q-card-section>
            <div class="text-h4 text-weight-medium">Profile</div>
          </q-card-section>

          <q-separator inset />

          <q-card-section>

            <q-input v-model="user.name" class="q-ma-md" disable prefix="Name:">
              <template v-slot:prepend>
                <q-icon name="account_circle" />
              </template>
            </q-input>


            <q-input v-model="user.email" class="q-ma-md" disable prefix="Email:">
              <template v-slot:prepend>
                <q-icon name="mail" />
              </template>
            </q-input>

          </q-card-section>
        </q-card>
      </div>
      <div class="col-md-4 col-xs-12 q-ma-sm">
        <q-card>
          <q-card-section>
            <div class="text-h4 text-weight-medium">Orders history</div>
          </q-card-section>

          <q-separator inset />

          <q-list padding>

            <div v-if="userOrdersHistory.length > 0">
              <q-item v-for="order in userOrdersHistory" :key="order.date" v-ripple clickable>
                <q-item-section>
                  <q-item-label>Date: {{ new Date(order.date).toDateString() }}</q-item-label>
                  <q-item-label caption>
                    Phone: {{ order.phone }}
                  </q-item-label>
                </q-item-section>

                <q-item-section side top>
                  {{ order.address }}
                </q-item-section>

              </q-item>
            </div>
            <div v-else>
              <q-item>
                <q-item-section>
                  <q-item-label>No date available</q-item-label>
                </q-item-section>
              </q-item>
            </div>

          </q-list>
        </q-card>
      </div>
    </div>
  </q-page>
</template>

<script>
import { useStore } from "vuex";
import { computed, ref } from "vue";
import { useRouter } from "vue-router";
import axios from "axios";
import authHeader from "@/services/auth-header";

export default {
  name: "Profile",
  setup() {
    const store = useStore();
    const router = useRouter();
    const user = computed(() => store.state.auth.user);

    if (!user.value) {
      router.push({name: 'login'});
    }

    const userOrdersHistory = ref([]);

    axios
        .get(process.env.VUE_APP_API_URL + '/users/me/orders', {headers: authHeader()})
        .then((res) => {
          userOrdersHistory.value = res.data;
        });

    return {user, userOrdersHistory};
  },
};
</script>
