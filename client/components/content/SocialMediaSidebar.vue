<template>
  <div id="social-media-sidebar">
    <a href="#" class="theme-btn theme-btn-red">
      <img src="~assets/images/social-icons/youtube-filled.svg" alt=""/>
    </a>
    <a href="#" class="theme-btn theme-btn-blue">
      <img src="~assets/images/social-icons/twitter-filled.svg" alt=""/>
    </a>
    <a href="#" class="theme-btn theme-btn-discord">
      <img src="~assets/images/social-icons/discord-filled.svg" alt=""/>
    </a>
  </div>
</template>

<style scoped>
#social-media-sidebar {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  position: fixed;
  top: calc(50vh - (200px / 2));
  left: 0;
  width: 70px;
  height: 200px;
  padding: 10px;
  /*background: rgba(255, 255, 255, 0.2);*/
  /*border-radius: 0 10px 10px 0;*/
  z-index: 2000;
}

#social-media-sidebar > a {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
  height: 50px;
  padding: 0;
  border-radius: 10px;
  cursor: pointer;
  z-index: 2000;
}

#social-media-sidebar > a > img {
  width: 30px;
  height: 30px;
}

#social-media-sidebar > a:not(:last-child) {
  margin-bottom: 10px;
}

.subscribe-btn,
.follow-btn {
  width: 170px;
}

.subscribe-btn i {
  margin-right: 8px;
  color: #ff5454;
  font-size: 16px;
}

.follow-btn i {
  margin-right: 8px;
  color: #fff;
  font-size: 16px;
}
</style>

<script>
export default {

}
</script>