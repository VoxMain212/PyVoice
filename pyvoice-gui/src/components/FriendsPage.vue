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
    display: flex;
    flex-direction: row;
}

#friend-list {
    min-width: 10vw;
}

.friend-item {
    margin-bottom: 5px;
    color: var(--text-primary);
    display: flex;
    flex-direction: row;
}

.friend-ip {
    color: var(--text-secondary);
}

.friend-avatar {
    border-radius: 25%;
}
</style>