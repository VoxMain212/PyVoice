<script>
export default {
  props: ['chat', 'profile'],
  data() {
    return {
      messages: [],
      isFocused: false
    }
  },
  mounted() {
    document.addEventListener('keypress', this.handleKeyPress)
  },
  beforeUnmount() {
    document.removeEventListener('keypress', this.handleKeyPress)
  },
  methods: {
    handleKeyPress(e) {
      if (e.key === "Enter" && !e.shiftKey) {
        e.preventDefault()
        this.sendMessage()
      }
    },
    sendMessage() {
      const text = this.$refs.messageInput.value.trim()
      if (!text) return

      const now = new Date()
      const dateText = `${now.getDate()}.${now.getMonth() + 1}.${now.getFullYear()} - ${now.getHours()}:${now.getMinutes()}:${now.getSeconds()}`

      this.messages.push({
        owner: { user_hash: 'self', nickname: 'You' },
        date: dateText,
        text: text
      })

      this.$refs.messageInput.value = ''
    }
  }
}
</script>

<template>
  <div id="server-chat-mes" class="flex-column" style="height: 100%;">
    <div id="messages-frame" class="flex-grow" style="padding: 16px; overflow-y: auto;">
      <div 
        class="message" 
        v-for="(message, index) in messages" 
        :key="index"
        :class="{ 'self-mes': message.owner.user_hash === 'self' }">
        <div class="mes-avatar avatar" v-if="message.owner.user_hash === 'self'">
          You
        </div>
        <div class="mes-text">
          <div class="mes-info">
            <div class="mes-owner-nick">{{ message.owner.nickname }}</div>
            <div class="mes-date">{{ message.date }}</div>
          </div>
          <div class="mes-message">{{ message.text }}</div>
        </div>
      </div>
    </div>
    <div class="mes-inp" style="padding: 16px;">
      <div class="mes-input-line" :class="{ focused: isFocused }">
        <textarea
          ref="messageInput"
          maxlength="2500"
          @focus="isFocused = true"
          @blur="isFocused = false"
        ></textarea>
        <button type="button" @click="sendMessage()">
          <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M22 2L11 13"></path>
            <path d="M22 2l-7 20-4-9-9-4 20-7z"></path>
          </svg>
        </button>
      </div>
    </div>
  </div>
</template>

<style scoped>
/* Всё в utils.css */
</style>