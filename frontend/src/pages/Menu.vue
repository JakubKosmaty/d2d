<template>
  <q-page>
    <div class="row justify-center q-pa-lg">
      <div class="col-12">
        <q-card>
          <q-card-section>
            <div class="text-h4 text-weight-medium">Menu</div>
          </q-card-section>

          <q-separator inset />

          <q-card-section>
            <q-splitter v-model="splitterModel" style="height: auto">
              <template v-slot:before>
                <q-tabs v-model="tab" class="text-blue" vertical>
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
                    <div class="text-h4 q-ma-md">{{ category.name }}</div>
                    <div class="row">
                      <div
                          v-for="itemInfo in category.items"
                          :key="itemInfo.id"
                          class="col-md-6 col-lg-4 col-sm-12 q-pa-md"
                      >
                        <CardMenuItem :itemInfo="itemInfo" />

                      </div>
                    </div>
                  </q-tab-panel>
                </q-tab-panels>
              </template>
            </q-splitter>
          </q-card-section>
        </q-card>
      </div>
    </div>
  </q-page>
</template>

<script>
import { computed, ref } from 'vue';
import { useStore } from 'vuex';
import CardMenuItem from '../components/CardMenuItem.vue';

export default {
  name: 'Menu',
  components: {CardMenuItem},
  setup() {
    const store = useStore();
    const categories = computed(() => store.state.categories.all);
    store.dispatch('categories/getAllCategories');
    return {
      tab: ref(1),
      splitterModel: ref(12),
      categories,
    };
  },
};
</script>
