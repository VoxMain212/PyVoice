<script>
import FriendsPage from './FriendsPage.vue';
import ServersPage from './ServersPage.vue';
import ProfilePage from './ProfilePage.vue';

export default {
    data() {
    
    },
    components: {
        FriendsPage,
        ServersPage,
        ProfilePage
    },
    methods: {
        changeComponent(component) {
            this.$emit('data-from-child', component)
            if (component == 'FriendsPage') {
                document.querySelector("#toolbar-friends").classList.add('active')
                document.querySelector("#toolbar-servers").classList.remove('active')
                document.querySelector("#toolbar-profile").classList.remove('active')
            } else if (component == 'ServersPage') {
                document.querySelector("#toolbar-servers").classList.add('active')
                document.querySelector("#toolbar-friends").classList.remove('active')
                document.querySelector("#toolbar-profile").classList.remove('active')
            } else if (component == 'ProfilePage') {
                document.querySelector("#toolbar-profile").classList.add('active')
                document.querySelector("#toolbar-servers").classList.remove('active')
                document.querySelector("#toolbar-friends").classList.remove('active')
            }
        }
    },
}
</script>

<template>
    <div>
        <div id="toolbar">
            <div id="toolbar-friends" class="toolbar-btn" @click="changeComponent('FriendsPage')">
                <div>
                    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <path d="M17 21v-2a4 4 0 0 0-4-4H7a4 4 0 0 0-4 4v2"/>
                        <circle cx="9" cy="7" r="4"/>
                        <path d="M23 21v-2a4 4 0 0 0-3-3.87"/>
                        <path d="M16 3.13a4 4 0 0 1 0 7.75"/>
                    </svg>
                </div>
                <div>
                    Друзья
                </div>
            </div>
            <div id="toolbar-servers" class="toolbar-btn" @click="changeComponent('ServersPage')">
                <div>
                    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <rect x="3" y="3" width="6" height="12" rx="1"/>
                        <rect x="15" y="6" width="6" height="12" rx="1"/>
                        <rect x="9" y="9" width="6" height="12" rx="1"/>
                    </svg>
                </div>
                <div>
                    Сервера
                </div>
            </div>
            <div id="toolbar-profile" class="toolbar-btn" @click="changeComponent('ProfilePage')">
                <div>
                    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <circle cx="12" cy="8" r="4"/>
                        <path d="M6 20V18a6 6 0 0 1 12 0v2"/>
                    </svg>
                </div>
                <div>
                    Профиль
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
#toolbar {
    overflow: hidden;
    display: flex;
    flex-direction: column;
    justify-content: start;
    align-items: center;
    background-color: var(--bg-sidebar);
    height: 100vh;
    border-right-color: var(--border);
    border-right-width: 1px;
    border-right-style: solid;
}

.toolbar-btn {
    padding: auto;
    margin-top: 1vh;
    display: flex;
    padding: 10px;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    align-content: center;
    color: var(--text-primary);
    
    transition: var(--transition);
}

.toolbar-btn:hover {
    background-color: var(--accent);
    border-radius: var(--radius);
    box-shadow: 0px 0px 4px var(--accent);
    transition: var(--transition);
}

.toolbar-btn.active {
    background-color: var(--hover-overlay);
    border-radius: 10%;
}
</style>