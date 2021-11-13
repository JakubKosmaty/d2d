<template>
  <q-page v-if="user">
    <div class="row justify-center q-pa-lg">
      <div class="col-md-4 col-xs-12">
        <q-card>
          <q-card-section>
            <div class="text-h4 text-weight-medium">Profile</div>
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


          </q-card-section>
        </q-card>
      </div>
    </div>
  </q-page>
</template>

<script>
import {useStore} from "vuex";
import {computed} from "vue";
import {useRouter} from "vue-router";

export default {
  name: "Profile",
  setup() {
    const store = useStore()
    const router = useRouter()
    const user = computed(() => store.state.auth.user)

    if (!user.value) {
      router.push({name: 'login'})
    }

    return {user}
  },
};
</script>
