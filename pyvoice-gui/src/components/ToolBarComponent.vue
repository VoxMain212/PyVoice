<script>
export default {
  data() {
    return {
      activeComponent: 'FriendsPage'
    }
  },
  methods: {
    changeComponent(component) {
      this.activeComponent = component
      this.$emit('data-from-child', component)
    }
  }
}
</script>

<template>
  <div id="toolbar" class="flex-column">
    <div 
      id="toolbar-friends" 
      class="toolbar-btn" 
      :class="{ active: activeComponent === 'FriendsPage' }"
      @click="changeComponent('FriendsPage')">
      <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <path d="M17 21v-2a4 4 0 0 0-4-4H7a4 4 0 0 0-4 4v2"/>
        <circle cx="9" cy="7" r="4"/>
        <path d="M23 21v-2a4 4 0 0 0-3-3.87"/>
        <path d="M16 3.13a4 4 0 0 1 0 7.75"/>
      </svg>
    </div>
    <div 
      id="toolbar-servers" 
      class="toolbar-btn" 
      :class="{ active: activeComponent === 'ServersPage' }"
      @click="changeComponent('ServersPage')">
      <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <rect x="3" y="3" width="6" height="12" rx="1"/>
        <rect x="15" y="6" width="6" height="12" rx="1"/>
        <rect x="9" y="9" width="6" height="12" rx="1"/>
      </svg>
    </div>
    <div 
      id="toolbar-profile" 
      class="toolbar-btn" 
      :class="{ active: activeComponent === 'ProfilePage' }"
      @click="changeComponent('ProfilePage')">
      <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <circle cx="12" cy="8" r="4"/>
        <path d="M6 20V18a6 6 0 0 1 12 0v2"/>
      </svg>
    </div>
  </div>
</template>

<style scoped>
#toolbar {
  height: 100%;
  background-color: var(--bg-sidebar);
  border-right: 1px solid var(--border);
  padding: 16px 0;
}
</style>