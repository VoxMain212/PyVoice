<script>
import SelectedServer from './SelectedServer.vue'

export default {
    components: {
        SelectedServer
    },
    data() {
        return {
            servers: [
                {
                    img: "",
                    nickname: 'server1'
                },
                {
                    img: "",
                    nickname: 'server5'
                },
                {
                    img: "",
                    nickname: 'server2'
                },
                {
                    img: "",
                    nickname: 'server3'
                },
            ],
            current_server: null
        }
    },
    methods: {
        selectServer(server) {
            this.current_server=server
            console.log("Выбран сервер"+String(server))
        },
        loadServerImg(server_name)
        {

        }
    }
}
</script>

<template>
<div id="server-page">
    <div id="server-list">
        <div v-for="server in servers" @click="selectServer(server)" class="server-item">
            <div class="server-avatar">
                <img :src="server.img" onerror="this.style.display='none'; this.nextElementSibling.style.display='block';">
                <span class="fallback-text">{{ server.nickname[0] }}</span>
            </div>
            <div class="server-text">
                {{ server.nickname }}
            </div>
        </div>
    </div>
    <div id="server-frame">
        <SelectedServer :server="current_server" />
    </div>
</div>
</template>

<style>
#server-page {
    display: flex;
    flex-direction: row;
}

#server-list {
    padding: 7px;
    border-right-style: solid;
    border-right-width: 1px;
    border-right-color: var(--border);
    height: 100vh;
    overflow-x: hidden;
}

.server-item {
    margin-top: 5px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: start;
}

.server-avatar {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 52px;
    height: 52px;
    border-radius: 100%;
    border-color: var(--border);
    border-style: solid;
    border-width: 1px;
    box-shadow: 0px 0px 6px var(--accent);
    overflow: hidden;
}

.server-avatar img {
    width: 52px;
    height: 52px;
    text-align: center;
}

.fallback-text {
    width: 52px;
    height: 52px;
    font-size: 38px;
    text-align: center;
    background-color: var(--accent);
}
</style>