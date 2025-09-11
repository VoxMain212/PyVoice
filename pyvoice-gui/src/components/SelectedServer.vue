<script>
import ServerChat from './ServerChat.vue';

export default {
  props: ['server'],
  components: { ServerChat },
  data() {
    return {
      members: [],
      channels: [],
      current_chat: null,
    }
  }
}
</script>

<template>
  <div id="server-frame-main" class="flex-column">
    <div id="server-title" class="block-title">
      #{{ server.nickname }}
    </div>
    <div id="server-main" class="flex-row flex-grow">
      <div id="server-channels" class="sidebar">
        <div class="server-subtitle">Комнаты</div>
        <div 
          v-for="channel in channels" 
          :key="channel.title"
          class="list-item"
          :class="channel.type === 'voice' ? 'voice-chat' : 'text-chat'">
          {{ channel.title }}
        </div>
      </div>
      <div id="server-chat" class="flex-grow">
        <ServerChat :chat="current_chat" />
      </div>
      <div id="server-members" class="sidebar sidebar-right">
        <div class="server-subtitle">Участники</div>
        <div 
          v-for="member in members" 
          :key="member.nickname"
          class="list-item"
          :class="{ online: member.online }">
          <div class="avatar">
            <img v-if="member.img" :src="member.img" :alt="member.nickname">
            <span v-else>{{ member.nickname[0].toUpperCase() }}</span>
          </div>
          <div class="member-nickname">{{ member.nickname }}</div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.server-subtitle {
  font-weight: bold;
  margin: 16px 0 8px;
  color: var(--text-primary);
}
</style>