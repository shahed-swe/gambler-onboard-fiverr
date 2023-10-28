<template>
  <div id="leaderboard">
    <div class="leaderboard-hero" :class="'hero-' + tab">
      <div class="uk-container">
        <div class="hero-content">
          <h1>
            <strong>{{ tab.toUpperCase() }}</strong> LEADERBOARD
          </h1>
          <h2>
            Win rewards by {{ leaderboards[tab].sort_field === 'deposited' ? 'depositing' : 'wagering' }} with <strong>CODE THEGAMBLER</strong>
          </h2>

          <div class="leaderboard-countdown">
            <CountdownTime v-if="leaderboards !== null && leaderboards[tab] !== null" :timestamp="leaderboards[tab].end_at"/>
          </div>

          <span class="leaderboard-last-update uk-margin">
            <i class="fa-regular fa-clock uk-margin-right-s"></i>
            Last updated: {{ leaderboards !== null ? formatIntoAbbreviatedString((new Date().getTime()) - leaderboards[tab].updated_at) : '' }}
          </span>
        </div>
      </div>
    </div>

    <div id="leaderboard-display">
      <div class="uk-container">
        <div class="leaderboard-nav">
          <button class="uk-btn-lb uk-btn-lb-roobet" :class="[tab === 'roobet' ? 'uk-btn-active' : '']" @click="openTab('roobet')">
            <img src="~assets/images/roobet.svg" alt="ClashGG" class="sponsor-logo"/>
          </button>
        </div>

        <LeaderboardDisplay :data="leaderboards[tab]" :show-active="showActive" :currency-image="currencyImage" :currency-name="currencyName"/>
      </div>
    </div>
  </div>
</template>

<style scoped>
#leaderboard {

}

#leaderboard-display {
  position: relative;
}

.leaderboard-nav {
  display: flex;
  align-items: center;
  position: relative;
  margin-top: 30px;
  margin-left: 30px;
}

.leaderboard-nav > *:not(:last-child) {
  margin-right: 20px;
}

.leaderboard-nav > button {
  width: 220px;
  height: 60px;
  border-radius: 10px 10px 0 0;
  box-shadow: none !important;
  border: 2px solid rgba(255, 255, 255, 0.1);
  border-bottom: none !important;
  transition: all ease-in-out 0.15s;
}

.leaderboard-nav > button:hover {
  background: linear-gradient(140deg, rgba(77, 77, 77,1) 0%, rgba(33, 33, 33,1) 100%);
}

.leaderboard-nav > button > .sponsor-logo {
  width: 120px;
}

.leaderboard-nav > button > .sponsor-coin {
  width: 20px;
  margin-right: 10px;
}

.leaderboard-countdown {
  display: flex;
  align-items: center;
  justify-content: center;
  margin-top: 30px;
  transition: all ease-in-out 0.15s;
  color: #fff;
  font-size: 16px;
  font-weight: bold;
}

.leaderboard-countdown > i {
  margin-right: 8px;
  font-size: 18px;
}

.leaderboard-last-update {
  color: #fff;
  font-weight: 500;
}

.leaderboard-hero {
  width: 100%;
  padding: 80px 0 40px 0;
  /*box-shadow: 0 0 10px #00000080;*/
}

.leaderboard-hero.hero-roobet {
  /*background-color: transparent;*/
  /*background: url('~assets/images/leaderboard-bg.png');*/
  /*background-size: calc(100% + 20px) calc(100% + 30px);*/
  /*background-position: center center;*/
  /*background-repeat: no-repeat;*/
}

.leaderboard-hero .hero-content {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.leaderboard-hero .hero-content h1,
.leaderboard-hero .hero-content h2 {
  margin: 0;
  color: #fff;
  font-weight: 900;
  letter-spacing: 1px;
}

.leaderboard-hero .hero-content h1 {
  font-size: 49px;
}

.leaderboard-hero .hero-content h2 {
  margin-top: 10px;
  color: rgba(255, 255, 255, 0.8);
  font-size: 18px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 1px;
}

.leaderboard-hero .hero-content strong {
  color: #2D2952;
  text-transform: uppercase;
}

.leaderboard-hero.hero-roobet .hero-content strong {
  color: #D7AF3F;
}

@media screen and (max-width: 768px) {
  .leaderboard-hero {
    height: auto;
    padding: 60px 0;
  }

  .leaderboard-hero .hero-content {
    margin-top: 0;
    text-align: center;
  }

  .leaderboard-hero .hero-content h2 {
    margin-top: 20px;
  }
}
</style>

<script>
import LeaderboardDisplay from "~/components/content/LeaderboardDisplay.vue";
import {formatIntoAbbreviatedString} from "~/util/time";

export default {
  components: {LeaderboardDisplay},
  head() {
    return {
      title: 'Leaderboard'
    }
  },
  data() {
    return {
      tab: 'roobet',
      leaderboards: {
        roobet: null,
      },
      showActive: true,
      currencyImage: null,
      currencyName: 'Dollars',
      formatIntoAbbreviatedString,
    }
  },
  async asyncData({$axios}) {
    const data = {
      leaderboards: {
        roobet: null,
      }
    };

    await $axios.get('/leaderboards').then(response => {
      console.log(response.data);
      if (response.status === 200) {
        data.leaderboards = response.data.leaderboards;
      } else {
        throw new Error('Unhandled status code');
      }
    }).catch(err => {
      console.log(err);
    });

    return data;
  },
  methods: {
    async openTab(tabName) {
      this.tab = tabName;

      if (tabName === 'roobet') {
        this.showActive = true;
        this.currencyImage = require('~/assets/images/clash-gem.svg');
        this.currencyName = 'Gems';
      }
    }
  }
}
</script>