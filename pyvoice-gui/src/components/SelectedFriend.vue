<script>
export default {
    props: ['friend'],
    mounted() {
        console.log('created')
    }
}
</script>

<template>
<div>
    <div id="friend-frame">
        <div id="friend-title">
            <div>
                {{ friend.nickname }}
            </div>
            <div>
                {{ friend.ip }}
            </div>
        </div>
        <div id="friend-chat-frame">
            <!-- Создать логику создания или загрузки чата -->
        </div>
    </div>
</div>
</template>

<style>

</style>