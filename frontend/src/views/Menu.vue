<template>
  <q-page class="q-pa-md">
    <div>
      <q-splitter v-model="splitterModel" style="height: auto">
        <template v-slot:before>
          <q-tabs v-model="tab" class="text-teal" vertical>
            <q-tab
                v-for="category in categories"
                :key="category.id"
                :label="category.name"
                :name="category.id"
            />
          </q-tabs>
        </template>

        <template v-slot:after>
          <q-tab-panels
              v-model="tab"
              animated
              swipeable
              transition-next="jump-up"
              transition-prev="jump-up"
              vertical
          >
            <q-tab-panel
                v-for="category in categories"
                :key="category.id"
                :name="category.id"
            >
              <div class="text-h4 q-mb-md">{{ category.name }}</div>
              <div class="row">
                <div
                    v-for="itemInfo in category.items"
                    :key="itemInfo.id"
                    class="col-4"
                >
                  <CardMenuItem :itemInfo="itemInfo"/>

                </div>
              </div>
            </q-tab-panel>
          </q-tab-panels>
        </template>
      </q-splitter>
    </div>
  </q-page>
</template>

<script>
import {computed, ref} from 'vue'
import {useStore} from 'vuex'
import CardMenuItem from '../components/CardMenuItem.vue'

export default {
  name: 'Menu',

  components: {CardMenuItem},
  setup() {
    const store = useStore()
    const categories = computed(() => store.state.categories.all)
    store.dispatch('categories/getAllCategories')
    return {
      tab: ref(1),
      splitterModel: ref(20),
      categories,
    }
  },
};
</script>
