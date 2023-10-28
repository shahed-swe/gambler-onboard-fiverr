<template>
  <div id="splash">
    <div class="uk-container">
      <div class="splash-hero">
        <span class="hero-title">
          TheGambler
        </span>

        <p class="hero-p uk-margin-s">
          Streams at 10:30 AM PST everyday. Uploads at 1:00 PM PST everyday.
        </p>

        <p class="hero-p uk-margin-s">
          Weekly leaderboard with over $250 in prizes!
        </p>

        <div class="grouped align-center uk-margin-l">
          <nuxt-link :to="{ name: 'leaderboard' }" class="uk-button uk-btn-gold">
            <i class="fa-solid fa-trophy-star"></i>
            View Leaderboard
          </nuxt-link>

          <nuxt-link :to="{ name: 'rewards' }" class="uk-button uk-btn-green uk-margin-left">
            <i class="fa-solid fa-treasure-chest"></i>
            Free Rewards
          </nuxt-link>
        </div>
      </div>

      <LivestreamDisplay :last-live="null" :livestream="livestream" class="uk-margin-xl uk-margin-left-auto"/>
      <VideosDisplay v-if="videos !== null" :data="videos" class="uk-margin-xl"/>
    </div>
  </div>
</template>

<style scoped>
#splash {
  display: flex;
  flex-direction: column;
  width: 100%;
  min-height: calc(100vh - 140px - 120px);
  padding: 60px 0;
}

.splash-hero {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  width: 100%;
  margin-bottom: 80px;
  padding: 20px 0 40px 0;
}

.splash-hero .hero-title {
  color: #fff;
  font-size: 48px;
  font-family: 'Bebas Neue', sans-serif;
  text-shadow: 0 5px rgba(0, 0, 0, 0.3);
  letter-spacing: 1px;
}

.splash-hero .hero-p {
  display: flex;
  align-items: center;
  justify-content: center;
  color: rgba(255, 255, 255, 0.8);
  font-size: 22px;
  font-family: 'Lexend', sans-serif;
  text-shadow: 0 2px rgba(0, 0, 0, 0.2);
}
</style>

<script>
import VideosDisplay from "~/components/content/VideosDisplay.vue";
import LivestreamDisplay from "~/components/content/LivestreamDisplay.vue";

export default {
  components: {LivestreamDisplay, VideosDisplay},
  layout: 'default',
  head() {
    return {
      title: 'TheGambler',
      titleTemplate: '%s'
    }
  },
  data() {
    return {
      videos: null,
      livestream: null,
      lastLive: null,
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

    await $axios.get('/livestream').then(response => {
      if (response.status === 200) {
        data.livestream = response.data.livestream;
        data.lastLive = response.data.last_live;
      } else {
        throw new Error('Unhandled status code');
      }
    }).catch(err => {
      console.log(err);
    });

    return data;
  },
  methods: {
    copyToClipboard(event, text) {
      this.$clipboard(text);
      this.$popup(event, 'Copied to clipboard!', 2.5);
    }
  },
  mounted() {

  }
}
</script>
