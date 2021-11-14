<template>
  <q-page>
    <div class="row justify-center q-pa-lg">
      <div class="col-md-4 col-xs-12">
        <q-card>
          <q-card-section>
            <div class="text-h4 text-weight-medium">Login</div>
          </q-card-section>

          <q-separator inset />

          <q-card-section>

            <q-form
                class="q-gutter-md"
                @submit="onSubmit"
            >
              <!--              <q-input v-model="email" filled prefix="Email:" type="email">-->
              <q-input v-model="email" filled prefix="Email:">
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

              <div>
                <q-btn color="primary" label="Login" type="submit" />
                <q-btn class="q-ml-sm" color="primary" flat label="Don't have account?" @click="routeToRegister" />
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

export default {
  name: "Login",
  setup() {
    const email = ref(null);
    const password = ref(null);
    const isPwd = ref(true);
    const store = useStore();
    const router = useRouter();

    const onSubmit = () => {
      store.dispatch('auth/login', {
        email: email.value,
        password: password.value
      }).then(
          () => {
            router.push({name: 'profile'});
          },
          (error) => {
            console.log(error);
          }
      );
    };

    const routeToRegister = () => router.push({name: 'register'});

    return {
      email,
      password,
      isPwd,
      onSubmit,
      routeToRegister
    };
  },
};
</script>
