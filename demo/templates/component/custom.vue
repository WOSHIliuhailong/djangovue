<template>
    <div>
        <button @click="emitadd">点击我+1</button>
    </div>
</template>
<script>
    export default {
        data(){
            return{}
        },
        methods:{
            emitadd(e){
                this.$emit('plus',1)
            }
        }
    }
</script>
