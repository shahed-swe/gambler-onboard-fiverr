export default {
  methods: {
    $popup(event, message, duration) {
      this.$store.dispatch('popups/popup', {event, message, duration});
    }
  }
}
