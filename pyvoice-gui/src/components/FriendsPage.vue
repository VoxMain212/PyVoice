<script>
import SelectedFriend from './SelectedFriend.vue'

export default {
  components: { SelectedFriend },
  data() {
    return {
      friends: [
        { nickname: "friend53", ip: "127.0.0.1", img: null },
        { nickname: "friend2", ip: "127.0.0.1", img: null },
        { nickname: "friend3", ip: "127.0.0.1", img: null },
        { nickname: "friend4", ip: "127.0.0.1", img: null }
      ],
      friend_selected: false,
      selected_friend: null
    }
  },
  methods: {
    selectFriend(friend) {
      this.friend_selected = true
      this.selected_friend = friend
    }
  }
}
</script>

<template>
  <div id="friend-block" class="flex-row" style="height: 100%;">
    <div id="friend-list" class="sidebar">
      <div 
        class="friend-item list-item" 
        v-for="friend in friends" 
        @click="selectFriend(friend)"
        :key="friend.nickname">
        <div class="avatar">
          <img v-if="friend.img" :src="friend.img" :alt="friend.nickname">
          <span v-else>{{ friend.nickname[0].toUpperCase() }}</span>
        </div>
        <div class="friend-text">
          <div>{{ friend.nickname }}</div>
          <div class="text-secondary">{{ friend.ip }}</div>
        </div>
      </div>
    </div>
    <div id="selected-friend-frame" v-if="friend_selected" class="flex-grow">
      <SelectedFriend :friend="selected_friend" />
    </div>
  </div>
</template>

<style scoped>
</style>