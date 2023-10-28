export default {
    target: 'static',
    server: {
        host: 'localhost',
        port: 80
    },
    ssr: false,
    head: {
        title: 'Loading',
        titleTemplate: '%s - TheGambler',
        htmlAttrs: {
            lang: 'en'
        },
        meta: [
            {
                charset: 'utf-8'
            },
            {
                name: 'viewport',
                content: 'width=device-width, initial-scale=1'
            },
            {
                hid: 'description',
                name: 'description',
                content: 'TheGambler is an upcoming content creator that uploads and streams gambling/variety content. Use our codes to claim rewards/prizes on affiliated sites. Gamble responsibly!'
            },
            {
                name: 'format-detection',
                content: 'telephone=no'
            },
            {
                name: 'twitter:widgets:theme',
                content: 'dark'
            }
        ],
        link: [
            {
                rel: 'preconnect',
                href: 'https://fonts.googleapis.com'
            },
            {
                rel: 'preconnect',
                href: 'https://fonts.gstatic.com'
            },
            {
                rel: 'stylesheet',
                type: 'text/css',
                href: 'https://cdn.jsdelivr.net/npm/uikit@3.5.7/dist/css/uikit.min.css'
            },
            {
                rel: 'stylesheet',
                href: 'https://cdnjs.cloudflare.com/ajax/libs/MaterialDesign-Webfont/6.5.95/css/materialdesignicons.min.css',
                crossorigin: 'anonymous',
                referrerpolicy: 'no-referrer'
            },
            {
                rel: 'icon',
                type: 'image/x-icon',
                href: '/favicon.ico'
            }
        ],
        script: [
            {
                src: 'https://cdn.jsdelivr.net/npm/uikit@3.5.7/dist/js/uikit.min.js'
            },
            {
                src: 'https://cdn.jsdelivr.net/npm/uikit@3.5.7/dist/js/uikit-icons.min.js'
            },
            {
                src: 'https://kit.fontawesome.com/1250b98b47.js',
                crossorigin: 'anonymous'
            },
            {
                src: 'https://cdnjs.cloudflare.com/ajax/libs/particlesjs/2.2.3/particles.min.js'
            },
            {
                src: 'https://platform.twitter.com/widgets.js',
                charset: 'utf-8'
            }
        ]
    },
    css: [
        {
            src: '~assets/styles/client.css'
        }
    ],
    plugins: [],
    components: {
        dirs: [
            '~/components',
            '~/components/ui'
        ]
    },
    loaders: {
        vue: {
            transformAssetUrls: {
                img: 'data-src',
                div: 'data-src'
            }
        }
    },
    buildModules: [
        // '@nuxtjs/eslint-module',
        '@nuxt/components'
    ],
    modules: [
        '@nuxtjs/axios',
    	'@nuxtjs/auth-next'
    ],
    axios: {
        baseURL: 'http://35.208.70.220:8000/api/',
        progress: true
    },
    build: {}
}
