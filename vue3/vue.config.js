const { defineConfig } = require('@vue/cli-service')
const BundleTracker = require("webpack-bundle-tracker")

module.exports = defineConfig({
    transpileDependencies: true,

    // Los puntos de entrada de nuestra aplicación.
    pages: {
        main: {
            entry: './src/main.ts',
        },
    },

    // La ruta donde estará disponible el bundle de los archivos estáticos
    publicPath: process.env.NODE_ENV === 'production'
        ? '/static/vue3/'
        : 'http://localhost:8080/',

    // Directorio donde se creará el bundle de archivos estáticos
    outputDir: './../static/vue3/',

    // Establece que se compile en tiempo de ejecución.
    runtimeCompiler: true,

    chainWebpack: config => {
        // El archivo que mapeará los estáticos del proyecto.
        config
            .plugin('BundleTracker')
            .use(BundleTracker, [{filename: '../vue3/webpack-stats.json'}]);

    },
    devServer: {
        client: {
            webSocketURL: 'auto://localhost:8080'
        },
        host: 'localhost',
        port: 8080,
        hot: 'only',
        https: false,
        headers : {"Access-Control-Allow-Origin": ["*"]},
        static: {
            watch: {
                poll: 1000,
            }
        },
    },
})
