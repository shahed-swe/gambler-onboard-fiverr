<template>
  <div id="footer">
    <div class="uk-container">
      <div class="footer__inner">
        <div class="footer__primary">
          <nuxt-link :to="{ name: 'index' }" class="brand">
            TheGambler
          </nuxt-link>

          <div class="footer__nav">
            <a href="https://www.youtube.com/@thegambler1999">
              <i class="fa-brands fa-youtube"></i>
            </a>
            <a href="https://www.kick.com/thegambler1999">
              <i class="fa-brands fa-kickstarter"></i>
            </a>
            <a href="https://www.twitter.com/TheGambler1999">
              <i class="fa-brands fa-twitter"></i>
            </a>
            <a href="https://discord.com/thegambler">
              <i class="fa-brands fa-discord"></i>
            </a>
          </div>
        </div>

        <div class="footer__secondary">
          <span class="disclaimer">
            Must be <strong>18+</strong> to participate. Gamble responsibly.
          </span>

          <div class="legal">
            <nuxt-link :to="{ name: 'faq' }">
              FAQ
            </nuxt-link>
            <nuxt-link :to="{ name: 'privacy' }">
              Privacy
            </nuxt-link>
            <a href="https://www.begambleaware.org">
              GambleAware
            </a>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
#footer,
#footer .footer__inner {
  height: 100px;
}

#footer {
  position: relative;
  z-index: 1500;
  width: 100%;
  background: rgb(23,45,73);
  background: linear-gradient(180deg, rgb(23,45,73) 0%, rgba(255, 255, 255, 0) 100%);
  border-top: 2px solid rgba(255, 255, 255, 0.1);
}

#footer .footer__inner {
  display: flex;
  align-items: center;
}

#footer .footer__primary {
  display: flex;
}

#footer .footer__secondary {
  display: flex;
  flex-direction: column;
  margin-left: auto;
}

#footer .brand {
  display: flex;
  align-items: center;
  font-size: 26px;
  font-weight: 700;
  letter-spacing: 1px;
  color: #fff;
}

#footer .brand > strong {
  display: block;
  margin-left: 6px;
  color: #FFD799;
}

#footer .footer__nav {
  display: flex;
  align-items: center;
  margin-top: 10px;
  margin-left: 40px;
}

#footer .footer__nav > a {
  color: rgba(255, 255, 255, 0.8);
  font-size: 14px;
  font-weight: bold;
  text-transform: uppercase;
}

#footer .footer__nav > a:not(:last-child) {
  margin-right: 20px;
}

#footer .footer__nav > a:hover {
  color: #fff;
}

#footer .footer__nav > a > i {
  width: 24px;
  color: rgba(255, 255, 255, 0.8);
  font-size: 20px;
  text-align: center;
}

#footer .footer__nav > a:not(:last-child) > i {
  margin-right: 8px;
}

#footer .footer__nav > a > i:hover {
  color: #fff;
}

#footer .legal {
  display: flex;
  align-items: center;
  justify-content: end;
  margin-top: 6px;
}

#footer .legal > a {
  color: rgba(255, 255, 255, 0.8);
  font-size: 14px;
  text-transform: uppercase;
  letter-spacing: 2px;
}

#footer .legal > a:not(:first-child) {
  margin-left: 20px;
}

#footer .legal > a:hover {
  color: #fff;
}

#footer .disclaimer {
  display: flex;
  align-items: center;
  color: #fff;
  font-size: 13px;
  font-weight: 700;
  letter-spacing: 1px;
  text-transform: uppercase;
}

#footer .disclaimer > strong {
  display: inline-block;
  margin: 0 5px;
  color: #ffdb59;
}

@media screen and (max-width: 768px) {
  #footer {
    height: auto;
  }

  #footer .footer__inner {
    height: auto;
    flex-direction: column;
    padding: 20px 10px;
  }

  #footer .footer__primary {
    flex-direction: column;
  }

  #footer .footer__secondary {
    flex-direction: column;
    margin-left: unset;
  }

  #footer .footer__nav {
    width: 100%;
    justify-content: center;
    margin-left: unset;
  }

  #footer .disclaimer {
    display: block;
    margin-top: 20px;
    text-align: center;
  }

  #footer .disclaimer > strong {
    margin: 0 3px;
  }

  #footer .legal {
    margin-top: 20px;
    margin-left: unset;
    justify-content: center;
  }
}
</style>

<script>
export default {

}
</script>
