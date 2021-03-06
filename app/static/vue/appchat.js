const api_get_chat = "/api/chat/getchats"
const api_get_chat_message = "/api/chat/getmessages-"
const api_post_send_message = "/api/chat/sendmessage"
const api_get_users = "/api/chat/getusers"
const api_post_create_chat = "/api/chat/createchat"
const appChat = {
    data() {
        return {
            users: [],
            checkUsers: [],
            currentChatId: 0,
            uid: '',
            chatMessage: '',
            chats: [],
            chatMessages: []
        }
    },
    methods: {
        send() {
            //console.log("Send in chat:" + id + " message:" + this.chatMessage)
            let message = {chat_id: this.currentChatId, message: this.chatMessage}
            self.axios.post(api_post_send_message, JSON.stringify(message), {
                headers: {
                    'Accept': 'aplication/json',
                    'Content-Type': 'application/json'
                }
            })
                .then(response => {
                    //console.log(response.data);
                })
                .catch(function (error) {
                    console.log(error);
                });
            this.chatMessage = ''
            self.axios.get(api_get_chat_message + this.currentChatId).then((response) => {
                this.chatMessages = response.data

            })
        },
        choiseChat(index, id) {
            this.currentChatId = id
            for (let i in this.chats) {
                this.chats[i].active = false
            }
            this.chats[index].active = true
            self.axios.get(api_get_chat_message + id).then((response) => {
                //console.log(response.data)
                if (response.data != "")
                    this.chatMessages = response.data
                else
                    this.chatMessages = []
            })
        },
        intervalFetchData: function () {
            setInterval(() => {
                self.axios.get(api_get_chat_message + this.currentChatId).then((response) => {
                    this.chatMessages = response.data
                })
            }, 550);
        },
        AddChat() {
            let users = {users: this.checkUsers}
            self.axios.post(api_post_create_chat, JSON.stringify(users), {
                headers: {
                    'Accept': 'aplication/json',
                    'Content-Type': 'application/json'
                }
            })
                .then(response => {
                    if (response.data.id != "") {
                        this.checkUsers = []
                        self.axios.get(api_get_chat).then((response) => {
                            this.chats = response.data

                            for (let i in this.chats) {
                                if (i != response.data.id)
                                    this.chats[i].active = false
                                else
                                    this.chats[i].active = true
                            }
                            this.currentChatId = response.data.id
                        })
                    }
                })
                .catch(function (error) {
                    //console.log(error);
                });
        }
    },
    created() {

        self.axios.get(api_get_chat).then((response) => {
            this.chats = response.data

            for (let i in this.chats) {
                if (i > 0)
                    this.chats[i].active = false
                else
                    this.chats[i].active = true
            }
            if(response.data!="")
                this.currentChatId = response.data[0].id
        })

    },
    mounted() {
        this.uid = this.$refs.uid.value
        this.intervalFetchData();
        self.axios.get(api_get_users).then((response) => {
            this.users = response.data
        })

    }

}

const appchat = Vue.createApp(appChat).use(VueAxios, axios)
appchat.mount('#appchat')