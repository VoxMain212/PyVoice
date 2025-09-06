<script>
import IconSVG from '../icons/IconSVG.vue'

export default {
    data() {
        return {
            register: true,
            nickname: "",
            password: "",
            confirm_password: ""
        }
    },
    methods: {
        gotoLogin() {
            this.register = false
            console.log(this.register)
            this.$emit('data-from-child', this.register)
        },
        register() {
            if (this.nickname.length !== 0 || this.password.length !== 0) {
                console.log("Поля пустые")
                return
            }
            if (this.password !== this.confirm_password)
            {
                console.log("Пароли не сходятся")
                return  
            }
            let data = {
                type: 'register',
                nickname: this.nickname,
                password: this.password
            }
            let json_data = JSON.stringify(data)
            window.electronAPI.sendCommand(json_data)
        }
    }
}
</script>

<template>
<main>
    <div style="width: 50vw;user-select: none" class="brand-section">
        <IconSVG style="transform: scale(0.8);"/>
        <h1>PyVoice</h1>
        <p>Современный способ общения с друзьями и коллегами. Быстро, безопасно и с красивым дизайном.</p>
    </div>
    <div id="reg-form" style="width: 50vw;">
        <form action="">
            <h1>Регистрация</h1>
            <input v-model="nickname" type="text" placeholder="Ник" class="stand-inp reg">
            <input v-model="password" type="text" placeholder="Пароль" class="stand-inp reg">
            <input v-model='confirm_password' type="text" placeholder="Подтвердите пароль" class="stand-inp reg">
            <button class="primary-btn" @click="register">
                Зарегистрироватся
            </button>
            <button class="primary-btn" @click="gotoLogin">
                Есть аккаунт
            </button>
        </form>
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