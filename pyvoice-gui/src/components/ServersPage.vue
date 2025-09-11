<script>
import SelectedServer from './SelectedServer.vue'

export default {
  components: { SelectedServer },
  data() {
    return {
      servers: [
        { img: "", nickname: 'server1' },
        { img: "", nickname: 'server5' },
        { img: "", nickname: 'server2' },
        { img: "", nickname: 'server3' }
      ],
      current_server: null
    }
  },
  methods: {
    selectServer(server) {
      this.current_server = server
    }
  }
}
</script>

<template>
  <div id="server-page" class="flex-row" style="height: 100%;">
    <div id="server-list" class="sidebar">
      <div 
        class="server-item list-item" 
        v-for="server in servers" 
        :key="server.nickname"
        @click="selectServer(server)">
        <div class="avatar avatar-large">
          <img v-if="server.img" :src="server.img" :alt="server.nickname">
          <span v-else>{{ server.nickname[0].toUpperCase() }}</span>
        </div>
        <div class="server-text">{{ server.nickname }}</div>
      </div>
    </div>
    <SelectedServer v-if="current_server" :server="current_server" />
  </div>
</template>

<style scoped>
</style>