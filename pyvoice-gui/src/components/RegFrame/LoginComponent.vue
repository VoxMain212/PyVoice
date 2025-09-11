<script>
export default {
  data() {
    return {
      register: false
    }
  },
  methods: {
    gotoLogin() {
      this.$emit('data-from-child', true)
    },
    login() {
      this.$emit("data-reg", true)
    }
  },
}
</script>

<template>
<main class="flex-row" style="height: 100%;">
  <div class="form-container">
    <h1>Вход</h1>
    <input type="text" placeholder="Ник" class="input">
    <input type="text" placeholder="Пароль" class="input">
    <button type="button" class="btn btn-primary" @click="login">Войти</button>
    <button type="button" class="btn btn-secondary" @click="gotoLogin">Зарегистрироваться</button>
  </div>
  <div class="brand-section">
    <IconSVG style="transform: scale(0.8);"/>
    <h1>PyVoice</h1>
    <p>Современный способ общения с друзьями и коллегами. Быстро, безопасно и с красивым дизайном.</p>
  </div>
</main>
</template>

<style scoped>
</style>