<script>
import ServerChat from './ServerChat.vue';

export default {
    props: [
        'server'
    ],
    components: {
        ServerChat
    },
    data() {
        return {
            members: [],
            channels: [],
            current_chat: null,
        }
    },
    mounted() {
        console.log(this.server)
    }
}
</script>

<template>
    <div id="server-frame-main">
        <div id="server-title">
            #{{ server.nickname }}
        </div>
        <div id="server-main">
            <div id="server-channels">
                <div class="server-subtitle">
                    Комнаты
                </div>
                <div v-for="channel in channels" :class="'chat' (channel.type == 'voice') ? 'voice-chat' : 'text-chat'">
                    {{ channel.title }}
                </div>
            </div>
            <div id="server-chat">
                <ServerChat :chat="current_chat" />
            </div>
            <div id="server-members">
                <div class="server-subtitle">
                    Участники
                </div>
                <div v-for="member in members" :class="(member.online) ? 'online' : ''">
                    <div class="member-avatar">
                        <img :src="member.img" alt="">
                    </div>
                    <div class="member-nickname">
                        {{ member.nickname }}
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<style>
#server-channels {
    width: 10vw;
    height: 100%;
    background-color: var(--bg-sidebar);
    border-right-color: var(--border);
    border-right-width: 1px;
    border-right-style: solid;
}

#server-chat {
    flex-grow: 1;
}

#server-members {
    width: 10vw;
    height: 100%;
    background-color: var(--bg-sidebar);
    border-left-color: var(--border);
    border-left-style: solid;
    border-left-width: 1px;
}

#server-main {
    display: flex;
    flex-direction: row;
    flex-grow: 1;
}

#server-frame-main {
    min-width: 70vw;
    width: 100%;
    background-color: var(--bg-chat);
    display: flex;
    flex-direction: column;
}

#server-title {
    padding: 10px;
    font-size: 28px;
    width: 100%;
    background-color: var(--bg-sidebar);
    border-bottom-style: solid;
    border-bottom-color: var(--border);
    border-bottom-width: 1px;
}
</style>