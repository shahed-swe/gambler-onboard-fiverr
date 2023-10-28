import Vue from 'vue';
import Vuelidate from 'vuelidate';
import VueTimeago from 'vue-timeago';
import Clipboard from 'v-clipboard';

import popups from '@/mixins/popups';

function loadPlugins() {
  Vue.use(Vuelidate);
  Vue.use(VueTimeago, {name: 'timeago', locale: 'en'});
  Vue.use(Clipboard);
}

function loadMixins() {
  Vue.mixin(popups);
}

loadMixins();
loadPlugins();

export default function ({store}) {
  store.dispatch('client/loadClient');
  store.dispatch('popups/load');
};
