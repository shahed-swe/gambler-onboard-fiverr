<template>
  <div id="layout">
    <Header/>

    <div id="nuxt-content">
      <nuxt/>
    </div>

    <Footer/>

    <SocialMediaSidebar/>

    <PopupsRenderer/>
  </div>
</template>

<style scoped>
#nuxt-content {
  position: relative;
  z-index: 1500;
}
</style>

<script>
import Header from "~/components/layout/Header";
import Footer from "~/components/layout/Footer";
import PopupsRenderer from "@/components/ui/PopupsRenderer";
import SocialMediaSidebar from "~/components/content/SocialMediaSidebar.vue";

export default {
  name: 'App',
  components: {Header, Footer, PopupsRenderer, SocialMediaSidebar},
  created() {
    this.$store.commit('popups/initVM', this);
  },
  mounted() {
    this.$store.dispatch('client/detectDevice');
  }
};
</script>
