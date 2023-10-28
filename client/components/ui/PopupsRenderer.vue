<template>
  <div class="uk-popups-container">
    <div v-for="popup in getActivePopups" :key="popup.id" class="uk-popup uk-animation-fade" :style="{ left: popup.posX + 'px', top: (popup.posY + 10) + 'px' }">
      {{ popup.message }}
    </div>
  </div>
</template>

<style scoped>
.uk-popups-container {
  position: fixed;
  z-index: 1100;
}

.uk-popup {
  position: fixed;
  display: flex;
  align-items: center;
  z-index: 1050;
  top: 0;
  width: auto;
  height: auto;
  max-width: 200px;
  padding: 4px 10px;
  background: #111;
  border-radius: 5px;
  box-sizing: border-box;
  color: #fff;
  font-size: 13px;
  font-weight: bold;
}
</style>

<script>
export default {
  mounted() {
    document.body.insertBefore(this.$el, document.body.firstChild);
  },
  computed: {
    getActivePopups() {
      return this.$store.getters['popups/getActive'];
    }
  }
}
</script>
