import {Loading} from 'element-ui'

let loading

function  startLoading() {
  loading = Loading.service({
    lock: true,
    // text: 'Load……',
    spinner: 'el-icon-loading',
    background: 'rgba(255, 255, 255, 0.7)',
    target: document.querySelector('.loading-area'),
  })
}
function endLoading() {
  loading.close()
}

let needLoadingRequestCount = 0

export function showFullScreenLoading() {
  if(needLoadingRequestCount === 0){
    startLoading()
  }
  needLoadingRequestCount++
}

export function hideFullScreenLoading() {
  if(needLoadingRequestCount <= 0) return
  needLoadingRequestCount--
  if(needLoadingRequestCount === 0){
    endLoading()
  }
}

export default{
    showFullScreenLoading,
    hideFullScreenLoading
}

