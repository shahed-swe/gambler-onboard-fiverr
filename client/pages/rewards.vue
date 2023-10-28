<template>
  <div id="rewards">
    <h1>
      Coming Soon
    </h1>
  </div>
</template>

<style scoped>
#rewards {
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 80px 0;
  width: 100%;
  min-height: calc(100vh - 120px - 140px);
}

#rewards h1 {
  font-size: 36px;
  font-weight: 900;
}
</style>

<script>
export default {
  head() {
    return {
      title: 'Free Rewards'
    }
  }
}
</script>
