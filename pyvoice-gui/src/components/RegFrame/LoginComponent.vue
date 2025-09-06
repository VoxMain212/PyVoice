<script>
export default {
    data() {
        return {
            register: false
        }
    },
    methods: {
        gotoLogin() {
            this.register = true
            console.log(this.register)
            this.$emit('data-from-child', this.register)
        },
        login() {
            // let data = {
			//     type: "auth"
    		// }
	    	// let json_data = JSON.stringify(data)
		    // console.log(json_data)
		    // window.electronAPI.sendCommand(json_data)
            this.$emit("data-reg", true)
        }
    },
}
</script>

<template>
<main>
    <div id="reg-form" style="width: 50vw;">
        <form action="">
            <h1 style="color:white">Вход</h1>
            <input type="text" placeholder="Ник" class="stand-inp">
            <input type="text" placeholder="Пароль" class="stand-inp">
            <button class="primary-btn" @click="login">Войти</button>
            <button class="primary-btn" @click="gotoLogin">Зарегистрироватся</button>
        </form>
    </div>
    <div style="width: 50vw;user-select: none" class="brand-section">
        <IconSVG style="transform: scale(0.8);"/>
        <h1>PyVoice</h1>
        <p>Современный способ общения с друзьями и коллегами. Быстро, безопасно и с красивым дизайном.</p>
    </div>
</main>


</template>

<style scoped>
.brand-section {
    padding: 30px;
    color: white;
    text-align: justify;
    flex: 1;
    background: linear-gradient(135deg, #7289da, #5865f2);
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding: 2rem;
    position: relative;
    overflow: hidden;
}

main {
    height: 100%;
    display: flex;
    flex-direction: row;
}
</style>