<template>
  <q-scroll-area class="fit">
    <q-list padding class="">
      <q-item to="/" v-ripple clickable>
        <q-item-section avatar>
          <q-icon name="home" />
        </q-item-section>

        <q-item-section>
          <q-item-label>Home</q-item-label>
        </q-item-section>
      </q-item>

      <q-item to="/menu" v-ripple clickable>
        <q-item-section avatar>
          <q-icon name="folder" />
        </q-item-section>

        <q-item-section>
          <q-item-label>Menu</q-item-label>
        </q-item-section>
      </q-item>
    </q-list>
  </q-scroll-area>
</template>

<script>

export default {
  name: 'NavMenuItems',
};
</script>
