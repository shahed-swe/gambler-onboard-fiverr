export const state = () => ({
    mobile: false,
    tablet: false,
    laptop: false,
    desktop: false,
    fullscreen: false,
    resizeListener: null,
});

export const getters = {
    isMobile: (state) => {
        return state.mobile;
    },
    isTablet: (state) => {
        return state.tablet;
    },
    isTabletOrBelow: (state) => {
        return state.tablet || state.mobile;
    },
    isTabletOrAbove: (state) => {
        return state.fullscreen || state.desktop || state.laptop || state.tablet;
    },
    isLaptop: (state) => {
        return state.laptop;
    },
    isLaptopOrBelow: (state) => {
        return state.laptop || state.tablet || state.mobile;
    },
    isLaptopOrAbove: (state) => {
        return state.fullscreen || state.desktop || state.laptop;
    },
    isDesktop: (state) => {
        return state.desktop;
    },
    isDesktopOrBelow: (state) => {
        return state.desktop || state.laptop || state.tablet || state.mobile;
    },
    isDesktopOrAbove: (state) => {
        return state.fullscreen || state.desktop;
    },
    isFullscreen: (state) => {
        return state.fullscreen;
    },
    hasResizeListener: (state) => {
        return state.resizeListener != null;
    }
};

export const mutations = {
    setMobile(state, value) {
        state.mobile = value;
    },
    setTablet(state, value) {
        state.tablet = value;
    },
    setLaptop(state, value) {
        state.laptop = value;
    },
    setDesktop(state, value) {
        state.desktop = value;
    },
    setFullscreen(state, value) {
        state.fullscreen = value;
    },
    setResizeListener(state, listener) {
        state.resizeListener = listener;
    },
};

export const actions = {
    async loadClient({commit}) {

    },
    detectDevice({commit, dispatch, getters}) {
        /*
        mobile      <= 478
        tablet      <= 768
        laptop      <= 959
        desktop     <= 1199
        fullscreen  > 1199
         */
        if (window.innerWidth <= 478) {
            commit('setMobile', true);
            commit('setTablet', false);
            commit('setLaptop', false);
            commit('setDesktop', false);
            commit('setFullscreen', false);
        } else if (window.innerWidth <= 768) {
            commit('setMobile', false);
            commit('setTablet', true);
            commit('setLaptop', false);
            commit('setDesktop', false);
            commit('setFullscreen', false);
        } else if (window.innerWidth <= 959) {
            commit('setMobile', false);
            commit('setTablet', false);
            commit('setLaptop', true);
            commit('setDesktop', false);
            commit('setFullscreen', false);
        } else if (window.innerWidth <= 1199) {
            commit('setMobile', false);
            commit('setTablet', false);
            commit('setLaptop', false);
            commit('setDesktop', true);
            commit('setFullscreen', false);
        } else {
            commit('setMobile', false);
            commit('setTablet', false);
            commit('setLaptop', false);
            commit('setDesktop', false);
            commit('setFullscreen', true);
        }

        if (!getters.hasResizeListener) {
            const listener = (event) => {
                dispatch('detectDevice');
            };

            commit('setResizeListener', listener);
            window.addEventListener('resize', listener, true);
        }
    }
};
