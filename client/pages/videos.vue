<template>
  <div id="videos" class="uk-margin-xl">
    <div class="uk-container">
      <VideosTable v-if="videos !== null" :data="videos"/>
    </div>
  </div>
</template>

<style scoped>
#videos {
  min-height: 646px;
  margin: 20px 0 60px 0;
}
</style>

<script>
import VideosTable from "@/components/content/VideosTable.vue";

export default {
  components: {VideosTable},
  head() {
    return {
      title: 'Videos'
    }
  },
  data() {
    return {
      videos: null,
    }
  },
  async asyncData({$axios}) {
    const data = {};

    await $axios.get('/videos').then(response => {
      if (response.status === 200) {
        data.videos = response.data.videos;
      } else {
        throw new Error('Unhandled status code');
      }
    }).catch(err => {
      console.log(err);
    });

    return data;
  },
}
</script>