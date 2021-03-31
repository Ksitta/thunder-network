module.exports = {
  devServer: {
    proxy: {
      '/api': {
        target: 'https://thunder-network-thunder.app.secoder.net/',
        changOrigin: true,
      }
    }
  }
}
