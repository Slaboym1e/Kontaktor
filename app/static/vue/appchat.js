const api_get_chat = "/api/chat/getchats"

const appChat = {
    data() {
        return {
            currentChatId: 0,
            chatMessage: '',
            chats : []
        }
    },
    methods: {
        send(id) {
            console.log("Send in chat:" + id + " message:" + this.chatMessage)
            this.chatMessage = ''
        },
        // delOperation(id) {
        //     this.changeOperation.splice(id, 1)
        // },
        // addOperatorOperator() {
        //     this.operatorList[this.operatorList.length] = {
        //         id: this.operatorList.length,
        //         priority: this.operatorList.length+1,
        //         operation: 0,
        //         operator: 0,
        //         machine: 0
        //     }
        // }
    },
    created() {
        self.axios.get(api_get_chat).then((response) => {
            this.chats = response.data
        })
        // self.axios.get(url_getoperators_api).then((response) => {
        //     this.operators = response.data
        // })
        // self.axios.get(url_getoperations_api).then((response) => {
        //     this.operations = response.data
        // })
    },
    mounted() {

    }

}
// //
const appchat = Vue.createApp(appChat).use(VueAxios, axios)
appchat.mount('#appchat')