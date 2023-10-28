<template>
  <div class="countdown-timer">
    <template v-if="finished" ref="text">
      <div class="timer-slot">
        <span class="timer-slot-value" ref="slot-1">
          00
        </span>
        <span class="timer-slot-name">
          Days
        </span>
      </div>
      <div class="timer-slot">
        <span class="timer-slot-value" ref="slot-2">
          00
        </span>
        <span class="timer-slot-name">
          Hrs
        </span>
      </div>
      <div class="timer-slot">
        <span class="timer-slot-value" ref="slot-3">
          00
        </span>
        <span class="timer-slot-name">
          Min
        </span>
      </div>
      <div class="timer-slot">
        <span class="timer-slot-value" ref="slot-4">
          00
        </span>
        <span class="timer-slot-name">
          Sec
        </span>
      </div>
    </template>
    <template v-else>
      <div class="timer-slot">
        <span class="timer-slot-value" ref="slot-1">
          00
        </span>
        <span class="timer-slot-name">
          Days
        </span>
      </div>
      <div class="timer-slot">
        <span class="timer-slot-value" ref="slot-2">
          00
        </span>
        <span class="timer-slot-name">
          Hrs
        </span>
      </div>
      <div class="timer-slot">
        <span class="timer-slot-value" ref="slot-3">
          00
        </span>
        <span class="timer-slot-name">
          Min
        </span>
      </div>
      <div class="timer-slot">
        <span class="timer-slot-value" ref="slot-4">
          00
        </span>
        <span class="timer-slot-name">
          Sec
        </span>
      </div>
    </template>
<!--      {{ time.formatIntoAbbreviatedString(getRemainingMS, true) }}-->
  </div>
</template>

<style scoped>
.countdown-timer {
  display: flex;
  align-items: center;
  justify-content: center;
}

.timer-slot {
  display: flex;
  align-items: center;
  flex-direction: column;
  flex-shrink: 0;
  width: 80px;
  padding: 15px 0;
  background: rgba(0, 0, 0, 0.5);
  border-radius: 5px;
}

.timer-slot:not(:last-child) {
  margin-right: 10px;
}

.timer-slot .timer-slot-value {
  color: #D7AF3F;
  font-size: 22px;
  font-weight: 900;
  text-transform: uppercase;
}

.timer-slot .timer-slot-name {
  color: #fff;
  font-size: 14px;
  font-weight: 500;
  text-transform: uppercase;
}
</style>

<script>
import {getAbbreviatedBreakdown} from "@/util/time";

export default {
	props: {
		timestamp: {
			type: Number,
			required: true,
		}
	},
	data() {
		return {
			updater: null,
      finished: false,
			time: require('~/util/time'),
		}
	},
	methods: {
		isCountdownFinished() {
			return new Date().getTime() >= this.timestamp;
		},
		getRemainingMS() {
			return this.timestamp - new Date().getTime();
		}
	},
	mounted() {
		setTimeout(() => {
			this.$forceUpdate();
		}, 3);

    if (this.isCountdownFinished()) {
      this.finished = true;
    }

    this.updater = setInterval(() => {
				if (this.isCountdownFinished()) {
          if (!this.finished) {
					  this.$emit('finished');
            this.finished = true;
          } else {
            return
          }
				} else {
          this.finished = false;
        }

        const breakdown = getAbbreviatedBreakdown(this.getRemainingMS(), true);

        if (this.$refs.hasOwnProperty('slot-1')) {
          this.$refs['slot-1'].innerHTML = breakdown[0];
          this.$refs['slot-2'].innerHTML = breakdown[1];
          this.$refs['slot-3'].innerHTML = breakdown[2];
          this.$refs['slot-4'].innerHTML = breakdown[3];
        }
			}, 1000);
	},
	destroyed() {
    clearInterval(this.updater);
	}
}
</script>
