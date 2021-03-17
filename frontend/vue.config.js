module.exports = {
  devServer: {
    proxy: {
      '/api': {
        target: 'http://183.172.139.80:8000',
        changOrigin: true,
      }
    }
  }
}
