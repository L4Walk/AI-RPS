const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  css: {
    loaderOptions: {
        // 给 sass-loader 传递选项
        scss: {
            // @/ 是 src/ 的别名
            // 注意：在 sass-loader v7 中，这个选项名是 "data"
            prependData: `@import "@nutui/nutui/dist/styles/variables.scss";`,
        }
    },
  }
}
)
