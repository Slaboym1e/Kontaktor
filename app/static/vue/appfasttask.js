// const url_getmachine_api = "/techproc/api/getmachines"
// const url_getoperators_api = "/techproc/api/getoperators"
// const url_getoperations_api = "/techproc/api/getoperations"


const appTechFastTasks = {
    data() {
        return {
            sendto: '',
            startdate: '',
            enddate: '',
            description: '',
            quantity: 0,
            file: '',
            article: '',
            title: '',
            qrcode: '',
            link: '',
            selectedTechOperation: [],
            machines: [],
            operators: [],
            operations: [],
            operationslist: '',
            changeOperation: [],
            operatorList: []
        }
    },
    methods: {
        addOperation(val) {
            this.changeOperation[this.changeOperation.length] = {id: val, title: this.operations[val - 1].title}
            this.operationslist = ''
        },
        delOperation(id) {
            this.changeOperation.splice(id, 1)
        },
        addOperatorOperator() {
            this.operatorList[this.operatorList.length] = {
                id: this.operatorList.length,
                priority: this.operatorList.length+1,
                operation: 0,
                operator: 0,
                machine: 0
            }
        }
    },
    created() {
        self.axios.get(url_getmachine_api).then((response) => {
            this.machines = response.data
        })
        self.axios.get(url_getoperators_api).then((response) => {
            this.operators = response.data
        })
        self.axios.get(url_getoperations_api).then((response) => {
            this.operations = response.data
        })
    },
    mounted() {

    }

}
// //
const appfasttasks = Vue.createApp(appTechFastTasks).use(VueAxios, axios)
appfasttasks.mount('#app-fasttask')