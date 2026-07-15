import React, {useEffect} from 'react'
import axios from 'axios'

export default function Login(){
  useEffect(()=>{
    // Telegram WebApp provides init data via window.Telegram.WebApp.initDataRaw or via query
    const params = new URLSearchParams(window.location.search)
    const init_data = params.get('init_data') || window.Telegram?.WebApp?.initData || ''
    if(init_data){
      axios.post('/api/auth/webapp-login', {init_data}).then(r=>{
        console.log('got token', r.data)
        alert('登录成功，模拟 token 已返回，查看控制台')
      }).catch(e=>{
        console.error(e)
        alert('登录失败（本地示例）')
      })
    }
  },[])
  return (
    <div>
      <p>This is a minimal WebApp login page. When opened by Telegram, init_data will be sent to backend to log in.</p>
    </div>
  )
}
