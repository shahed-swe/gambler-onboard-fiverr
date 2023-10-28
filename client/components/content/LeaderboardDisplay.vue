<template>
  <div v-if="data !== null" class="leaderboard">
    <div class="leaderboard-top-container">
      <div class="uk-container">
        <div class="leaderboard-top">
          <div v-for="entry in getLeaderboardTopEntries" :key="entry.userId" class="top-entry"
            :class="'top-entry-' + entry.position">
            <div class="entry-position">
              <img v-if="entry.position === 1" src="~assets/images/goldcoin.png" alt="" />
              <img v-else-if="entry.position === 2" src="~assets/images/silvercoin.png" alt="" />
              <img v-else-if="entry.position === 3" src="~assets/images/bronzecoin.png" alt="" />
            </div>

            <!--            <img class="entry-avatar" :src="getEntryAvatar(entry)" :alt="entry.name"/>-->

            <div class="grouped align-center uk-margin-s">
              <template v-if="showActive">
                <div v-if="entry.active" class="active-dot" />
                <div v-else class="inactive-dot" />
              </template>

              <span class="entry-name">
               {{ getMaskedName(entry.name)}}
                <!-- {{ trim(entry.name, 14) }} -->
              </span>
            </div>

            <div class="entry-value value-amount uk-margin-s">
              <span class="value-name">
                {{ data.sort_field === 'deposited' ? 'Deposited' : 'Wagered' }}
              </span>

              <span class="value-number">
                <img v-if="!isDollarCurrency" class="game-currency-small uk-margin-right-s" :src="currencyImage"
                  :alt="currencyName" />

                <template v-if="isDollarCurrency">
                  ${{ entry.wagered.toLocaleString('en-us') }}
                </template>
                <template v-else>
                  {{ entry.wagered.toLocaleString('en-us') }} <small>{{ currencyName }}</small>
                </template>
              </span>
            </div>

            <div class="entry-value prize-amount">
              <span class="value-name">
                Prize
              </span>

              <span class="value-number">
                <img v-if="!isDollarCurrency" class="game-currency-small uk-margin-right-s" :src="currencyImage"
                  :alt="currencyName" />

                <template v-if="isDollarCurrency">
                  ${{ entry.prize.toLocaleString('en-us') }}
                </template>
                <template v-else>
                  {{ entry.prize.toLocaleString('en-us') }} <small>{{ currencyName }}</small>
                </template>
              </span>
            </div>
          </div>

          <template v-if="getLeaderboardTopEntries.length < 3">
            <div v-for="i in [2, 1, 3]" :key="i" class="top-entry" :class="'top-entry-' + i">
              <template v-if="getLeaderboardTopEntries.length < i">
                <div class="entry-position">
                  <img v-if="entry.position === 1" src="~assets/images/goldcoin.png" alt="" />
                  <img v-else-if="entry.position === 2" src="~assets/images/silvercoin.png" alt="" />
                  <img v-else-if="entry.position === 3" src="~assets/images/bronzecoin.png" alt="" />
                </div>

                <img class="entry-avatar" src="~assets/images/default_avatar.png" alt="Nobody" />

                <div class="grouped align-center uk-margin-s">
                  <span class="entry-name">
                    ?
                  </span>
                </div>

                <div class="entry-value value-amount uk-margin-s">
                  <span class="value-name">
                    {{ data.sort_field === 'deposited' ? 'Deposited' : 'Wagered' }}
                  </span>

                  <span class="value-number">
                    <img v-if="!isDollarCurrency" class="game-currency-small uk-margin-right-s" :src="currencyImage"
                      :alt="currencyName" />

                    <template v-if="isDollarCurrency">
                      ${{ (0).toLocaleString('en-us') }}
                    </template>
                    <template v-else>
                      {{ (0).toLocaleString('en-us') }} <small>{{ currencyName }}</small>
                    </template>
                  </span>
                </div>

                <div class="entry-value prize-amount">
                  <span class="value-name">
                    Prize
                  </span>

                  <span class="value-number">
                    <img v-if="!isDollarCurrency" class="game-currency-small uk-margin-right-s" :src="currencyImage"
                      :alt="currencyName" />

                    <template v-if="isDollarCurrency">
                      ${{ getPrizes[i - 1].toLocaleString('en-us') }}
                    </template>
                    <template v-else>
                      {{ getPrizes[i - 1].toLocaleString('en-us') }} <small>{{ currencyName }}</small>
                    </template>
                  </span>
                </div>
              </template>
            </div>
          </template>
        </div>
      </div>
    </div>

    <div class="uk-container">
      <div v-if="getLeaderboardBottomEntries.length > 0" class="leaderboard-entries">
        <template v-if="getLeaderboardBottomEntries.length > 0">
          <div class="leaderboard-header">
            <div>
              <span>
                Rank
              </span>
            </div>
            <div>
              <span>
                Player
              </span>
            </div>
            <div>
              <span>
                {{ data.sort_field === 'deposited' ? 'Deposited' : 'Wagered' }}
              </span>
            </div>
            <div>
              <span>
                Prize
              </span>
            </div>
          </div>

          <div v-for="entry in getLeaderboardBottomEntries" :key="entry.userId" class="leaderboard-entry">
            <div class="leaderboard-entry__player">
              <div>
                <span class="entry-position">
                  <small>#</small>{{ entry.position }}
                </span>
              </div>
              <div>
                <img class="entry-avatar" :src="getEntryAvatar(entry)" :alt="entry.name" />

                <template v-if="showActive">
                  <div v-if="entry.active" class="active-dot" />
                  <div v-else class="inactive-dot" />
                </template>

                <span class="entry-name">
                  {{ getMaskedName(entry.name) }}
                </span>
              </div>
            </div>
            <div class="leaderboard-entry__stats">
              <div>
                <span class="entry-value value-amount">
                  <img v-if="!isDollarCurrency" class="game-currency-small uk-margin-right-s" :src="currencyImage"
                    :alt="currencyName" />

                  <template v-if="isDollarCurrency">
                    ${{ (data.sort_field === 'deposited' ? entry.deposited : entry.wagered).toLocaleString('en-us') }}
                  </template>
                  <template v-else>
                    {{ (data.sort_field === 'deposited' ? entry.deposited : entry.wagered).toLocaleString('en-us') }}
                    <small>{{ currencyName }}</small>
                  </template>
                </span>
              </div>
              <div>
                <span class="entry-value prize-amount">
                  <img v-if="!isDollarCurrency" class="game-currency-small uk-margin-right-s" :src="currencyImage"
                    :alt="currencyName" />

                  <template v-if="isDollarCurrency">
                    ${{ entry.prize.toLocaleString('en-us') }}
                  </template>
                  <template v-else>
                    {{ entry.prize.toLocaleString('en-us') }} <small>{{ currencyName }}</small>
                  </template>
                </span>
              </div>
            </div>
          </div>
        </template>
      </div>
    </div>
  </div>
  <div v-else class="uk-loading">
    <div uk-spinner />
  </div>
