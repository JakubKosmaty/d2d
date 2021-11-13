<template>


  <q-img class="absolute-top" src="https://cdn.quasar.dev/img/material.png" style="height: 150px">
    <div class="absolute-bottom bg-transparent">
      <div v-if="user">
        <q-avatar class="q-mb-sm" color="teal" icon="person" size="45px"/>
        <div class="text-weight-bold">{{ user.name }}</div>
        <div>{{ user.email }}</div>
      </div>
    </div>
  </q-img>


  <q-scroll-area style="height: calc(100% - 150px); margin-top: 150px; border-right: 1px solid #ddd">
    <q-list class="text-grey-8">

      <q-item v-ripple :to="{name: 'home'}" active-class="menu-active" clickable>
        <q-item-section avatar>
          <q-icon name="home"/>
        </q-item-section>

        <q-item-section>
          <q-item-label>Home</q-item-label>
        </q-item-section>
      </q-item>

      <q-item v-ripple :to="{name: 'menu'}" active-class="menu-active" clickable>
        <q-item-section avatar>
          <q-icon name="lunch_dining"/>
        </q-item-section>

        <q-item-section>
          <q-item-label>Menu</q-item-label>
        </q-item-section>
      </q-item>

      <div v-if="!user">
        <q-item v-ripple :to="{name: 'login'}" active-class="menu-active" clickable>
          <q-item-section avatar>
            <q-icon name="login"/>
          </q-item-section>

          <q-item-section>
            <q-item-label>Login</q-item-label>
          </q-item-section>
        </q-item>

        <q-item v-ripple :to="{name: 'register'}" active-class="menu-active" clickable>
          <q-item-section avatar>
            <q-icon name="app_registration"/>
          </q-item-section>

          <q-item-section>
            <q-item-label>Register</q-item-label>
          </q-item-section>
        </q-item>
      </div>
      <div v-else>
        <q-item v-ripple :to="{name: 'profile'}" active-class="menu-active" clickable>
        <q-item-section avatar>
          <q-icon name="settings"/>
        </q-item-section>

        <q-item-section>
          <q-item-label>Profile</q-item-label>
        </q-item-section>
        </q-item>

        <q-item v-ripple active-class="menu-active" clickable @click="logout">
          <q-item-section avatar>
            <q-icon name="logout"/>
          </q-item-section>

          <q-item-section>
            <q-item-label>Logout</q-item-label>
          </q-item-section>
        </q-item>
      </div>

    </q-list>
  </q-scroll-area>

</template>


<script>
import {useStore} from "vuex"
import {computed} from "vue"
import {useRouter} from "vue-router"

export default {
  name: "NavMenuItems",
  setup() {
    const store = useStore()
    const router = useRouter()
    const user = computed(() => {
      return store.state.auth.user
    })

    const logout = () => {
      store.dispatch('auth/logout')
      router.push({name: 'home'})
    }

    return {user, logout}
  }
}
</script>

<style>
.menu-active {
  color: white;
  background: #F2C037;
}

</style>