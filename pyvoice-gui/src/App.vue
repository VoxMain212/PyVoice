<script>
import RegComponent from './components/RegFrame/RegComponent.vue'
import LoginComponent from './components/RegFrame/LoginComponent.vue'
import ToolBarComponent from './components/ToolBarComponent.vue'
import FriendsPage from './components/FriendsPage.vue'
import ServersPage from './components/ServersPage.vue'
import ProfilePage from './components/ProfilePage.vue'

export default {
  components: {
    RegComponent,
    LoginComponent,
    ToolBarComponent,
    FriendsPage,
    ServersPage,
    ProfilePage
  },
  data() {
    return {
      selected_component: 'FriendsPage',
      comp_dict: {
        'FriendsPage': FriendsPage,
        'ServersPage': ServersPage,
        'ProfilePage': ProfilePage
      },
      registered: false,
      register: false,
      currentComponent: null,
      servers: []
    }
  },
  watch: {
    selected_component(newVal) {
      this.currentComponent = this.comp_dict[newVal]
    }
  },
  methods: {
    getServers() {
      window.electronAPI.sendCommand("get-servers")
    },
  },
  mounted() {
    window.electronAPI.onPythonData((data) => {
      console.log('Получено от Python:', data);
      if (data.type === 'auth') {
        this.registered = data.status === 'auth';
      }
    })
  },
}
</script>

<template>
  <div v-if="!registered">
    <transition name="fade" mode="out-in">
      <RegComponent v-if="register" @data-from-child="register = $event"/>
      <LoginComponent v-else @data-from-child="register = $event" @data-reg="registered=$event" />
    </transition>
  </div>
  <main id="main-screen" v-else>
    <ToolBarComponent @data-from-child="currentComponent=$event" id="toolbar-comp"/>
    <div id="main-space">
      <component :is="currentComponent"/>
    </div>
  </main>
</template>

<style scoped>
#main-screen {
  width: 100%;
  display: flex;
  height: 100%;
}

#toolbar-comp {
  width: 5vw;
  max-width: 50px;
  flex-shrink: 0;
}

#main-space {
  flex-grow: 1;
  height: 100%;
}
</style>