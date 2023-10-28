<template>
  <div class="videos">
    <div class="videos-list">
      <div class="videos-shadow-left"/>
      <div class="videos-shadow-right"/>
      <div class="videos-shadow-top"/>

      <a v-for="video in getSortedVideos" :key="video.video_id" class="video" :href="video.video_url">
        <img class="video-thumbnail" :src="video.thumbnail.url" :alt="video.video_title"/>

        <div class="video-details">
          <a class="video-link" :href="video.video_url">
            {{ trim(video.video_title, 40) }}
          </a>

          <a class="channel-link" :href="video.channel_url">
            {{ video.channel_title }}
          </a>

          <span class="video-timestamp">
            <timeago :datetime="video.published_at"/>
          </span>
        </div>
      </a>
    </div>
  </div>
</template>

<style scoped>
.videos {
  width: 100%;
  position: relative;
  border-radius: 10px;
}

.videos-list {
  position: relative;
  display: flex;
  align-items: stretch;
  flex-wrap: wrap;
  width: 100%;
  max-width: 1500px;
  padding: 40px 40px 40px 50px;
  background: linear-gradient(180deg, #014C7A 0%, rgba(23,45,73,0.2) 100%);
  border-radius: 10px;
  box-shadow: 0 3px 5px rgba(0, 0, 0, 0.3);
}

.videos-list::-webkit-scrollbar {
    background: #0e131c;
    -webkit-appearance: scrollbarthumb-vertical;
}

.videos-list::-webkit-scrollbar-thumb {
    background: #161e2d;
    -webkit-appearance: scrollbartrack-vertical;
}

/*.videos-list .videos-shadow-left {*/
/*  position: absolute;*/
/*  left: 0;*/
/*  top: 0;*/
/*  width: 50px;*/
/*  height: 100%;*/
/*  z-index: 1500;*/
/*  background: linear-gradient(-90deg, rgba(0,0,0,0) 0%, #080a0c 100%);*/
/*  border-radius: 10px;*/
/*}*/

/*.videos-list .videos-shadow-right {*/
/*  position: absolute;*/
/*  right: 0;*/
/*  top: 0;*/
/*  width: 50px;*/
/*  height: 100%;*/
/*  background: linear-gradient(90deg, rgba(0,0,0,0) 0%, #080a0c 100%);*/
/*  border-radius: 10px;*/
/*  z-index: 1500;*/
/*}*/

/*.videos-list .videos-shadow-top {*/
/*  position: absolute;*/
/*  left: 0;*/
/*  top: 0;*/
/*  width: 100%;*/
/*  height: 50px;*/
/*  background: linear-gradient(0deg, rgba(0,0,0,0) 0%, #080a0c 100%);*/
/*  border-radius: 10px;*/
/*  z-index: 1500;*/
/*}*/

.video {
  display: flex;
  flex-direction: column;
  flex: 0 1 calc(25% - 20px);
  border-radius: 5px;
  transform: scale(1.0);
  transition: all .15s ease-in-out;
  margin-right: 20px;
}

.video:hover {
  transform: scale(1.1);
}

.video .video-thumbnail {
  flex-grow: 1;
  display: block;
  width: 100%;
  border: 4px solid rgba(0, 0, 0, 0.4);
  border-radius: 5px;
}

.video .video-details {
  padding: 20px 20px 20px 0;
}

.video .video-link {
  display: flex;
  align-items: center;
  max-height: 70px;
  color: rgba(255, 255, 255, 0.9);
  font-size: 16px;
  font-weight: 900;
  text-transform: uppercase;
  text-shadow: 0 1px 3px #283F6930;
  letter-spacing: 1px;
}

.video .channel-link {
  display: flex;
  align-items: center;
  color: rgba(255, 255, 255, 0.6);
  font-size: 12px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 1px;
  margin-top: 10px;
}

.video .video-timestamp {
  display: flex;
  align-items: center;
  color: #FED691;
  font-size: 11px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 1px;
  margin-top: 2px;
}

@media screen and (max-width: 768px) {
  .videos-list {
    flex-direction: column;
  }

  .video {
    width: 100%;
  }

  .video:not(:last-child) {
    margin-bottom: 20px;
  }
}
</style>

<script>
import {trim} from '~/util/text';

export default {
  props: {
    data: {
      type: Array,
      required: true
    }
  },
  data() {
    return {
      trim: trim
    }
  },
  computed: {
    getSortedVideos() {
      let videos = [...this.data];
      videos.sort((a, b) => new Date(b.published_at) - new Date(a.published_at));
      return videos;
    }
  }
}
</script>
