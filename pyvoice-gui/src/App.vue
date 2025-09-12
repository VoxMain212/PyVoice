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
				if (data.status === 'auth') {
					this.registered = true
				}
				else {
					this.registered = false
				}
			}
		})
	},
}
</script>

<template>
	<div v-if="!registered" id="reg-container">
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
#reg-container {
	width: 100%;
}

#main-screen {
	width: 100%;
	display: flex;
	flex-direction: row;
	align-items: stretch;
}

#toolbar-comp {
	width: 5vw;
	max-width: 50px;
	flex-shrink: 0;
}

#main-space {
	flex-grow: 1;
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease;
}

.fade-enter-from {
  opacity: 0;
}

.fade-leave-to {
  opacity: 0;
}
</style>
