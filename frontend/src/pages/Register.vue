<template>
  <q-page>
    <div class="row justify-center q-pa-lg">
      <div class="col-md-4 col-xs-12">
        <q-card>
          <q-card-section>
            <div class="text-h4 text-weight-medium">Register</div>
          </q-card-section>

          <q-separator inset />

          <q-card-section>

            <q-form
                class="q-gutter-md"
                @submit="onSubmit"
            >
              <q-input v-model="name" filled prefix="Name:">
                <template v-slot:prepend>
                  <q-icon name="account_circle" />
                </template>
              </q-input>


              <q-input v-model="email" filled prefix="Email:" type="email">
                <template v-slot:prepend>
                  <q-icon name="mail" />
                </template>
              </q-input>

              <q-input v-model="password" :type="isPwd ? 'password' : 'text'" filled prefix="Password:">
                <template v-slot:prepend>
                  <q-icon name="lock" />
                </template>
                <template v-slot:append>
                  <q-icon
                      :name="isPwd ? 'visibility_off' : 'visibility'"
                      class="cursor-pointer"
                      @click="isPwd = !isPwd"
                  />
                </template>
              </q-input>

              <q-input v-model="confirmPassword" :type="isPwd ? 'password' : 'text'" filled prefix="Confirm Password:">
                <template v-slot:prepend>
                  <q-icon name="lock" />
                </template>
                <template v-slot:append>
                  <q-icon
                      :name="isPwd ? 'visibility_off' : 'visibility'"
                      class="cursor-pointer"
                      @click="isPwd = !isPwd"
                  />
                </template>
              </q-input>

              <div>
                <q-btn color="primary" label="Register" type="submit" />
              </div>
            </q-form>
          </q-card-section>
        </q-card>
      </div>
    </div>
  </q-page>
</template>

<script>
import { ref } from 'vue';
import { useStore } from "vuex";
import { useRouter } from "vue-router";
import { useQuasar } from "quasar";

export default {
  name: "Register",
  setup() {
    const name = ref(null);
    const email = ref(null);
    const password = ref(null);
    const confirmPassword = ref(null);

    const isPwd = ref(true);
    const store = useStore();
    const router = useRouter();

    const $q = useQuasar()

    const onSubmit = () => {
      if (password.value !== confirmPassword.value) {
        return;
      }

      store.dispatch('auth/register', {
        name: name.value,
        email: email.value,
        password: password.value
      }).then(
          () => {
            $q.notify({
              type: 'positive',
              message: 'Successfully Register',
              position: 'bottom-right'
            })

            router.push({name: 'login'});
          },
          (error) => {
            $q.notify({
              type: 'negative',
              message: 'Invalid Data',
              position: 'bottom-right'
            })
          }
      );
    };

    const routeToRegister = () => router.push({name: 'register'});

    return {
      name,
      email,
      password,
      confirmPassword,
      isPwd,
      onSubmit,
      routeToRegister
    };
  },
};
</script>
