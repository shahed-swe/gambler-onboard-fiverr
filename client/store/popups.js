function isActive(popup) {
  return popup.expires > new Date();
}

export const state = () => ({
  popups: [],
  $forceUpdate: null,
});

export const getters = {
  isReady: (state) => {
    return state.$forceUpdate !== null;
  },
  getAll: (state) => {
    return state.popups;
  },
  getActive: (state) => {
    const filtered = [];
    for (let i = 0; i < state.popups.length; i++) {
      const popup = state.popups[i];
      if (isActive(popup)) {
        filtered.push(popup);
      }
    }
    return filtered;
  }
};

export const mutations = {
  initVM(state, vm) {
    state.$forceUpdate = vm.$forceUpdate;
  },
  update(state) {
    state.$forceUpdate();
  },
  addPopup(state, popup) {
    state.popups.push(popup);
  },
  removePopups(state, {popups}) {
    if (popups.length > 0) {
      const filtered = [];
      for (let i = 0; i < state.popups.length; i++) {
        const popup = state.popups[i];
        if (!popups.includes(popup)) {
          filtered.push(popup);
        }
      }
      state.popups = filtered;
      state.$forceUpdate();
    }
  }
};

export const actions = {
  load({getters, commit}) {
    setInterval(() => {
      const remove = [];
      const active = getters.getAll;
      for (let i = 0; i < active.length; i++) {
        const popup = active[i];
        if (!isActive(popup)) {
          remove.push(popup);
        }
      }
      if (remove.length > 0) {
        commit('removePopups', {popups: remove});
      }
    }, 250);
  },
  popup({getters, commit}, {event, message, duration}) {
    const popup = {
      id: Math.round(Math.random() * 1000),
      posX: event.clientX,
      posY: event.clientY,
      message,
      expires: new Date(new Date().getTime() + (duration * 1000.0)),
    }

    console.log(popup)

    commit('addPopup', popup);

    if (getters.isReady) {
      commit('update');
    }
  }
};
