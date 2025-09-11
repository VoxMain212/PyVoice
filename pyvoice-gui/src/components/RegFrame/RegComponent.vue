<script>
import IconSVG from '../icons/IconSVG.vue'

export default {
  data() {
    return {
      nickname: "",
      password: "",
      confirm_password: ""
    }
  },
  methods: {
    gotoLogin() {
      this.$emit('data-from-child', false)
    },
    register() {
      if (!this.nickname || !this.password) {
        console.log("Поля пустые")
        return
      }
      if (this.password !== this.confirm_password) {
        console.log("Пароли не сходятся")
        return  
      }
      let data = {
        type: 'register',
        nickname: this.nickname,
        password: this.password
      }
      window.electronAPI.sendCommand(JSON.stringify(data))
    }
  }
}
</script>

<template>
<main class="flex-row" style="height: 100%;">
  <div class="brand-section">
    <IconSVG style="transform: scale(0.8);"/>
    <h1>PyVoice</h1>
    <p>Современный способ общения с друзьями и коллегами. Быстро, безопасно и с красивым дизайном.</p>
  </div>
  <div class="form-container">
    <h1>Регистрация</h1>
    <input v-model="nickname" type="text" placeholder="Ник" class="input">
    <input v-model="password" type="password" placeholder="Пароль" class="input">
    <input v-model="confirm_password" type="password" placeholder="Подтвердите пароль" class="input">
    <button type="button" class="btn btn-primary" @click="register">Зарегистрироваться</button>
    <button type="button" class="btn btn-secondary" @click="gotoLogin">Есть аккаунт</button>
  </div>
</main>
</template>

<style scoped>
</style>