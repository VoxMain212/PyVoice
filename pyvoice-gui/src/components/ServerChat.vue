<script>
export default {
    props: [
        'chat',
        'profile'
    ],
    data() {
        return {
            messages: [

            ],
        }
    },
    mounted() {
        document.addEventListener('keypress', (e) => {
            console.log(e)
            if (e.key == "Enter" && e.shiftKey==false) {
                this.sendMessage()
            }
        })
    },
    methods: {
        sendMessage() {
            let now_data = new Date()
            let message_text = document.querySelector("#mes-input-label").value.trim()
            if (message_text === "") {
                return 
            }
            document.querySelector("#mes-input-label").value = ''
            let date_text = `${now_data.getDate()}.${now_data.getMonth()}.${now_data.getFullYear()} - ${now_data.getHours()}:${now_data.getMinutes()}:${now_data.getSeconds()}`

            let new_message = {
                owner: {
                    user_hash: 'self',
                    nickname:'nickname',

                },
                date: date_text,
                text: message_text,
                pin: null
            }
            this.messages.push(new_message)
        },
        focusInpLabel(select) {
            if (select) {
                document.querySelector("#mes-input-line").classList.add("focused")
            }
            else {
                document.querySelector("#mes-input-line").classList.remove("focused")
            }
        }
    }
}
</script>

<template>
<div id="server-chat-mes">
    <div id="messages-frame">
        <div class="message" v-for="message in messages" 
        @data-owner="message.owner.user_hash"
        :class="(message.owner.user_hash=='self') ? 'self-mes' : ''">
            <div class="mes-avatar" v-if="message.owner=='self'">
                {{ message.owner.img }}
            </div>
            <div class="mes-text">
                <div class="mes-info">
                    <div class="mes-owner-nick">
                        {{ message.owner.nickname }}
                    </div>
                    <div class="mes-date">
                        {{ message.date }}
                    </div>
                </div>
                <div class="mes-message">
                    {{ message.text }}
                </div>
                <div v-if="message.pin">
                    pinned
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

<style scoped>
#server-chat-mes {
    display: flex;
    flex-direction: column;
    height: 100%;
}

#messages-frame {
    flex-grow: 1;
}


.mes-date {
    font-size: small;
    color: var(--text-secondary);
}

.message.self-mes {
    text-align: right;
}
</style>