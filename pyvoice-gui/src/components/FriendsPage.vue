<script>
export default {
    data() {
        return {
            handler: null,
            friendList: []
        }
    },
    methods: {
        getFriends() {
            // let gettedData = JSON.parse(data)
            this.friendList = [
                {
                    'nickname':'vova',
                    'ip': '127.0.0.1',
                    'online': true
                }
            ]
            // console.log(gettedData)
        }
    },
    mounted() {
        // this.handler = this.getFriends
        // window.electronAPI.onPythonData(this.handler)
        // let data = {
        //     type: 'get-friends'
        // }
        // window.electronAPI.sendCommand(JSON.stringify(data))
    },
    beforeUnmount() {
        if (this.handler){
            const { ipcRenderer } = require('electron')
            ipcRenderer.off('python-data', this.handler)
            this.handler = null
            console.log('Unmounted')
        }
    }
}
</script>

<template>
<div id="friend-list">
    <div v-for="friend in friendList">
        <div class="friend-avatar">

        </div>
        <div class="friend-nickname">

        </div>
        <div class="friend-ip">

        </div>
    </div>
</div>
</template>

<style>

</style>