<template>
  <div id="header">
    <div class="header__inner">
      <div class="header__primary">
        <div class="brand">
          <img src="~assets/images/logo.png" alt=""/>

          <nuxt-link :to="{ name: 'index' }" class="brand-name">
            TheGambler
          </nuxt-link>
<!--            <nuxt-link :to="{ name: 'index' }" class="shiny">-->
<!--              <span class="inner-shiny">TheGambler</span>-->
<!--            </nuxt-link>-->
        </div>

        <div class="header__nav">
          <nuxt-link :to="{ name: 'leaderboard' }" class="leaderboard-link">
            <i class="fa-solid fa-trophy-star"></i>
            Leaderboard
          </nuxt-link>
          <nuxt-link :to="{ name: 'videos' }">
            <i class="fa-solid fa-play"></i>
            Videos
          </nuxt-link>
          <nuxt-link :to="{ name: 'rewards' }" class="rewards-link">
            <i class="fa-solid fa-treasure-chest"></i>
            Rewards
          </nuxt-link>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
#header,
#header .header__inner {
  height: 100px;
}

#header {
  position: relative;
  z-index: 1500;
  width: 100%;
  background: rgb(23,45,73);
  background: linear-gradient(180deg, rgb(23,45,73) 0%, rgba(255, 255, 255, 0) 100%);
  border-bottom: 2px solid rgba(255, 255, 255, 0.1);
  padding: 0 40px;
}

#header .header__inner {
  display: flex;
  align-items: center;
}

#header .header__primary {
  display: flex;
  width: 100%;
}

#header .brand {
  display: flex;
  align-items: center;
}

#header .brand > .brand-name {
  color: #fff;
  font-size: 36px;
  font-family: 'Bebas Neue', sans-serif;
  text-shadow: 0 5px rgba(0, 0, 0, 0.3);
  letter-spacing: 1px;
  line-height: 36px;
}

#header .brand > img {
  width: 30px;
  height: 35px;
  margin-right: 14px;
}

#header .brand > strong {
  display: block;
  margin-left: 6px;
  color: #fff;
}

#header .header__nav {
  display: flex;
  align-items: center;
  margin-left: auto;
}

#header .header__nav > a {
  flex-shrink: 0;
  display: block;
  padding: 14px 26px;
  background: rgba(66, 119, 187, 0.4);
  border-radius: 10px;
  color: rgba(255, 255, 255, 0.8);
  font-weight: bold;
  font-size: 16px;
  transition: all ease-in-out .15s;
}

#header .header__nav > a:not(:last-child) {
  margin-right: 20px;
}

#header .header__nav > a:hover {
  color: #fff;
}

#header .header__nav > a i {
  margin-right: 8px;
  color: rgba(255, 255, 255, 0.6);
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
  transition: all ease-in-out .15s;
}

#header .header__nav > a:hover > i {
  transform: scale(1.3) rotate(-10deg);
}

@media screen and (max-width: 768px) {
  #header {
    height: auto;
  }

  #header .header__inner {
    flex-direction: column;
    align-items: flex-start;
    height: auto;
    padding: 20px 10px;
  }

  #header .header__primary {
    width: 100%;
    flex-direction: column;
  }

  #header .header__nav {
    flex-direction: column;
    align-items: flex-start;
    margin-top: 10px;
    margin-left: unset;
  }

  #header .header__nav > a:not(:last-child) {
    margin-bottom: 10px;
  }
}
</style>

<script>
export default {}
</script>
