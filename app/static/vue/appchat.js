const appChat = {
    data() {
        return {
            chatId: ''
        }
    },
    methods: {
        // addOperation(val) {
        //     this.changeOperation[this.changeOperation.length] = {id: val, title: this.operations[val - 1].title}
        //     this.operationslist = ''
        // },
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
        // self.axios.get(url_getmachine_api).then((response) => {
        //     this.machines = response.data
        // })
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