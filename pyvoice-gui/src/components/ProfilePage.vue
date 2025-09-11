<script>
export default {
  data() {
    return {}
  }
}
</script>

<template>
  <div id="profile-block" style="padding: 2rem; height: 100%;">
    <div id="baseinfo" class="set-block">
      <h1>Основная информация</h1>
      <input type="file" class="input" style="max-width: none; margin: 16px 0;">
      <input type="text" placeholder="Имя пользователя" class="input">
    </div>
    <div id="settings" class="set-block" style="margin-top: 2rem;">
      <h2>Дополнительные настройки</h2>
      <!-- Добавь сюда настройки -->
    </div>
  </div>
</template>

<style scoped>
.set-block {
  background-color: var(--bg-sidebar);
  padding: 1.5rem;
  border-radius: var(--radius);
  margin-bottom: 1rem;
}
</style>