<template>
    <div style="text-align: center;margin-top: 100px;">
        <div>
            <h1 style="color:#44B78B;line-height: 100px;">
                Django +
                <img src="https://cn.vuejs.org/images/logo.png" height="100px"width="100px" align="center" />
            </h1>

        </div>
        <h3>{{ content }}</h3>
    </div>

</template>
<script>
    export default {
        data(){
            return {
                content:'让Django支持引入Vue的组件'
            }
        }
    }
</script>