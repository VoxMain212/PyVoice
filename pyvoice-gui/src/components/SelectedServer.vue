<script>
export default {
    props: [
        'server'
    ],
    data() {
        return {

        }
    },
    mounted() {
        console.log(this.server)
    }
}
</script>

<template>
<div>
    <div id="server-frame">
        <div id="server-title">
            #{{ server.nickname }}
        </div>
        <div id="server-main">
            <div id="server-channels">

            </div>
            <div id="server-chat">

            </div>
            <div id="server-members">
                
            </div>
        </div>
    </div>
</div>
</template>

<style>
#server-frame {
    min-width: 70vw;
    width: 90vw;
    max-width: 90vw;
    height: 100vh;
    background-color: var(--bg-chat);
}

#server-title {
    padding: 10px;
    font-size: 28px;
    width: 100%;
    background-color: var(--bg-sidebar);
}
</style>