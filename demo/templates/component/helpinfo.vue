<template>
    <div style="text-align: center;">
        |
        <span v-for="link in msg">
            <a :href="link.url">{{ link.title }}&nbsp;</a>
            |
        </span>
        <div style="margin-top: 10px;">
            <a :href="git">这个有趣的小实验的项目地址</a>
        </div>
    </div>
</template>
<script>
    export default {
        data() {
            return {
                git:'https://github.com/WOSHIliuhailong/djangovue',
                msg: [
                    {
                        url: 'https://cn.vuejs.org/',
                        title: 'Vue 的官网介绍'
                    },
                    {
                        url: 'https://www.djangoproject.com',
                        title: 'django 的官网介绍'
                    }
                ]
            }
        }
    }
</script>