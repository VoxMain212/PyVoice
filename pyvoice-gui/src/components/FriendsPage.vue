<script>
import SelectedFriend from './SelectedFriend.vue'

export default {
    data() {
        return {
            friends: [
                {
                    nickname: "friend53",
                    ip: "127.0.0.1",
                    img: null,
                },
                {
                    nickname: "friend2",
                    ip: "127.0.0.1",
                    img: null,
                },
                {
                    nickname: "friend3",
                    ip: "127.0.0.1",
                    img: null,
                },
                {
                    nickname: "friend4",
                    ip: "127.0.0.1",
                    img: null,
                }
            ],
            friend_selected: false,
            selected_friend: null
        }
    },
    components: {
        SelectedFriend,
    },
    methods: {
        selectFriend(friend) {
            this.friend_selected = true,
            this.selected_friend = friend
        }
    }
}
</script>

<template>
<div>
    <div id="friend-block">
        <div id="friend-list">
            <div class="friend-item" v-for="friend in friends" @click="selectFriend(friend)">
                <div class="friend-avatar">
                    <img :src="friend.img" alt="404">
                </div>
                <div class="friend-text">
                    <div class="friend-nickname">
                        {{ friend.nickname }}
                    </div>
                    <div class="friend-ip">
                        {{ friend.ip }}
                    </div>
                </div>
            </div>
        </div>
        <div id="seleted-friend-frame" v-if="friend_selected">
            <SelectedFriend :friend="selected_friend" />
        </div>
    </div>
</div>
</template>

<style>
#friend-block {
    overflow: hidden;
    display: flex;
    flex-direction: row;
}

#friend-list {
    padding: 20px;
    min-width: 10vw;
    overflow: hidden;
}

.friend-item {
    margin-bottom: 5px;
    color: var(--text-primary);
    display: flex;
    flex-direction: row;
}
.friend-text {
    margin-left: 20px;
    font-size: var(--font-size-primary);
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}

.friend-ip {
    color: var(--text-secondary);
    font-size: var(--font-size-secondary)
}

.friend-avatar {
    width: 42px;
    height: 42px;
    overflow: hidden;
    border-radius: 100%;
    border-width: 1px;
    border-style: solid;
    border-color: var(--border);
}

#seleted-friend-frame {
    max-width: 90vw;
    min-width: 80vw;
    height: 100vh;
}
</style>