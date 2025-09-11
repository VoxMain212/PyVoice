<script>
export default {
    props: ['friend'],
    data() {
        return {
            messages: []
        }
    },
    mounted() {
        console.log('created')
    }
}
</script>

<template>
    <div id="friend-frame">
        <div id="friend-title">
            <div>
                {{ friend.nickname }}
            </div>
            <div>
                {{ friend.ip }}
            </div>
        </div>
        <div id="friend-chat-frame" style="flex-grow: 1;">
            <div id="friend-messages">
                <div class="message" v-for="message in messages" @data-message-owner="message.owner.user_hash">
                    <div class="message-avatar">
                        <img src="" alt="">
                    </div>
                    <div class="message-info">
                        <div class="message-owner">
                            {{ message.owner.nickname }}
                        </div>
                        <div class="message-date">
                            {{ message.date }}
                        </div>
                    </div>
                    <div class="message-text">
                        {{ message.text }}
                    </div>
                </div>
            </div>
        </div>
        <div class="mes-inp">
            <div class="mes-input-line">
                <textarea id="mes-input-label" maxlength="2500" style="overflow: hidden; resize: none;" @focusin="focusInpLabel(true)" @focusout="focusInpLabel(false)"></textarea>
                <button type="button" @click="sendMessage()">
                    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <path d="M22 2L11 13"></path>
                        <path d="M22 2l-7 20-4-9-9-4 20-7z"></path>
                    </svg>
                </button>
            </div>
        </div>
    </div>
</template>

<style>
#friend-frame {
    display: flex;
    flex-direction: column;
    height: 100%;
    background-color: var(--bg-chat);
}

#friend-title {
    display: flex;
    flex-direction: row;
}
</style>