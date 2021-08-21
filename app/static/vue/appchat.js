const api_get_chat = "/api/chat/getchats"
const api_get_chat_message = "/api/chat/getmessages-"
const api_post_send_message = "/api/chat/sendmessage"

const appChat = {
    data() {
        return {
            currentChatId: 0,
            uid: null,
            chatMessage: '',
            chats: [],
            chatMessages: []
        }
    },
    // computed:
    // {
    //     activeChat(index){
    //         if (index==0){
    //             return {active: true}
    //         }
    //     }
    // },
    methods: {
        send(id) {
            //console.log("Send in chat:" + id + " message:" + this.chatMessage)
            let message = {chat_id: id, message: this.chatMessage}
            self.axios.post(api_post_send_message,  JSON.stringify(message), {headers: {'Accept':'aplication/json','Content-Type': 'application/json'}})
            .then(response => {
                //console.log(response.data);
            })
            .catch(function (error) {
                console.log(error);
            });
            this.chatMessage = ''
            self.axios.get(api_get_chat_message + id).then((response) => {
                this.chatMessages = response.data

            })
        },
        choiseChat(index, id) {
            console.log(index, id)
            for (let i in this.chats) {
                this.chats[i].active = false
            }
            this.chats[index].active = true
            self.axios.get(api_get_chat_message + id).then((response) => {
                this.chatMessages = response.data
            })
        },
        intervalFetchData: function () {
            setInterval(() => {
                self.axios.get(api_get_chat_message + this.currentChatId).then((response) => {
                    this.chatMessages = response.data
                })
                }, 550);
        }
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

            for (let i in this.chats) {
                if (i > 0)
                    this.chats[i].active = false
                else
                    this.chats[i].active = true
            }
            this.currentChatId = response.data[0].id
        })
        // self.axios.get(url_getoperators_api).then((response) => {
        //     this.operators = response.data
        // })
        // self.axios.get(url_getoperations_api).then((response) => {
        //     this.operations = response.data
        // })
    },
    mounted() {
        this.intervalFetchData();
    }

}
// //
const appchat = Vue.createApp(appChat).use(VueAxios, axios)
appchat.mount('#appchat')