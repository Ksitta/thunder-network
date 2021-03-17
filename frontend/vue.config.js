module.exports = {
  devServer: {
    proxy: {
      '/api': {
        target: 'http://183.172.144.236:8000',
        changOrigin: true,
      }
    }
  }
}
