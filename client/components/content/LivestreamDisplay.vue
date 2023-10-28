<template>
  <div class="livestream">
    <div class="grouped align-center">
      <div class="livestream-title">
        <span v-if="livestream !== null">
          Live
        </span>
        <span v-else>
          Not Live
        </span>

        <span>
          Livestream
        </span>
      </div>
    </div>

    <div class="livestream-preview">
      <a href="https://www.kick.com/thegambler">
        <img src="~assets/images/livestream-bg.jpg" alt="TheGambler on Kick"/>
      </a>
    </div>

    <div class="livestream-details">
      <a class="livestream-link" href="https://www.kick.com/thegambler1999">
        <i class="fa-brands fa-kickstarter uk-margin-right-xs"/>
        TheGambler1999
      </a>

      <span class="livestream-timestamp uk-margin-left-auto">
        <template v-if="lastLive === null">

        </template>
        <template v-else>
          {{ time.getTimeago(lastLive, $timeago) }}
        </template>
      </span>
    </div>
  </div>
</template>

<style scoped>
.livestream {
  display: flex;
  flex-direction: column;
  flex-shrink: 0;
  width: 550px;
  height: 380px;
  padding: 30px 40px 40px 40px;
  background: linear-gradient(180deg, #014C7A 0%, rgba(23,45,73,0.2) 100%);
  border-radius: 12px;
  box-shadow: 0 3px 5px rgba(0, 0, 0, 0.3);
}

.livestream .livestream-title > span:nth-child(1) {
  display: block;
  color: rgba(255, 255, 255, 0.8);
  font-size: 12px;
  font-weight: 500;
  letter-spacing: 2px;
  text-transform: uppercase;
}

.livestream .livestream-title > span:nth-child(2) {
  display: block;
  color: #FFFFFF;
  font-size: 24px;
  font-weight: 700;
  letter-spacing: 2px;
  text-transform: uppercase;
}

.livestream .livestream-preview {
  margin-top: 10px;
  border: 4px solid rgba(0, 0, 0, 0.4);
  border-radius: 5px;
  object-fit: cover;
  object-position: center;
}

.livestream .livestream-preview img {
  width: 100%;
  height: 220px;
}

.livestream-details {
  display: flex;
  align-items: center;
  margin-top: 14px;
}

.livestream-link {
  color: #fff;
  font-size: 15px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 1px;
}

.livestream-timestamp {
  margin-top: 2px;
  color: rgba(255, 255, 255, 0.8);
  font-size: 13px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 1px;
}

@media screen and (max-width: 768px) {
  .livestream {
    width: 100%;
  }
}
</style>

<script>
export default {
  props: {
    livestream: {
      type: Object,
      required: true
    },
    lastLive: {
      type: Number,
      required: true
    }
  },
  data() {
    return {
      time: require('~/util/time.js'),
    }
  }
}
</script>
