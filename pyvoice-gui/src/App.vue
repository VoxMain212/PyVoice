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
	display: flex;
	flex-direction: row;
	height: 100%;
}

#toolbar-comp {
	width: 10vw;
	max-width: 100px;
}

#main-space {
	width: 90vw;
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