</template>

<style scoped>
.leaderboard {
  position: relative;
  z-index: 1500;
  width: 100%;
  padding: 40px 40px 60px 40px;
  background: linear-gradient(180deg, #383360 0%, rgba(22, 22, 22, 1) 100%);
  background: url('~/assets/images/roobet-repeating-bg.png');
  background-position: center;
  border: 2px solid rgba(255, 255, 255, 0.1);
  border-top: none;
  border-radius: 10px;
  box-shadow: 0 3px 5px rgba(0, 0, 0, 0.3);
  box-sizing: border-box;
  margin-bottom: 80px;
}

.leaderboard-top-container {
  width: 100%;
  position: relative;
}

.leaderboard-top {
  width: 100%;
  display: flex;
  align-items: flex-end;
  justify-content: center;
  position: relative;
  z-index: 1500;
  margin-top: 50px;
}

.leaderboard-top .top-entry {
  position: relative;
  z-index: 1500;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: flex-end;
  flex: 0 1 calc(33% - 20px);
  padding: 70px 15px 15px 15px;
  background: radial-gradient(100% 100% at 50% 0, rgba(27, 29, 33, .25) 0, rgba(27, 28, 30, 0) 100%), rgba(14, 15, 17, .75);
  border-top: none;
  border-radius: 10px;
  box-sizing: border-box;
  /*animation-name: theme-float;*/
  /*animation-duration: 3.5s;*/
  /*animation-iteration-count: infinite;*/
  /*animation-timing-function: ease-in-out;*/
}

.leaderboard-top .top-entry.top-entry-1 {
  top: 20px;
  -moz-box-align: center;
  margin-left: 70px;
  margin-right: 70px;
  /*background: linear-gradient(140deg, rgba(20, 20, 20,1) 0%, #FED69170 150%);*/
  /*background: linear-gradient(140deg, #2D2952 0%, #4d4a80 100%);*/
}

.leaderboard-top .top-entry.top-entry-2 {
  top: 20px;
  /*background: linear-gradient(140deg, rgba(20, 20, 20,1) 0%, #ADADAD70 150%);*/
  /*background: linear-gradient(140deg, #2D2952 0%, #4d4a80 100%);*/
}

.leaderboard-top .top-entry.top-entry-3 {
  top: 20px;
  /*background: linear-gradient(140deg, rgba(20, 20, 20,1) 0%, #DF8F6170 150%);*/
  /*background: linear-gradient(140deg, #2D2952 0%, #4d4a80 100%);*/
}

.leaderboard-top .top-entry .entry-position {
  position: absolute;
  width: 100%;
  top: -40px;
  left: 0;
  display: flex;
  align-items: center;
  justify-content: center;
}

.leaderboard-top .top-entry .entry-position>img {
  width: 105px;
  height: 105px;
  animation-name: theme-float;
  animation-duration: 3.5s;
  animation-iteration-count: infinite;
  animation-timing-function: ease-in-out;
}

.leaderboard-top .top-entry.top-entry-1 .entry-position>img {}

.leaderboard-top .top-entry.top-entry-2 .entry-position>img {}

.leaderboard-top .top-entry.top-entry-3 .entry-position>img {}

.leaderboard-top .top-entry .entry-position>span {
  position: absolute;
  top: 20px;
  left: calc(50% - 50px);
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100px;
  color: #333;
  font-size: 20px;
  font-weight: 800;
  letter-spacing: 1px;
  text-align: center;
  text-transform: uppercase;
  text-shadow: 0 3px 0 #00000029;
}

.leaderboard-top .top-entry .entry-avatar {
  width: 80px;
  height: 80px;
  border-radius: 5px;
}

.leaderboard-top .top-entry.top-entry-1 .entry-avatar {
  width: 120px;
  height: 120px;
}

.leaderboard-top .top-entry.top-entry-2 .entry-avatar {}

.leaderboard-top .top-entry.top-entry-3 .entry-avatar {}

.leaderboard-top .top-entry .entry-name {
  margin: 10px 0 20px 0;
  color: #fff;
  font-size: 16px;
  font-weight: 900;
  font-style: italic;
  text-transform: uppercase;
  letter-spacing: 1px;
}

.leaderboard-top .top-entry .entry-value {
  display: flex;
  align-items: center;
  width: 100%;
  padding: 9px 15px;
}

.leaderboard-top .top-entry.top-entry-1 .entry-value {}

.leaderboard-top .top-entry.top-entry-2 .entry-value {}

.leaderboard-top .top-entry.top-entry-3 .entry-value {}

.leaderboard-top .top-entry .entry-value.value-amount {
  background: rgba(100, 100, 100, 0.05);
  border-radius: 5px;
}

.leaderboard-top .top-entry .entry-value.prize-amount {
  margin-top: 10px;
  background: rgba(100, 100, 100, 0.05);
  border-radius: 5px;
}

.leaderboard-top .top-entry .entry-value>span {
  display: flex;
  align-items: center;
}

.leaderboard-top .top-entry .entry-value>.value-name {
  color: #fff;
  font-size: 13px;
  font-weight: 900;
  text-transform: uppercase;
  letter-spacing: 1px;
}

.leaderboard-top .top-entry .entry-value>.value-number {
  display: flex;
  align-items: center;
  margin-left: auto;
  color: #fff;
  font-size: 15px;
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: 1px;
}

.leaderboard-top .top-entry .entry-value>span:nth-child(2)>small {
  margin-left: 5px;
  font-size: 13px;
}

.leaderboard-header>div:nth-child(1) {
  padding-left: 40px;
  width: 120px;
}

.leaderboard-header>div:nth-child(2) {
  width: auto;
}

.leaderboard-header>div:nth-child(3) {
  width: 220px;
  margin-left: auto;
}

.leaderboard-header>div:nth-child(4) {
  width: 220px;
}

.leaderboard-header {
  display: flex;
  margin-top: 20px;
}

.leaderboard-header>div {
  display: flex;
  align-items: center;
  margin-right: 20px;
}

.leaderboard-header>div>span {
  color: #fff;
  font-size: 16px;
  font-weight: 900;
  text-align: left;
  text-transform: uppercase;
  letter-spacing: 1px;
}

.leaderboard-entries {
  position: relative;
  width: 100%;
  display: flex;
  flex-direction: column;
  padding: 50px 0 0 0;
  border-radius: 5px;
}

.leaderboard-entry>.leaderboard-entry__player>div:nth-child(1) {
  padding-left: 40px;
  width: 80px;
}

.leaderboard-entry>.leaderboard-entry__player>div:nth-child(2) {
  width: auto;
}

.leaderboard-entry>.leaderboard-entry__stats>div {
  width: 50%
}

.leaderboard-entry {
  display: flex;
  align-items: center;
  width: 100%;
  height: 70px;
  background: radial-gradient(100% 100% at 50% 0, rgba(27, 29, 33, .25) 0, rgba(27, 28, 30, 0) 100%), rgba(14, 15, 17, .75);
  box-shadow: 0 0 10px #00000080;
  border: 1px solid #FFFFFF1A;
  border-radius: 5px;
  transition: background-color ease-in-out 25ms;
}

.leaderboard-entry:hover {
  background: radial-gradient(100% 100% at 50% 0, rgba(27, 29, 33, .5) 0, rgba(27, 28, 30, 0) 100%), rgba(14, 15, 17, .9);
}

.leaderboard-entry:not(:first-child) {
  margin-top: 20px;
}

.leaderboard-entry>.leaderboard-entry__player {
  width: 60%;
}

.leaderboard-entry>.leaderboard-entry__stats {
  width: 40%;
  margin-right: 30px;
}

.leaderboard-entry>.leaderboard-entry__player,
.leaderboard-entry>.leaderboard-entry__stats {
  flex-grow: 1;
  display: flex;
  align-items: center;
}

.leaderboard-entry>div>div {
  display: flex;
  align-items: center;
  height: 70px;
  margin-right: 20px;
}

.leaderboard-entry>div>div>* {
  flex-shrink: 0;
}

.leaderboard-entry .entry-position {
  width: 80px;
  color: #fff;
  font-size: 16px;
  font-weight: 800;
  letter-spacing: 1px;
  text-align: center;
}

.leaderboard-entry .entry-position>small {
  font-size: 12px;
}

.leaderboard-entry .entry-avatar {
  width: 35px;
  height: 35px;
  margin-right: 20px;
  border: 1px solid #FFFFFF54;
  border-radius: 5px;
}

.leaderboard-entry .entry-name {
  color: #fff;
  font-size: 16px;
  font-weight: 900;
  text-transform: uppercase;
  letter-spacing: 1px;
}

.leaderboard-entry .entry-value {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 220px;
  height: 45px;
  padding: 0 20px;
  background: rgba(55, 55, 55, 0.1);
  border-radius: 5px;
  font-size: 14px;
  font-weight: 800;
  text-transform: uppercase;
  text-align: left;
  letter-spacing: 1px;
  color: #FFFFFF;
}

.leaderboard-entry .entry-value>small {
  position: relative;
  top: 2px;
  margin-left: 6px;
  font-size: 12px;
}

.leaderboard-footer {
  width: 100%;
  height: 70px;
  margin-top: 20px;
  padding: 15px;
  background: radial-gradient(100% 100% at 50% 0, rgba(27, 29, 33, .25) 0, rgba(27, 28, 30, 0) 100%), rgba(14, 15, 17, .75);
  box-shadow: 0 0 10px #00000080;
  border: 1px solid #FFFFFF1A;
  border-radius: 5px;
}

.leaderboard-footer .next-reset {
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(55, 55, 55, 0.1);
  border-radius: 5px;
  color: #fff;
  font-size: 14px;
  font-weight: 800;
  text-align: center;
  letter-spacing: 1px;
}

.leaderboard-footer .next-reset>strong {
  display: block;
  margin-left: 5px;
  color: #FFC701;
}

@media screen and (max-width: 768px) {
  .leaderboard-top-container {
    position: relative;
    left: unset;
    top: unset;
    margin-top: 60px;
  }

  .leaderboard-top {
    top: unset;
    flex-direction: column;
    align-items: center;
  }

  .leaderboard-top .top-entry:not(:last-child) {
    margin-bottom: 60px;
  }

  .leaderboard-entries {
    top: unset;
    padding: 30px 20px;
  }

  .leaderboard-entries .leaderboard-entry .entry-position {
    padding: 0 10px;
  }

  .leaderboard-header {
    margin-top: 0;
  }

  .leaderboard-header>div:nth-child(1) {
    width: auto;
  }

  .leaderboard-header>div:nth-child(2) {
    width: auto;
  }

  .leaderboard-header>div:nth-child(3) {
    width: auto;
  }

  .leaderboard-header>div:nth-child(4) {
    width: auto;
  }

  .leaderboard-top .top-entry {
    width: 100%;
  }

  .leaderboard-top .top-entry:not(:last-child) {
    margin-bottom: 80px;
  }
}
</style>

<script>
import { trim } from '~/util/text';

export default {
  props: {
    data: {
      type: Object,
      required: true
    },
    showActive: {
      type: Boolean,
      required: true
    },
    currencyName: {
      type: String,
      required: true
    },
    currencyImage: {
      type: String,
      required: false
    }
  },
  data() {
    return {
      trim: trim,
      avatarImage: require('~/assets/images/lb-avatar-anonymous.png')
    }
  },
  computed: {
    isDollarCurrency() {
      return this.currencyImage === null;
    },
    getPrizes() {
      return this.data.prizes;
    },
    getLeaderboardTopEntries() {
      if (this.data.entries.length === 0) {
        return [];
      } else {
        const topEntries = this.data.entries.slice(0, Math.min(3, this.data.entries.length));
        if (this.$store.getters['client/isTabletOrBelow']) {
          return topEntries;
        } else {
          return [topEntries[1], topEntries[0], topEntries[2]];
        }
      }
    },
    getLeaderboardBottomEntries() {
      if (this.data.entries.length >= 3) {
        return this.data.entries.slice(3, this.data.entries.length >= 10 ? 10 : this.data.entries.length);
      } else {
        return [];
      }
    }
  },
  methods: {
    getEntryAvatar(entry) {
      return this.avatarImage;
      // console.log(entry.avatar);
      // if (entry.avatar === '/assets/csgo/avatar-anonymous.png') {
      //   return require('~/assets/images/lb-avatar-anonymous.png');
      // } else {
      //   return entry.avatar;
      // }
    },

    getMaskedName(name) {
      if (name) {
        const firstThreeCharacters = name.substring(0, 3);
        const maskedFirstThreeCharacters = '*'.repeat(3);
        // Combine the masked first three characters with the rest of the string
        const maskedRestOfName = name.substring(3);
        return maskedFirstThreeCharacters + maskedRestOfName;

      } else {
        return name
      }
      
    }
  }
}
</script>
